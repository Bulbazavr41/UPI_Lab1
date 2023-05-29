# Функция перевда строчного символа в заглавный
def charToUpper(char):
    if len(char) > 1:
        print("Ошибка, введите ровно 1 символ")
    elif char >= 'a' and char <= 'z':
        return chr(ord(char) - 32)
    else:
        return char

# Функция для консольного ввода списка студентов
def input_students():
    students = []
    n = int(input("Введите количество студентов: "))
    for i in range(n):
        print(f"Студент {i+1}:")
        name = input("Фамилия и имя: ")
        birth_year = int(input("Год рождения: "))
        birth_month = int(input("Месяц рождения: "))
        birth_day = int(input("День рождения: "))
        record_book = []
        m = int(input("Количество предметов: "))
        for j in range(m):
            print(f"Предмет {j+1}:")
            subject = input("Название предмета: ")
            exam_date = input("Дата экзамена: ")
            teacher = input("Преподаватель: ")
            mark = int(input("Оценка: "))
            record_book.append((subject, exam_date, teacher, mark))
        student = (name, (birth_year, birth_month, birth_day), record_book)
        students.append(student)
    return students

# Функция для вывода ФИО, предмета и оценки студента с самой лучшей успеваемостью
def print_best_student(students):
    best_student = None
    best_mark = 0
    for student in students:
        for subject, _, _, mark in student[2]:
            if mark > best_mark:
                best_student = student[0]
                best_subject = subject
                best_mark = mark
    if best_student is None:
        print("Нет студентов")
    else:
        print(f"Лучший студент: {best_student}, предмет: {best_subject}, оценка: {best_mark}")  
    
while 1:
    try:
        option = int(input("Введите номер задачи. Для выхода используйте любое число меньше 0: "))
    except ValueError:
        print("Нужна циферка")
    if option == 1:
        print("Задание 1")
        char = charToUpper(input("Введите символ: "))
        print(char)
        elif option == 2:
        print("Задание 2")
        students = input_students()
        print_best_student(students)  
    elif option < 0:
        break
    else:
        print("Всего 2 задачи")   
