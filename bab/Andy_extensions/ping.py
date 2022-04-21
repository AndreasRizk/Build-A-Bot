import hikari
import lightbulb

plugin = lightbulb.Plugin("ping")

@plugin.command
@lightbulb.command("ping", description="The bot's ping") # has the bot reply pong to check if the bot is online
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond("Pong!")


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)
