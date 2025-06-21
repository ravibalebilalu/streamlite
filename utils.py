import streamlit as st 

@st.fragment()
def toggle_and_text():
    cols = st.columns(2)
    cols[0] = st.toggle("Toggle")
    cols[1] = st.text_area("Enter text")