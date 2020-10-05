# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_info(**kwargs):
    return kwargs["name"] + ' ' + kwargs["surname"] + ' ' + kwargs["birthday"] + ' ' \
           + kwargs["city"] + ' ' + kwargs["email"] + ' ' + kwargs["phone"]


print(user_info(name='Oleg', surname='D', birthday='01.01.2900', city='Moscow', email='super@email.my', phone='128500'))
