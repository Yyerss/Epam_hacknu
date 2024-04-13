# Используем официальный образ Python как базовый
FROM python:3.10

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /code

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY . .