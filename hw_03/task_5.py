# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь
# введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.
big_num = 0

while True:
    user_string = input('Введите числа через пробел или q для завершения: ')
    if user_string.find('q') != -1:
        user_string = map(int, user_string[:user_string.index('q')].split())
        big_num += sum(user_string)
        print(big_num)
        break
    else:
        user_string = map(int, user_string.split())
        big_num += sum(user_string)
        print(big_num)
