import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

from data import fetch_data, prepare_dataset
from model import XGBModel
from backtest import Backtester


def main():
    tickers = ['AAPL', 'MSFT']
    start = '2018-01-01'
    end = '2023-01-01'
    raw = fetch_data(tickers[0], start, end)
    features, labels = prepare_dataset(raw)

    split = int(len(features) * 0.8)
    X_train, X_test = features.iloc[:split], features.iloc[split:]
    y_train, y_test = labels.iloc[:split], labels.iloc[split:]

    model = XGBModel()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    tester = Backtester()
    results = tester.run(raw['Close'].iloc[split:], preds)

    plt.figure(figsize=(10, 5))
    plt.plot(results.index, results['equity'], label='Strategy Equity')
    plt.title('Portfolio Growth')
    plt.xlabel('Date')
    plt.ylabel('Equity')
    plt.legend()
    plt.tight_layout()
    plt.savefig('results/equity.png')
    results.to_csv('results/backtest.csv')
    model.save('models/xgb_model.pkl')


if __name__ == '__main__':
    main()
