from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies(df):
    if len(df) < 5: return df # Need minimum data
    model = IsolationForest(contamination=0.05) # Assume 5% anomaly rate
    df['anomaly_score'] = model.fit_predict(df[['consumption']])
    # -1 is an anomaly in sklearn
    df['anomaly_flag'] = df['anomaly_score'].apply(lambda x: 1 if x == -1 else 0)
    return df