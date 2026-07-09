from rules.base_rule import BaseRule, Finding


class ZeroQuantityRule(BaseRule):
    """
    Flags invoices with zero or negative quantity.

    SAP integration note:
        In SAP, invoice quantity is matched against GR quantity (EKBE table).
        Future: compare invoice_quantity against cumulative GR quantity
        from EKBE-MENGE where EKBE-VGABE = '1' (Goods Receipt movements).
    """

    def check(self, invoice, shipment) -> Finding | None:
        if invoice.invoice_quantity <= 0:
            return Finding(
                rule="ZeroQuantityRule",
                severity="HIGH",
                field="invoice_quantity",
                message=f"Invoice {invoice.invoice_number} has an invalid quantity of {invoice.invoice_quantity}.",
                recommendation="Verify quantity against GR documents. Use MIGO to check goods receipt.",
                sap_tcode="MIGO"
            )
        return None
