import os, signal
import dill as pickle
import subprocess
import shutil
import tkinter as tk
import tkinter.filedialog as tkf
import webbrowser
from tkinter import *
from tkhtmlview import *
from os.path import exists
import markdown
from sys import platform

sidebar_color = "#1e2124"
main_color = "#424549"
button_color = "#7289da"

#############CLASS##################
class Bot:
    def __init__(self, name, token, guild_id):
        self.name_ = name
        self.token_ = token
        self.guild_id_ = guild_id
        self.obj_ = None
        self.running_ = False

    def run_bot(self):
        if self.obj_ == None:
            self.obj_ = subprocess.Popen(['python', '-m', 'bab', self.token_, self.guild_id_, f"./bab/{self.name_}_extensions"])
            self.running_ = True
            save()

    def stop_bot(self):
        self.running_ = False
        save()
        if not self.obj_ == None:
            if platform == "win32":
                print(self.obj_.pid)
                self.obj_.kill()
            else:
                print(self.obj_.pid)
                os.kill(self.obj_.pid, signal.SIGKILL)

        self.obj_ = None
        save()

#############Data Management##################
Bots = {}
if (exists("gui/data/existing_bots")):
        with open("gui/data/existing_bots","rb") as f:
            Bots = pickle.load(f)
            print("loaded")
            print("bots = ")
            print(Bots)

def save():
    if not (exists("gui/data/")):
        os.mkdir("gui/data/")
    with open("gui/data/existing_bots","wb") as f:
        print("dumped")
        print("bots = ")
        print(Bots)
        pickle.dump(Bots,f)


#############Helper Functions##################
def githublink():
    webbrowser.open_new(r"https://github.com/Andy-8/Build-A-Bot")

def clear(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    frame.grid_propagate(0)
    frame.pack_propagate(0)

def botKILL(frame,bot):
    bot.stop_bot()
    edit_bot(frame,bot)

def botRUN(frame,bot):
    bot.run_bot()
    bot_running(frame,bot)

def create_new_bot(name, token, guild_id,frame):
    Bots[name] = Bot(name, token, guild_id)
    save()
    edit_bot(frame,Bots[name])

def open_file(frame):
    file_path = tkf.askopenfile(mode='r', filetypes=[('Python files', '*py')])
    if file_path is not None:
        file_name = os.path.basename(file_path.name)
        shutil.copyfile(file_path.name, "extensions/"+file_name)
        package_handler(frame)

def include_ext(dir_name, exe):
    if exists(dir_name+"/"+exe):
        os.remove(dir_name+"/"+exe)
    else:
        shutil.copyfile("extensions/"+exe, dir_name+"/"+exe)

def on_close():
    print("Would have errored")
    #for bot in Bots.values():
    #    bot.stop_bot()

def update_bot(name, token, guild_id, frame, bot):
    print(name,token,guild_id)
    if name == bot.name_ or len(name)==0:
        if not len(token) == 0:
            bot.token_ = token
        if not len(guild_id) == 0:
            bot.guild_id_ = guild_id
        print("Same")
    else:
        if name in Bots:
            pass #error for creating duplicate bot
        dir_name = f"bab/{bot.name_}_extensions"
        os.rename(dir_name,f"bab/{name}_extensions")
        if len(token) == 0:
            token=bot.token_
        if len(guild_id) == 0:
            guild_id = bot.guild_id_
        Bots.pop(bot.name_)
        bot = Bots[name] = Bot(name, token, guild_id)

        print("New")
    print(bot.name_,bot.token_,bot.guild_id_)
    edit_bot(frame,bot)

#############Frame Loaders##################
def bot_selection(frame):
    clear(frame)
    if len(Bots)==0:
        no_bots = tk.Label(frame, text="You have not created any bots!", font=('Arial',20), relief=tk.RIDGE, borderwidth= 0, height=3, bg=main_color, fg="black")
        no_bots.pack()
        create = tk.Button(frame, text="Create one!", padx=30, pady=20, font=('Arial',12), fg="black", bg=button_color, command=lambda : create_bot(frame))
        create.pack()

    count = 0
    for bot_name, bot in Bots.items():
        background = button_color
        if bot.running_: #if running make color green
            background = "#008000"
        x = tk.Button(frame, text=bot_name, padx=30, pady=20, font=('Arial',12), fg="black", bg=background, command=lambda bot=bot: edit_bot(frame, bot))
        x.grid(row=count//3,column=count%3,padx=90,pady=50)
        count+=1

def bot_running(frame, bot):
    clear(frame)
    stop = tk.Button( frame, text="Stop", anchor="center", padx=10, pady=10, font=('Arial',20), fg="black", bg=button_color, command=lambda : botKILL(frame,bot))
    stop.pack()

def bot_delete(frame, bot):
    dir_name = f"bab/{bot.name_}_extensions"
    shutil.rmtree(dir_name, ignore_errors=True)
    del Bots[bot.name_]
    save()
    bot_selection(frame)

def edit_bot_data(frame,bot):
    clear(frame)

    name_title = tk.Label( frame, bg=main_color, text="Name of Bot", anchor="center", pady=50, padx=350, width=15, font=('Arial',20))
    name = tk.Entry( frame, relief=tk.SUNKEN, width=30, font=('Arial',20))
    #name.insert(bot.name_,0)

    token_title = tk.Label( frame, bg=main_color, text="Bot Token", anchor="center", pady=50, padx=350, width=15, font=('Arial',20))
    token = tk.Entry( frame, relief=tk.SUNKEN, width=30, font=('Arial',20))
    #token.insert(bot.token_,0)

    guild_title = tk.Label( frame, bg=main_color, text="Guild ID", anchor="center", pady=50, padx=350, width=15, font=('Arial',20))
    guild_id = tk.Entry( frame, relief=tk.SUNKEN, width=30, font=('Arial',20))
    #guild_id.insert(bot.guild_id_,0)

    spacer = tk.Label( frame, bg=main_color, anchor="center", pady=30, width=15)

    create = tk.Button( frame, text="Update", anchor="center", padx=10, pady=20, font=('Arial',20), fg="black", bg=button_color, command=lambda : update_bot(name.get(), token.get(), guild_id.get(), frame, bot))

    name_title.pack()
    name.pack()
    token_title.pack()
    token.pack()
    guild_title.pack()
    guild_id.pack()
    spacer.pack()
    create.pack()

def edit_bot(frame, bot):
    if bot.running_:
        bot_running(frame,bot)
    else:
        clear(frame)
        dir_name = f"bab/{bot.name_}_extensions"
        if not exists(dir_name):
            os.mkdir(dir_name)
            os.mkdir(f"{dir_name}/data")

        dir_list = os.listdir("extensions")
        dir_list = [dirName for dirName in dir_list if 'py' in dirName.lower()]

        count=0
        for i in dir_list:
            iVar = tk.IntVar()
            c1 = tk.Checkbutton(frame, anchor="center", text=i, variable=iVar, onvalue=0, offvalue=1, command=lambda exe = i:include_ext(dir_name, exe))
            c1.grid(row=count//3,column=count%3, padx=10, pady=10)
            count+=1
        delete = tk.Button( frame, text="Delete", padx=10, pady=10, font=('Arial',20), fg="black", bg=button_color, command=lambda : bot_delete(frame,bot))
        delete.grid(row=count//3+1,column=0, padx=30, pady=30)

        edit = tk.Button( frame, text="Edit", padx=10, pady=10, font=('Arial',20), fg="black", bg=button_color, command=lambda : edit_bot_data(frame,bot))
        edit.grid(row=count//3+1,column=1, padx=30, pady=30)

        run = tk.Button( frame, text="Run", padx=10, pady=10, font=('Arial',20), fg="black", bg=button_color, command=lambda : botRUN(frame,bot))
        run.grid(row=count//3+1,column=2, padx=30, pady=30)

def create_bot(frame):
    clear(frame)

    name_title = tk.Label( frame, bg=main_color, text="Name of Bot", anchor="center", pady=50, padx=350, width=15, font=('Arial',20))
    name = tk.Entry( frame, relief=tk.SUNKEN, width=30, font=('Arial',20))

    token_title = tk.Label( frame, bg=main_color, text="Bot Token", anchor="center", pady=50, padx=350, width=15, font=('Arial',20))
    token = tk.Entry( frame, relief=tk.SUNKEN, width=30, font=('Arial',20))

    guild_title = tk.Label( frame, bg=main_color, text="Guild ID", anchor="center", pady=50, padx=350, width=15, font=('Arial',20))
    guild_id = tk.Entry( frame, relief=tk.SUNKEN, width=30, font=('Arial',20))

    spacer = tk.Label( frame, bg=main_color, anchor="center", pady=30, width=15)

    create = tk.Button( frame, text="Create", anchor="center", padx=10, pady=20, font=('Arial',20), fg="black", bg=button_color, command=lambda : create_new_bot(name.get(), token.get(), guild_id.get(), frame))

    name_title.pack()
    name.pack()
    token_title.pack()
    token.pack()
    guild_title.pack()
    guild_id.pack()
    spacer.pack()
    create.pack()

def help(frame):
    clear(frame)
    #Initial help page
    ghimg = PhotoImage(file= "gui/images/github.png")
    github_button = tk.Button(frame, image= ghimg, fg="white", bg=main_color, borderwidth=0,  command=githublink)
    github_button.image = ghimg
    github_button.pack()
    github_button.config(highlightthickness=0)


    html = ''
    with open('README.md', 'r') as f:
        for line in f.readlines():
            if line[0]=='!' or line[0]=='`':
                continue
            html += markdown.markdown(line)
    readme = HTMLScrolledText(frame)
    readme.set_html(html)
    readme.pack(pady=15, padx=15, fill=BOTH)
    readme.fit_height()

def package_handler(frame):
    clear(frame)

    ph_label = tk.Label(frame, text="Package Handler", font=('Arial',20), relief=tk.RIDGE, borderwidth= 0, height=3, anchor="w", bg=main_color, fg="black")
    ph_label.grid(row=0, column=0, sticky=NW)

    scroll = Scrollbar(frame)
    scroll.grid(row=1, column=1, sticky=NS)

    exes = Text(frame, font=('Arial',15), wrap=WORD, height=24, width=60, yscrollcommand = scroll.set)

    dir_list = os.listdir("extensions")
    dir_list = [dirName for dirName in dir_list if 'py' in dirName.lower()]

    for name in dir_list:
        exes.insert(END,name+"\n")
    exes.config(state=DISABLED)
    # exes.pack(side=tk.TOP, fill=BOTH)
    exes.grid(row=1, column=0)
    scroll.config(command=exes.yview)

    new_exes = tk.Label(frame, text='Upload new extension ',bg=main_color, fg="black")
    new_exes.grid(row=2, column=0, padx=10)

    adharbtn = tk.Button(frame, text ='Choose File', bg=button_color, command = lambda:open_file(frame))
    adharbtn.grid(row=2, column=1)

def launch():
    root = tk.Tk()
    root.title("Build-A-Bot")
    root.iconbitmap("logo.ico")
    root.resizable(width=False, height=False)

    canvas = tk.Canvas(root,height=750,width=1000,bg=main_color)
    canvas.pack()


    frame = tk.Frame(root, bg=sidebar_color)
    frame.place(relwidth=1,relheight=1, relx=0.0, rely=0.0)

    sideBar = tk.Frame(frame, width=100, bg=sidebar_color)
    sideBar.pack(fill=tk.Y, side=tk.LEFT)

    workspace = tk.Frame(frame, width=root.winfo_screenwidth() - 100, bg=main_color)
    workspace.pack(fill=tk.Y, side=tk.RIGHT)

    #buttons on the sidebar
    logoimg = PhotoImage(file= "gui/images/bab.png")
    logo = tk.Button(sideBar, image= logoimg, border=0, command=lambda : help(workspace))
    logo.pack(padx=35, pady=35)
    logo.config(highlightthickness=0)

    existingbotsimg = PhotoImage(file= "gui/images/existingbots.png")
    existingbots = tk.Button(sideBar, image= existingbotsimg, border=0, command=lambda : bot_selection(workspace))
    existingbots.pack( padx=35, pady=35)
    existingbots.config(highlightthickness=0)

    createimg = PhotoImage(file= "gui/images/createbutton.png")
    create = tk.Button(sideBar, image= createimg, border=0, command=lambda : create_bot(workspace))
    create.pack(padx=35, pady=35)
    create.config(highlightthickness=0)

    fileexpimg = PhotoImage(file= "gui/images/files.png")
    fileexp = tk.Button(sideBar, image= fileexpimg, border=0, command=lambda : package_handler(workspace))
    fileexp.pack(padx=35, pady=35)
    fileexp.config(highlightthickness=0)

    help(workspace)

    #root.protocol("WM_DELETE_WINDOW", on_close())
    root.mainloop()

if __name__ == "__main__":
    launch()
