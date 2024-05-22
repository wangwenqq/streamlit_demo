import streamlit as st

if 'AZURE_API_KEY' not in st.session_state:
    st.session_state['AZURE_API_KEY'] = ''
if 'AZURE_ENDPOINT' not in st.session_state:
    st.session_state['AZURE_ENDPOINT'] = ''
if 'API_VERSION' not in st.session_state:
    st.session_state['API_VERSION'] = ''
st.set_page_config(page_title='azure openai settings', layout='wide')
st.title('azure openai settings')

key = st.text_input('azure api key', value=st.session_state['AZURE_API_KEY'], max_chars=None, key=None, type='default')
endpoint = st.text_input('azure endpoint', value=st.session_state['AZURE_ENDPOINT'], max_chars=None,
                         key=None, type='default')
version = st.text_input('azure api version', value=st.session_state['API_VERSION'], max_chars=None, key=None, type='default')

saved = st.button('save')
if saved:
    st.session_state['AZURE_API_KEY'] = key
    st.session_state['AZURE_ENDPOINT'] = endpoint
    st.session_state['API_VERSION'] = version
