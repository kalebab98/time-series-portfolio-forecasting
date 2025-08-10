import yfinance as yf
import os
import pandas as pd

def fetch_asset_data(ticker, start="2015-07-01", end="2025-07-31", save_path=None):
    df = yf.download(ticker, start=start, end=end)
    df.reset_index(inplace=True)
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        df.to_csv(save_path, index=False)
    return df

if __name__ == "__main__":
    tickers = {
        "TSLA": "data/raw/tsla.csv",
        "BND": "data/raw/bnd.csv",
        "SPY": "data/raw/spy.csv"
    }

    for ticker, path in tickers.items():
        print(f"Fetching {ticker} data...")
        fetch_asset_data(ticker, save_path=path)
