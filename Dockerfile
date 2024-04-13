# Используем официальный образ Python как базовый
FROM python:3.10

# Установим рабочую директорию в контейнере
WORKDIR /app

# Установим переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=Epam_hacknu.settings

# Устанавливаем зависимости
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем наш проект в контейнер
COPY . /app/

# Копируем и даем права на выполнение для entrypoint.sh
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Объявляем порт, на котором будет работать приложение
EXPOSE 8000

# Устанавливаем скрипт entrypoint.sh как точку входа
ENTRYPOINT ["/app/entrypoint.sh"]