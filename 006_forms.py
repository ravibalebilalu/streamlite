import streamlit as st 

import pandas as pd

with st.form(key="sample_form"):
    st.subheader("Text Input")
    name = st.text_input("Enter your name")

    st.subheader("Date and Time inputs")
    dob = st.date_input(label="Select your date of birth")
    time_of_preference =  st.time_input("Enter prefered time")
    st.write(time_of_preference)

    st.subheader("Selectors")
    choice = st.radio("Select an option",["option1","option2","option3"])
    gender = st.selectbox("Select Gender",["Male","Female"])
    slider_value_step = st.select_slider(label="Select A Range In Step",options=[i for i in range(1,21)])
    slider = st.slider(label="Select a range",min_value=1,max_value=100)

    st.subheader("Toggles and Checkbox")
    notofication = st.checkbox("Recive notification?")
    toggle_vlue = st.checkbox("Enable Dark Mode?",value=False)
    
    submit_button = st.form_submit_button(label="Submit")
    