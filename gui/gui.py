import os
<<<<<<< HEAD
import dill as pickle
=======
import pickle
import dill
>>>>>>> dev
import subprocess
import shutil
import tkinter as tk
import webbrowser
from tkinter import *
from os.path import exists

<<<<<<< HEAD
class Bot:
    def __init__(self, name, token, guild_id):
        self.name_ = name
        self.token_ = token
        self.guild_id_ = guild_id
        self.obj_ = None

    def run_bot(self):
        if self.obj_ == None:
            self.obj_ = subprocess.Popen(['python', '-m', 'bab', self.token_, self.guild_id_])

    def stop_bot(self):
        if not self.obj_ == None:
            self.obj_.kill()
            self.obj_ = None

Bots = {}
if (exists("gui/data/existing_bots")):
        with open("gui/data/existing_bots","rb") as f:
            Bots = pickle.load(f)
print(len(Bots))

def save():
    with open("gui/data/existing_bots","wb") as f:
        pickle.dump(Bots,f)
=======
global ghimg

class Bot:
    def __init__(self, name):
        self.name_ = name
        self.obj_ = subprocess.Popen(['python', '-m', 'bab'])

    def run_bot(self):
        if self.obj_ == None:
            self.obj_ = subprocess.Popen(['python', '-m', 'bab'])

    def stop_bot(self):
        self.obj_.kill()
        self.obj_ = None

    def get_name(self):
        return self.name_
>>>>>>> dev

def githublink():
    webbrowser.open_new(r"https://github.com/Andy-8/Build-A-Bot")

def clear(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def help(frame):
    clear(frame)

    #Initial help page
    help_label = tk.Label(frame, text="Help", font=('Arial',20), relief=tk.RIDGE, borderwidth= 0, height=3, anchor="w", bg="#FFFFFF", fg="black")
    help_label.grid(row=0, column=0, sticky=NW)

    ghimg = PhotoImage(file= "gui/images/github.png")
    github_button = tk.Button(frame, image= ghimg,  fg="white", bg="#FFFFFF", borderwidth=0,  command=githublink)
    github_button.image = ghimg
    github_button.grid(row=0, column=1, sticky=NE)
    # github_button.pack(side=TOP, anchor=NE )
<<<<<<< HEAD
    
<<<<<<< HEAD
=======

    
>>>>>>> dev
=======



>>>>>>> 8537ae896378797e09bf79b04344254356696ad7
    # help_label.pack(side=TOP, anchor=NW)
    # textframe.pack()
    scroll = Scrollbar(frame)
    # scroll.pack(side=RIGHT, fill=Y)
    scroll.grid(row=1, column=1, sticky=NS)

    help = Text(frame, font=('Arial',15), wrap=WORD, height=28, width=60, yscrollcommand = scroll.set)
<<<<<<< HEAD
<<<<<<< HEAD
    for i in range(1): 
=======
    for i in range(50): 
>>>>>>> dev
=======
    for i in range(50):
>>>>>>> 8537ae896378797e09bf79b04344254356696ad7
        help.insert(END,"this is some text\n")
    help.config(state=DISABLED)
    # help.pack(side=tk.TOP, fill=BOTH)
    help.grid(row=1, column=0)
    scroll.config(command=help.yview)

<<<<<<< HEAD
def bot_selection(frame):
    clear(frame)
    for bot in Bots.keys():
        x = tk.Button(frame, text=bot, padx=30, pady=20, font=('Arial',12), fg="black", bg="#FFFFFF", command=lambda bot=bot: edit_bot(frame, bot))
        x.pack()

def bot_running(frame, bot):
    pass

def edit_bot(frame, botName):
    clear(frame)
    bot = Bots[botName]
    run = tk.Button( frame, text="Run", anchor="center", padx=350, pady=50, font=('Arial',20), fg="black", bg="#FFFFFF", command=lambda : bot.run_bot())
    run.pack()

    spacer = tk.Label( frame, bg="#FFFFFF", anchor="center", pady=30, width=15)
    spacer.pack()

    stop = tk.Button( frame, text="Stop", anchor="center", padx=350, pady=50, font=('Arial',20), fg="black", bg="#FFFFFF", command=lambda : bot.stop_bot())
    stop.pack()

def create_new_bot(name, token, guild_id, frame):
    Bots[name] = Bot(name, token, guild_id)
    save()
    edit_bot(frame,name)

def create_bot(frame):
    clear(frame)

=======
def create_new_bot(bots, name, frame):
    clear(frame)

    newBot = Bot(name.get())
    print(name.get())
    bots.append(newBot)
    bot = bots[len(bots)-1]
    with open("gui/data/existing_bots","wb") as f:
        dill.dump(bots,f)

    run = tk.Button(frame, text="Run", padx=10, pady=5, fg="black", bg="#A9A9A9", command=bot.run_bot)
    run.pack()

    stop = tk.Button(frame, text="Stop", padx=10, pady=5, fg="black", bg="#A9A9A9", command=bot.stop_bot)
    stop.pack()

def includeExt(dir_name, exe):
    if exists(dir_name+"/"+exe):
        os.remove(dir_name+"/"+exe)
    else:
        shutil.copyfile("extensions/"+exe, dir_name+"/"+exe)

def add_extensions(bots, name, frame):
    botName = name.get()

    clear(frame)

    dir_name = "bab/"+botName+ "_extensions"
    if not exists(dir_name):
        os.mkdir(dir_name)

    dir_list = os.listdir("extensions")
    dir_list = [name for name in dir_list if 'py' in name.lower()]

    vars = []
    for i in range(len(dir_list)):
        vars.append(tk.IntVar())

        c1 = tk.Checkbutton(frame, text=dir_list[i],variable=vars[i], onvalue=1, offvalue=0, command=lambda exe = dir_list[i]:includeExt(dir_name, exe))
        c1.pack()

    run = tk.Button( frame, text="Next", anchor="center", padx=10, pady=20, font=('Arial',20), fg="black", bg="#FFFFFF", command=lambda : create_new_bot(bots, botName, frame))
    run.pack()

def edit_bot(bot):
    tk.Button(text=bot.get_name()+" start", padx=10, pady=5, fg="black", bg="#A9A9A9", command=bot.run_bot).pack()
    tk.Button(text=bot.get_name()+" stop", padx=10, pady=5, fg="black", bg="#A9A9A9", command=bot.stop_bot).pack()


def create_bot(frame, bots):
    clear(frame)

    print(len(bots))
>>>>>>> dev
    name_title = tk.Label( frame, bg="#FFFFFF", text="Name of Bot", anchor="center", pady=50, padx=350, width=15, font=('Arial',20))
    name = tk.Entry( frame, relief=tk.SUNKEN, width=30, font=('Arial',20))

    token_title = tk.Label( frame, bg="#FFFFFF", text="Bot Token", anchor="center", pady=50, padx=350, width=15, font=('Arial',20))
    token = tk.Entry( frame, relief=tk.SUNKEN, width=30, font=('Arial',20))

    guild_title = tk.Label( frame, bg="#FFFFFF", text="Guild ID", anchor="center", pady=50, padx=350, width=15, font=('Arial',20))
    guild_id = tk.Entry( frame, relief=tk.SUNKEN, width=30, font=('Arial',20))

    spacer = tk.Label( frame, bg="#FFFFFF", anchor="center", pady=30, width=15)
<<<<<<< HEAD
<<<<<<< HEAD
    create = tk.Button( frame, text="Create", anchor="center", padx=10, pady=20, font=('Arial',20), fg="black", bg="#FFFFFF", command=lambda : create_new_bot(name.get(), token.get(), guild_id.get(), frame))
=======
    run = tk.Button( frame, text="Run", anchor="center", padx=10, pady=20, font=('Arial',20), fg="black", bg="#FFFFFF", command=lambda : create_new_bot(bots, name, frame))
>>>>>>> dev
=======
    run = tk.Button( frame, text="Next", anchor="center", padx=10, pady=20, font=('Arial',20), fg="black", bg="#FFFFFF", command=lambda : add_extensions(bots, name, frame))
>>>>>>> 8537ae896378797e09bf79b04344254356696ad7

    name_title.pack()
    name.pack()
    token_title.pack()
    token.pack()
    guild_title.pack()
    guild_id.pack()
    spacer.pack()
<<<<<<< HEAD
    create.pack()

def on_close():
    for bot in Bots.values():
        bot.stop_bot()
=======
    run.pack()

def on_closing(bots):
    with open("gui/data/existing_bots","wb") as f:
        dill.dump(bots,f)
>>>>>>> dev

def launch():
    root = tk.Tk()
    root.title("Build-A-Bot")
    root.iconbitmap("logo.ico")

<<<<<<< HEAD
=======
    bots = []

    if (exists("gui/data/existing_bots")):
        with open("gui/data/existing_bots","rb") as f:
            bots = dill.load(f)

>>>>>>> dev
    canvas = tk.Canvas(root,height=800,width=1000,bg="#FFFFFF")
    canvas.pack()


    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.98,relheight=0.98, relx=0.01, rely=0.01)

    sideBar = tk.Frame(frame, width=100, bg="white")
    sideBar.pack(fill=tk.Y, side=tk.LEFT)

    workspace = tk.Frame(frame, width=root.winfo_screenwidth() - 100, bg="white")
    workspace.pack(fill=tk.Y, side=tk.RIGHT)

<<<<<<< HEAD
    #buttons on the sidebar
    logoimg = PhotoImage(file= "gui/images/bab.png")
    logo = tk.Button(sideBar, image= logoimg, borderwidth=0, fg="white", bg="#FFFFFF", command=lambda : help(workspace))
    logo.pack(padx=30, pady=30)

    existingbotsimg = PhotoImage(file= "gui/images/existingbots.png")
    existingbots = tk.Button(sideBar, image= existingbotsimg, borderwidth=0, fg="white", bg="#FFFFFF", command=lambda : bot_selection(workspace))
    existingbots.pack( padx=30, pady=30)

    createimg = PhotoImage(file= "gui/images/createbutton.png")
    create = tk.Button(sideBar, image= createimg, borderwidth=0, fg="white", bg="#FFFFFF", command=lambda : create_bot(workspace))
    create.pack(padx=30, pady=30)

    fileexpimg = PhotoImage(file= "gui/images/files.png")
    fileexp = tk.Button(sideBar, image= fileexpimg, borderwidth=0, fg="white", bg="#FFFFFF", command=lambda : create_bot(workspace))
    fileexp.pack(padx=30, pady=30)
=======
    print(len(bots))
    for bot in bots:
        tk.Button(sideBar, text=bot.get_name(), padx=10, pady=5, fg="black", bg="#A9A9A9", command=lambda : edit_bot(bot)).pack()

    #buttons on the sidebar
    logoimg = PhotoImage(file= "gui/images/bab.png")
    logo = tk.Button(sideBar, image= logoimg, borderwidth=0, fg="white", bg="#FFFFFF", command=lambda : help(workspace))
    logo.pack( padx=30, pady=30)

    existingbotsimg = PhotoImage(file= "gui/images/existingbots.png")
    existingbots = tk.Button(sideBar, image= existingbotsimg, borderwidth=0, fg="white", bg="#FFFFFF")
    existingbots.pack( padx=30, pady=30)

    createimg = PhotoImage(file= "gui/images/createbutton.png")
    create = tk.Button(sideBar, image= createimg, borderwidth=0, fg="white", bg="#FFFFFF", command=lambda : create_bot(workspace, bots))
    create.pack( padx=30, pady=30)

    fileexpimg = PhotoImage(file= "gui/images/files.png")
    fileexp = tk.Button(sideBar, image= fileexpimg, borderwidth=0, fg="white", bg="#FFFFFF", command=lambda : create_bot(workspace, bots))
    fileexp.pack( padx=30, pady=30)
>>>>>>> dev


    help(workspace)

<<<<<<< HEAD
<<<<<<< HEAD
    root.protocol("WM_DELETE_WINDOW", on_close())
=======
    print(len(bots))
=======
>>>>>>> 8537ae896378797e09bf79b04344254356696ad7
    root.protocol("WM_DELETE_WINDOW", on_closing(bots))
>>>>>>> dev
    root.mainloop()
