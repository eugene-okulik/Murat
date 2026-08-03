import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

query = 'insert into students (name,second_name,group_id) values (%s, %s, %s)'
values = ('testpyDB', 'testpyDB', None)
cursor.execute(query, values)

student_id = cursor.lastrowid

query = 'INSERT INTO books (title, taken_by_student_id) values (%s, %s)'
values = ('Алгебра', student_id)
cursor.execute(query, values)

query = 'INSERT INTO `groups` (title,start_date,end_date) values (%s, %s, %s)'
values = ('ВТК-16-1', '01.01.2016', '01.01.2020')
cursor.execute(query, values)
group_id = cursor.lastrowid

update_query = 'UPDATE students SET group_id = %s WHERE id = %s'
values = (group_id, student_id)
cursor.execute(update_query, values)

query = 'INSERT INTO subjects (title) VALUES (%s)'
values = [('1',), ('12',)]

subjects_id = []

for value in values:
    cursor.execute(query, value)
    subjects_id.append(cursor.lastrowid)

lesson_query = """INSERT INTO lessons (title, subject_id)
                  VALUES (%s, %s)"""

lessons = [("Алгебра", subjects_id[0]),
           ("Теңсіздіктер", subjects_id[0]),
           ("Треугольники", subjects_id[1]),
           ("Площадь круга", subjects_id[1]),
           ]
lessons_id = []
for lesson in lessons:
    cursor.execute(lesson_query, lesson)
    lessons_id.append(cursor.lastrowid)
cursor.executemany(query, values)

marks_query = """
              INSERT INTO marks (value, student_id, lesson_id)
              VALUES (%s, %s, %s) \
              """

marks = [
    (5, student_id, lessons_id[0]),
    (4, student_id, lessons_id[1]),
    (5, student_id, lessons_id[2]),
    (4, student_id, lessons_id[3]),
]
cursor.executemany(marks_query, marks)
db.commit()

cursor.execute('''SELECT m.value
                  FROM marks m
                  WHERE m.student_id = %s;
               ''', (student_id,))
print(cursor.fetchall())

cursor.execute('''SELECT b.id, b.title
                  FROM books b
                  WHERE b.taken_by_student_id = %s;
               ''', (student_id,))
print(cursor.fetchall())

cursor.execute('''SELECT s.id,
                         s.name,
                         s.second_name,
                         s.group_id,
                         g.title   AS group_title,
                         b.title   AS book_title,
                         m.value   AS mark,
                         l.title   AS lesson_title,
                         sub.title AS subject_title
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
                  WHERE s.id = %s;
               ''', (student_id,))
print(cursor.fetchall())
db.close()
