FROM python:3.10-slim

WORKDIR /app

# Встановлюємо системні залежності
RUN apt-get update && apt-get install -y \
    git \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Встановлюємо Chatterbox TTS прямо з PyPI (офіційний пакет)
RUN pip install --no-cache-dir chatterbox-tts fastapi uvicorn

# Копіюємо наш власний сервер (не використовуємо чужий engine.py)
COPY server.py /app/server.py

EXPOSE 8000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
