import streamlit as st 


st.title("Counter example with Immediate Rerun")

if "count" not in st.session_state:
    st.session_state.count = 0

def increament_and_rerun():
    st.session_state.count += 1
    st.rerun()

st.write(f"Current count",st.session_state.count)

if st.button("increment and run immediatly"):
    increament_and_rerun()