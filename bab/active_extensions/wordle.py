import hikari
import lightbulb
import random
import pickle
from os.path import exists

############################# CLASS ############################################

# Game class which holds all the data for each wordle game
class Game:
    def __init__(self, answer):
        self.answer = answer
        self.r_guesses = 6
        self.w_guesses = []

    def guess(self,word): # Function called when a user makes a guess
        self.r_guesses-=1 # decrement remaining guesses
        result = ""
        finished = True
        for id,c in enumerate(word):
            if word[id] == self.answer[id]: # Char is correct in the right spot
                result+=f"**{word[id]}**  "
                continue
            a_pos = self.answer.find(c)
            if a_pos == -1: # Char is incorrect
                result+=f"~~{word[id]}~~  "
                finished = False
            else: # Char is correct in the wrong spot
                result+=f"{word[id]}  "
                finished = False

        self.w_guesses.append(result.upper()) # Add to list of guesses with formatting
        return finished, self.r_guesses == 0 # return if finished and if last

############################# GLOBALS AND DATA MANAGEMENT ############################################

colors = ["#8b0000","#ffff00","#00ff00"] # array used for printing different colors based on guess number

games = {} # Dictionary that holds all wordle games with user.id as key and Game object as value

if (exists("bab/active_extensions/data/wordle_games")): # Reads in saved wordle games on launch if they exist
    with open("bab/active_extensions/data/wordle_games","rb") as f:
        games = pickle.load(f)      

def save(): # Save funtion to call when games dictionary is updated
    with open("bab/active_extensions/data/wordle_games","wb") as f:
        pickle.dump(games,f)


words = {} # Dictionary to hold all possible words

if (exists("bab/active_extensions/data/wordle_words")): # If the dictionary of words is saved load it in
    with open("bab/active_extensions/data/wordle_words","rb") as f:
        words = pickle.load(f)      
else: # Otherwise create the dictionary from the txt and save it
    with open('words.txt') as f:
        for i in f:
            words[i.strip()] = 0
    with open("bab/active_extensions/data/wordle_words","wb") as f:
        pickle.dump(words,f)

############################# HELPER FUNCTIONS ############################################

async def no_game_exists(ctx): # Prints error embed for if a game doesnt exist
    embed = (
    hikari.Embed(title="ERROR!", description="You do not have a game running!")
    .add_field("Options", "Start one with /wordle play")
    .set_footer(f"{ctx.user}'s game")
    )
    await ctx.respond(embed)

async def game_update(ctx): # sends game update message with number of guesses remaining and all previous guesses
    if ctx.user.id in games:
        if (games[ctx.user.id].r_guesses == 6):
            embed = (
            hikari.Embed(title="6 guesses left",color="#00ff00")
            .add_field("Guesses:", "No Guesses")
            .set_footer(f"{ctx.user}'s game")
            )
            await ctx.respond(embed)
        else:
            guesses = ""
            for guess in games[ctx.user.id].w_guesses:
                    guesses+= guess + "\n"
            embed = (
            hikari.Embed(title=f"{games[ctx.user.id].r_guesses} guesses left",color=colors[round(games[ctx.user.id].r_guesses/2)])
            .add_field("Guesses:", guesses)
            .set_footer(f"{ctx.user}'s game")
            )
            await ctx.respond(embed)
    else:
        await no_game_exists(ctx)


############################# LIGHTBULB PLUGIN COMMANDS ############################################

plugin = lightbulb.Plugin("wordle")

@plugin.command # Main wordle command group
@lightbulb.command("wordle", "wordle game")
@lightbulb.implements(lightbulb.SlashCommandGroup,lightbulb.PrefixCommandGroup)
async def wordle(ctx: lightbulb.MessageContext)->None:
    pass

                ################# COMMANDS WITHIN GROUP #########################

@wordle.child
@lightbulb.command("play", "start a wordle game")
@lightbulb.implements(lightbulb.SlashSubCommand,lightbulb.PrefixSubCommand)
async def play(ctx: lightbulb.MessageContext)->None:
    if ctx.user.id in games:
        embed = (
            hikari.Embed(title="ERROR!", description="You already have a game running.")
            .add_field("Options", "Get a game update with /wordle update\n End the game with /wordle end then start a new one with /wordle play")
            .set_footer(f"{ctx.user}'s game")
        )
        await ctx.respond(embed)
    else:
        x = random.randint(1,len(words)-1)
        answer = list(words)[x]
        games[ctx.user.id] = Game(answer)
        save()

        embed = (
            hikari.Embed(title=f"Your wordle game has begun!", description="The goal is to guess the mystery 5 letter word in 6 guesses")
            .add_field("Game info", "Bold characters (**b**) represents a correct letter in the correct spot\n Characters with a strikethrough (~~s~~) represents an incorrect letter\n Regular characters (n) represents a correct letter in the wrong spot\n ")
            .set_footer(f"{ctx.user}'s game")
        )
        await ctx.respond(embed)

@wordle.child
@lightbulb.option("word","Your guess must be 5 characters long.", str, required=True)
@lightbulb.command("guess", "Make a guess.")
@lightbulb.implements(lightbulb.SlashSubCommand,lightbulb.PrefixSubCommand)
async def guess(ctx: lightbulb.MessageContext)->None:
    user_guess = ctx.options.word.lower().strip()
    if not ctx.user.id in games:
        await no_game_exists(ctx)
    elif not len(user_guess) == 5:
        embed = (
            hikari.Embed(title="ERROR!", description=f"\"{user_guess}\" is not of the correct length 5!")
            .add_field("Options", "Guess a word of length 5")
            .set_footer(f"{ctx.user}'s game")
        )
        await ctx.respond(embed)
    elif not user_guess in words:
        embed = (
            hikari.Embed(title="ERROR!", description=f"\"{user_guess}\" is not a valid word!")
            .add_field("Options", "Guess a valid word")
            .set_footer(f"{ctx.user}'s game")
        )
        await ctx.respond(embed)
    else:
        finished, last = games[ctx.user.id].guess(user_guess)

        if last and not finished:
            embed = (
            hikari.Embed(title=f"Better Luck next time!",description=f"You are out of guesses and did not get the word! The word was \"{games[ctx.user.id].answer}\"" ,color=colors[0])
            .set_footer(f"{ctx.user}'s game")
            )
            await ctx.respond(embed)
            games.pop(ctx.user.id)
        elif finished:
            embed = (
            hikari.Embed(title=f"Congrats!",description=f"You figured out the word \"{games[ctx.user.id].answer}\" in {6-games[ctx.user.id].r_guesses} guess(es)!" ,color=colors[2])
            .set_footer(f"{ctx.user}'s game")
            )
            await ctx.respond(embed)
            games.pop(ctx.user.id)
        else:
            await game_update(ctx)

        save()

@wordle.child
@lightbulb.command("end", "End your wordle game.")
@lightbulb.implements(lightbulb.SlashSubCommand,lightbulb.PrefixSubCommand)
async def end(ctx: lightbulb.MessageContext)->None:
    if ctx.user.id in games:
        games.pop(ctx.user.id)
        save()

        embed = (
        hikari.Embed(title=f"Your game has been ended!")
        .set_footer(f"{ctx.user}'s game")
        )
        await ctx.respond(embed)
    else:
        await no_game_exists(ctx)


@wordle.child
@lightbulb.command("update", "Resends your previous guesses.")
@lightbulb.implements(lightbulb.SlashSubCommand,lightbulb.PrefixSubCommand)
async def update(ctx: lightbulb.MessageContext)->None:
    if ctx.user.id in games:
        await game_update(ctx)
    else:
        await no_game_exists(ctx)


############################# LOADING AND UNLOADING THE PLUGIN ############################################
def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)