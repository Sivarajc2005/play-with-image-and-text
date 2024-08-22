import requests
import streamlit as st



API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": st.text_input('enter the image you what to create'),
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))

if st.button('generate'):
	st.image(image)
	

#image to text
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

def query(filename):
#     with open(filename, "rb") as f:
#         data = f.read()
     response = requests.post(API_URL, headers=headers, data=filename)
     return response.json()

uploaded_file=st.file_uploader('chose the image you like to summarise')

if st.button('Generate the summary'):
    if uploaded_file is not None:
        output = query(uploaded_file)
        st.write(output[0]['generated_text'])
    else:
        st.warning("Please upload an image file.")