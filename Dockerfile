FROM python:3.11-slim

WORKDIR /app

COPY a2a_spec_agent_http.py ./

RUN pip install flask

CMD ["python", "a2a_spec_agent_http.py"]
