# Берем нужный базовый образ
FROM python:3.11-alpine
# Копируем все файлы из текущей директории в /app контейнера
COPY ./ /app
# Устанавливаем все зависимости
RUN apk update && pip install -r /app/requirements.txt --no-cache-dir
# Запуск нашего приложения при старте контейнера
ENTRYPOINT ["python", "/app/main.py"]