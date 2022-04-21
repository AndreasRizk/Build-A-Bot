import hikari
import lightbulb
import random

plugin = lightbulb.Plugin("dice")

@plugin.command # rolls a dice of any number of sides and returns the result to the user 
@lightbulb.option("sides","Number of sides on the dice. Go crazy with it!", int, required=True)
@lightbulb.command("dice", "rolls a dice")
@lightbulb.implements(lightbulb.SlashCommand,lightbulb.PrefixCommand)
async def cmd_say(ctx: lightbulb.MessageContext)->None:
    if ctx.options.sides == 0:
        await ctx.respond("0... Well that was pointless.")
    elif ctx.options.sides < 0:
        await ctx.respond("Negative sides... really!")
    else:
        x = random.randint(1,int(ctx.options.sides))
        await ctx.respond(f"You rolled a {str(x)}!")


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)