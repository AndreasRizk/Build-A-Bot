import os
import lightbulb

bot = lightbulb.BotApp(
    os.environ["TOKEN"],
    default_enabled_guilds=int(os.environ["GUILD_ID"]),
    help_slash_command=True,
    prefix="!",
)

def run():
    bot.load_extensions_from("./bab/active_extensions")
    bot.run()