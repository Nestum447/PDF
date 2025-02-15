import streamlit as st
from pdf2docx import Converter
import os

def pdf_to_word(pdf_path, docx_path):
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    cv.close()

st.title("Convertir PDF a Word")

uploaded_file = st.file_uploader("Sube un archivo PDF", type=["pdf"])

if uploaded_file is not None:
    pdf_path = f"temp_{uploaded_file.name}"
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.read())

    docx_path = pdf_path.replace(".pdf", ".docx")
    pdf_to_word(pdf_path, docx_path)

    with open(docx_path, "rb") as f:
        st.download_button("Descargar Word", f, file_name=docx_path, mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")

    os.remove(pdf_path)
    os.remove(docx_path)
