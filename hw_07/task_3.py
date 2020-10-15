# 3. Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

# В классе необходимо реализовать метод make_order(),

# принимающий экземпляр класса и количество клеток в ряду. Данный метод позволяет организовать ячейки по рядам.

# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
#
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Zooblast:
    def __init__(self, cell_count):
        self.cell_count = cell_count

    def __add__(self, other):
        return self.__class__(self.cell_count + other.cell_count)

    def __sub__(self, other):
        if self.cell_count > other.cell_count:
            self.cell_count = self.cell_count - other.cell_count
            return f'Осталось {self.cell_count} клетка(и)'
        else:
            return f'Слишком мало клеток...'

    def __mul__(self, other):
        return self.__class__(self.cell_count * other.cell_count)

    def __truediv__(self, other):
        return self.__class__(self.cell_count // other.cell_count)

    def make_order(self, row_count):
        return ('*' * row_count + '\n') * (self.cell_count // row_count) + '*' * (self.cell_count % row_count)


zooblast_1 = Zooblast(10)

zooblast_2 = Zooblast(7)

zooblast_3 = zooblast_1 + zooblast_2

zooblast_4 = zooblast_1 * zooblast_2

zooblast_5 = zooblast_1 / zooblast_2

# print(zooblast_3.cell_count)
#
# print(zooblast_1 - zooblast_2)
# print(zooblast_1.cell_count)
# print(zooblast_5.cell_count)

print(zooblast_1.make_order(5))
