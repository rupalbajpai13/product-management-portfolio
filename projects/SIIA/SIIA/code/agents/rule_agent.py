# Rule Agent
# Applies configurable business rules to flag discrepancies between invoices and shipments.

class RuleAgent:
    def __init__(self, rules=None):
        self.rules = rules or []

    def evaluate(self, invoice, shipment):
        """Apply all loaded rules and return a list of discrepancy findings."""
        findings = []
        for rule in self.rules:
            result = rule.check(invoice, shipment)
            if result:
                findings.append(result)
        return findings
