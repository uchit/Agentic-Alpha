
from enum import Enum
from pydantic import BaseModel


class TradingSignal(str, Enum):
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"


class RiskLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class TradingDecision(BaseModel):
    symbol: str
    decision: TradingSignal
    confidence: float
    reasoning: str
