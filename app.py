import streamlit as st
import pdfplumber
from pdf2image import convert_from_bytes

st.title("PDF Reader")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:

    pdf_bytes = uploaded_file.read()

    pdf = pdfplumber.open(uploaded_file)
    total_pages = len(pdf.pages)

    if total_pages > 1:
        page_number = st.slider("Select Page", 1, total_pages, 1)
    else:
        page_number = 1

    # IMAGE RENDER
    images = convert_from_bytes(pdf_bytes)
    st.image(images[page_number-1])

    # TEXT EXTRACT
    page = pdf.pages[page_number-1]
    text = page.extract_text()

    if text:
        st.text_area("Content", text, height=400, key=f"text_{page_number}", disabled=True)

    st.write(f"Page {page_number} of {total_pages}")