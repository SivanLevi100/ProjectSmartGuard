# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st
#import mymodel as my
from page2 import *

#st.write("My name is: Sivan")
st.title("Welcome to the SmartGuard application")

b = st.button("click here")
if b:
    st.write("SmartGuard" + ":smile:")




cls="Violence" #משתנה השומר את סיווג הסרטון
st.write("Classification: " +cls)

#הסרטון שאנו מסווגים
video_file = open('V_1.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)



st.button(
    label='CLASSIFICATION',
    key='classify',
    help='Click to classify',
    on_click=classify_video,
    args=(user_video,),
    kwargs={
        'border_radius': '10px',
        'padding': '15px 32px',
        'font_size': '20px',
        'font_weight': 'bold',
        'background_color': '#0066CC',
        'color': '#ffffff'
    }
)



def go_to_page2():
    st.experimental_singleton().clear()
    page2()

st.button('Go to Page 2', on_click=go_to_page2)


x = st.slider("Select a value")
st.write(x, "דירוג האפליקציה")

#st.button("Reset", type="primary")
#if st.button('Say hello'):
#    st.write('Why hello there')
#else:
#    st.write('Goodbye')
#st.set_page_config(page_title="sivan")

