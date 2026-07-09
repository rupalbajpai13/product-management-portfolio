from rules.base_rule import BaseRule, Finding


class MissingPORule(BaseRule):
    """
    Flags invoices with no PO reference.

    SAP integration note:
        In SAP, PO-based invoices are posted via MIRO (MM path).
        If po_number is missing, it may be an FI direct invoice (FB60).
        Future: validate po_number exists in EKKO table via RFC or OData.
    """

    def check(self, invoice, shipment) -> Finding | None:
        if not invoice.po_number or invoice.po_number.strip() == "":
            return Finding(
                rule="MissingPORule",
                severity="HIGH",
                field="po_number",
                message=f"Invoice {invoice.invoice_number} has no PO reference.",
                recommendation="Link a valid PO before posting. Use ME23N to verify PO exists.",
                sap_tcode="ME23N"
            )
        return None
