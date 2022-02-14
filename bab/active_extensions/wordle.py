import hikari
import lightbulb
import random

class Game:
    def __init__(self, answer):
        self.answer = answer
        self.r_guesses = 6
        self.w_guesses = []
    def guess(self,word):
        self.r_guesses-=1
        if self.r_guesses == 0:
            return True
        else:
            return False
    def compare(self,word):
        result = ""
        finished = True
        for id,c in enumerate(word):
            if word[id] == self.answer[id]:
                result+=f"**{word[id]}**  "
                continue
            a_pos = self.answer.find(c)
            if a_pos == -1:
                result+=f"~~{word[id]}~~  "
                finished = False
            else:
                result+=f"{word[id]}  "
                finished = False
        self.w_guesses.append(result)
        return finished

games = {}

plugin = lightbulb.Plugin("wordle")

@plugin.command
@lightbulb.command("wordle", "wordle game")
@lightbulb.implements(lightbulb.SlashCommandGroup,lightbulb.PrefixCommandGroup)
async def wordle(ctx: lightbulb.MessageContext)->None:
    pass

@wordle.child
@lightbulb.command("play", "start a wordle game")
@lightbulb.implements(lightbulb.SlashSubCommand,lightbulb.PrefixSubCommand)
async def play(ctx: lightbulb.MessageContext)->None:
    x = random.randint(1,1972)
    answer = "tests"
    with open('words.txt') as words:
        c = 1
        for i in words:
            if not c == x:
                c+=1
                continue
            answer = i.strip()
            break

    if ctx.user.id in games:
        embed = (
            hikari.Embed(title="ERROR!", description="You already have a game running.")
            .add_field("Options", "Get a game update with /wordle update\n End the game with /wordle end then start a new one with /wordle play")
            .set_footer(f"{ctx.user}'s game")
        )
        await ctx.respond(embed)
    else:
        games[ctx.user.id] = Game(answer)
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
    if not ctx.user.id in games:
        embed = (
            hikari.Embed(title="ERROR!", description="You do not have a game running!")
            .add_field("Options", "Start one with /wordle play")
            .set_footer(f"{ctx.user}'s game")
        )
        await ctx.respond(embed)
    elif not len(ctx.options.word) == 5:
        embed = (
            hikari.Embed(title="ERROR!", description=f"\"{ctx.options.word}\" is not of the correct length 5!")
            .add_field("Options", "Guess a word of length 5")
            .set_footer(f"{ctx.user}'s game")
        )
        await ctx.respond(embed)
    else:
        last = games[ctx.user.id].guess(ctx.options.word.lower())
        finished = games[ctx.user.id].compare(ctx.options.word.lower())
        guesses = ""
        for guess in games[ctx.user.id].w_guesses:
            guesses+= guess + "\n"

        colors = ["#8b0000","#ffff00","#00ff00"]

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
            embed = (
            hikari.Embed(title=f"{games[ctx.user.id].r_guesses} guesses left",color=colors[round(games[ctx.user.id].r_guesses/2)])
            .add_field("Guesses:", guesses)
            .set_footer(f"{ctx.user}'s game")
            )
            await ctx.respond(embed)

@wordle.child
@lightbulb.command("end", "End your wordle game.")
@lightbulb.implements(lightbulb.SlashSubCommand,lightbulb.PrefixSubCommand)
async def end(ctx: lightbulb.MessageContext)->None:
    games.pop(ctx.user.id)
    embed = (
    hikari.Embed(title=f"Your game has been ended!")
    .set_footer(f"{ctx.user}'s game")
    )
    await ctx.respond(embed)

@wordle.child
@lightbulb.command("update", "Resends your previous guesses.")
@lightbulb.implements(lightbulb.SlashSubCommand,lightbulb.PrefixSubCommand)
async def update(ctx: lightbulb.MessageContext)->None:
    guesses = ""
    colors = ["#8b0000","#ffff00","#00ff00"]
    for guess in games[ctx.user.id].w_guesses:
            guesses+= guess + "\n"
    embed = (
    hikari.Embed(title=f"{games[ctx.user.id].r_guesses} guesses left",color=colors[round(games[ctx.user.id].r_guesses/2)])
    .add_field("Guesses:", guesses)
    .set_footer(f"{ctx.user}'s game")
    )
    await ctx.respond(embed)

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)