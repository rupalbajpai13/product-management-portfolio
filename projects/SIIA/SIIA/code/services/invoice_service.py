import json
from pathlib import Path

from models.invoice import Invoice


class InvoiceService:
    """
    Service responsible for retrieving invoice data.

    Current implementation:
        - Reads from mock JSON.

    Future implementation:
        - SAP OData API
        - SAP RFC
        - REST API
        - Database
    """

    def __init__(self):
        self.data_file = (
            Path(__file__).resolve().parent.parent.parent
            / "mock_data"
            / "invoices.json"
        )

    def get_invoice(self, invoice_number: str) -> Invoice | None:

        with open(self.data_file, "r") as file:
            invoices = json.load(file)

        for invoice in invoices:

            if invoice["invoice_number"] == invoice_number:
                return Invoice(**invoice)

        return None
