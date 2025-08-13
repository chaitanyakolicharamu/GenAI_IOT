import streamlit as st
import json
import requests

st.set_page_config(page_title="GEN-IoT Dashboard", layout="wide")
st.title("🌐 GEN-IoT Monitoring Dashboard")

st.markdown("---")

# Simulated API call — replace with actual backend later
def get_latest_data():
    return {
        "device_id": "Sensor-001",
        "temperature": 35.4,
        "humidity": 76,
        "aqi": 181,
        "timestamp": "2025-08-02 10:34:21",
        "genai_insight": "⚠️ Air quality is poor and temperature is high. Recommend staying indoors."
    }

data = get_latest_data()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📟 Sensor Data")
    st.write(f"**Device ID:** {data['device_id']}")
    st.write(f"**Temperature:** {data['temperature']} °C")
    st.write(f"**Humidity:** {data['humidity']} %")
    st.write(f"**Air Quality Index (AQI):** {data['aqi']}")
    st.write(f"**Timestamp:** {data['timestamp']}")

with col2:
    st.subheader("🧠 GenAI Insight")
    st.success(data["genai_insight"])  # or st.warning() based on severity

st.markdown("---")
st.info("🔄 This dashboard simulates a local IoT device with real-time GenAI reasoning.")
