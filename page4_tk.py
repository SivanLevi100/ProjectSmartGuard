

import subprocess
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\owner\Desktop\לימודים - שנה ג\סמסטר א\Tkinter-Designer-master (1)\Tkinter-Designer-master\build\assets\frame0")


ASSETS_PATH1=OUTPUT_PATH/Path(r"Images_UI/frame_4")
def relative_to_assets1(path: str) -> Path:
    return ASSETS_PATH1 / Path(path)



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

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
image_1 = canvas.create_image(
    223.0,
    105.0,
    image=image_image_1
)
def click_b1():
    window.destroy()
    subprocess.call(['python', 'page2_tk.py'])

button_image_1 = PhotoImage(
    file=relative_to_assets1("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click_b1(),
    relief="flat"
)
button_1.place(
    x=16.0,
    y=9.0,
    width=51.0,
    height=49.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets1("image_2.png"))
image_2 = canvas.create_image(
    231.0,
    195.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
