import hikari
import lightbulb
import random
from bab import bot

plugin = lightbulb.Plugin("music")

@plugin.command # Main music command group
@lightbulb.command("music", "Music!")
@lightbulb.implements(lightbulb.SlashCommandGroup,lightbulb.PrefixCommandGroup)
async def music(ctx: lightbulb.MessageContext)->None:
    pass

                ################# COMMANDS WITHIN GROUP #########################

@music.child
@lightbulb.command("join", "Makes bot join channel") # testing allowing the bot's ability to join a channel
@lightbulb.implements(lightbulb.SlashSubCommand,lightbulb.PrefixSubCommand)
async def join(ctx: lightbulb.MessageContext)->None:
    hikari.connect_to(
        self,
        guild: ctx.guild_id,
        channel: ctx.channel_id,
        voice_connection_type: Type[~_VoiceConnectionT],
        deaf: bool = True,
        mute: bool = False
    )


@music.child
@lightbulb.command("leave", "Makes bot leave channel")# testing allowing the bot's ability to leave a channel
@lightbulb.implements(lightbulb.SlashSubCommand,lightbulb.PrefixSubCommand)
async def leave(ctx: lightbulb.MessageContext)->None:
    await bot.update_voice_state(ctx.guild_id, None)



def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)