import hikari
import lightbulb
import pickle
import random
from os.path import exists

############################# CLASS ############################################

# Game class which holds all the data for each poll game
class Poll:
    def __init__(self, user, text):
        self.user = user
        self.text = text
        self.yay = 0
        self.nae = 0

############################# GLOBALS AND DATA MANAGEMENT ############################################

polls = {}

if (exists("bab/active_extensions/data/polls")):
    with open("bab/active_extensions/data/polls","rb") as f:
        polls = pickle.load(f)      

def save(): 
    with open("bab/active_extensions/data/polls","wb") as f:
        pickle.dump(polls,f)

############################# LIGHTBULB PLUGIN COMMANDS ############################################

plugin = lightbulb.Plugin("poll")

@plugin.command # Main poll command group
@lightbulb.command("poll", "A poll")
@lightbulb.implements(lightbulb.SlashCommandGroup,lightbulb.PrefixCommandGroup)
async def poll(ctx: lightbulb.MessageContext)->None:
    pass

################# COMMANDS WITHIN GROUP #########################

def poll_id():
    x = random.randint(1,100)
    while x in polls:
        x = random.randint(1,100)
    return x
        
@poll.child
@lightbulb.option("text","The text describing your poll.", str, required=True)
@lightbulb.command("create", "Create a poll.")
@lightbulb.implements(lightbulb.SlashSubCommand,lightbulb.PrefixSubCommand)
async def play(ctx: lightbulb.MessageContext)->None:
        id = poll_id()
        polls[id] = poll(ctx.user.id,ctx.options.text)
        embed = (
            hikari.Embed(title=f"{ctx.options.text}", description=f"Poll create by {ctx.user.name}")
            .add_field(f"Poll id is {id}", "")
            .set_footer(f"{ctx.user}'s poll")
        )
        await ctx.respond(embed)

@poll.child
@lightbulb.option("id","ID of the pole you want to vote on.", int, required=True)
@lightbulb.option("vote","Vote yea or nay.", str, required=True)
@lightbulb.command("vote", "vote on a poll")
@lightbulb.implements(lightbulb.SlashSubCommand,lightbulb.PrefixSubCommand)
async def guess(ctx: lightbulb.MessageContext)->None:
    pass

@poll.child
@lightbulb.option("id","ID of the pole you want to end.", int, required=True)
@lightbulb.command("end", "End your poll.")
@lightbulb.implements(lightbulb.SlashSubCommand,lightbulb.PrefixSubCommand)
async def end(ctx: lightbulb.MessageContext)->None:
    if not ctx.user.id == polls[ctx.options.id].user:
        ctx.user.reply("You cannot end a poll you did not start!")
        return
    polls.pop(ctx.options.id)



############################# LOADING AND UNLOADING THE PLUGIN ############################################
def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)