import streamlit as st 

from datetime import datetime

min_date = datetime(1900,1,1)
max_date = datetime.now()

st.title("User information form")

with st.form(key="user_info_form",clear_on_submit=True):
    name = st.text_input('Enter Your Name')
    birth_date = st.date_input("Select your date of birth",min_value=min_date,max_value=max_date)

    if birth_date:
        age = max_date.year - birth_date.year

        if birth_date.month > max_date.month or (birth_date.month == max_date.month and birth_date.day > max_date.day):
            age -= 1
        st.write(f"Your calculated age is {age} years")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        if not name or not birth_date:
            st.warning("Please fill in all form inputs")
        else:
            st.success(f"Thank You {name} ,Your age is {age}")
            st.balloons()