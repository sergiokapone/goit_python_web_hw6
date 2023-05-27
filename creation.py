import sqlite3
from faker import Faker

# Створення бази даних
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Створення таблиці студентів
cursor.execute(
    """CREATE TABLE students (
                    student_id INTEGER PRIMARY KEY,
                    student_name TEXT,
                    group_id INTEGER,
                    FOREIGN KEY (group_id) REFERENCES groups(group_id)
                )"""
)

# Створення таблиці груп
cursor.execute(
    """CREATE TABLE groups (
                    group_id INTEGER PRIMARY KEY,
                    group_name TEXT
                )"""
)

# Створення таблиці викладачів
cursor.execute(
    """CREATE TABLE teachers (
                    teacher_id INTEGER PRIMARY KEY,
                    teacher_name TEXT
                )"""
)

# Створення таблиці предметів
cursor.execute(
    """CREATE TABLE subjects (
                    subject_id INTEGER PRIMARY KEY,
                    subject_name TEXT,
                    teacher_id INTEGER,
                    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
                )"""
)

# Створення таблиці оцінок
cursor.execute(
    """CREATE TABLE grades (
                    grade_id INTEGER PRIMARY KEY,
                    student_id INTEGER,
                    subject_id INTEGER,
                    grade FLOAT,
                    date_received TEXT,
                    FOREIGN KEY (student_id) REFERENCES students(student_id),
                    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
                )"""
)

# Наповнення бази даних випадковими даними на українській мові
fake = Faker("uk_UA")

# Наповнення таблиці груп
groups = ["Група 1", "Група 2", "Група 3"]
for group_name in groups:
    cursor.execute("INSERT INTO groups (group_name) VALUES (?)", (group_name,))
    conn.commit()

# Наповнення таблиці студентів
for _ in range(30):
    student_name = fake.name()
    group_id = fake.random_int(min=1, max=3)
    cursor.execute(
        "INSERT INTO students (student_name, group_id) VALUES (?, ?)",
        (student_name, group_id),
    )
    conn.commit()

# Наповнення таблиці викладачів
for _ in range(3):
    teacher_name = fake.name()
    cursor.execute("INSERT INTO teachers (teacher_name) VALUES (?)", (teacher_name,))
    conn.commit()

# Наповнення таблиці предметів
subjects = ["Математика", "Фізика", "Хімія", "Українська мова", "Історія"]
for subject_name in subjects:
    teacher_id = fake.random_int(min=1, max=3)
    cursor.execute(
        "INSERT INTO subjects (subject_name, teacher_id) VALUES (?, ?)",
        (subject_name, teacher_id),
    )
    conn.commit()

# Наповнення таблиці оцінок
for student_id in range(1, 31):
    for subject_id in range(1, 6):
        num_grades = fake.random_int(min=1, max=20)
        for _ in range(num_grades):
            grade = fake.random_int(min=2, max=5) + fake.random_number(digits=1)
            date_received = fake.date_between(start_date="-1y", end_date="today")
            cursor.execute(
                "INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)",
                (student_id, subject_id, grade, date_received),
            )
            conn.commit()

# Закриття з'єднання з базою даних
conn.close()
