import tkinter.messagebox

import Computer_Camera_without_pre_model

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\owner\Desktop\לימודים - שנה ג\סמסטר א\בינה מלאכותית וישומה\Tkinter-Designer-master\Tkinter-Designer-master\build\assets\frame0")
#ASSETS_PATH1=Path("/ProjectSmartGuard/Images_UI/")

#def relative_to_assets1(path: str) -> Path:
#    return ASSETS_PATH1 / Path(path)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("436x645")
window.configure(bg = "#F5F5F5")


canvas = Canvas(
    window,
    bg = "#F5F5F5",
    height = 645,
    width = 436,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=122.0,
    y=86.0,
    width=168.0,
    height=122.0
)

def click_button_2():
    print("work")
    label = Computer_Camera_without_pre_model.main("NV_183.mp4")
   # Tk.messagebox.showerror(label)
    Tk.title(label)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))

button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click_button_2(),
    relief="flat"
)

button_2.place(
    x=45.0,
    y=269.0,
    width=182.0,
    height=82.0
)



button_3 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click_button_2(),
    relief="flat"
)


button_3.place(
    x=80.0,
    y=350.0,
    width=182.0,
    height=82.0
)

window.resizable(False, False)
window.mainloop()
