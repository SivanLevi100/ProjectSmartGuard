
#Page 3 - List of unclassified videos - To classify a video, click on its name in the list and receive the classification.

import subprocess
import Videos_main
from pathlib import Path
import time
import tkinter.ttk as ttk
from tkinter import simpledialog
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from PIL import ImageTk, Image
import pygame

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH1=OUTPUT_PATH/Path(r"Images_UI/frame_3")

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

#Function - button click event
def click_home():
    # Added a button click sound
    pygame.init()
    pygame.mixer.music.load("ButtonSoundEffect.mp3")
    pygame.mixer.music.play()
    window.destroy()
    subprocess.call(['python', 'page2_tk.py'])#Opening the requested page

button_image_1 = PhotoImage(
    file=relative_to_assets1("button_1.png"))
button_home = Button(
    bg="white",
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click_home(),
    relief="flat"
)
button_home.place(
    x=19.0,
    y=15.0,
    width=64.0,
    height=49.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets1("image_1.png"))
image_title = canvas.create_image(220.0,111.0,image=image_image_1)

image_image_2 = PhotoImage(
    file=relative_to_assets1("image_2.png"))
image_unclassifiedVideos = canvas.create_image(200.0,183.0,image=image_image_2)


image_image_3 = PhotoImage(
    file=relative_to_assets1("image_3.png"))
image_search_icon = canvas.create_image(17.0,248.0,image=image_image_3)

canvas.create_text(
    34.0,
    238.0,
    anchor="nw",
    text="Please select a video to classify",
    fill="#000000",
    font=("InriaSans Bold", 16 * -1)
)

global cls
cls = "none"
#A label showing the video's classification
label = tk.Label(window, text="The classification is: " + cls, bg="white", fg="blue")

#An array containing all existing videos before classification
videos_list1=[
    ["A Prague kindergarte", "None"],  # NV
    ["Children hugging their father", "None"],  # NV
    ["Camera phone at school", "None"],  # V
    ["People are crossing a crosswalk", "None"],  # NV
    ["Driver violence on the road", "None"],  # V
    ["Gun battle", "None"],  # V
    ["people at bus station", "None"],  # NV
    ["Security camera in the store", "None"],  # V
    ["people walk in mall", "None"],  # NV
    ["pupils in class", "None"],  # NV
    ["Security camera on the street", "None"],  # V
    ["Pupils leave the classroom", "None"],  # NV
    ["Violence against police officers", "None"],  # V
    ["Violence in a hospital", "None"],  # V
    ["Running competition", "None"],  # NV
    ["The chef games", "None"],  # NV
    ["Violence in Jerusalem on Jaffa Street", "None"],  # V
    ["X factor israel", "None"]  # NV
    ]

def read_data():
   for index, line in enumerate(videos_list1):
      tree.insert('', tk.END, text = line[0], values = line[1:])

columns = ("cls")

tree= ttk.Treeview(window, columns=columns ,height = 14)
tree.pack(padx = 5, pady = 5)
tree.heading('#0', text='Name videos')
tree.heading('cls', text='Classification')
tree.place(x=20,y=300.0)
read_data()


#Function - Click event on an item in the list.
def item_selected(event):
    # Added a button click sound
    pygame.init()
    pygame.mixer.music.load("ButtonSoundEffect.mp3")
    pygame.mixer.music.play()

    selected_items = tree.selection()
    item = tree.item(selected_items[0])
    # A call to the classification function
    cls = Videos_main.main("youtube_vidoes/" + item['text'] +".mp4")
    if cls == "Violence":
        label.config(text="The classification is: " + cls+"!!!",fg="red",font=("Arial", 16))#Label showing classification: Violence
        #Play a warning sound
        pygame.init()
        pygame.mixer.music.load("WARNING_SOUND.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play()
        time.sleep(3)
        pygame.mixer.music.stop()
    else:
        label.config(text="The classification is: " + cls, fg="green",font=("Arial", 12))#Label showing classification: Non Violence
    label.pack()
    #Inserting the classification into the list
    if selected_items:
        item = selected_items[0]
        tree.set(item, "#1", cls)

    # tree.tag_configure('color_text', foreground='red')
    # selected_item = tree.selection()
    # tree.item(selected_item[0], tags=('color_text'))
    # tree.update()

tree.bind("<<TreeviewSelect>>", item_selected)#When clicking on an item in the list, the item_selected function is activated


window.resizable(False, False)
window.mainloop()
