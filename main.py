import streamlit as st
from functions import pdf_to_text, text_to_pdf
import os


st.title("PDF to Text Converter")

tab_1, tab_2 = st.tabs(["pdf to text", "text to pdf"])

with tab_1:
    uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])
    if uploaded_file is not None:
        with st.spinner("Extracting text..."):
            text = pdf_to_text(uploaded_file)
        
        st.header("Extracted Text :")
        st.write(text)
        
        st.download_button(
            label="Download Text File",
            data=text,
            file_name="extracted text.txt",
            mime="text/plain",
        )
        os.remove("output.txt")

with tab_2:
    uploaded_file = st.file_uploader("Upload your text file", type=["txt"])
    if uploaded_file is not None:
        with st.spinner("Converting text to PDF..."):
            text = uploaded_file.read().decode("utf-8")
            text = text_to_pdf(text)
            st.header("Extracted Text :")
            st.write(text)

        st.download_button(
            label="Download PDF",
            data=open("output.pdf", "rb").read(),
            file_name="converted_pdf.pdf",
            mime="application/pdf",
        )
        os.remove("output.pdf")
