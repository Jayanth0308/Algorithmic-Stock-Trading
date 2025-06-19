import xgboost as xgb
from pathlib import Path
import pickle


class XGBModel:
    def __init__(self):
        self.model = xgb.XGBRegressor(n_estimators=100, max_depth=3, learning_rate=0.1)

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def save(self, path):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'wb') as f:
            pickle.dump(self.model, f)

    def load(self, path):
        with open(path, 'rb') as f:
            self.model = pickle.load(f)


