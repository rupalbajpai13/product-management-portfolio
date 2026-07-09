from rules.base_rule import BaseRule, Finding


class ZeroAmountRule(BaseRule):
    """
    Flags invoices with zero or negative amount.

    SAP integration note:
        SAP allows credit memos with negative amounts (RBKP-RBSTAT = S).
        Future: distinguish credit memos from invalid zero-amount invoices
        using RBKP-XRECH flag before applying this rule.
    """

    def check(self, invoice, shipment) -> Finding | None:
        if invoice.invoice_amount <= 0:
            return Finding(
                rule="ZeroAmountRule",
                severity="HIGH",
                field="invoice_amount",
                message=f"Invoice {invoice.invoice_number} has an invalid amount of ${invoice.invoice_amount}.",
                recommendation="Correct the invoice amount and resubmit. Use MIR7 to edit parked invoices.",
                sap_tcode="MIR7"
            )
        return None
