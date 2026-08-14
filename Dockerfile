FROM ghcr.io/devnen/chatterbox-tts-server:latest

# Встановлюємо змінні для сервера
ENV PORT=8000
ENV HOST=0.0.0.0

# Відкриваємо порт
EXPOSE 8000

# Запускаємо сервер (у цьому образі вже є все готове)
CMD ["python", "server.py"]
