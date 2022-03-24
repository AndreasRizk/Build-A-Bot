import os
import pickle
import dill
import subprocess
import tkinter as tk
import webbrowser
from tkinter import *
from os.path import exists

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
    

    
    # help_label.pack(side=TOP, anchor=NW)
    # textframe.pack()
    scroll = Scrollbar(frame)
    # scroll.pack(side=RIGHT, fill=Y)
    scroll.grid(row=1, column=1, sticky=NS)

    help = Text(frame, font=('Arial',15), wrap=WORD, height=28, width=60, yscrollcommand = scroll.set)
    for i in range(50): 
        help.insert(END,"this is some text\n")
    help.config(state=DISABLED)
    # help.pack(side=tk.TOP, fill=BOTH)
    help.grid(row=1, column=0)
    scroll.config(command=help.yview)

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

def edit_bot(bot):
    tk.Button(text=bot.get_name()+" start", padx=10, pady=5, fg="black", bg="#A9A9A9", command=bot.run_bot).pack()
    tk.Button(text=bot.get_name()+" stop", padx=10, pady=5, fg="black", bg="#A9A9A9", command=bot.stop_bot).pack()


def create_bot(frame, bots):
    clear(frame)

    print(len(bots))
    name_title = tk.Label( frame, bg="#FFFFFF", text="Name of Bot", anchor="center", pady=50, padx=350, width=15, font=('Arial',20))
    name = tk.Entry( frame, relief=tk.SUNKEN, width=30, font=('Arial',20))

    token_title = tk.Label( frame, bg="#FFFFFF", text="Bot Token", anchor="center", pady=50, padx=350, width=15, font=('Arial',20))
    token = tk.Entry( frame, relief=tk.SUNKEN, width=30, font=('Arial',20))

    guild_title = tk.Label( frame, bg="#FFFFFF", text="Guild ID", anchor="center", pady=50, padx=350, width=15, font=('Arial',20))
    guild_id = tk.Entry( frame, relief=tk.SUNKEN, width=30, font=('Arial',20))

    spacer = tk.Label( frame, bg="#FFFFFF", anchor="center", pady=30, width=15)
    run = tk.Button( frame, text="Run", anchor="center", padx=10, pady=20, font=('Arial',20), fg="black", bg="#FFFFFF", command=lambda : create_new_bot(bots, name, frame))

    name_title.pack()
    name.pack()
    token_title.pack()
    token.pack()
    guild_title.pack()
    guild_id.pack()
    spacer.pack()
    run.pack()

def on_closing(bots):
    with open("gui/data/existing_bots","wb") as f:
        dill.dump(bots,f)

def launch():
    root = tk.Tk()
    root.title("Build-A-Bot")
    root.iconbitmap("logo.ico")

    bots = []

    if (exists("gui/data/existing_bots")):
        with open("gui/data/existing_bots","rb") as f:
            bots = dill.load(f)

    canvas = tk.Canvas(root,height=800,width=1000,bg="#FFFFFF")
    canvas.pack()


    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.98,relheight=0.98, relx=0.01, rely=0.01)

    sideBar = tk.Frame(frame, width=100, bg="white")
    sideBar.pack(fill=tk.Y, side=tk.LEFT)

    workspace = tk.Frame(frame, width=root.winfo_screenwidth() - 100, bg="white")
    workspace.pack(fill=tk.Y, side=tk.RIGHT)

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


    help(workspace)

    print(len(bots))
    root.protocol("WM_DELETE_WINDOW", on_closing(bots))
    root.mainloop()
