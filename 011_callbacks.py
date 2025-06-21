import streamlit as st 

# set step and info in session_state
if "step" not in st.session_state:
    st.session_state.step = 1

if "info" not in st.session_state:
    st.session_state.info = {}
#functions for buttons
def go_to_step1():
    st.session_state.step = 1


def go_to_step2(name):
    st.session_state.info["name"] = name
    # move to step 2
    st.session_state.step = 2


# step 1 task
if st.session_state.step == 1:
    st.header("PART 1 : Info")
    name = st.text_input("Name",value=st.session_state.info.get("name",""))
    st.button("Next",on_click=go_to_step2,args=(name,))
        


if st.session_state.step == 2:
    st.header("Part 2 : Review")
    st.subheader("Step : 2")
    st.write(f"**name** {st.session_state.info.get('name','')}")
    # do task  if button pressed
    if st.button("Submit"):
        st.success("Great!")
        st.balloons()
        st.session_state.info = {}
    # 1 step back
    st.button("Back",on_click=go_to_step1)
         


