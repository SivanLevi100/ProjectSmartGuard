
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
import subprocess
import threading
from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas,Entry, Text, Button, PhotoImage
from tkinter import messagebox
#import real_time_main


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH1=OUTPUT_PATH/Path(r"Images_UI/frame_2")

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
def click_button_exit():
    window.destroy()
    subprocess.call(['python', 'page1_tk.py'])

button_exit = PhotoImage(
    file=relative_to_assets1("image_5.png"))
button_Exit = Button(
    image=button_exit,
    bg="white",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click_button_exit(),
    relief="flat"
)
button_Exit.place(
    x=14.0,
    y=31.0,
    width=27.0,
    height=27.06114959716797
)

image_image_1 = PhotoImage(
    file=relative_to_assets1("image_1.png"))
image_title = canvas.create_image(220.0,110.0,image=image_image_1)

image_image_2 = PhotoImage(
    file=relative_to_assets1("image_2.png"))
image_view_icon = canvas.create_image(115.0,277.0,image=image_image_2)

def show_message():
    messagebox.showinfo("Loading", "Loading the classification model")

def click_button_Class():
    window.destroy()
    x = threading.Thread(target=show_message)
    x.start()
    subprocess.call(['python', 'page3_tk.py'])


button_class = PhotoImage(
    file=relative_to_assets1("button_2.png"))
button_Class = Button(
    image=button_class,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click_button_Class(),
    relief="flat"
)
button_Class.place(
    x=239.0,
    y=302.0,
    width=146.0,
    height=40.0
)
def click_button_real_time():
    print("real time button")
    window.destroy()
    x = threading.Thread(target=show_message)
    x.start()
    subprocess.call(['python', 'page4_tk.py'])


button_real_time = PhotoImage(
    file=relative_to_assets1("button_3.png"))
button_Real_Time = Button(
    image=button_real_time,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click_button_real_time(),
    relief="flat"
)
button_Real_Time.place(
    x=39.0,
    y=302.0,
    width=146.0,
    height=40.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets1("image_3.png"))
image_search_icon = canvas.create_image(311.0,277.0, image= image_image_3)

def click_Violent_Video():
    window.destroy()
    subprocess.call(['python', 'page4_tk.py'])

# button_violent_videos = PhotoImage(
#     file=relative_to_assets1("button_4.png"))
# button_Violent_Videos = Button(
#     image=button_violent_videos,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: click_Violent_Video(),
#     relief="flat"
# )
# button_Violent_Videos.place(
#     x=160.0,
#     y=456.0,
#     width=120.0,
#     height=55.0
# )

# image_image_4 = PhotoImage(
#     file=relative_to_assets1("image_4.png"))
# image_warning_icon = canvas.create_image(220.0,430.0,image=image_image_4)

window.resizable(False, False)
window.mainloop()
