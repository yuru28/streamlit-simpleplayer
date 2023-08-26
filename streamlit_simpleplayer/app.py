from datetime import datetime

import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

from streamlit_simpleplayer.lib import load_data

episodes_df = load_data()
episodes_df['published_at'] = pd.to_datetime(episodes_df['published_at'])
published_episodes = episodes_df[episodes_df['published_at'] <= datetime.now()]

show_id = 'f414b397-96fb-42c5-aa9d-04baa2cde5ac'

st.title('Simple Player')

st.header('エピソード一覧', divider=True)
option = st.selectbox(
    '再生したいエピソードを選択',
    options=published_episodes.sort_values(by='number', ascending=False)[["art19_uuid", "title"]],
    key='episode',
    format_func=lambda x: episodes_df[episodes_df["art19_uuid"] == x]["title"].values[0]
)

if option:
    episode = episodes_df[episodes_df["art19_uuid"] == option].iloc[0].to_dict()
    st.header(episode['title'], divider=True)
    src_url = f'https://www.art19.com/shows/{show_id}/episodes/{option}/embed?type=micro&download-enabled=0'
    components.iframe(src_url, scrolling=False, height=42)
    st.markdown(episode['content'])

st.info('src is here: https://github.com/yuru28/streamlit-simpleplayer')
