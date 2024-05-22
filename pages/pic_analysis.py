import streamlit as st
from langchain_community.callbacks import StreamlitCallbackHandler
from openai.lib.azure import AzureOpenAI

from tools.img_tools import image_to_data_url


st.set_page_config(page_title='chat with your pic!', page_icon='random', layout='wide')
st.title('chat with your pic!')

uploaded_file = st.file_uploader(
    '请上传图片',
    type=["jpg", "jpeg", "png"],
    help='请上传"jpg", "jpeg", "png"格式的文件'
)

if not uploaded_file:
    st.warning('必须上传图片以进行分析')
if uploaded_file:
    st.image(uploaded_file, width=200)
    data_url = image_to_data_url(uploaded_file)

if 'message' not in st.session_state or st.sidebar.button('clear conversation history'):
    st.session_state['message'] = [{'role': 'assistant', 'content': '我有什么可以帮你的吗'}]

for msg in st.session_state.message:
    st.chat_message(msg['role']).write(msg['content'])

if query := st.chat_input(placeholder='请描述图片所讲内容'):
    st.session_state.message.append({'role': 'user', 'content': query})
    st.chat_message('user').write(query)
    if not st.session_state['AZURE_API_KEY']:
        st.info('请添加azure openai key')
        st.stop()
    if not st.session_state['API_VERSION']:
        st.info('请添加azure api version')
        st.stop()
    if not st.session_state['AZURE_ENDPOINT']:
        st.info('请添加azure endpoint')
        st.stop()

    client = AzureOpenAI(
        api_key=st.session_state['AZURE_API_KEY'],
        api_version=st.session_state['API_VERSION'],
        azure_endpoint=st.session_state['AZURE_ENDPOINT'],
    )

    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {"role": "system", "content": "你是一个智能助手"},
            {"role": "user", "content": [
                {
                    "type": "text",
                    "text": f"{query}:"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"{data_url}"
                    }
                }
            ]}
        ],
        max_tokens=2000
    )
    with st.chat_message('assistant'):
        st_cb = StreamlitCallbackHandler(st.container())
        st.session_state.message.append({'role': 'assistant', 'content': response.choices[0].message.content})
        st.write(response.choices[0].message.content)
