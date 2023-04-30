import streamlit as st

st.title("Welcome, Admin")
# set back homepage state
st.session_state.click = False

# default admin session sate as false
# st.session_state.admin = False
# set admin sesstion state
if 'admin' not in st.session_state:
  st.session_state.admin = False


if not st.session_state.admin:
    st.warning("You must log-in to see the content of this page!")
    st.stop()
else:
  # only show it when logged in with Admin crendentials
  # sidebar for admin page

  with st.sidebar:
      side_bar = st.radio("Welcome",("Create Profile","View Profile", "Edit Profile", "Delete Profile","Access Azure"))
