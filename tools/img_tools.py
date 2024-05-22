import base64


def image_to_data_url(uploaded_file):
    mime_type = uploaded_file.type
    image_data = uploaded_file.read()
    # 将图像数据进行 Base64 编码
    base64_encoded_data = base64.b64encode(image_data).decode('utf-8')
    return f"data:{mime_type};base64,{base64_encoded_data}"
