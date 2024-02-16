import streamlit as st
from docx import Document
import openai

# Function to read .docx content
def read_docx(file):
    doc = Document(file)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

# Function to summarize text using OpenAI API
def summarize_text(text):
    openai.api_key = 'your_openai_api_key_here'
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt="Summarize the following text:\n\n" + text,
      temperature=0.7,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    return response.choices[0].text.strip()

# Streamlit app interface
st.title('Google Meet Transcript Summarizer')
uploaded_file = st.file_uploader("Choose a .docx file", type="docx")
if uploaded_file is not None:
    text = read_docx(uploaded_file)
    if st.button('Summarize'):
        summary = summarize_text(text)
        st.subheader('Summary')
        st.write(summary)
