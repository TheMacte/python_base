# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

debit = float(input('Введите сумму выручки '))
credit = float(input('Введите сумму издержек '))
delta = debit - credit

if delta > 0:
    print(f'Выша выручка больше издержек на {delta} $')
    profit = delta / debit
    print(f'Выша рентабельность {profit * 100} %')
    staff = int(input('Численность сотрудников: '))
    profit_on_staff = delta / staff
    print(f'На одного сотрудника в среднем приходится {profit_on_staff} $ прибыли.')
else:
    print(f'Выши издержки больше прибыли на {delta * (- 1)} $')
