SELECT students.student_name, grades.grade, grades.date_received
FROM students
JOIN grades ON students.student_id = grades.student_id
JOIN subjects ON subjects.subject_id = grades.subject_id
JOIN groups ON groups.group_id = students.group_id
WHERE groups.group_name = ? AND subjects.subject_name = ?
      AND grades.date_received = (
          SELECT MAX(date_received)
          FROM grades
          WHERE subject_id = subjects.subject_id
            AND students.student_id = grades.student_id
      )