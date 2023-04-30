# import dependencies
import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page


# set page config
st.set_page_config(
    page_title="Ellie - Smart Attendance",
    layout="wide"
)

# set up session state
if 'click' not in st.session_state:
    st.session_state.click = False

def reset():
  st.session_state.click = True

# login form
def new_signin():
    st.session_state.click = True
    admin_email = "admin@gmail.com"
    admin_password = "admin123"

    with st.form(key="signin"):
        email = st.text_input("Email")
        password = st.text_input("Password", type='password')
        submit = st.form_submit_button("Login")

    if submit and email == admin_email and password == admin_password:
        st.session_state.admin = True
        switch_page("Admin")


if not st.session_state.click:
  # show homepage content

  # set page layout
  col1, col2, col3 = st.columns([3,2,1])

  with col1:
    st.title(":blue[Modern Attendance System for education.]")
    st.title(":blue[Save Time]")
    st.title(":blue[Focus on the important]")
    st.text("")

    st.header(":blue[Manually taking attendance can be time consuming and daunting. ELLIE automates the process with state-of-the-art facial recognition technology, easy to use and navigate.]")


  with col2:
    img = Image.open("face_recognition.png")
    st.image(img)


  with col3:
    sign = st.button("Log in", on_click=reset)
    if sign:
      st.session_state.click = True
else:
  new_signin()
