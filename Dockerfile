# Simple Dockerfile for A2A Spec Agent
FROM python:3.11-slim

WORKDIR /app

COPY a2a_spec_agent.py ./

CMD ["python", "a2a_spec_agent.py"]
