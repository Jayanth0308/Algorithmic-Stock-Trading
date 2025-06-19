diff --git a/README.md b/README.md
index dd3182b4749a7b8a84b05999581ad760b1eae689..4f022e42117826c253c9d8c2dfaf9adc51ff3e9a 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,21 @@
-# Algorithmic-Stock-Trading
+# Algorithmic Stock Trading
+
+This project demonstrates a simple machine learning based trading strategy. Historical data for stocks such as AAPL and MSFT are fetched from Yahoo Finance. Technical indicators like SMA, RSI and MACD are used as features for an XGBoost model that predicts the next day's return. The predictions drive a basic long/flat trading simulation. Results including the equity curve are stored in the `results/` directory.
+
+## Project Structure
+
+- `src/` – scripts for data loading, feature engineering, model training and backtesting
+- `data/` – placeholder for any downloaded datasets
+- `models/` – trained model artifacts
+- `results/` – backtesting results and plots
+
+## Usage
+
+Install requirements and run the main script:
+
+```bash
+pip install -r requirements.txt
+python src/main.py
+```
+
+The script will output `results/equity.png` and `results/backtest.csv` showing strategy performance.
