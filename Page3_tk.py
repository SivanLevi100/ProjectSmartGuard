
import subprocess
import Computer_Camera_without_pre_model
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\owner\Desktop\לימודים - שנה ג\סמסטר א\Tkinter-Designer-master (1)\Tkinter-Designer-master\build\assets\frame0")


ASSETS_PATH1=OUTPUT_PATH/Path(r"Images_UI/frame_3")
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
def click_b1():
    window.destroy()
    subprocess.call(['python', 'page2_tk.py'])


canvas.place(x = 0, y = 0)
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
    x=19.0,
    y=15.0,
    width=64.0,
    height=49.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets1("image_1.png"))
image_1 = canvas.create_image(
    220.0,
    111.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets1("image_2.png"))
image_2 = canvas.create_image(
    200.0,
    183.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets1("image_3.png"))
image_3 = canvas.create_image(
    17.0,
    248.0,
    image=image_image_3
)
def click_b2():
    label = Computer_Camera_without_pre_model.main("NV_183.mp4")

button_image_2 = PhotoImage(
    file=relative_to_assets1("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click_b2(),
    relief="flat"
)
button_2.place(
    x=298.0,
    y=233.0,
    width=112.0,
    height=29.0
)

canvas.create_text(
    34.0,
    238.0,
    anchor="nw",
    text="Please select a video to classify",
    fill="#000000",
    font=("InriaSans Bold", 16 * -1)
)
window.resizable(False, False)
window.mainloop()
