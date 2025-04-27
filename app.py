import streamlit as st
import json

# Show the form
st.title('Submit Form')

option = st.radio('Select an option', ('Json', 'Dictionary'))
user_input = st.text_input('Enter your data')

if st.button('Submit'):
    # Process the data and store or handle it
    response = {
        'option': option,
        'userInput': user_input
    }
    st.write('Form Submitted Successfully!')
    st.json(response)
