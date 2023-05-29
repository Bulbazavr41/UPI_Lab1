# Функция перевда строчного символа в заглавный
def charToUpper(char):
    if len(char) > 1:
        print("Ошибка, введите ровно 1 символ")
    elif char >= 'a' and char <= 'z':
        return chr(ord(char) - 32)
    else:
        return char
    
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
    elif option < 0:
        break
    else:
        print("Всего 2 задачи")   
