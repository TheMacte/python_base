# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = ['oleg', 22, 3.14159, True, [1, 2, 3], ('o', 'l', 'e', 'g'), {1, 'o'}, None]

for item in my_list:
    print(type(item))
