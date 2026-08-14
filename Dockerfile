FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir chatterbox-tts fastapi uvicorn soundfile numpy

COPY server.py /app/server.py

EXPOSE 8000

CMD ["python", "server.py"]

