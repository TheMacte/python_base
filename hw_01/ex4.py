# 4. Пользователь вводит целое положительное число. 
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_num = int(input('Введите целое положительное число '))

user_max = 0

while user_num > 0:
    if user_num % 10 > user_max:
        user_max = user_num % 10
    user_num = user_num // 10
else:
    print(user_max)