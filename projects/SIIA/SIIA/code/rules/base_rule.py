from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class Finding:
    rule: str
    severity: str        # HIGH, MEDIUM, LOW
    message: str
    recommendation: str
    sap_tcode: str       # SAP transaction code to resolve (e.g. MIR7, MRBR, FB60)
    field: Optional[str] = None   # which invoice field triggered this rule


class BaseRule(ABC):
    """
    Abstract base for all invoice validation rules.

    SAP integration note:
        When connecting to SAP, rule inputs (invoice, shipment) will come from
        OData services (e.g. /sap/opu/odata/sap/MM_PUR_POITEMS_MANAGE_SRV)
        or RFC calls. The rule interface stays the same — only the data source changes.
    """

    @abstractmethod
    def check(self, invoice, shipment) -> Optional[Finding]:
        """
        Evaluate the rule against invoice and shipment data.
        Returns a Finding if the rule is violated, None otherwise.
        """
        pass
