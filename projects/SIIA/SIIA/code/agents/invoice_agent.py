from services.invoice_service import InvoiceService
from models.invoice import Invoice


class InvoiceAgent:
    """
    Responsible for fetching invoice data.
    Delegates data retrieval to InvoiceService.
    """

    def __init__(self):
        self.service = InvoiceService()

    def fetch(self, invoice_number: str) -> Invoice | None:
        return self.service.get_invoice(invoice_number)
