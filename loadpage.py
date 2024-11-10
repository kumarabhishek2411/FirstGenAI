import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# hashed_passwords = stauth.Hasher(['abc', 'def']).generate()
# print(hashed_passwords)

with open('C:\\Users\\91841\\Desktop\\Hackathon\\authen.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
    config['credentials'],
    # config['cookie']['name'],
    # config['cookie']['key'],
    # config['cookie']['expiry_days']
    )
           

# name, authentication_status, username = authenticator.login('Login', 'main')
# if authentication_status:
#     authenticator.logout('Logout', 'main')
#     st.write(f'Welcome *{name}*')
#     st.title('Some content')
# elif authentication_status == False:
#     st.error('Username/password is incorrect')
# elif authentication_status == None:
#     st.warning('Please enter your username and password')
# st.session_state['authentication_status'] = False
try:
    authenticator.login(location='main')
    if st.session_state['authentication_status']:
        st.write(f"Welcome {st.session_state['name']}")
        authenticator.logout(location='main')
        st.title("Personalized User Dashboard")
    elif st.session_state['authentication_status'] == None:
        st.write("Please provide a username and password to login")
    elif not st.session_state['authentication_status']:
        st.error("Username/Password incorrect")
    

    
    
    # if authentication_status:
    #     # authenticator.logout(location='main')
    #     st.write(f'Welcome *{name}*')
    #     st.title('Personalized User Details')
    # elif authentication_status == False:
    #     st.error('Username/password is incorrect')
    # elif authentication_status == None:
    #     st.warning('Please enter your username and password')
except Exception as e:
    st.error(e)
