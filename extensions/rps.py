import hikari
import lightbulb
import random

plugin = lightbulb.Plugin("rps")

@plugin.command
@lightbulb.option("choice","\"rock\" for rock, \"paper\" for paper, or \"scissors\" for scissors", str, required=True)
@lightbulb.command("rps", "play rock paper scissors") # allows the user to play a rock paper scissors game versus the bot
@lightbulb.implements(lightbulb.SlashCommand,lightbulb.PrefixCommand)
async def rps(ctx: lightbulb.Context) -> None:
	list = ["rock", "paper", "scissors"]
	choice = random.choice(list)
	user_choice = ctx.options.choice.lower()

	if(user_choice != "rock" and user_choice != "scissors" and user_choice != "paper"):
		await ctx.respond("Unrecognized choice, try again!")
	else:
		win = False
		tie = False
		if(user_choice == "rock"):
			if(choice == "rock"):
				tie = True
			elif(choice == "scissors"):
				win = True
		elif(user_choice == "paper"):
			if(choice == "paper"):
				tie = True
			elif(choice == "rock"):
				win = True
		elif(user_choice == "scissors"):
			if(choice == "scissors"):
				tie = True
			elif(choice == "paper"):
				win == True
		
		if(tie):
			await ctx.respond("Uh oh! I chose " + choice + " so we tied! :(")
		elif(win):
			await ctx.respond("You Win! I chose " + choice + ".")
		else:
			await ctx.respond("You Lost! I chose " + choice + ". Haha, take the L loser.")
	
def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)			