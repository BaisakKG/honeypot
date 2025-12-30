# Используем Python 3.9 в качестве базового образа
FROM python:alpine3.22

RUN apk update && apk upgrade && \
    # Устанавливаем tzdata для корректного TZ
    apk add --no-cache tzdata && \
    # Добавляем стандартного пользователя, под которым будет работать скрипт
    adduser -D appuser

# Устанавливаем зависимости
RUN pip install requests

ENV TZ=Asia/Bishkek

# Копируем наш скрипт в контейнер
COPY listener.py /app/listener.py

# Переходим в рабочую директорию
WORKDIR /app

RUN chown -R appuser:appuser /app
USER appuser

# Запускаем скрипт
CMD ["python", "listener.py"]
