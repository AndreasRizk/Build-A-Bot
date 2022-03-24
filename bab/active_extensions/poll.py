import hikari
import lightbulb

plugin = lightbulb.Plugin("poll")

@plugin.command 
@lightbulb.option("prompt","Poll prompt.", str, required=True)
@lightbulb.command("poll", "A poll")
@lightbulb.implements(lightbulb.SlashCommand,lightbulb.PrefixCommand)
async def poll(ctx: lightbulb.MessageContext)->None:
        embed = (
        hikari.Embed(title=f"{ctx.options.prompt}", description=f"Poll create by {ctx.user}")
        .set_footer("Build-A-Bot Poll")
        )
        rp = await ctx.respond(embed)
        msg = await rp.message()
        await msg.add_reaction("✅")
        await msg.add_reaction("❌")

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)