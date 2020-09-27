# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

rating = [7, 5, 3, 3, 2]

try:
    new_element = int(input('Новый элемент рейтинга '))
except ValueError:
    new_element = None

if rating.count(new_element) > 0:
    rating.reverse()
    rating.insert(rating.index(new_element), new_element)
    rating.reverse()
    # print('Аналогичные элементы есть в списке')
else:
    if new_element > rating[0]:
        rating.insert(0, new_element)
        # print('Вставить первый элемент')
    elif new_element < rating[len(rating) - 1]:
        rating.insert(len(rating), new_element)
        # print('Вставить последний элемент')
    else:
        for element in rating:
            if element < new_element:
                rating.insert(rating.index(element), new_element)
                break
        # print('Перебор и поиск меньшего')

print(rating)


