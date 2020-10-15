class Matrix:
    def __init__(self, list_of_lists):
        self.i = -1
        self.list_of_lists = list_of_lists
        self.matrix_width = len(self.list_of_lists[0])
        self.matrix_length = len(self.list_of_lists)

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i < self.matrix_length:
            return self.list_of_lists[self.i]
        else:
            self.i = 0
            raise StopIteration

    def __str__(self):
        self.base_str = ''
        for i in self.list_of_lists:
            self.base_str += ' '.join(map(str, i)) + '\n'
        return self.base_str

    def __add__(self, other):
        if isinstance(other, Matrix):
            if other.matrix_width == self.matrix_width and other.matrix_length == self.matrix_length:
                new_matrix = []
                num_element = 0
                for line_matrix_1, line_matrix_2 in zip(self.list_of_lists, other):
                    new_matrix.append([])
                    for el_m_1, el_m_2 in zip(line_matrix_1, line_matrix_2):
                        new_matrix[num_element].append(el_m_1 + el_m_2)
                    num_element += 1
                return new_matrix
            else:
                print('Невозможно сложить разноразмерные матрицы')
                return False
        print('Складывать можно только матрицы (объекты класса Matrix)')
        return False


test_list_1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
test_list_2 = [[30, 31, 32], [20, 21, 22], [10, 11, 12]]
bad_list_1 = [[1, 1, 1], [2, 2, 2]]
bad_list_2 = [[3, 3], [2, 2], [1, 1]]

test_matrix = Matrix(test_list_1)
test_matrix2 = Matrix(test_list_2)

print(test_matrix)

print(test_matrix + test_matrix2)
