class OwnError(Exception):
    def __init__(self):
        self.txt = 'Делить на ноль может только Чак Норис.'


try:
    zero = int(input('Напримень нуль: '))
    if zero == 0:
        raise OwnError()
except OwnError as error:
    print(error.txt)
else:
    print(100 / zero)
