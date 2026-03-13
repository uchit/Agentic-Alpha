
from app.tools.pydantic_market_tools import (
    get_market_data,
    get_fibonacci_analysis,
    analyze_patterns
)

from app.models.trading_models import TradingDecision, TradingSignal


def market_analyst_agent(symbol):

    fib = get_fibonacci_analysis(symbol)

    return {
        "symbol": symbol,
        "fibonacci_levels": fib
    }


def strategy_agent(symbol):

    data = get_market_data(symbol)

    return {
        "symbol": symbol,
        "market_data": data
    }


def trading_signal_agent(symbol):

    data = get_market_data(symbol)
    pattern = analyze_patterns(symbol)

    decision = TradingSignal.HOLD

    if pattern["pattern"] == "bullish":
        decision = TradingSignal.BUY
    elif pattern["pattern"] == "bearish":
        decision = TradingSignal.SELL

    result = TradingDecision(
        symbol=symbol,
        decision=decision,
        confidence=0.75,
        reasoning=f"Pattern detected: {pattern['pattern']}"
    )

    return result
