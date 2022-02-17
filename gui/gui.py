import os
import tkinter as tk
from tkinter import filedialog, Text

def run_bot():
    os.system('bash gui/run.sh')

def launch():
    root = tk.Tk()

    canvas = tk.Canvas(root,height=700,width=700,bg="#A9A9A9")
    canvas.pack()
    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.98,relheight=0.98, relx=0.01, rely=0.01)

    run = tk.Button(frame, text="Run", padx=10, pady=5, fg="white", bg="#A9A9A9", command=run_bot)
    run.pack()

    root.mainloop()