import yfinance as yf
import numpy as np
import pandas as pd

def fetch_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    df['Return'] = 100 * np.log(df['Adj Close'] / df['Adj Close'].shift(1))
    df.dropna(inplace=True)
    return df[['Adj Close', 'Return']]
