from dataclasses import dataclass, field

from models.invoice import Invoice
from rules.base_rule import Finding


@dataclass
class InvestigationResult:
    invoice: Invoice
    findings: list[Finding]
    confidence: float
    root_cause: str
    recommendation: str
    knowledge_articles: list = field(default_factory=list)
    investigated_by: list = field(default_factory=list)
