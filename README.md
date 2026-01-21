GEN-IOT: Generative IoT with AWS
Objective
Simulate real-time IoT data, process it using AWS Lambda, and generate insights using a Generative AI model (via Amazon Bedrock).

Structure
device-simulator: Python code for virtual IoT devices
data-ingestion: Interfaces with AWS IoT Core
lambda-functions: AWS Lambda code to process/filter data
llm-integration: Interfaces with Amazon Bedrock for GenAI processing
logs: CloudWatch log integration and offline logging
