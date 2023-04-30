import streamlit as st

# set back homepage state
st.session_state.click = False

# set up teacher ui session state
if 'teacher' not in st.session_state:
  st.session_state.teacher = False


if not st.session_state.teacher:
  st.warning("You must log-in to see the content of this page!")
  st.stop()
else:
  # only show it when logged in with Teacher crendentials
  # sidebar for teacher page
  st.title("Welcome, Teacher")

  menu = ["Start Attendance","View Attendance"]
  choice = st.sidebar.radio("Select operation",menu)
  if choice == "Start Attendance":
    st.subheader("Start Attendance")

  elif choice == "View Attendance":
    st.subheader("View Attendance")