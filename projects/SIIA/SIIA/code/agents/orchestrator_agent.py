from agents.invoice_agent import InvoiceAgent
from agents.knowledge_agent import KnowledgeAgent
from agents.rule_agent import RuleAgent


class OrchestratorAgent:
    def __init__(self):
        self.invoice_agent = InvoiceAgent()
        self.knowledge_agent = KnowledgeAgent()
        self.rule_agent = RuleAgent()

    def run(self, invoice_number: str, error_message: str = ""):
        invoice = self.invoice_agent.fetch(invoice_number)
        if not invoice:
            return None

        self.knowledge_agent.enrich(invoice, shipment=None)
        findings = self.rule_agent.evaluate(invoice, shipment=None)

        return {
            "invoice": invoice,
            "findings": findings,
            "error_message": error_message
        }
