from pathlib import Path
import re
from datetime import datetime, timedelta


def read_file():
    file_path = Path(__file__).resolve().parents[2] / "eugene_okulik" / "hw_13" / "data.txt"
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            yield line


for line in read_file():
    numbers = re.findall(r'\d+', line)
    if numbers[0] == '1':
        date_text = re.search(
            r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}",
            line
        ).group()
        date = datetime.strptime(date_text, "%Y-%m-%d %H:%M:%S.%f")
        new_date = date + timedelta(days=7)
        print(new_date)

    elif numbers[0] == '2':
        date_text = re.search(
            r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}",
            line
        ).group()
        date = datetime.strptime(date_text, "%Y-%m-%d %H:%M:%S.%f")
        print(date.weekday())

    elif numbers[0] == '3':
        date_text = re.search(
            r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}",
            line
        ).group()
        date = datetime.strptime(date_text, "%Y-%m-%d %H:%M:%S.%f")
        today = datetime.now()
        days_ago = today - date
        print(days_ago.days)
