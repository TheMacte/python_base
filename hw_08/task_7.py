import re


class ComplexNumber:
    def __init__(self, real_part, minimum_part):
        if real_part and minimum_part != 0:
            if int(minimum_part) > 0:
                self.my_str_complex = str(real_part) + '+' + str(minimum_part) + 'j'
            else:
                self.my_str_complex = str(real_part) + str(minimum_part) + 'j'
        elif real_part == 0 and minimum_part != 0:
            self.my_str_complex = str(minimum_part) + 'j'
        elif real_part != 0 and minimum_part == 0:
            self.my_str_complex = str(real_part)
        else:
            self.my_str_complex = 0

    def __add__(self, other):
        complex_list = [x for x in re.split(r'\D', str(complex(str(self.my_str_complex)) + complex(str(other)))) if
                        x != '']
        return ComplexNumber(complex_list[0], complex_list[1])

    def __mul__(self, other):
        complex_list = [x for x in re.split(r'\D', str(complex(str(self.my_str_complex)) * complex(str(other)))) if
                        x != '']
        return ComplexNumber(complex_list[0], complex_list[1])
        # return complex(str(self.my_str_complex)) * complex(str(other))

    def __str__(self):
        return f'{self.my_str_complex}'


num_1 = ComplexNumber(0, 3)
num_2 = ComplexNumber(8, -1)
num_3 = ComplexNumber(3, 0)
num_4 = ComplexNumber(3, 3)
print(num_4)
add = num_1 + num_2
print(add)
mul = num_1 * num_2
print(mul)
print(type(mul))
