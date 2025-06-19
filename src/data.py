import yfinance as yf
import pandas as pd


def fetch_data(tickers, start, end):
    """Fetch historical OHLCV data for given tickers."""
    data = yf.download(tickers, start=start, end=end, progress=False)
    return data


def add_indicators(df, window=14):
    df = df.copy()
    df['sma'] = df['Close'].rolling(window=window).mean()
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window).mean()
    rs = gain / loss
    df['rsi'] = 100 - (100 / (1 + rs))
    df['ema12'] = df['Close'].ewm(span=12, adjust=False).mean()
    df['ema26'] = df['Close'].ewm(span=26, adjust=False).mean()
    df['macd'] = df['ema12'] - df['ema26']
    df['signal'] = df['macd'].ewm(span=9, adjust=False).mean()
    df = df.dropna()
    return df


def prepare_dataset(df):
    """Add technical indicators and compute next-day return as label."""
    df = add_indicators(df)
    df['return'] = df['Close'].pct_change().shift(-1)
    df = df.dropna()
    features = df[['sma', 'rsi', 'macd', 'signal']]
    labels = df['return']
    return features, labels



