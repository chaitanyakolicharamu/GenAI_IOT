import boto3
import logging
import json
from botocore.exceptions import BotoCoreError, ClientError

# Setup logging
logger = logging.getLogger("BedrockHandler")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

# Bedrock runtime client
bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

# Model ID for Titan Text Lite
MODEL_ID = "amazon.titan-text-lite-v1"

def query_bedrock(prompt: str) -> str:
    body = {
        "inputText": prompt,
        "textGenerationConfig": {
            "maxTokenCount": 200,
            "temperature": 0.7,
            "topP": 0.9,
            "stopSequences": []
        }
    }

    try:
        response = bedrock.invoke_model(
            body=json.dumps(body),
            modelId=MODEL_ID,
            accept="application/json",
            contentType="application/json"
        )

        response_body = json.loads(response["body"].read())
        return response_body.get("results", [{}])[0].get("outputText", "[No output]")

    except (BotoCoreError, ClientError, KeyError, ValueError) as e:
        logger.warning("⚠️ Bedrock call failed, falling back to local GenAI simulation.")
        logger.warning(f"Error: {e}")
        return "⚠️ Alert: Abnormal environmental conditions detected. Please investigate immediately."

# Sample usage for testing
if __name__ == "__main__":
    sample_prompt = """Sensor sensor_001 reported anomalies:
Temperature: 34.72°C
AQI: 181
Timestamp: 2025-08-04T12:00:00
Generate a human-readable alert message."""
    
    print("[Bedrock Response]:", query_bedrock(sample_prompt))
