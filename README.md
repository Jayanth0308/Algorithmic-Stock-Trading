# Algorithmic Stock Trading

This repository contains a minimal example of building a machine-learning driven trading strategy. The goal is to demonstrate how historical price data can be used to train a predictive model and evaluate a simple trading rule.

## Overview
1. **Data** – Daily OHLCV data is downloaded from [Yahoo Finance](https://finance.yahoo.com) for a set of tickers (e.g. AAPL, MSFT).
2. **Features** – Basic technical indicators such as SMA, RSI and MACD are computed and used as model inputs.
3. **Model** – A small `xgboost` regressor is trained to forecast the next-day return of a single stock.
4. **Backtest** – Predictions are converted to long/flat signals and the resulting equity curve is calculated.

All scripts live in the `src/` directory and results (plots, csv files, trained model) are written to `results/` and `models/`.

## Directory Structure
- `src/` – data loading, indicator functions, model wrapper and backtesting code
- `data/` – optional location to store fetched datasets
- `models/` – persisted models
- `results/` – output from backtests

## Requirements
Dependencies are listed in `requirements.txt`. The project relies on `pandas`, `numpy`, `matplotlib`, `yfinance` and `xgboost`. Install them with:

```bash
pip install -r requirements.txt
```

*Note: the Codex environment used for automated testing does not have internet access, so installing packages or downloading data may fail in that environment.*

## Running the Example
Once the required packages are installed, execute the main script:

```bash
python src/main.py
```

The script will download price data, train the model, run a simple backtest and save:

- `results/equity.png` – a plot of cumulative equity
- `results/backtest.csv` – detailed daily returns
- `models/xgb_model.pkl` – the fitted model

These outputs allow inspection of the basic strategy performance.
