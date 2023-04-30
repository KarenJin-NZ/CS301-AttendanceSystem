import streamlit as st

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
  st.title("Welcome, Admin")
  # sidebar for admin page

  menu = ["Create Profile","View Profile", "Edit Profile", "Delete Profile","Access Azure"]
  choice = st.sidebar.radio("Select operation",menu)
  if choice == "Create Profile":
    st.subheader("Create Profile")

  elif choice == "View Profile":
    st.subheader("View Profile")

  elif choice == "Edit Profile":
    st.subheader("Edit Profile")

  elif choice == "Delete Profile":
    st.subheader("Delete Profile")

  elif choice == "Access Azure":
    st.subheader("Access Azure")
