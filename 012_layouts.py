import streamlit as st 
# sidebars
st.sidebar.title("This is sidebar")
st.sidebar.write("You can place elements like sliders,buttons and text here.")
sidebar_input = st.sidebar.text_input("Enter something in sidebar")

# tabs
tab1,tab2,tab3 = st.tabs(["Tab 1","Tab 2","Tab 3"])

with tab1:
    st.write("You are in Tab 1")

with tab2:
    st.write("You are in Tab 2")
with tab3:
    st.write("You are in Tab 3")

#columns
col1,col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.write("Content for column 1")

with col2:
    st.header("Column 2")
    st.write("Content for column 2")

# container
with st.container(border=True):
    st.header("Container")
    st.write("This is inside container.")
    st.write("You can think of containers as a grouping of elements.")
    st.write("Containers helps manage sections of the page.")

# placeholder
place_holder = st.empty()
place_holder.write("This is empty placeholder,usefull for dynamic contents.")
if st.button("Update placeholder"):
    place_holder.write("The content of this placeholder has been updated.")

# expander
with st.expander("Expand fo more details"):
    st.write("This additional information that is hidden by default.")
    st.write("You can use expanders to keep your interface clean.")

# tooltip
st.write("Hover over this button for a tooltip")
st.button("Button with tooltip",help="This is a tooltip or popover on hover")

# sidebar input content
if  sidebar_input:
    st.write(f"You entered in the sidebar : {sidebar_input}")
    

