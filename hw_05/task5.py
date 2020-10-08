# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('rand_numbers', 'w+') as numbers_file:
    numbers_file.write('50 32 17 92 22 14 7 13')
    numbers_file.seek(0)
    content = numbers_file.read()
    print(sum(map(int, content.split())))


