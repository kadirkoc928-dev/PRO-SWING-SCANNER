from indicators import get_data, rsi, macd, ema_trend
from universe import load_universe

def swing_score(df):
    close = df["Close"]
    volume = df["Volume"]

    rsi_val = rsi(close).iloc[-1]
    macd_val = macd(close)
    macd_cross = macd_val.iloc[-1] > macd_val.iloc[-2]

    trend = ema_trend(close)

    vol_spike = volume.iloc[-1] > volume.mean() * 1.5
    breakout = close.iloc[-1] > close.max() * 0.98

    score = 0

    # RSI
    if 40 <= rsi_val <= 65:
        score += 20

    # Trend
    if trend:
        score += 25

    # MACD
    if macd_cross:
        score += 20

    # Volume
    if vol_spike:
        score += 15

    # Breakout
    if breakout:
        score += 20

    return min(score, 100)


def scan_market(limit=200):
    universe = load_universe()[:limit]  # safety limit for streamlit

    results = []

    for symbol in universe:
        try:
            df = get_data(symbol)

            if df is None or len(df) < 50:
                continue

            score = swing_score(df)

            results.append({
                "symbol": symbol,
                "score": score
            })

        except:
            continue

    return sorted(results, key=lambda x: x["score"], reverse=True)
