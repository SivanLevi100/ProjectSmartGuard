

import subprocess
import threading
from pathlib import Path
import real_time_main
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox

import tkinter as tk
import datetime

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH1=OUTPUT_PATH/Path(r"Images_UI/frame_4")

def relative_to_assets1(path: str) -> Path:
    return ASSETS_PATH1 / Path(path)


x = 350
y = 80
window = Tk()
window.geometry(f'+{x}+{y}')


window.geometry("440x650")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 650,
    width = 440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

image_image_1 = PhotoImage(
    file=relative_to_assets1("image_1.png"))
image_title = canvas.create_image(220.0,110.0,image=image_image_1)

global cls
cls = "none"
label = tk.Label(window, text="The classification is: " + cls, bg="white", fg="blue")

global now


def click_button_real_time():
    print("real time button")

    now = datetime.datetime.now()
    now = now.strftime("%H:%M:%S")

    label1 = tk.Label(window, text="The time is: " + str(now),bg="white",fg="blue",font=("Arial", 10))
    label1.pack()
    label1.place(x="40",y="510")

    cls = real_time_main.main(0)
    if cls == "Violence":
        label.config(text="The classification is: " + cls+"!!!",fg="red",font=("Arial", 16))
    else:
        label.config(text="The classification is: " + cls, fg="green",font=("Arial", 10))
    label.pack()
    label.place(x="40", y="480")


button_image_1 = PhotoImage(
    file=relative_to_assets1("button_1.png"))
button_real_time = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click_button_real_time(),
    relief="flat"
)
button_real_time.place(
    x=76.0,
    y=363.0,
    width=289.0,
    height=84.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets1("image_2.png"))
image_camera = canvas.create_image(
    220.0,
    303.0,
    image=image_image_2
)
def click_home():
    window.destroy()
    subprocess.call(['python', 'page2_tk.py'])

button_image_2 = PhotoImage(
    file=relative_to_assets1("button_2.png"))
button_home = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click_home(),
    relief="flat",
    bg="white"
)
button_home.place(
    x=9.0,
    y=14.0,
    width=64.0,
    height=49.0
)

window.resizable(False, False)
window.mainloop()

