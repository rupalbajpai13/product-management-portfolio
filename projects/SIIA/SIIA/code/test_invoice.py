import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from agents.invoice_agent import InvoiceAgent

agent = InvoiceAgent()
invoice = agent.fetch("INV-1001")

if invoice:
    print("Invoice fetched successfully:")
    print(f"  Invoice Number : {invoice.invoice_number}")
    print(f"  Vendor         : {invoice.vendor_name}")
    print(f"  Amount         : {invoice.invoice_amount}")
    print(f"  PO Number      : {invoice.po_number}")
    print(f"  Status         : {invoice.status}")
    print(f"  Quantity       : {invoice.invoice_quantity}")
else:
    print("Invoice not found.")
