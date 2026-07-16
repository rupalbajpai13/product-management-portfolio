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

def fetch_invoices(top: int = 10):
    api_key = os.getenv("SAP_API_KEY")
    if not api_key:
        print("ERROR: SAP_API_KEY environment variable not set.")
        print("  Set it with: set SAP_API_KEY=your_key_here")
        return

    params = {
        "$format": "json",
        "$top": top,
        "$select": "SupplierInvoice,Supplier,DocumentTotalAmount,PurchaseOrder,PostingStatus,FiscalYear",
    }
    headers = {"APIKey": api_key, "Accept": "application/json"}

    print(f"Fetching top {top} invoices from SAP sandbox...\n")

    try:
        response = requests.get(SAP_SANDBOX_URL, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        results = response.json().get("d", {}).get("results", [])

        if not results:
            print("No invoices found in sandbox.")
            return

        print(f"{'Invoice No.':<20} {'Supplier':<20} {'Amount':<15} {'PO Number':<20} {'Status'}")
        print("-" * 85)
        for inv in results:
            print(
                f"{inv.get('SupplierInvoice',''):<20} "
                f"{inv.get('Supplier',''):<20} "
                f"{inv.get('DocumentTotalAmount',''):<15} "
                f"{inv.get('PurchaseOrder',''):<20} "
                f"{inv.get('PostingStatus','')}"
            )

        print(f"\nRaw first record:\n{json.dumps(results[0], indent=2)}")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e.response.status_code} — {e.response.text}")
    except requests.exceptions.ConnectionError:
        print("Connection error — check your internet/VPN.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    fetch_invoices()
