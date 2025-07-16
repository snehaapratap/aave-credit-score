from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import RobustScaler
import numpy as np
import pandas as pd

class CreditScorer:
    def __init__(self):
        self.scaler = RobustScaler()
        self.iforest = IsolationForest(
            n_estimators=500, max_samples='auto', contamination=0.1,
            random_state=42)

    def fit(self, X: pd.DataFrame):
        Xs = self.scaler.fit_transform(X)
        self.iforest.fit(Xs)
        return self

    def predict(self, X: pd.DataFrame) -> pd.Series:
        Xs = self.scaler.transform(X)
        rel = -self.iforest.decision_function(Xs)          
        score = (1 - (rel - rel.min()) / (rel.max() - rel.min())) * 1000
        return score.round(0).astype(int)                  
