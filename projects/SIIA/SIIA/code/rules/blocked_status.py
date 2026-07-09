from rules.base_rule import BaseRule, Finding


class BlockedStatusRule(BaseRule):
    """
    Flags invoices with SAP blocked status.

    SAP integration note:
        In SAP, RBSTAT field on RBKP table holds the blocking reason.
        Blocking codes: A=manual, B=price variance, R=quantity variance, Z=stochastic.
        Future: fetch RBSTAT via RFC_READ_TABLE or OData to get exact block code.
    """

    def check(self, invoice, shipment) -> Finding | None:
        if invoice.status == "Blocked":
            return Finding(
                rule="BlockedStatusRule",
                severity="HIGH",
                field="status",
                message=f"Invoice {invoice.invoice_number} is blocked in SAP.",
                recommendation="Check for price variance or missing Goods Receipt (GR). Use MRBR to release after resolving.",
                sap_tcode="MRBR"
            )
        return None
