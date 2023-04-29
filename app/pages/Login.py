import streamlit as st

# Create an empty container
placeholder = st.empty()

test_email ="email"
test_password="password"

# insert login form into the container
with placeholder.form("login"):
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")


if submit and email == test_email and password == test_password:
    # If the form is submitted and the email and password are correct,
    # Clearn the form/container and display a success message
    placeholder.empty()
    st.success("Login successful")
    st.title("Welcome Karen")
elif submit and email !=test_email and password !=test_password:
    st.error("Login failed")
else:
    pass
