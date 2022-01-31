import os
import urllib.request
import re
import lightbulb

bot = lightbulb.BotApp(
    os.environ["TOKEN"],
    default_enabled_guilds=int(os.environ["GUILD_ID"]),
    help_slash_command=True,
)

@bot.command
@lightbulb.command("ping", description="The bot's ping")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond(f"Pong! Latency: {bot.heartbeat_latency*1000:.2f}ms")

@bot.command
@lightbulb.option("text", "test to search", modifier=lightbulb.commands.OptionModifier.CONSUME_REST)
@lightbulb.command("find", description="search youtube")
@lightbulb.implements(lightbulb.SlashCommand)
async def find(ctx: lightbulb.Context) -> None:
    search = ctx.options.text
    search = search.replace(" ", "+")
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search, timeout=1)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    await ctx.respond("https://www.youtube.com/watch?v="+ video_ids[0])

def run():
    bot.load_extensions_from("./bab/active_extensions")
    bot.run()
