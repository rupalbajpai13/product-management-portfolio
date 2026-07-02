import streamlit as st

st.set_page_config(
    page_title="SIIA",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Smart Invoice Investigation Assistant")

st.write("AI-powered Invoice Root Cause Analysis Assistant")

st.divider()

invoice = st.text_input(
    "Invoice Number",
    placeholder="Example: INV1001"
)

error = st.text_area(
    "Error Message",
    placeholder="Paste SAP error message here..."
)

if st.button("🔍 Investigate"):

    st.success("Investigation Completed")

    st.subheader("Root Cause")

    st.info("Invoice amount exceeds Purchase Order amount.")

    st.subheader("Recommendation")

    st.write("✔ Contact Buyer for approval.")

    st.subheader("SAP Transaction")

    st.code("MRBR")

    st.subheader("SAP Note")

    st.code("1234567")