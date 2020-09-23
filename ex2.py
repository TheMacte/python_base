# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_seconds = int(input('Введите произвольное количество секунд '))
minuts = user_seconds // 60
seconds = user_seconds % 60
hours = minuts // 60
minuts = minuts % 60

#
# if seconds < 10:
#     seconds = '0' + str(seconds)
# if minuts < 10:
#     minuts = '0' + str(minuts)
# if hours < 10:
#     hours = '0' + str(hours)

# print(hours, ':', minuts, ':', seconds)

print('{:02d}:{:02d}:{:02d}'.format(hours, minuts, seconds))
