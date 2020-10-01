# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

def degree(*args):
    if args[1] != 0:
        return args[0] / args[1]
    else:
        return 'На ноль делить нельзя'

try:
    first_num = float(input('Введите делимое '))
    second_num = float(input('Введите делитель '))
except ValueError:
    first_num = 0
    second_num = 1

print(degree(first_num, second_num))
