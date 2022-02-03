import re
import urllib.request
import os
import hikari
import lightbulb

plugin = lightbulb.Plugin("find")

@plugin.command
@lightbulb.option("text", "test to search", modifier=lightbulb.commands.OptionModifier.CONSUME_REST)
@lightbulb.command("find", description="search youtube")
@lightbulb.implements(lightbulb.SlashCommand)
async def find(ctx: lightbulb.Context) -> None:
    search = ctx.options.text
    search = search.replace(" ", "+")
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search, timeout=1)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    await ctx.respond("https://www.youtube.com/watch?v="+ video_ids[0])

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)
