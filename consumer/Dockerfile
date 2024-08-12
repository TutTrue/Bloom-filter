FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir redis

CMD ["python3", "consumer.py"]
