import hikari
import lightbulb
import random

plugin = lightbulb.Plugin("dice")

@plugin.command
@lightbulb.option("sides","Number of sides on the dice.", int, required=True)
@lightbulb.option("user","user", hikari.Member, required=True)
@lightbulb.command("dice", "rolls a dice")
@lightbulb.implements(lightbulb.SlashCommand,lightbulb.PrefixCommand)
async def cmd_say(ctx: lightbulb.MessageContext)->None:
    if ctx.options.sides < 1:
        await ctx.respond("A dice cannot have less then 1 side")
    else:
        x = random.randint(1,int(ctx.options.sides))
        await ctx.respond("@{} you rolled a {}!".format(ctx.options.user.id,str(x)))


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)