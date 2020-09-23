# 3. Узнайте у пользователя число n. 
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_num = int(input('Введите произвольное число '))
double_num = int(str(user_num) + str(user_num))
triple_num = int(str(user_num) + str(user_num) + str(user_num))
print(user_num + double_num + triple_num)
