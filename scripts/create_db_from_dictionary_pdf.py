import pdfplumber
import json
import re


def remove_text_in_brackets(text):
    return re.sub(r"\s*\([^)]*\)", "", text)


def is_russian(word):
    return re.match(r'^[а-яА-ЯёЁ]+$', word)


pdf_path = '/home/yersultan/Downloads/Russko_-_kazakhskiy_tematicheskiy_slovar_9000_slov.pdf'
data = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        for line in text.split('\n'):
            cleaned_line = remove_text_in_brackets(line)
            parts = cleaned_line.split()

            russian_words = []
            kazakh_words = []
            for part in parts:
                if is_russian(part) and kazakh_words:
                    data.append({
                        'russian': ' '.join(russian_words),
                        'kazakh': ' '.join(kazakh_words)
                    })
                    russian_words = [part]
                    kazakh_words = []
                elif is_russian(part):
                    russian_words.append(part)
                else:
                    kazakh_words.append(part)

            if russian_words and kazakh_words:
                data.append({
                    'russian': ' '.join(russian_words),
                    'kazakh': ' '.join(kazakh_words)
                })

json_data = json.dumps(data, ensure_ascii=False, indent=2)
output_file_path = 'words.json'

with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(json_data)



