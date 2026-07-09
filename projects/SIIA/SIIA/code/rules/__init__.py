from rules.blocked_status import BlockedStatusRule
from rules.missing_po import MissingPORule
from rules.amount_tolerance import AmountToleranceRule
from rules.zero_amount import ZeroAmountRule
from rules.zero_quantity import ZeroQuantityRule

ALL_RULES = [
    BlockedStatusRule(),
    MissingPORule(),
    AmountToleranceRule(),
    ZeroAmountRule(),
    ZeroQuantityRule(),
]
