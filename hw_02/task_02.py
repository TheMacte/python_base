# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input(). +

input_list = list(input('Введите элементы массива, разделя их пробелом ').split())
if len(input_list) > 1:  # to ignore empty and shot lists
    item_position = len(input_list) - 1 if len(input_list) % 2 == 0 else \
        len(input_list) - 2  # if list has odd element to ignore last element
    while item_position > 0:
        input_list[item_position], input_list[item_position - 1] = \
            input_list[item_position - 1], input_list[item_position]
        item_position -= 2
    else:
        print(input_list)
else:
    print('Нечего переставлять')
