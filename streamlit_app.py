import streamlit as st
import openai
import fitz  # PyMuPDF

# Function to extract text from a PDF file
def read_pdf(file):
    with fitz.open(stream=file) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text

# Function to summarize text using OpenAI API
def summarize_text(text):
    openai.api_key = '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'
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Summarize the following text with main points being Actions that need to be completed, Agenda of the meeting, Who the Attendees are, and the general Notes from the meeting:\n\n" + text,
        temperature=0.7,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

# Streamlit app interface
st.title('Text and PDF Summarizer')
text_input = st.text_area("Or enter text here:")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if st.button('Summarize'):
    if uploaded_file is not None:
        text = read_pdf(uploaded_file)
    elif text_input:
        text = text_input
    else:
        st.write("Please input text or upload a PDF file.")
        st.stop()

    summary = summarize_text(text)
    st.subheader('Summary')
    st.write(summary)
