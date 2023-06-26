import streamlit as st
from send_email import send_email
st.header("Contact Me")


with st.form("email_form"):
    user_email = st.text_input("Your mail address")
    message = st.text_area("Your message")
    raw_message = message+"\n"+user_email
    message = f"""\
    Subject: new mail from {user_email} 
    
    From: {user_email}
    {raw_message}
    """
    button = st.form_submit_button("submit")
    if button:
        send_email(message)
        st.info("Your email was sent")