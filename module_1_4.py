# Запрашиваем у пользователя ввод строки
my_string = input("Введите произвольный текст: ")

# Выводим количество символов в строке
print("Количество символов в введённом тексте:", len(my_string))

# Запрашиваем у пользователя ввод строки
my_string = input("Введите произвольный текст: ")

# Выводим строку в верхнем регистре
print("Строка в верхнем регистре:", my_string.upper())

# Выводим строку в нижнем регистре
print("Строка в нижнем регистре:", my_string.lower())


my_string_no_spaces = my_string.replace(" ", "")
print("Строка без пробелов:", my_string_no_spaces)
if my_string:
    print("Первый символ строки:", my_string[0])
else:
    print("Строка пуста, нет первого символа.")
if my_string:
    print("Последний символ строки:", my_string[-1])
else:
    print("Строка пуста, нет последнего символа.")