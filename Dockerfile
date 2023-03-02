# Берем нужный базовый образ
FROM python:3.11-alpine
# Копируем все файлы из текущей директории в /app контейнера
COPY ./ /app
# Устанавливаем все зависимости
RUN apk update && pip install -r /app/requirements.txt --no-cache-dir
# Устанавливаем аргумент при сборке
ARG token
ENV token=${token}
# Запуск нашего приложения при старте контейнера
CMD python /app/main.py ${token}
