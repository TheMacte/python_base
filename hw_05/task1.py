# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
# окончании ввода данных свидетельствует пустая строка.
import os

while True:
    new_line = input('Введите строку или "q" для завершения ')
    if new_line != 'q':
        # pass
        with open('user_said', 'a', encoding='utf-8') as file:
            file.write(f'{new_line} \n')
    else:
        break
