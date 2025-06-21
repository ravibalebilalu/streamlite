import streamlit as st 
st.write("Page2")


if st.button("Home"):
   st.switch_page("Home.py")
elif st.button("Page 1"):
   st.switch_page("pages/page_1.py")
elif st.button("Page 2"):
   st.switch_page("pages/page_2.py")
elif st.button("Page 3"):
   st.switch_page("pages/page_3.py")