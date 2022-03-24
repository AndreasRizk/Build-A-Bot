import os
import sys
import lightbulb

bot = lightbulb.BotApp(
    sys.argv[1],
    default_enabled_guilds=int(sys.argv[2]),
    help_slash_command=True,
    prefix="!",
)

def run():
    bot.load_extensions_from("./bab/active_extensions")
    bot.run()