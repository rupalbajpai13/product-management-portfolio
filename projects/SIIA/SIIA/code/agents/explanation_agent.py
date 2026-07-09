from models.invoice import Invoice
from models.investigation_result import InvestigationResult
from rules.base_rule import Finding
from services.llm_service import LLMService


class ExplanationAgent:
    """
    Generates a human-readable RCA explanation using LLM.
    Delegates LLM calls to LLMService.

    SAP integration note:
        When connected to SAP, invoice and findings will come from
        OData/RFC responses. The prompt and explanation logic stays unchanged.
    """

    def __init__(self):
        self.service = LLMService()

    def explain(
        self,
        invoice: Invoice,
        findings: list[Finding],
        error_message: str = ""
    ) -> dict:
        prompt = self._build_prompt(invoice, findings, error_message)
        return self.service.generate(prompt)

    def _build_prompt(
        self,
        invoice: Invoice,
        findings: list[Finding],
        error_message: str
    ) -> str:

        invoice_context = f"""
Invoice Number : {invoice.invoice_number}
Vendor         : {invoice.vendor_name}
PO Number      : {invoice.po_number}
Amount         : ${invoice.invoice_amount:,}
Quantity       : {invoice.invoice_quantity}
Status         : {invoice.status}
"""

        findings_text = ""
        for f in findings:
            findings_text += f"""
- [{f.severity}] {f.rule}
  Issue          : {f.message}
  Recommendation : {f.recommendation}
  SAP T-Code     : {f.sap_tcode}
"""

        error_context = f"\nError Message from SAP: {error_message}" if error_message else ""

        return f"""You are an SAP Accounts Payable expert helping an AP specialist investigate a blocked invoice.

Invoice Details:
{invoice_context}
{error_context}

Investigation Findings:
{findings_text}

Based on the above, provide:

1. Root Cause
Explain in 1-2 sentences why this invoice is blocked.

2. Resolution
Provide step-by-step actions to resolve, including SAP T-codes.

3. Risk
What is the business risk if this is not resolved promptly?
"""
