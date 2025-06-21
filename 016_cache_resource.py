import streamlit as st 

file_path = "example.txt"

@st.cache_resource
def get_file_handler():
    
    file = open(file_path,"a+")
    
    return file

file_handler = get_file_handler()

if st.button("write to file"):
    
    file_handler.write("New line of text\n")
    file_handler.flush()
    st.success("Wrote a new line to the file!")

if st.button("Read"):
    file_handler.seek(0)
    content = file_handler.read()
    st.text(content)

def file_close():
    file_handler.close()
    st.success("File closed")

if st.button("Close file" ):
     file_close()