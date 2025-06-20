import streamlit as st 
import os

st.title("This is Title")
st.header('This is Header')
st.subheader("This is Subheader")

st.markdown("This is Markdown1")
st.markdown("This is _Markdown2_")

st.caption('This is caption')


code_example = """

def greet():
    print('Hello there')

"""

st.code(code_example,language="python")

st.divider()

st.image(  os.path.join(os.getcwd(),'static','cat.png'),width=139,caption="Cat",clamp=False)