while 1:
    try:
        option = int(input("Введите номер задачи. Для выхода используйте любое число меньше 0: "))
    except ValueError:
        print("Нужна циферка")
    if option == 1:
        print("Задание 1")
    elif option == 2:
        print("Задание 2")
    elif option < 0:
        break
    else:
        print("Всего 2 задачи")   