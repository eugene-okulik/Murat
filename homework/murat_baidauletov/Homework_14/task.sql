-- Создайте студента (student)
INSERT INTO students (name, second_name, group_id)
VALUES ('Murat', 'Baidauletov', NULL)

-- Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
INSERT INTO books (title, taken_by_student_id)
VALUES ('Алгебра',23028),('Геометрия', 23028)

-- Создайте группу (group) и определите своего студента туда
INSERT INTO `groups` (title,start_date,end_date)
VALUES ('ВТК-16-1', '01.01.2016','01.01.2020')

UPDATE students SET group_id = 22838
WHERE id = 23028

-- Создайте несколько учебных предметов (subjects)
INSERT INTO subjects (title)
VALUES ('Математика'), ('Геометрия');


-- Создайте по два занятия для каждого предмета (lessons)
INSERT INTO lessons  (title, subject_id)
VALUES ('Теңсіздіктер', 23044),('Теңдеу', 23044),
('sin', 23045),('cos', 23045)


-- Поставьте своему студенту оценки (marks) для всех созданных вами занятий

INSERT INTO marks (value, lesson_id, student_id)
VALUES
    (5, 76403, 23028),
    (4, 76402, 23028),
    (5, 76401, 23028),
    (4, 76400, 23028)

-- Все оценки студента
SELECT m.value
FROM marks m
WHERE m.student_id = 23028;

-- Все книги, которые находятся у студента
SELECT b.id, b.title
FROM books b
WHERE b.taken_by_student_id = 23028;

-- Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
SELECT
    s.*, g.title, b.title, m.value, l.title, sub.title
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
WHERE s.id = 23028;
