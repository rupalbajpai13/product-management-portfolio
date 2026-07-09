from rules.base_rule import BaseRule, Finding

AMOUNT_TOLERANCE = 10000


class AmountToleranceRule(BaseRule):
    """
    Flags high-value invoices that may require additional approval.

    SAP integration note:
        SAP uses tolerance keys (e.g. BD, PP, ST) configured in OMR6.
        Future: fetch tolerance limits from T169G table and compare
        against actual invoice amount from RBKP-RWBTR field.
    """

    def check(self, invoice, shipment) -> Finding | None:
        if invoice.invoice_amount > AMOUNT_TOLERANCE:
            return Finding(
                rule="AmountToleranceRule",
                severity="MEDIUM",
                field="invoice_amount",
                message=f"Invoice amount ${invoice.invoice_amount:,} exceeds tolerance threshold of ${AMOUNT_TOLERANCE:,}.",
                recommendation="Verify amount against PO value in SAP. Use MIR4 to review invoice details.",
                sap_tcode="MIR4"
            )
        return None
