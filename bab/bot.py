import os
import sys
import lightbulb

data_path =  f"./bab/{sys.argv[3]}/data/"#path to specific bot data folder

bot = lightbulb.BotApp( #creates bot object
    sys.argv[1],
    default_enabled_guilds=int(sys.argv[2]),
    help_slash_command=True,
    prefix="!",
)

def run(): #loads extensions and runs the bot
    bot.load_extensions_from(f"./bab/{sys.argv[3]}")
    bot.run()
