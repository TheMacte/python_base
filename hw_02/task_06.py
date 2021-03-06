# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара:
# название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

database = [
            (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
            (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
            (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
           ]

while True:
    ask = input('Добавить элемент ( э ), вывести анализ ( а ) или  выход ( в ) ')
    if ask == 'э':
        database.append((len(database) + 1, {'название': input('Название '), 'цена': input('Цена '),
                                             'количество': input('Количество '), 'eд': input('Единица измерения ')}))
        print(f'Элемент {database[len(database) - 1][1]["название"]} успешно добавлен\n')
    elif ask == 'а':
        analysis = {'название': [], 'цена': [], 'количество': [], 'eд': []}
        for item in database:
            analysis['название'].append(item[1]['название'])
            analysis['цена'].append(item[1]['цена'])
            analysis['количество'].append(item[1]['количество'])
            analysis['eд'].append(item[1]['eд'])
        print(analysis)
    elif ask == 'в':
        break
