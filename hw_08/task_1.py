# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода.
#
# Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число».
#
# Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date):
        self.date = date  # dd-mm-gggg

    @classmethod
    def validation(cls, date):
        day, month, year = cls.date_converter(date)
        if month in (1, 3, 5, 7, 8, 10, 12) and day <= 31:
            return 'date correct'
        elif month in (4, 6, 9, 11) and day <= 30:
            return 'date correct'
        elif month == 2:
            if cls.is_leap_year(year) and day <= 29:
                return 'date correct'
            elif day <= 28:
                return 'date correct'
        return 'error date'

    @staticmethod
    def date_converter(date):
        return tuple(map(int, date.split('-')))

    @staticmethod
    def is_leap_year(year):
        if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
            return True


a = Date('31-09-2020')
print(a.validation(a.date))
