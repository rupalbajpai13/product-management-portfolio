"""
Run this script to fetch invoices from the SAP sandbox API.

Usage:
    set SAP_API_KEY=your_key_here
    python fetch_sandbox_invoices.py
"""

import os
import json
import requests

SAP_SANDBOX_URL = (
    "https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap"
    "/API_SUPPLIER_INVOICE_SRV/A_SupplierInvoice"
)

def fetch_invoices(top: int = 50):
    api_key = os.getenv("SAP_API_KEY")
    if not api_key:
        print("ERROR: SAP_API_KEY environment variable not set.")
        print("  Set it with: set SAP_API_KEY=your_key_here")
        return

    params = {
        "$top": top,
        "$select": "SupplierInvoice,InvoicingParty,InvoiceGrossAmount,SupplierInvoiceIDByInvcgParty,PaymentBlockingReason,FiscalYear",
    }
    headers = {"APIKey": api_key, "Accept": "application/json"}

    print(f"Fetching top {top} invoices from SAP sandbox...\n")

    try:
        response = requests.get(SAP_SANDBOX_URL, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        results = response.json().get("value", [])

        if not results:
            print("No invoices found in sandbox.")
            return

        print(f"{'Invoice No.':<15} {'Invoicing Party':<20} {'Amount':<12} {'Blocking Reason':<20} {'Status'}")
        print("-" * 80)
        blocked = []
        for inv in results:
            blocking = inv.get("PaymentBlockingReason", "")
            status = "🔴 BLOCKED" if blocking else "🟢 Open"
            if blocking:
                blocked.append(inv.get("SupplierInvoice"))
            print(
                f"{inv.get('SupplierInvoice',''):<15} "
                f"{inv.get('InvoicingParty',''):<20} "
                f"{inv.get('InvoiceGrossAmount',''):<12} "
                f"{blocking:<20} "
                f"{status}"
            )

        print(f"\nBlocked invoices: {blocked if blocked else 'None found in top {top}'}")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e.response.status_code} — {e.response.text}")
    except requests.exceptions.ConnectionError:
        print("Connection error — check your internet/VPN.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    fetch_invoices()
