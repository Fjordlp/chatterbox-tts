FROM ghcr.io/devnen/chatterbox-tts-server:latest

# Встановлюємо змінну для норвезької моделі (якщо сервер підтримує)
ENV MODEL_NAME=akhbar/chatterbox-tts-norwegian

# Сервер уже слухає на порту 4123
EXPOSE 4123
