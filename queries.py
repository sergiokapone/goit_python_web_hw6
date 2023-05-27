import sqlite3
from prettytable import PrettyTable

# ============================= Обробник запитів ==============================
def execute_query(query_file, result_handler, params=()):
    # Встановити з'єднання з базою даних
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Прочитати запит з файлу
    with open(query_file, "r") as file:
        query = file.read()

    # Виконати запит з параметрами, якщо вони передані
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)

    # Отримати результат
    result = cursor.fetchall()

    # Обробити результат за допомогою заданої функції
    result_handler(result)

    # Закрити з'єднання з базою даних
    cursor.close()
    conn.close()


# ================================ Обробники =================================


def handle_query_1(result):

    table = PrettyTable()
    table.field_names = ["Name", "Average Grade"]
    table.align["Name"] = "l"  # Вирівнювання по лівому краю для першої колонки

    for row in result:
        student_id, student_name, average_grade = row
        table.add_row([student_name, average_grade])

    print(table)


# -----------------------------------------------------------------------------


def handle_query_3(result):
    table = PrettyTable()
    table.field_names = ["Group", "Subject", "Average Grade"]
    table.align["Group"] = "l"  # Align the first column to the left
    prev_group = None
    group_count = 0

    for row in result:
        group_name, subject, average_grade = row
        if group_name == prev_group:
            table.add_row(["", subject, average_grade])
        else:
            if group_count > 0:
                table.add_row(["", subject, average_grade], divider=True)
            table.add_row([group_name, subject, average_grade])
            prev_group = group_name
            group_count += 1

    print(table)


# -----------------------------------------------------------------------------


def handle_query_4(result):

    table = PrettyTable()
    table.field_names = ["Average Grade"]

    for row in result:
        average_grade = row[0]
        table.add_row([average_grade])

    print(table)


# -----------------------------------------------------------------------------


def handle_query_5(result):

    table = PrettyTable()
    table.field_names = ["Teacher", "Subject"]
    table.align["Teacher"] = "l"

    for row in result:
        teacher_name, subject = row
        table.add_row([teacher_name, subject])

    print(table)


# -----------------------------------------------------------------------------


def handle_query_6(result):
    table = PrettyTable()
    table.field_names = ["Group", "Student"]
    table.align["Group"] = "l"  # Align the first column to the left
    prev_group = None
    group_count = 0

    for row in result:
        group_name, _, student = row
        if group_name == prev_group:
            table.add_row(["", student])
        else:
            if group_count > 0:
                table.add_row(["", student], divider=True)
            table.add_row([group_name, student])
            prev_group = group_name
            group_count += 1

    print(table)


# -----------------------------------------------------------------------------


def handle_query_7(result):

    print(f"Група: {result[0][0]}, Предмет: {result[0][1]}")
    table = PrettyTable()
    table.field_names = ["Student", "Grades", "Date"]
    table.align["Student"] = "l"  # Align the first column to the left

    prev_student = None
    student_count = 0
    for row in result:
        _, _, student_name, grades, date_received = row
        if student_name == prev_student:
            table.add_row(["", grades, date_received])
        else:
            if student_count > 0:
                table.add_row(["", grades, date_received], divider=True)
            table.add_row([student_name, grades, date_received])
            prev_student = student_name
            student_count += 1

    print(table)


# -----------------------------------------------------------------------------


def handle_query_8(result):

    table = PrettyTable()
    table.field_names = ["Teacher", "Subject", "Average Grade"]
    table.align["Teacher"] = "l"

    for row in result:
        teacher_name, subject, average_grade = row
        table.add_row([teacher_name, subject, average_grade])

    print(table)


# -----------------------------------------------------------------------------


def handle_query_9(result):

    table = PrettyTable()
    table.field_names = ["Student", "Subjects"]
    table.align["Teacher"] = "l"

    for row in result:
        student, subjects = row
        table.add_row([student, subjects])

    print(table)


# -----------------------------------------------------------------------------


def handle_query_10(result):
    print(f"Предмет: {result[0][1]} для  {result[0][2]} читає  {result[0][0]} ")


# ============================= Головна програма ==============================

if __name__ == "__main__":
    query_handlers = {
        1: [
            "Знайти 5 студентів із найбільшим середнім балом з усіх предметів.",
            handle_query_1,
        ],
        2: [
            "Знайти студента із найвищим середнім балом з певного предмета.",
            handle_query_1,
        ],
        3: ["Знайти середній бал у групах з певного предмета.", handle_query_3],
        4: ["Знайти середній бал на потоці (по всій таблиці оцінок).", handle_query_4],
        5: ["Знайти які курси читає певний викладач.", handle_query_5],
        6: ["Знайти список студентів у певній групі.", handle_query_6],
        7: [
            "Знайти оцінки студентів у окремій групі з певного предмета.",
            handle_query_7,
        ],
        8: [
            "Знайти середній бал, який ставить певний викладач зі своїх предметів.",
            handle_query_8,
        ],
        9: [
            "Знайти список курсів, які відвідує студент.",
            handle_query_9,
        ],
        10: [
            "Список курсів, які певному студенту читає певний викладач.",
            handle_query_10,
        ],
    }
    for i in range(1, len(query_handlers) + 1):
        print("=" * 79)
        print(f"{i}.  {query_handlers[i][0]}")
        print("=" * 79)
        if i == 7:
            params = ("ФФ-11", "Фізика")
        elif i == 10:
            params = ("Аарон Цибуленко", "Микола Джеря")
        else:
            params = ()
        execute_query(f"query_{i}.sql", query_handlers[i][1], params=params)
