from dataclasses import dataclass


@dataclass
class Invoice:
    invoice_number: str
    vendor_name: str
    invoice_amount: float
    po_number: str
    status: str
    invoice_quantity: int
