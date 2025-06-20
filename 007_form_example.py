import streamlit as st 
from datetime import datetime

st.title("User information form")

form_values  = {
    "name":None,
    "age":None,
    "gender":None,
    "date_of_birth" : None
}
min_date = datetime(1900,1,1)
max_date = datetime.now()
with st.form(key="user_info_form"):
    form_values["name"] = st.text_input("Enter Name")
    form_values["age"] = st.number_input('Enter your Age')
    form_values["gender"] = st.selectbox("Select Gender",options=["Male","Female"])
    form_values["date_of_birth"] = st.date_input("Enter date of birth",min_value=min_date,max_value=max_date)
    

    subbmitt_button = st.form_submit_button("Submit") 
    if subbmitt_button:
        if not all(form_values.values()):
            st.warning("Please fill in all of the fields!")
        else:
            st.balloons()


     

