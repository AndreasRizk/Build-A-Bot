import re
import urllib.request
from bs4 import BeautifulSoup
import requests
import os
import hikari
import lightbulb

plugin = lightbulb.Plugin("news")

@plugin.command
@lightbulb.option("text", "test to search", modifier=lightbulb.commands.OptionModifier.CONSUME_REST)
@lightbulb.command("news", description="Get the top headline from your favorite new outlet")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    outlet = ctx.options.text
    if outlet.lower() == "npr":
        out = npr()
    elif outlet.lower() == "bbc":
        out = bbc()
    else:
        await ctx.respond(outlet + " not recognized please try npr or bbc")

    await ctx.respond('\n'.join(out))


def npr():
    page = requests.get("https://www.npr.org/sections/news/")
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="main-section")
    stories = results.find_all("article", class_="item")
    topStories = []
    for i in range(5):
        info = stories[i].find("h2", class_="title")
        a = info.find("a")
        topStories.append(a["href"])
    print(topStories)
    return topStories

def bbc():
    page = requests.get("https://www.bbc.com/news")
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="news-top-stories-container")
    stories = results.find_all("a")
    topStories = []
    for i in range(5):
        topStories.append("https://www.bbc.com"+stories[i]["href"])
    print(topStories)
    return topStories

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)
