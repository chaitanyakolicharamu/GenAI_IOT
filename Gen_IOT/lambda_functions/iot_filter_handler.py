import json
from datetime import datetime

# Example simple filters (can be replaced with smarter logic later)
CRITICAL_TEMP = 32.0
CRITICAL_AQI = 150

def analyze_payload(payload):
    reasons = []

    if payload["temperature"] > CRITICAL_TEMP:
        reasons.append("⚠️ High temperature detected")

    if payload["air_quality_index"] > CRITICAL_AQI:
        reasons.append("⚠️ Poor air quality")

    return reasons

def lambda_handler(event):
    try:
        payload = json.loads(event)

        # Analyze and decide what to do
        alerts = analyze_payload(payload)

        if alerts:
            prompt = (
                f"Sensor {payload['device_id']} reported anomalies:\n"
                f"Temperature: {payload['temperature']}°C\n"
                f"AQI: {payload['air_quality_index']}\n"
                f"Timestamp: {payload['timestamp']}\n"
                f"Generate a human-readable alert message."
            )
            print("[GenAI Prompt Prepared]:", prompt)
            # Normally, send to GenAI backend (bedrock_handler) here
        else:
            print("[Normal]: No critical events detected.")

    except Exception as e:
        print("❌ Error in filter handler:", str(e))

# For testing locally
if __name__ == "__main__":
    from iot_simulator.device_sim import generate_sensor_payload
    test_payload = json.dumps(generate_sensor_payload())
    lambda_handler(test_payload)
