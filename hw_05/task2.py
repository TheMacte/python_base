# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
with open('user_said') as file:
    content = file.read()
print('Всего строк: ', len(content.split("\n")))
for i in range(1, len(content.split("\n")) + 1):
    print('Количество слов в строке №', i, ': ', len(content.split("\n")[i - 1].split()))
