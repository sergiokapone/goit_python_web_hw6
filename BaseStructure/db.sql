-- Создание таблицы студентов
CREATE TABLE students (
  student_id INTEGER PRIMARY KEY,
  student_name TEXT,
  group_id INTEGER,
  FOREIGN KEY (group_id) REFERENCES groups(group_id)
);

-- Создание таблицы групп
CREATE TABLE groups (
  group_id INTEGER PRIMARY KEY,
  group_name TEXT
);

-- Создание таблицы викладачей
CREATE TABLE teachers (
  teacher_id INTEGER PRIMARY KEY,
  teacher_name TEXT
);

-- Создание таблицы предметов
CREATE TABLE subjects (
  subject_id INTEGER PRIMARY KEY,
  subject_name TEXT,
  teacher_id INTEGER,
  FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

-- Создание таблицы оценок
CREATE TABLE grades (
  grade_id INTEGER PRIMARY KEY,
  student_id INTEGER,
  subject_id INTEGER,
  grade FLOAT,
  date_received TEXT,
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);
