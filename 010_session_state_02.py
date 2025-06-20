import streamlit as st 

if "counter" not in st.session_state:
    st.session_state.counter = 0
print(f"First :{st.session_state}")

if st.button("Increament counter"):
    st.session_state.counter += 1
    st.write(f"Counter incremented to {st.session_state.counter}")
    print(f"After button press : {st.session_state}")

if st.button("Reset"):
    st.session_state.counter = 0
else:
    st.write("Counter did not reset")

st.write(f"Counter value {st.session_state.counter}")