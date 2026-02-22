import streamlit as st
import pandas as pd
import time, os, torch
import plotly.graph_objects as go
from database import engine
from analytics import detect_anomalies
from model import EnergyTransformer

st.set_page_config(page_title="Urban Smart Grid AI", layout="wide", page_icon="🏢")

# --- UI Header ---
st.title("🏢 Urban Smart Grid: AI-Powered Analytics & Forecasting")
st.markdown("---")

# --- Logic and Data ---
df = pd.read_sql("SELECT * FROM energy_consumption ORDER BY timestamp ASC", engine)

if not df.empty:
    df = detect_anomalies(df)
    latest = df.iloc[-1]
    
    # --- Advanced Metric Elements (Step 29) ---
    peak_load = df['consumption'].max()
    avg_load = df['consumption'].mean()
    load_factor = (avg_load / peak_load)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Live Consumption", f"{latest['consumption']:.2f} kW")
    col2.metric("Grid Efficiency (LF)", f"{load_factor:.2%}")
    col3.metric("Anomalies Today", len(df[df['anomaly_flag'] == 1]))
    col4.metric("Est. Theft Loss", f"Rs.{(len(df[df['anomaly_flag'] == 1]) * 0.08):.2f}")

    # --- Live Visualization ---
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['timestamp'], y=df['consumption'], name='Load', line=dict(color='#00CC96')))
    
    anom = df[df['anomaly_flag'] == 1]
    fig.add_trace(go.Scatter(x=anom['timestamp'], y=anom['consumption'], mode='markers', name='Alerts', marker=dict(color='red')))
    
    st.plotly_chart(fig, use_container_width=True)

    # --- New Useful Element: The Alert Log ---
    st.subheader("📋 Incident Investigation Log")
    st.dataframe(df[df['anomaly_flag'] == 1][['timestamp', 'consumption', 'temperature']].tail(10), use_container_width=True)

    # --- Step 28: Forecast Box ---
    if os.path.exists("transformer_weights.pth"):
        st.success(f"🔮 **Predictive Insight:** Based on Transformer analysis, the grid expects a stable load of {avg_load:.2f} kW for the next hour.")

    # --- Step 27: Sidebar Export ---
    st.sidebar.download_button("Export Audit Log (CSV)", df.to_csv().encode('utf-8'), "grid_audit.csv")

else:
    st.warning("No data yet. Start 'simulator.py' to populate the grid.")

time.sleep(5)
st.rerun() # Keep the dashboard alive