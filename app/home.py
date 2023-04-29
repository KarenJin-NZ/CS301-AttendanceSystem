# import dependencies
import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page


# set page config
st.set_page_config(
    page_title="Ellie - Smart Attendance",
    layout="wide"
)

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
  log_in = st.button("Log In")
  if log_in:
    switch_page("Login")

