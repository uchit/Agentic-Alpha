
import yfinance as yf


def get_stock_data(symbol: str):

    stock = yf.Ticker(symbol)
    hist = stock.history(period="1mo")

    return {
        "symbol": symbol,
        "latest_close": float(hist["Close"].iloc[-1]),
        "high": float(hist["High"].max()),
        "low": float(hist["Low"].min())
    }


def calculate_fibonacci_levels(symbol: str):

    data = get_stock_data(symbol)

    high = data["high"]
    low = data["low"]

    diff = high - low

    return {
        "0.236": high - diff * 0.236,
        "0.382": high - diff * 0.382,
        "0.5": high - diff * 0.5,
        "0.618": high - diff * 0.618,
        "0.786": high - diff * 0.786
    }


def get_fibonacci_analysis(symbol: str):
    fib_data = calculate_fibonacci_levels(symbol)
    return fib_data


def get_market_data(symbol: str):
    data = get_stock_data(symbol)
    return data


def analyze_patterns(symbol: str):

    data = get_stock_data(symbol)

    if data["latest_close"] > (data["high"] + data["low"]) / 2:
        return {"pattern": "bullish"}
    else:
        return {"pattern": "bearish"}
