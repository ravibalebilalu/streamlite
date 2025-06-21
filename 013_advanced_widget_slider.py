import streamlit as st 

if  "slider" not in st.session_state:
    st.session_state.slider = 25

# widget with same name but different keyes
st.button("ok",key="btn1")
st.button("ok",key="btn2")


min_value = st.slider("Set min value",0,50,25)

st.session_state.slider = st.slider("Slider",min_value,100,st.session_state.slider)