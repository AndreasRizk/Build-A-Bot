import hikari
import lightbulb
import random

plugin = lightbulb.Plugin("powerball")

@plugin.command
@lightbulb.option("money","How much money do you want to spend on tickets? ($2 per ticket)", int, required=True)
@lightbulb.command("powerball", "play the powerball ($141 million)")
@lightbulb.implements(lightbulb.SlashCommand,lightbulb.PrefixCommand)
async def powerball(ctx: lightbulb.MessageContext) -> None:
	if(ctx.options.money >= 2):
		num_tix = int(ctx.options.money / 2)
		odds = 292201338
		actual_odds = int(odds / num_tix)

		if(actual_odds == 0 or random.randrange(actual_odds) == 0):
			await ctx.respond("YOU WON THE POWERBALL BY BUYING " + str(formatted_num(num_tix)) + " TICKETS, WORTH $" + str(formatted_num(ctx.options.money)) + ", WITH ODDS OF 1 IN " + str(formatted_num(actual_odds)) + "! CONGRATS!")
		else:
			await ctx.respond("Unfortunately you lost and succumbed to the terrible odds of powerball. You lost with " + str(formatted_num(num_tix)) + " tickets, worth $" + str(formatted_num(ctx.options.money)) + ", with actual odds of 1 in " + str(formatted_num(actual_odds)) + ". Good luck next time!")
	else:
		await ctx.respond("Choose a valid money amount >= $2")
def formatted_num(num):
	return ("{:,}".format(num))

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)