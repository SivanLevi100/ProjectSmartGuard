import streamlit as st

import random
import pandas as pd
from pathlib import Path

st.button("Go")

name_V="V_"
name_NV="NV_"
counter_V=1
counter_NV=1


videos = [
    {'class': 'V', 'Date': '01.02.2024', 'Button': 'cls','file': open('V_1.mp4','rb')},
    {'class': 'NV','Date': '02.02.2024', 'Button': 'cls', 'file': open('NV_1.mp4','rb')}
]

df = pd.DataFrame(videos)

for index, row in df.iterrows():
    st.write(row['Date'])
    st.checkbox("Use container width", value=False, key="use_container_width")
    if row['class'] == 'V':
        video_file = open(name_V+str(counter_V)+'.mp4', 'rb')
        counter_V=counter_V+1
    else:
        video_file = open(name_NV +str(counter_NV) + '.mp4', 'rb')
        counter_NV=counter_NV+1

    video_bytes = video_file.read()
    st.video(video_bytes)












df = pd.DataFrame(
    {
        "name": ["12.1", "Extras", "Issues"],
        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
        "stars": [st.button("Button"),st.button("Button"),st.button("Button")],
        "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
    }
)
st.dataframe(
    df,
    column_config={
        "name": "Date",
        "stars": st.write("SmartGuard" + ":smile:"),
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)


