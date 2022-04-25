from genericpath import exists
from itertools import count
from urllib import response
import hikari
import lightbulb
import markovify
import os
from os.path import exists
import pickle
from bab.bot import data_path

print(data_path)

data_path = data_path[6:-1]

#C:\Users\Liam Roberts\Documents\CSCI\SDD\Build-A-Bot\bab\1_extensions\data  \markov_user_data

plugin = lightbulb.Plugin("markov")

text_models = {}

if (not os.path.exists(f"extensions/data/markov_raw")):
    os.makedirs(f"extensions/data/markov_raw")

if (exists(f"extensions/data/text_models")): # Reads in saved markvov keys on launch if they exist
    with open(f"extensions/data/text_models","rb") as f:
        text_models = pickle.load(f)  

for file in os.listdir(f"extensions/data/markov_raw"):
    if file[:-4] in text_models:
        continue
    f = open(f"extensions/data/markov_raw/" + file)
    text = f.readlines()
    text_models[file[:-4]] = markovify.Text(text)

userList = [x for x in text_models.keys()]
users = ""
for x in userList:
    users+= f"\"{x}\" "

@plugin.command # allows the user to generate a number of statememnets with a certial lenght and emotion based on a perons markov chain
@lightbulb.option("user",users, str, required=True)
@lightbulb.option("quantity","Number of sentences to generate.", int, required=False)
@lightbulb.option("length", "Length of sentences (must be greater than 50).", int, required=False)
@lightbulb.command("markov", description="Friend not online? This is close enough. We're CS majors. This bot is out friend")
@lightbulb.implements(lightbulb.SlashCommand)

async def markov(ctx: lightbulb.Context) -> None:
    user = ctx.options.user.lower()
    if (len(text_models) == 0):
        await ctx.respond("User has not entered any Markov data files")
        return

    elif (user not in text_models.keys()):
        await ctx.respond(f"Cannot find Markov data for {user}")
        return

    count = ctx.options.quantity
    length = ctx.options.length
    if count == None:
        count = 1
    if length == None or length < 50:
        length = 300

    response = user + ":```"

    for i in range(count):
        response += f"{i+1}. {text_models[user].make_short_sentence(length)}\n"

    response += '```'
    await ctx.respond(response)


############################# LOADING AND UNLOADING THE PLUGIN ############################################
def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)