from datetime import datetime

import streamlit as st
import pandas as pd

from streamlit_simpleplayer.lib import load_data


episodes_df = load_data()
episodes_df['published_at'] = pd.to_datetime(episodes_df['published_at'])
published_episodes = episodes_df[episodes_df['published_at'] <= datetime.now()]

option = st.selectbox(
    '再生したいエピソードを選択',
    options=published_episodes.sort_values(by='number', ascending=False)[["art19_uuid", "title"]],
    key='episode',
    format_func=lambda x: episodes_df[episodes_df["art19_uuid"] == x]["title"].values[0]
)

st.write('You selected:', option)
