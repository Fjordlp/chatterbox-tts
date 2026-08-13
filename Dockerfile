FROM python:3.10-slim

WORKDIR /app

# Встановлюємо необхідні пакети
RUN apt-get update && apt-get install -y \
    git \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Клонуємо Chatterbox-TTS-Server (перевірений репозиторій)
RUN git clone https://github.com/devnen/Chatterbox-TTS-Server.git /app

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Відкриваємо порт
EXPOSE 4123

# Запускаємо сервер
CMD ["python", "server.py"]
