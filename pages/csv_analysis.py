import streamlit as st
from langchain.agents import AgentType
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain_community.chat_models import ChatOpenAI
from langchain_experimental.agents import create_csv_agent

st.set_page_config(page_title='chat with your csv!', page_icon='random', layout='wide')
st.title('chat with your csv!')

uploaded_file = st.file_uploader(
    '请上传数据',
    type='csv',
    help='请上传csv格式的文件'
)

if not uploaded_file:
    st.warning('必须上传csv以进行分析')

if 'message' not in st.session_state or st.sidebar.button('clear conversation history'):
    st.session_state['message'] = [{'role': 'assistant', 'content': '我有什么可以帮你的吗'}]

for msg in st.session_state.message:
    st.chat_message(msg['role']).write(msg['content'])

if query := st.chat_input(placeholder='这是什么数据？'):
    st.session_state.message.append({'role': 'user', 'content': query})
    st.chat_message('user').write(query)
    if not st.session_state['OPENAI_API_KEY']:
        st.info('请添加openai key')
        st.stop()

    llm = ChatOpenAI(
        openai_api_key=st.session_state['OPENAI_API_KEY'],
        openai_api_base=st.session_state['OPENAI_API_BASE']
    )
    csv_agent = create_csv_agent(
        llm,
        uploaded_file,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
    )

    with st.chat_message('assistant'):
        st_cb = StreamlitCallbackHandler(st.container())
        response = csv_agent.run(query)
        st.session_state.message.append({'role': 'assistant', 'content': response})
        st.write(response)
