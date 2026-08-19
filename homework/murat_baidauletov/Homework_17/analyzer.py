import os
import argparse
from datetime import datetime


def parse_args():
    parser = argparse.ArgumentParser(description='Find logs by text')
    parser.add_argument('path', help='File name or directory')
    parser.add_argument('-t', '--text', required=True, help='Word to find')
    return parser.parse_args()


args = parse_args()

file_path = args.path
word_to_find = args.text

if os.path.isdir(file_path):
    files = list(filter(lambda name: name.endswith('.log'), os.listdir(file_path)))
    files.sort()
    files = list(map(lambda name: os.path.join(file_path, name), files))
else:
    files = [file_path]


def get_date_from_line(line_content):
    if len(line_content) >= 23:
        date_candidate = line_content[:23]
        try:
            datetime.fromisoformat(date_candidate)
            return date_candidate
        except ValueError:
            pass
    return None


for file in files:
    data = {}

    with open(file, encoding='utf-8') as log_file:
        for i, line in enumerate(log_file, start=1):
            line_date = get_date_from_line(line)

            if line_date:
                date_key = line_date
                data[date_key] = {
                    'text': line,
                    'line_number': i
                }
            else:
                data[date_key]['text'] += line

    for key, entry in data.items():
        if word_to_find in entry['text']:

            words = entry['text'].split()

            for index, word in enumerate(words):
                if word_to_find in word:
                    start = max(0, index - 5)
                    end = index + 6

                    error_piece = ' '.join(words[start:end])

                    print(f'Файл: {os.path.basename(file)}')
                    print(f'Строка: {entry["line_number"]}')
                    print(f'Время ошибки: {key}')
                    print(f'Текст ошибки: {error_piece}')
