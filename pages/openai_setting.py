import streamlit as st

if 'OPENAI_API_KEY' not in st.session_state:
    st.session_state['OPENAI_API_KEY'] = ''
if 'OPENAI_API_BASE' not in st.session_state:
    st.session_state['OPENAI_API_BASE'] = ''
st.set_page_config(page_title='openai settings', layout='wide')
st.title('openai settings')
key = st.text_input('api key', value=st.session_state['OPENAI_API_KEY'], max_chars=None, key=None, type='password')
base_url = st.text_input('base url', value=st.session_state['OPENAI_API_BASE'],
                         max_chars=None, key=None, type='default')
saved = st.button('save')
if saved:
    st.session_state['OPENAI_API_KEY'] = key
    st.session_state['OPENAI_API_BASE'] = base_url
