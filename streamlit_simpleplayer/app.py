import streamlit as st

from streamlit_simpleplayer.lib import load_data


data = load_data()
st.dataframe(data)
