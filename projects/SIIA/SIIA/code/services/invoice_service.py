# Invoice Service
# Loads invoice data from JSON (MVP). SAP API integration is a future stub.

import json
import os


class InvoiceService:
    def __init__(self, data_source="json"):
        self.data_source = data_source

    def get_invoice(self, invoice_number):
        if self.data_source == "json":
            return self._load_from_json(invoice_number)
        elif self.data_source == "sap_api":
            return self._load_from_sap_api(invoice_number)

    def _load_from_json(self, invoice_number):
        json_path = os.path.join(os.path.dirname(__file__), "../../mock_data/invoices.json")
        with open(json_path, "r") as f:
            invoices = json.load(f)
        for invoice in invoices:
            if invoice["invoice_number"] == invoice_number:
                return invoice
        return None

    def _load_from_sap_api(self, invoice_number):
        # TODO: integrate SAP API
        raise NotImplementedError("SAP API integration not yet implemented.")
