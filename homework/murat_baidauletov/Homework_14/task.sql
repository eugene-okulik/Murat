--Все оценки студента
SELECT m.value
FROM marks m
WHERE m.student_id = 23019;

--Все книги, которые находятся у студента
SELECT b.id, b.title
FROM books b
WHERE b.taken_by_student_id = 23019;

--Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
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
WHERE s.id = 23019;
