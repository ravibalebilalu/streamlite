import streamlit as st 

if "checkbox" not in st.session_state:
    st.session_state.checkbox = False
if "user_input" not in st.session_state:
    st.session_state.user_input = "nothing"

def toggle_input():
    st.session_state.checkbox = not st.session_state.checkbox
    
# assign checkbox value from session_state
st.checkbox(label="Show input field",value=st.session_state.checkbox,on_change=toggle_input)


if st.session_state.checkbox:
    #assign  text_input value from session_state
    user_input = st.text_input("Write something",value=st.session_state.user_input)
    #update session_state.user_input with actual user_input
    st.session_state.user_input = user_input
    
else:
    # if not checkbox checked assign value from session_state
    user_input = st.session_state.get("user_input","")

st.write(f"User input : {user_input}")
 