# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_seconds = int(input('Введите произвольное количество секунд '))
minuts = user_seconds // 60
seconds = user_seconds % 60
hours = minuts // 60
minuts = minuts % 60

print('{:02d}:{:02d}:{:02d}'.format(hours, minuts, seconds))
