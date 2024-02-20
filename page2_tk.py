
#Page 2 - There are 2 options - one is classification of existing videos and the other is classification in real time

import subprocess
import threading
from pathlib import Path
from tkinter import Tk, Canvas,Entry, Text, Button, PhotoImage
from tkinter import messagebox
import pygame

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH1=OUTPUT_PATH/Path(r"Images_UI/frame_2")

#A function that accepts a path and returns a relative path
def relative_to_assets1(path: str) -> Path:
    return ASSETS_PATH1 / Path(path)

x = 300
y = 30

window = Tk()
window.geometry(f'+{x}+{y}')
window.geometry("440x600")
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

#Function - button click event
def click_button_exit():
    # Added a button click sound
    pygame.init()
    pygame.mixer.music.load("ButtonSoundEffect.mp3")
    pygame.mixer.music.play()
    window.destroy()
    subprocess.call(['python', 'page1_tk.py']) #Opening the requested page

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

#messagebox - Loading the classification model
def show_message():
    messagebox.showinfo("Loading", "Loading the classification model")

#Function - button click event
def click_button_Class():
    #Added a button click sound
    pygame.init()
    pygame.mixer.music.load("ButtonSoundEffect.mp3")
    pygame.mixer.music.play()
    window.destroy()
    x = threading.Thread(target=show_message)
    x.start()
    subprocess.call(['python', 'page3_tk.py']) #Opening the requested page


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

#Function - button click event
def click_button_real_time():
    # Added a button click sound
    pygame.init()
    pygame.mixer.music.load("ButtonSoundEffect.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()
    window.destroy()
    x = threading.Thread(target=show_message)
    x.start()
    subprocess.call(['python', 'page4_tk.py']) #Opening the requested page


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


window.resizable(False, False)
window.mainloop()

# def click_Violent_Video():
#     window.destroy()
#     subprocess.call(['python', 'page4_tk.py'])

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
