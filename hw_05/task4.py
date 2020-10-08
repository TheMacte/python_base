# 4. Создать (не программно) текстовый файл со следующим содержимым: One — 1 Two — 2 Three — 3 Four — 4 Необходимо
# написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
import os

with open('task4_en.txt') as english:
    for line in english.readlines():
        wr_mode = 'a' if os.path.exists('task4_ru.txt') else 'w'
        with open('task4_ru.txt', wr_mode) as russian:
            if line.strip().split()[0] == 'One':
                russian.write(f'Один {line.strip().split()[1]} {line.strip().split()[2]}\n')
            elif line.strip().split()[0] == 'Two':
                russian.write(f'Два {line.strip().split()[1]} {line.strip().split()[2]}\n')
            elif line.strip().split()[0] == 'Three':
                russian.write(f'Три {line.strip().split()[1]} {line.strip().split()[2]}\n')
            elif line.strip().split()[0] == 'Four':
                russian.write(f'Четыре {line.strip().split()[1]} {line.strip().split()[2]}\n')
