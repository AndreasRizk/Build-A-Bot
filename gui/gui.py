import os
import tkinter as tk
from PIL import Image, ImageTk

def run_bot():
    os.system('start cmd /k python -m bab"')

def kill_bot():
    os.system('')

def launch():
    root = tk.Tk()
    root.title("Build-A-Bot")
    root.iconbitmap("logo.ico")

    canvas = tk.Canvas(root,height=700,width=700,bg="#A9A9A9")
    canvas.grid(columnspan=2)
    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.98,relheight=0.98, relx=0.01, rely=0.01)

    run = tk.Button(frame, text="Run", padx=10, pady=5, fg="white", bg="#A9A9A9", command=run_bot)
    run.pack()

    kill = tk.Button(frame, text="Shutdown", padx=10, pady=5, fg="white", bg="#A9A9A9", command=kill_bot)
    kill.pack()

    root.mainloop()