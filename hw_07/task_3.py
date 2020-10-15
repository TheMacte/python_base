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
