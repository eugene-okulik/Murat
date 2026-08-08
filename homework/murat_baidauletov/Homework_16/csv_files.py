import mysql.connector as mysql
import dotenv
import csv
import os

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
jenya_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(jenya_file_path, newline='') as f:
    reader = csv.DictReader(f)
    data = list(reader)

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor()
for row in data:
    print(row['name'])

    cursor.execute('''SELECT s.id
                      FROM students s
                               JOIN `groups` g
                                    ON g.id = s.group_id
                               JOIN books b
                                    ON b.taken_by_student_id = s.id
                               JOIN marks m
                                    ON m.student_id = s.id
                               JOIN lessons l
                                    ON l.id = m.lesson_id
                               JOIN subjects sub
                                    ON sub.id = l.subject_id
                      WHERE s.name = %s
                        and s.second_name = %s
                        and g.title = %s
                        and b.title = %s
                        and sub.title = %s
                        and l.title = %s
                        and m.value = %s''',
                   (row['name'], row['second_name'], row['group_title'], row['book_title'],
                    row['subject_title'], row['lesson_title'], row['mark_value'],))
    result = cursor.fetchone()

    if result is None:
        print(f'В базе нет данных: {row}')

print(db.is_connected())
db.close()
