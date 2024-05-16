import streamlit as st

if 'PINECONE_API_KEY' not in st.session_state:
    st.session_state['PINECONE_API_KEY'] = ''
st.set_page_config(page_title='openai settings', layout='wide')
st.title('openai settings')
key = st.text_input('api key', value=st.session_state['PINECONE_API_KEY'], max_chars=None, key=None, type='default')
saved = st.button('save')
if saved:
    st.session_state['PINECONE_API_KEY'] = key
