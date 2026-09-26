# app.py - Streamlit UI
document_type = st.text_input("Document Type")
parties = st.text_area("Parties Involved")
terms = st.text_area("Terms & Conditions")
dates = st.text_input("Effective Date")

# Send to backend
response = requests.post("http://localhost:8000/generate", json={
    "document_type": document_type,
    "parties": parties,
    "terms": terms,
    "dates": dates
})
if st.session_state.get("show_edit"):
    edited_text = st.text_area("Edit Document Below:", generated_text, height=300)
    st.session_state.generated_text = edited_text

# Downloads
st.download_button("📄 Download as .TXT", data=generated_text, ...)
st.download_button("📝 Download as .DOCX", data=format_docx(...), ...)
st.download_button("📕 Download as .PDF", data=format_pdf(...), ...)
# app.py
# Streamlit collects input -> FastAPI handles it
response = requests.post("http://localhost:8000/generate", json={...})
# Step 1: Streamlit Page Configuration and Layout Setup
st.set_page_config(page_title="LegalEase", layout="centered")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(WEB_LOGO_PATH, use_container_width=True)

# Step 2: Header and Title
st.markdown(
    "<h2 style='text-align: center;'>AI Legal Document Generator</h2>",
    unsafe_allow_html=True
)

# Step 3: User Input Interface
document_type = st.text_input("Document Type")
parties = st.text_area("Parties Involved")
terms = st.text_area("Terms & Conditions")
dates = st.text_input("Effective Date")
