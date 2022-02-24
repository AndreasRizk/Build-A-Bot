import os
import pickle
import dill
import subprocess
import tkinter as tk
from tkinter import filedialog, Text
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
    tk.Button(text=bot.get_name()+"start", padx=10, pady=5, fg="black", bg="#A9A9A9", command=bot.run_bot).pack()
    tk.Button(text=bot.get_name()+"stop", padx=10, pady=5, fg="black", bg="#A9A9A9", command=bot.stop_bot).pack()


def create_bot(frame, bots):
    print(len(bots))
    title = tk.Label( text="Name of Bot", relief=tk.RIDGE, width=15)
    name = tk.Entry( relief=tk.SUNKEN, width=10)

    run = tk.Button( text="Run", padx=10, pady=5, fg="black", bg="#A9A9A9", command=lambda : create_new_bot(bots, name, frame))

    title.pack()
    name.pack()
    run.pack()

def on_closing(bots):
    with open("gui/data/existing_bots","wb") as f:
        dill.dump(bots,f)


def launch():
    root = tk.Tk()

    bots = []

    if (exists("gui/data/existing_bots")):
        with open("gui/data/existing_bots","rb") as f:
            bots = dill.load(f)

    canvas = tk.Canvas(root,height=700,width=700,bg="#A9A9A9")
    canvas.pack()

    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.98,relheight=0.98, relx=0.01, rely=0.01)

    sideBar = tk.Frame(frame, width=70, bg="grey")
    sideBar.pack(fill=tk.Y, side=tk.LEFT)

    print(len(bots))
    for bot in bots:
        tk.Button(sideBar, text=bot.get_name(), padx=10, pady=5, fg="black", bg="#A9A9A9", command=lambda : edit_bot(bot)).pack()

    create = tk.Button(sideBar, text="Create New Bot", padx=10, pady=5, fg="black", bg="#A9A9A9", command=lambda : create_bot(frame, bots))
    create.pack()

    print(len(bots))
    root.protocol("WM_DELETE_WINDOW", on_closing(bots))
    root.mainloop()
