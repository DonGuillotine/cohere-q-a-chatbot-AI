import streamlit as st
from main import CoHere
from decouple import config

st.header('A Cohere Powered Application')

api_key = config('API_KEY')

st.header('Your Personal chat bot - Donald!')

question_for_donald = st.text_input('Question for Donald')

cohere = CoHere(api_key)

if st.button('Answer'):
    st.write(cohere.cohere(question_for_donald))