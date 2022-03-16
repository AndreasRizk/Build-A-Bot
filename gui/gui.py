import os
import pickle
import dill
import subprocess
import tkinter as tk
import webbrowser
from tkinter import *
from os.path import exists

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

def create_new_bot(bots, name, frame):
    #nameBox.destroy()
    #title.destroy()
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
    print(len(bots))
    title = tk.Label( frame, text="Name of Bot", relief=tk.RIDGE, width=15)
    name = tk.Entry( frame, relief=tk.SUNKEN, width=10)

    run = tk.Button( frame, text="Run", padx=10, pady=5, fg="black", bg="#A9A9A9", command=lambda : create_new_bot(bots, name, frame))

    title.pack()
    name.pack()
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

    canvas = tk.Canvas(root,height=700,width=700,bg="#FFFFFF")
    canvas.pack()


    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.98,relheight=0.98, relx=0.01, rely=0.01)

    sideBar = tk.Frame(frame, width=100, bg="white")
    sideBar.pack(fill=tk.Y, side=tk.LEFT)

    print(len(bots))
    for bot in bots:
        tk.Button(sideBar, text=bot.get_name(), padx=10, pady=5, fg="black", bg="#A9A9A9", command=lambda : edit_bot(bot)).pack()

    logoimg = PhotoImage(file= "gui/bab.png")
    logo = tk.Button(sideBar, image= logoimg, borderwidth=0, fg="white", bg="#FFFFFF", command=githublink)
    logo.pack( padx=20, pady=20)

    existingbotsimg = PhotoImage(file= "gui/existingbots.png")
    existingbots = tk.Button(sideBar, image= existingbotsimg, borderwidth=0, fg="white", bg="#FFFFFF")
    existingbots.pack( padx=20, pady=20)

    createimg = PhotoImage(file= "gui/createbutton.png")
    create = tk.Button(sideBar, image= createimg, borderwidth=0, fg="white", bg="#FFFFFF", command=lambda : create_bot(frame, bots))
    create.pack( padx=20, pady=20)

    fileexpimg = PhotoImage(file= "gui/files.png")
    fileexp = tk.Button(sideBar, image= fileexpimg, borderwidth=0, fg="white", bg="#FFFFFF", command=lambda : create_bot(frame, bots))
    fileexp.pack( padx=20, pady=20)

    print(len(bots))
    root.protocol("WM_DELETE_WINDOW", on_closing(bots))
    root.mainloop()
