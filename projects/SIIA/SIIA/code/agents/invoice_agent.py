from services.invoice_service import InvoiceService
from models.invoice import Invoice


class InvoiceAgent:
    """
    Responsible for fetching and validating invoice data.
    Delegates data retrieval to InvoiceService.
    """

    def __init__(self):
        self.service = InvoiceService()

    def fetch(self, invoice_number: str) -> Invoice | None:
        return self.service.get_invoice(invoice_number)

    def validate(self, invoice: Invoice) -> list[str]:
        issues = []

        if invoice.invoice_amount <= 0:
            issues.append("Invoice amount must be greater than zero.")

        if invoice.invoice_quantity <= 0:
            issues.append("Invoice quantity must be greater than zero.")

        if not invoice.po_number:
            issues.append("PO number is missing.")

        return issues
