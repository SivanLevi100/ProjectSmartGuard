
#Page 4 - Real-time classification

import subprocess
import threading
from pathlib import Path
import real_time_main
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox
import tkinter as tk
import datetime
import pygame

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH1=OUTPUT_PATH/Path(r"Images_UI/frame_4")

#A function that accepts a path and returns a relative path
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

global now
global cls
cls = "none"
#A label showing the video's classification
label = tk.Label(window, text="The classification is: " + cls, bg="white", fg="blue")

#Function - button click event
def click_button_real_time():
    # Added a button click sound
    pygame.init()
    pygame.mixer.music.load("ButtonSoundEffect.mp3")
    pygame.mixer.music.play()

    #The time when a button is pressed - classification in real time
    now = datetime.datetime.now()
    now = now.strftime("%H:%M:%S")

    #A label that shows the time
    label1 = tk.Label(window, text="The time is: " + str(now),bg="white",fg="blue",font=("Arial", 10))
    label1.pack()
    label1.place(x="40",y="510")

    cls = real_time_main.main(0) #Opening the computer camera

    if cls == "Violence":
        label.config(text="The classification is: " + cls+"!!!",fg="red",font=("Arial", 16))#Label showing classification: Violence
    else:
        label.config(text="The classification is: " + cls, fg="green",font=("Arial", 12))#Label showing classification: Non Violence
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
image_camera = canvas.create_image(220.0, 303.0, image=image_image_2)

#Function - button click event
def click_home():
    # Added a button click sound
    pygame.init()
    pygame.mixer.music.load("ButtonSoundEffect.mp3")
    pygame.mixer.music.play()
    window.destroy()
    subprocess.call(['python', 'page2_tk.py']) #Opening the requested page

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

