import pandas as pd
import numpy as np
import yfinance as yf

def get_data(symbol):
    return yf.Ticker(symbol).history(period="6mo")

def rsi(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def macd(series):
    ema12 = series.ewm(span=12).mean()
    ema26 = series.ewm(span=26).mean()
    return ema12 - ema26

def ema_trend(series):
    ema20 = series.ewm(span=20).mean()
    ema50 = series.ewm(span=50).mean()
    return series.iloc[-1] > ema20.iloc[-1] > ema50.iloc[-1]
