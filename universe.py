import pandas as pd

def load_universe():
    sp500 = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]["Symbol"]

    nasdaq = pd.read_html("https://en.wikipedia.org/wiki/Nasdaq-100")[0]["Ticker"]

    # Russell 2000 Proxy (ETF holdings)
    russell = pd.read_csv(
        "https://www.ishares.com/us/products/239710/ishares-russell-2000-etf/1467271812596.ajax?fileType=csv&fileName=IWM_holdings&dataType=fund",
        skiprows=9
    )["Ticker"]

    universe = pd.concat([sp500, nasdaq, russell])
    universe = universe.dropna().drop_duplicates()

    return list(universe)
