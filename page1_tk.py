
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\owner\Desktop\לימודים - שנה ג\סמסטר א\Tkinter-Designer-master (1)\Tkinter-Designer-master\build\assets\frame0")

ASSETS_PATH1=OUTPUT_PATH/Path(r"C:\Users\owner\PycharmProjects\ProjectSmartGuard1\ProjectSmartGuard\Images_UI\frame_1")
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
    220.0,
    98.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets1("entry_1.png"))
entry_bg_1 = canvas.create_image(
    223.0,
    358.5,
    image=entry_image_1
)
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
entry_bg_2 = canvas.create_image(
    223.0,
    455.5,
    image=entry_image_2
)
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
    x=168.0,
    y=517.0,
    width=110.0,
    height=41.0
)

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
image_4 = canvas.create_image(
    303.0,
    185.0,
    image=image_image_4
)

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
