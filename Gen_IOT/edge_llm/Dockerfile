FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY edge_llm_server.py .
COPY llm_handler.py .

EXPOSE 8080

CMD ["python", "edge_llm_server.py"]
