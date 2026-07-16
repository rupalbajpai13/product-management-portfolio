import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import streamlit as st
from agents.orchestrator_agent import OrchestratorAgent

st.set_page_config(
    page_title="SIIA | SAP Invoice Investigation",
    page_icon="🔍",
    layout="wide"
)

# SAP Fiori CSS
st.markdown("""
<style>
    /* Global */
    .stApp {
        background-color: #F7F7F7;
        font-family: '72', '72full', Arial, Helvetica, sans-serif;
    }

    /* Shell Bar */
    .fiori-shell {
        background-color: #354A5E;
        color: white;
        padding: 12px 24px;
        display: flex;
        align-items: center;
        margin-bottom: 24px;
        border-radius: 4px;
    }
    .fiori-shell-title {
        font-size: 16px;
        font-weight: 600;
        color: white;
        margin: 0;
    }
    .fiori-shell-subtitle {
        font-size: 12px;
        color: #9DA8B4;
        margin: 0;
    }

    /* Cards */
    .fiori-card {
        background: white;
        border-radius: 4px;
        padding: 20px 24px;
        margin-bottom: 16px;
        box-shadow: 0 0 0 1px rgba(0,0,0,0.08), 0 2px 4px rgba(0,0,0,0.04);
    }
    .fiori-card-title {
        font-size: 14px;
        font-weight: 700;
        color: #32363A;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 16px;
        padding-bottom: 8px;
        border-bottom: 2px solid #0070F2;
    }

    /* Object Header */
    .fiori-object-header {
        background: white;
        border-radius: 4px;
        padding: 20px 24px;
        margin-bottom: 16px;
        box-shadow: 0 0 0 1px rgba(0,0,0,0.08);
        border-left: 4px solid #0070F2;
    }

    /* Status Badge */
    .status-blocked {
        background: #BB0000;
        color: white;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
    }
    .status-open {
        background: #107E3E;
        color: white;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
    }

    /* Key-Value pairs */
    .fiori-kv {
        display: flex;
        flex-direction: column;
        margin-bottom: 12px;
    }
    .fiori-kv-label {
        font-size: 11px;
        color: #6A6D70;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .fiori-kv-value {
        font-size: 16px;
        font-weight: 600;
        color: #32363A;
    }

    /* Finding items */
    .finding-high {
        border-left: 4px solid #BB0000;
        background: #FFF4F4;
        padding: 12px 16px;
        border-radius: 0 4px 4px 0;
        margin-bottom: 8px;
    }
    .finding-medium {
        border-left: 4px solid #E9730C;
        background: #FFF8F0;
        padding: 12px 16px;
        border-radius: 0 4px 4px 0;
        margin-bottom: 8px;
    }
    .finding-low {
        border-left: 4px solid #107E3E;
        background: #F0FFF4;
        padding: 12px 16px;
        border-radius: 0 4px 4px 0;
        margin-bottom: 8px;
    }
    .finding-title {
        font-size: 14px;
        font-weight: 700;
        color: #32363A;
        margin-bottom: 4px;
    }
    .finding-message {
        font-size: 13px;
        color: #32363A;
        margin-bottom: 4px;
    }
    .finding-tcode {
        font-size: 12px;
        color: #0070F2;
        font-family: monospace;
        font-weight: 600;
    }

    /* RCA Section */
    .rca-root-cause {
        background: #FFF4F4;
        border: 1px solid #BB0000;
        border-radius: 4px;
        padding: 16px;
        margin-bottom: 8px;
    }
    .rca-recommendation {
        background: #F0FFF4;
        border: 1px solid #107E3E;
        border-radius: 4px;
        padding: 16px;
        margin-bottom: 8px;
    }
    .rca-label {
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 6px;
    }

    /* SAP Blue button override */
    .stButton > button {
        background-color: #0070F2 !important;
        color: white !important;
        border: none !important;
        border-radius: 4px !important;
        padding: 8px 24px !important;
        font-weight: 600 !important;
        font-size: 14px !important;
    }
    .stButton > button:hover {
        background-color: #0057D9 !important;
    }

    /* Input fields */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        border: 1px solid #89919A !important;
        border-radius: 4px !important;
        font-size: 14px !important;
    }
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #0070F2 !important;
        box-shadow: 0 0 0 2px rgba(0,112,242,0.2) !important;
    }

    /* Footer */
    .fiori-footer {
        font-size: 11px;
        color: #89919A;
        text-align: center;
        padding: 16px;
        border-top: 1px solid #E5E5E5;
        margin-top: 32px;
    }

    /* Hide default streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Shell Bar
st.markdown("""
<div class="fiori-shell">
    <div>
        <p class="fiori-shell-title">🔍 SIIA — Smart Invoice Investigation Assistant</p>
        <p class="fiori-shell-subtitle">AI-powered Invoice Root Cause Analysis</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Input Card
st.markdown('<div class="fiori-card"><div class="fiori-card-title">Invoice Investigation</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])
with col1:
    invoice_number = st.text_input("Invoice Number", placeholder="Example: INV-1001")
with col2:
    error = st.text_area("Error Message", placeholder="Paste SAP error message here...", height=80)

investigate = st.button("🔍 Investigate")
st.markdown('</div>', unsafe_allow_html=True)

if investigate:
    if not invoice_number:
        st.markdown('<div class="fiori-card"><p style="color:#BB0000;font-weight:600;">⚠ Please enter an invoice number.</p></div>', unsafe_allow_html=True)
    else:
        with st.spinner("Investigating invoice..."):
            orchestrator = OrchestratorAgent()
            result = orchestrator.run(invoice_number, error)

        if result:
            invoice = result.invoice
            findings = result.findings

            # Object Header
            status_class = "status-blocked" if invoice.status == "Blocked" else "status-open"
            st.markdown(f"""
            <div class="fiori-object-header">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <div style="font-size:20px; font-weight:700; color:#32363A;">{invoice.invoice_number}</div>
                        <div style="font-size:14px; color:#6A6D70;">{invoice.vendor_name}</div>
                    </div>
                    <span class="{status_class}">{invoice.status}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Invoice Details Card
            st.markdown('<div class="fiori-card"><div class="fiori-card-title">Invoice Details</div>', unsafe_allow_html=True)
            c1, c2, c3, c4, c5 = st.columns(5)
            with c1:
                st.markdown(f'<div class="fiori-kv"><span class="fiori-kv-label">Invoice No.</span><span class="fiori-kv-value">{invoice.invoice_number}</span></div>', unsafe_allow_html=True)
            with c2:
                st.markdown(f'<div class="fiori-kv"><span class="fiori-kv-label">Vendor</span><span class="fiori-kv-value">{invoice.vendor_name}</span></div>', unsafe_allow_html=True)
            with c3:
                st.markdown(f'<div class="fiori-kv"><span class="fiori-kv-label">PO Number</span><span class="fiori-kv-value">{invoice.po_number}</span></div>', unsafe_allow_html=True)
            with c4:
                st.markdown(f'<div class="fiori-kv"><span class="fiori-kv-label">Amount</span><span class="fiori-kv-value">${invoice.invoice_amount:,}</span></div>', unsafe_allow_html=True)
            with c5:
                st.markdown(f'<div class="fiori-kv"><span class="fiori-kv-label">Quantity</span><span class="fiori-kv-value">{invoice.invoice_quantity}</span></div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            # Findings Card
            if findings:
                st.markdown('<div class="fiori-card"><div class="fiori-card-title">Investigation Findings</div>', unsafe_allow_html=True)
                for finding in findings:
                    css_class = {"HIGH": "finding-high", "MEDIUM": "finding-medium", "LOW": "finding-low"}.get(finding.severity, "finding-low")
                    severity_icon = {"HIGH": "🔴", "MEDIUM": "🟡", "LOW": "🟢"}.get(finding.severity, "⚪")
                    st.markdown(f"""
                    <div class="{css_class}">
                        <div class="finding-title">{severity_icon} {finding.rule} — {finding.severity}</div>
                        <div class="finding-message">{finding.message}</div>
                        <div class="finding-message"><b>Recommendation:</b> {finding.recommendation}</div>
                        <div class="finding-tcode">T-Code: {finding.sap_tcode}</div>
                    </div>
                    """, unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            # RCA Summary Card
            st.markdown('<div class="fiori-card"><div class="fiori-card-title">RCA Summary</div>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""
                <div class="rca-root-cause">
                    <div class="rca-label" style="color:#BB0000;">Root Cause</div>
                    <div style="font-size:14px;color:#32363A;">{result.root_cause}</div>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown(f"""
                <div class="rca-recommendation">
                    <div class="rca-label" style="color:#107E3E;">Recommendation</div>
                    <div style="font-size:14px;color:#32363A;">{result.recommendation}</div>
                </div>
                """, unsafe_allow_html=True)

            confidence_pct = int(result.confidence * 100)
            st.progress(result.confidence, text=f"AI Confidence: {confidence_pct}%")
            st.markdown('</div>', unsafe_allow_html=True)

            # Footer
            st.markdown(f'<div class="fiori-footer">Investigated by: {" · ".join(result.investigated_by)}</div>', unsafe_allow_html=True)

        else:
            st.markdown(f'<div class="fiori-card"><p style="color:#BB0000;font-weight:600;">⚠ Invoice \'{invoice_number}\' not found.</p></div>', unsafe_allow_html=True)
