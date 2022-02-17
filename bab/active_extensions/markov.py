import hikari
import lightbulb
import markovify

plugin = lightbulb.Plugin("markov")

@plugin.command
@lightbulb.command("markov", description="Fancy a conversation with William Shakespeare? Fancy no more ye of little faith!")
@lightbulb.implements(lightbulb.SlashCommand)

async def markov(ctx: lightbulb.Context) -> None:

    # Get raw text as string.
    with open("bab/active_extensions/data/shakespeare.txt") as f:
        text = f.read()

    # Build the model.
    text_model = markovify.Text(text)

    # Print five randomly-generated sentences
    for i in range(5):
        await ctx.respond(text_model.make_short_sentence(400))
        #await ctx.respond(text_model.make_short_sentence(100))

    



############################# LOADING AND UNLOADING THE PLUGIN ############################################
def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)