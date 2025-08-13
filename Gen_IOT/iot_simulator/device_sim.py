import json
import random
import time
from datetime import datetime

def generate_sensor_payload():
    payload = {
        "device_id": "sensor_001",
        "timestamp": datetime.utcnow().isoformat(),
        "temperature": round(random.uniform(20.0, 35.0), 2),
        "humidity": round(random.uniform(30.0, 70.0), 2),
        "air_quality_index": random.randint(50, 200),
        "status": "active"
    }
    return payload

def run_simulator(interval_seconds=5):
    print("📡 Virtual IoT Device Simulator started.")
    try:
        while True:
            payload = generate_sensor_payload()
            print("[Simulated Sensor Output]:", json.dumps(payload))
            # In production, this will POST to Lambda or a local handler
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        print("❌ IoT Simulation stopped manually.")

if __name__ == "__main__":
    run_simulator()
