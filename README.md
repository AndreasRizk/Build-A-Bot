# Build-A-Bot
RPI Software Design and Documentation Project. Customizable discord bot for user who do not know how to code.

# How to get the Discord Bot Token
1. Go to https://discord.com/developers/applications and login to discord.

2. Click __“New Application”__.

![New Application](https://imgur.com/QabFRLB.png)

3. Give it a name and hit __“Create”__ (This is just the application name and the Bot name can be different and can be changed whenever).

![Application Name](https://imgur.com/9EgYaRz.png)

4. Next go to __“Bot”__ and click __“Add Bot”__ and click Yes on the popup.

![Add Bot](https://imgur.com/ZLgn9NV.png)

5. Finally you need to click __“Copy”__ under the bot token. You can also now modify the bot's name and Icon.

![Copy Token](https://imgur.com/8uyPy69.png)

# Inviting the Bot to your server
1. While in the appliation you created for the bot, select __“URL Generator”__, and tick the boxes for __“bot”__, __“applications.commands”__ and __“Administrator”__.

![URL Generator](https://imgur.com/OD7phrB.png)

2. Then scroll down, click __“Copy”__ and open the link.

![Copy URL](https://imgur.com/RaZIwfN.png)

3. Then open the dropdown, select the server you would like to add the bot to and click __“Continue”__, then finally click __“Authorize”__.

![Select Server](https://imgur.com/W6wR15D.png)
![Authorize](https://imgur.com/RwNIWf5.png)

# Instructions for us Developers
1. Clone this repository to your local machine using:
```
git clone https://github.com/Andy-8/Build-A-Bot
```
<br>

2. Next you need to get the libraries installed. I recomend that you don't do that globally but setup a virtual environment for the project and install them there. I set mine up by being inside my project folder and running:
```
python -m venv .venv
```
This should create the virtual environment, then to get into the environment I run:
```
source .venv/Scripts/activarte
```
however I use git bash and this might be different on your system. If this is done right you will see (.venv) in your commandline prompt. Now to install the libraries, simply run:
```
pip install -r requirements.txt
```
this will install all the libraries listed in requirements.txt

<br>

3. Then to add the environment variables, create a ".env" file with will hold environment variables, in this case the bot token you should get from the discord developer portal and the guild id of our server. And the varaibles should be titled "TOKEN" and "GUILD_ID". For example here is my .env file:

```
#.env
TOKEN=OTM1MzQ4OTY3MTM3NTA5Mzc3.Ye9Vmw.QCYMMmKxMxjeuZmGlr0Nf_1TBsU
GUILD_ID=933813327749070848
```
<br>

4. Now to run the bot, use the command:
```
python -m bab
```
which runs the folder bab as it has a \_\_init\_\_.py and \_\_main\_\_.py