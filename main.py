#import mymodel as my
import streamlit as st
#from ProjectSmartGuard.pages.page2 import *





st.title("Welcome to the SmartGuard application")

st.sidebar.success("select page above")



b = st.button("click here")
if b:
    st.write("SmartGuard" + ":smile:")




cls="Violence" #משתנה השומר את סיווג הסרטון
st.write("Classification: " +cls)

#הסרטון שאנו מסווגים
video_file = open('V_1.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)



x = st.slider("Select a value")
st.write(x, "דירוג האפליקציה")

#st.button("Reset", type="primary")
#if st.button('Say hello'):
#    st.write('Why hello there')
#else:
#    st.write('Goodbye')
#st.set_page_config(page_title="sivan")

