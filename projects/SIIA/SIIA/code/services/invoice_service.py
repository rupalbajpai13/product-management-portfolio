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
                "$format": "json",
                "$top": 1,
            }
            headers = {"APIKey": self.api_key, "Accept": "application/json"}
            response = requests.get(
                self.SAP_SANDBOX_URL, params=params, headers=headers, timeout=10
            )
            response.raise_for_status()
            results = response.json().get("d", {}).get("results", [])
            if not results:
                return None
            return self._map_sap_response(results[0])
        except Exception:
            return None

    def _map_sap_response(self, data: dict) -> Invoice:
        return Invoice(
            invoice_number=data.get("SupplierInvoice", ""),
            vendor_name=data.get("Supplier", "Unknown Vendor"),
            invoice_amount=float(data.get("DocumentTotalAmount", 0)),
            po_number=data.get("PurchaseOrder", ""),
            status=data.get("PostingStatus", "Unknown"),
            invoice_quantity=int(float(data.get("QuantityInBaseUnit", 0))),
        )

    def _fetch_from_mock(self, invoice_number: str) -> Invoice | None:
        with open(self.data_file, "r") as file:
            invoices = json.load(file)

        for invoice in invoices:
            if invoice["invoice_number"] == invoice_number:
                return Invoice(**invoice)

        return None
