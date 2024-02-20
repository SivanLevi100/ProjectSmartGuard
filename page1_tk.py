
#Page 1 - the home page of the application - login

import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
import pygame
import time
import tkinter as tk

# ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\owner\Desktop\לימודים - שנה ג\סמסטר א\Tkinter-Designer-master (1)\Tkinter-Designer-master\build\assets\frame0")

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH1 = OUTPUT_PATH / Path(r"Images_UI/frame_1")

#A function that accepts a path and returns a relative path
def relative_to_assets1(path: str) -> Path:
    return ASSETS_PATH1 / Path(path)


x = 300
y = 30

window = Tk()
window.geometry(f'+{x}+{y}')
window.geometry("440x600")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=650,
    width=440,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets1("image_1.png"))
image_1 = canvas.create_image(220.0,98.0,image=image_image_1)

entry_image_1 = PhotoImage(
    file=relative_to_assets1("entry_1.png"))
entry_bg_1 = canvas.create_image(223.0,358.5,image=entry_image_1)
entry_1 = Entry(
    bd=0,
    bg="#FF0000",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=112.0,
    y=340.0,
    width=222.0,
    height=35.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets1("entry_2.png"))
entry_bg_2 = canvas.create_image(223.0,455.5,image=entry_image_2)
entry_2 = Entry(
    bd=0,
    bg="#FF0000",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=112.0,
    y=437.0,
    width=222.0,
    height=35.0
)


#Function - button click event
def click_button_connect():
    #Added a button click sound
    # pygame.init()
    # pygame.mixer.music.load("ButtonSoundEffect.mp3")
    # pygame.mixer.music.play()

    window.destroy()
    subprocess.call(['python', 'page2_tk.py'])  # Opening the requested page


button_connect = PhotoImage(
    file=relative_to_assets1("button_1.png"))

button_Connect = Button(
    image=button_connect,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click_button_connect(),
    relief="flat",
    #state="disabled"
    state=tk.DISABLED
)
button_Connect.place(
    x=168.0,
    y=517.0,
    width=110.0,
    height=41.0
)

#If the username and password are correct then the button will be available
def check_entries(*args):
    if entry_1.get() == 'Admin' and entry_2.get() == '100':
        button_Connect.config(state=tk.ACTIVE)
    else:
        button_Connect.config(state=tk.DISABLED)

#If you enter text in the username and password field, then the function that checks the correctness of the input is called
entry_1.bind("<KeyRelease>", check_entries)
entry_2.bind("<KeyRelease>", check_entries)


image_image_2 = PhotoImage(
    file=relative_to_assets1("image_2.png"))
image_2 = canvas.create_image(
    73.0,
    356.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets1("image_3.png"))
image_3 = canvas.create_image(
    73.0,
    448.0,
    image=image_image_3
)

canvas.create_text(
    131.0,
    178.0,
    anchor="nw",
    text="We happy to see you!\n",
    fill="#000000",
    font=("InriaSans Bold", 16 * -1)
)

canvas.create_text(
    109.0,
    233.0,
    anchor="nw",
    text="Please connect first...",
    fill="#000000",
    font=("InriaSans Bold", 24 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets1("image_4.png"))
image_4 = canvas.create_image(303.0, 185.0,image=image_image_4)

canvas.create_text(
    105.0,
    416.0,
    anchor="nw",
    text="Enter a password",
    fill="#000000",
    font=("InriaSans Bold", 14 * -1)
)

canvas.create_text(
    105.0,
    322.0,
    anchor="nw",
    text="Enter a username",
    fill="#000000",
    font=("InriaSans Bold", 14 * -1)
)

window.resizable(False, False)
window.mainloop()
