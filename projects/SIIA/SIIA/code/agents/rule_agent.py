from rules import ALL_RULES


class RuleAgent:
    """
    Applies business rules to flag invoice discrepancies.

    SAP integration note:
        Rules are currently evaluated against mock data.
        When connected to SAP, invoice and shipment objects will be
        populated from OData/RFC responses — rule logic stays unchanged.
        Add new rules in rules/ and register them in rules/__init__.py.
    """

    def __init__(self, rules=None):
        self.rules = rules if rules is not None else ALL_RULES

    def evaluate(self, invoice, shipment):
        findings = []
        for rule in self.rules:
            result = rule.check(invoice, shipment)
            if result:
                findings.append(result)
        return findings
