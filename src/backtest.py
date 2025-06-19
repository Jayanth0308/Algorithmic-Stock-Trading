import pandas as pd


class Backtester:
    def __init__(self, initial_cash=10000):
        self.initial_cash = initial_cash

    def run(self, prices, predictions):
        df = pd.DataFrame({'price': prices, 'pred': predictions})
        df['signal'] = df['pred'] > 0
        df['position'] = df['signal'].astype(int)
        df['market_return'] = df['price'].pct_change()
        df['strategy_return'] = df['position'].shift(1) * df['market_return']
        df['equity'] = (1 + df['strategy_return']).cumprod() * self.initial_cash
        return df


