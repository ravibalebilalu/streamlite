import streamlit as st 
import pandas as pd

st.title("Streamlite Data Demo")
st.subheader("Dataframe")

df = pd.DataFrame({
    "name":["Alice","Charlie",'Bob',"David"],
    "Age":[23,34,24,21],
    "Occupation":["Engineer","Doctor","Artist","Cheff"]

})

st.dataframe(df)

st.subheader("Data Editor")

editable_table = st.data_editor(df)

st.subheader("Static Table")

st.table(df)
st.divider()
st.subheader("Metrics")

st.metric(label="Total Rows",value=len(df))
st.metric(label="Total columns",value=df.shape[1])
st.metric(label='Age Mean',value=str(round(df["Age"].mean(),1)))
st.subheader("JSON: ")
dict_sample = {
    "name":"Ravi",
    "age":23,
}

st.json(dict_sample)
 