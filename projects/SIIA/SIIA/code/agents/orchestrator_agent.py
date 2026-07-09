from agents.invoice_agent import InvoiceAgent
from agents.knowledge_agent import KnowledgeAgent
from agents.rule_agent import RuleAgent
from agents.explanation_agent import ExplanationAgent
from models.investigation_result import InvestigationResult


class OrchestratorAgent:
    def __init__(self):
        self.invoice_agent = InvoiceAgent()
        self.knowledge_agent = KnowledgeAgent()
        self.rule_agent = RuleAgent()
        self.explanation_agent = ExplanationAgent()

    def run(self, invoice_number: str, error_message: str = "") -> InvestigationResult | None:
        invoice = self.invoice_agent.fetch(invoice_number)
        if not invoice:
            return None

        self.knowledge_agent.enrich(invoice, shipment=None)
        findings = self.rule_agent.evaluate(invoice, shipment=None)

        explanation = self.explanation_agent.explain(invoice, findings, error_message)

        return InvestigationResult(
            invoice=invoice,
            findings=findings,
            confidence=explanation.get("confidence", 0.0),
            root_cause=explanation.get("root_cause", ""),
            recommendation=explanation.get("recommendation", ""),
            investigated_by=["InvoiceAgent", "RuleAgent", "ExplanationAgent"],
        )
