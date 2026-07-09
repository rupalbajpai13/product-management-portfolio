import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import streamlit as st
from agents.orchestrator_agent import OrchestratorAgent

st.set_page_config(
    page_title="SIIA",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Smart Invoice Investigation Assistant")
st.write("AI-powered Invoice Root Cause Analysis Assistant")
st.divider()

invoice_number = st.text_input(
    "Invoice Number",
    placeholder="Example: INV-1001"
)

error = st.text_area(
    "Error Message",
    placeholder="Paste SAP error message here..."
)

if st.button("🔍 Investigate"):

    if not invoice_number:
        st.warning("Please enter an invoice number.")
    else:
        orchestrator = OrchestratorAgent()
        result = orchestrator.run(invoice_number, error)

        if result:
            invoice = result["invoice"]
            st.success(f"Invoice {invoice.invoice_number} fetched successfully.")

            st.subheader("Invoice Details")
            col1, col2 = st.columns(2)

            with col1:
                st.metric("Invoice Number", invoice.invoice_number)
                st.metric("Vendor", invoice.vendor_name)
                st.metric("PO Number", invoice.po_number)

            with col2:
                st.metric("Amount", f"${invoice.invoice_amount:,}")
                st.metric("Quantity", invoice.invoice_quantity)
                st.metric("Status", invoice.status)

        else:
            st.error(f"Invoice '{invoice_number}' not found.")
