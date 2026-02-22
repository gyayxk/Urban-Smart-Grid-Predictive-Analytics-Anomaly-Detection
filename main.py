import pandas as pd
import time
import torch
import os
from database import engine
from analytics import detect_anomalies
from model import EnergyTransformer

def monitor_grid():
    print("--- Smart Grid AI Monitor Active ---")
    
    # 1. Try to load the Transformer "Brain"
    model = None
    weights_path = "transformer_weights.pth"
    
    if os.path.exists(weights_path):
        try:
            model = EnergyTransformer(feature_size=1)
            model.load_state_dict(torch.load(weights_path))
            model.eval()
            print("✅ Transformer model loaded successfully for forecasting.")
        except Exception as e:
            print(f"⚠️ Could not load model: {e}")
    else:
        print("ℹ️ No trained model found. Skipping forecast, focusing on anomaly detection.")

    while True:
        # 2. Fetch data from Database
        try:
            df = pd.read_sql("SELECT * FROM energy_consumption", engine)
        except Exception as e:
            print(f"Database error: {e}")
            time.sleep(5)
            continue

        if not df.empty:
            # 3. Analytics: Detect Anomaly (Isolation Forest)
            df = detect_anomalies(df)
            latest = df.iloc[-1]
            
            # 4. AI: Forecast (Transformer) - Only if model exists
            forecast_str = ""
            if model is not None:
                with torch.no_grad():
                    # Take the last reading to predict the next
                    input_val = torch.FloatTensor([latest['consumption']]).view(1, 1, 1)
                    prediction = model(input_val)
                    forecast_str = f" | Next Prediction: {prediction.item():.2f} kW"

            # 5. Output Result
            status = "⚠️ ALERT!" if latest['anomaly_flag'] == 1 else "Normal"
            print(f"[{latest['timestamp']}] {status} | Actual: {latest['consumption']:.2f} kW{forecast_str}")
        
        time.sleep(5)

if __name__ == "__main__":
    monitor_grid()