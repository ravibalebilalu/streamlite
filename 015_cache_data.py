import streamlit as st 
import time


@st.cache_data(ttl=60)
def fetch_data():
    time.sleep(10)
    return {"data":"This is cached data!"}
if st.button("Fetch"):
    st.write("Fetching data.......")
    data = fetch_data()
    st.write(data)