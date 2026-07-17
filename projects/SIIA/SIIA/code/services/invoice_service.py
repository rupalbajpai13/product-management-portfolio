import json
import os
import requests
from pathlib import Path

from models.invoice import Invoice


class InvoiceService:
    """
    Service responsible for retrieving invoice data.

    Source priority:
        1. SAP API (API_SUPPLIER_INVOICE_SRV) — if SAP_API_KEY is set
        2. Mock JSON — fallback for local dev/demo
    """

    SAP_SANDBOX_URL = (
        "https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap"
        "/API_SUPPLIER_INVOICE_SRV/A_SupplierInvoice"
    )

    def __init__(self):
        self.api_key = os.getenv("SAP_API_KEY")
        self.data_file = (
            Path(__file__).resolve().parent.parent.parent
            / "mock_data"
            / "invoices.json"
        )

    def get_invoice(self, invoice_number: str) -> Invoice | None:
        if self.api_key:
            invoice = self._fetch_from_sap(invoice_number)
            if invoice:
                return invoice

        return self._fetch_from_mock(invoice_number)

    def _fetch_from_sap(self, invoice_number: str) -> Invoice | None:
        try:
            params = {
                "$filter": f"SupplierInvoice eq '{invoice_number}'",
                "$top": 1,
            }
            headers = {"APIKey": self.api_key, "Accept": "application/json"}
            response = requests.get(
                self.SAP_SANDBOX_URL, params=params, headers=headers, timeout=10
            )
            response.raise_for_status()
            results = response.json().get("value", [])
            if not results:
                return None
            return self._map_sap_response(results[0])
        except Exception:
            return None

    def _map_sap_response(self, data: dict) -> Invoice:
        # Map PaymentBlockingReason — empty means Open, any value means Blocked
        blocking_reason = data.get("PaymentBlockingReason", "")
        status = "Blocked" if blocking_reason else "Open"

        return Invoice(
            invoice_number=data.get("SupplierInvoice", ""),
            vendor_name=data.get("InvoicingParty", "Unknown Vendor"),
            invoice_amount=float(data.get("InvoiceGrossAmount", 0)),
            po_number=data.get("SupplierInvoiceIDByInvcgParty", ""),
            status=status,
            invoice_quantity=0,  # requires line item API call (A_SuplrInvcItemPurOrdRef)
        )

    def _fetch_from_mock(self, invoice_number: str) -> Invoice | None:
        with open(self.data_file, "r") as file:
            invoices = json.load(file)

        for invoice in invoices:
            if invoice["invoice_number"] == invoice_number:
                return Invoice(**invoice)

        return None
