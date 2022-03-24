import hikari
import lightbulb
import pickle
from os.path import exists
from flask import Flask, request, url_for, session, redirect 
import spotipy
from spotipy.oauth2 import SpotifyOAuth
############################# CLASS ############################################
class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password

############################# GLOBALS AND DATA MANAGEMENT ############################################

app = Flask(__name__)
app.secret_key = "asjfhuwebljkcnas"
app.config['SESSION_COOKIE_NAME'] = 'bab Cookie'

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id = "9236ad1406734b7aa4c6e62bdeff3caf",
        client_secret = "60551bfc0ab6463ebc44bbe9b540e0b3",
        redirect_uri = url_for('redirect',_external=True),
        scope="user-library-read"
    )

@app.route('/')
def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/redirect')
def redirect():
    return redirect

@app.route('/getTracks')
def getTracks():
    return "test"


spotipy_tokens = {}

if (exists("bab/active_extensions/data/spotipy_tokens")):
    with open("bab/active_extensions/data/spotipy_tokens","rb") as f:
        spotipy_tokens = pickle.load(f)      

def save():
    with open("bab/active_extensions/data/spotipy_tokens","wb") as f:
        pickle.dump(spotipy_tokens,f)

############################# HELPER FUNCTIONS ############################################



############################# LIGHTBULB PLUGIN COMMANDS ############################################

plugin = lightbulb.Plugin("music")

@plugin.command
@lightbulb.command("music", "Music Manager")
@lightbulb.implements(lightbulb.SlashCommandGroup,lightbulb.PrefixCommandGroup)
async def wordle(ctx: lightbulb.MessageContext)->None:
    pass

################# COMMANDS WITHIN GROUP #########################

@wordle.child
@lightbulb.command("login", "Login to your spotify account.")
@lightbulb.implements(lightbulb.SlashSubCommand,lightbulb.PrefixSubCommand)
async def login(ctx: lightbulb.MessageContext)->None:
    token_dict = create_spotify_oauth().get_access_token()
    spotipy_tokens[ctx.user.id] = token_dict['access_token']

@wordle.child
@lightbulb.command("play", "Play a song.")
@lightbulb.implements(lightbulb.SlashSubCommand,lightbulb.PrefixSubCommand)
async def play(ctx: lightbulb.MessageContext)->None:
    pass

############################# LOADING AND UNLOADING THE PLUGIN ############################################
def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)