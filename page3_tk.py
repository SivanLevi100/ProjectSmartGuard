
import subprocess
import keras
import Videos_main
from pathlib import Path
import time

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from PIL import ImageTk, Image


OUTPUT_PATH = Path(__file__).parent
# ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\owner\Desktop\לימודים - שנה ג\סמסטר א\Tkinter-Designer-master (1)\Tkinter-Designer-master\build\assets\frame0")


ASSETS_PATH1=OUTPUT_PATH/Path(r"Images_UI/frame_3")
def relative_to_assets1(path: str) -> Path:
    return ASSETS_PATH1 / Path(path)

# def relative_to_assets(path: str) -> Path:
#     return ASSETS_PATH / Path(path)


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
def click_classification():
    print("print button classification")
    #label = Computer_Camera_without_pre_model.main("NV_183.mp4")

button_image_2 = PhotoImage(
    file=relative_to_assets1("button_2.png"))
button_classification = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click_classification(),
    relief="flat"
)
button_classification.place(
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



# listbox = tk.Listbox(window)
# listbox.pack()
#
# listbox.insert(1, "פריט 1")
# listbox.insert(2, "פריט 2","image_4.png")
# listbox.insert(3, "פריט 3","image_4.png")

listbox = tk.Listbox(window)
listbox.pack()

#image = ImageTk.PhotoImage(Image.open("Images_UI/frame_2/image_4.png"))

videos_list=["V_1", "NV_183"]

for item in videos_list:
    listbox.insert('end', item)

listbox.place( x=60,y=300.0)

listbox.config(height=70, width=20,font=("Times", 20),fg="blue",bg="black",borderwidth=2, relief="groove")

#image = ImageTk.PhotoImage(Image.open("Images_UI/frame_2/image_4.png"))

#listbox.insert(tk.END, "Item 1", image=image)
def item_selected(event):
    #subprocess.call(['python', 'page3_tk.py'])
    selected_item = listbox.get(listbox.curselection())
    model = keras.models.load_model("Models/cnn_lstm_model_PRO.hdf5")
    label = Videos_main.main(selected_item +".mp4",model)
    print(label)
   #  if label == "Violent":
   #      page4_tk.addVideosToList(selected_item)


listbox.bind('<<ListboxSelect>>', item_selected)




window.resizable(False, False)
window.mainloop()
