import streamlit as st 

counter = 0

st.write(f"Counter value : {counter}")

if st.button("Increament Button"):
    counter += 1
    st.write(f"Counter incremented to {counter}")
else:
    st.write(f'Counter stays at {counter}')