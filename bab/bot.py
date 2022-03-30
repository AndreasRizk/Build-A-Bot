import os
import sys
import lightbulb

data_path =  f"bab/{sys.argv[3]}/data/"

bot = lightbulb.BotApp(
    sys.argv[1],
    default_enabled_guilds=int(sys.argv[2]),
    help_slash_command=True,
    prefix="!",
)

def run():
    bot.load_extensions_from(sys.argv[3])
    bot.run()
