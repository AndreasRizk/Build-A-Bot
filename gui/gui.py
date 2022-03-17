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

def clear(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def create_new_bot(bots, name, frame):
    clear(frame)

    for widget in frame.winfo_children():
        widget.destroy()
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
    clear(frame)

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

    workspace = tk.Frame(frame, width=600, bg="white")
    workspace.pack(fill=tk.Y, side=tk.RIGHT)

    print(len(bots))
    for bot in bots:
        tk.Button(sideBar, text=bot.get_name(), padx=10, pady=5, fg="black", bg="#A9A9A9", command=lambda : edit_bot(bot)).pack()

    logoimg = PhotoImage(file= "gui/bab.png")
    logo = tk.Button(sideBar, image= logoimg, borderwidth=0, fg="white", bg="#FFFFFF", command=githublink)
    logo.pack( padx=20, pady=20)

    #buttons on the sidebar
    existingbotsimg = PhotoImage(file= "gui/existingbots.png")
    existingbots = tk.Button(sideBar, image= existingbotsimg, borderwidth=0, fg="white", bg="#FFFFFF")
    existingbots.pack( padx=20, pady=20)

    createimg = PhotoImage(file= "gui/createbutton.png")
    create = tk.Button(sideBar, image= createimg, borderwidth=0, fg="white", bg="#FFFFFF", command=lambda : create_bot(workspace, bots))
    create.pack( padx=20, pady=20)

    fileexpimg = PhotoImage(file= "gui/files.png")
    fileexp = tk.Button(sideBar, image= fileexpimg, borderwidth=0, fg="white", bg="#FFFFFF", command=lambda : create_bot(workspace, bots))
    fileexp.pack( padx=20, pady=20)

    #Initial help page
    help_label = tk.Label(workspace, text="Help", font=('Helvatical bold',20), relief=tk.RIDGE, borderwidth= 0, width=27, height=3, anchor="w", bg="#FFFFFF", fg="black")
    help_label.pack(pady=20)
    textframe = tk.Frame(workspace, width=200, height=100, bg="white")
    textframe.pack()
    scroll = Scrollbar(textframe)
    scroll.pack(side=RIGHT, fill=Y)
    help = Text(textframe, width=50, height=20, wrap=WORD, yscrollcommand = scroll.set)
    for i in range(20): 
        help.insert(END,"this is some text\n")
    help.config(state=DISABLED)
    help.pack(side=TOP, fill=X)
    scroll.config(command=help.yview)

    print(len(bots))
    root.protocol("WM_DELETE_WINDOW", on_closing(bots))
    root.mainloop()
