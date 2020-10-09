# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.
#
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
# получила убытки, в расчет средней прибыли ее не включать. Далее реализовать список. Он должен содержать словарь с
# фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
# словарь (со значением убытков). Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}]. Итоговый список сохранить в виде json-объекта в соответствующий файл. Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

firm = {}

with open('firms.txt') as firms:
    for line in firms.readlines():
        name = line.split()[0]
        profit = int(line.split()[2]) - int(line.split()[3])
        firm[name] = profit
profit_firms = [int(firm[el]) for el in firm if firm[el] > 0]
average = {'average_profit': sum(profit_firms) / len(profit_firms)}
out_info = [firm, average]
# print(out_info)

with open("my_file.json", "w") as my_json:
    json.dump(out_info, my_json)
