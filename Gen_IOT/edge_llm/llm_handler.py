import os
import logging

# Optional: OpenAI API for local LLM if applicable
try:
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("EdgeLLM")

def generate_response(prompt: str) -> str:
    try:
        if OPENAI_AVAILABLE:
            response = openai.Completion.create(
                engine="text-davinci-003",  # Replace with your preferred local model
                prompt=prompt,
                max_tokens=100
            )
            return response.choices[0].text.strip()
        else:
            raise Exception("OpenAI not available")
    except Exception as e:
        logger.warning(f"⚠️ Local LLM call failed: {e}")
        return simulate_llm_response(prompt)

def simulate_llm_response(prompt: str) -> str:
    # Simple mock logic (can improve with keyword-based patterns)
    if "AQI" in prompt or "temperature" in prompt:
        return "⚠️ Alert: Environmental conditions are beyond safe limits."
    return "✅ System normal. No anomalies detected."
