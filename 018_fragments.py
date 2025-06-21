import streamlit as st 

st.title("My Awesome App")

@st.fragment()
def toggle_and_text():
    cols = st.columns(2)
    cols[0] = st.toggle("Toggle")
    cols[1] = st.text_area("Enter text")
   


@st.fragment()
def filter_and_file():
    new_cols = st.columns(5)
    new_cols[0] = st.checkbox("filter")
    new_cols[1] = st.file_uploader("Upload file")
    new_cols[2] = st.selectbox("Choose options ",["option 1","option 2","option 3"])
    new_cols[3] = st.slider("Select Value",0,100,50)
    new_cols[4] = st.text_input("Enter text")





toggle_and_text()
cols = st.columns(2)
cols[0] = st.selectbox("select",[1,2,3],None)
cols[1] = st.button("Update")

filter_and_file()