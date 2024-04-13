import json
from googletrans import Translator
from words.models import Word

translator = Translator()

def determine_difficulty(word):
    if len(word) <= 4:
        return 'E'
    elif len(word) <= 7:
        return 'M'
    else:
        return 'H'

def fill_db_words():
    with open('/home/yersultan/PycharmProjects/Epam_hacknu/scripts/words.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for item in data:
        russian = item.get('russian', '')
        kazakh = item.get('kazakh', '')
        if russian.isdigit() or "словарь" in russian.lower():
            continue

        # Перевод с русского на английский
        translated = translator.translate(russian, src='ru', dest='en')
        english = translated.text

        difficulty = determine_difficulty(kazakh)

        # Сохранение в БД
        word = Word(kazakh=kazakh, russian=russian, english=english, difficulty=difficulty)
        word.save()

    print("Загрузка завершена.")
