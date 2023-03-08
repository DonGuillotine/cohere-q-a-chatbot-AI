import streamlit as st
import cohere
from secrets import secrets;
from main import CoHere

st.header('A Co:here Powered Application')

api_key = st.text_input('OpenAI API Key:', type='password')