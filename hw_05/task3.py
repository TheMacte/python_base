# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.

losers = []
losers_salary = 20000
salaries = []

with open('super_test_file.txt') as info_list:
    staffing_table = info_list.readlines()
for staff in staffing_table:
    salaries.append(int(staff.strip().split()[1]))
    if int(staff.strip().split()[1]) < losers_salary:
        losers.append(staff.strip().split()[0])

print(f'Сотрудники с зарплатой менее {losers_salary}: {", ".join(losers)}.')
print(f'Средняя зарплата сотрудников: {sum(salaries)/len(salaries):.2f}')
