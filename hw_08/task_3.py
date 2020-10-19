import re


class OwnError(Exception):
    def __init__(self,num):
        self.num = num
        self.txt = f'Мне нужны цифры... А это... ' \
                   f'В общем я не знаю, что это, но это не то, что я ожидал, что это вообще такое "{num}"'


class TheGame:
    def __init__(self):
        self.my_list = []

    def start(self):
        while True:
            next_num = input('Введите число: ')
            if next_num != 'stop':
                if self._check(next_num) is not None:
                    self.my_list.append(int(next_num))
                else:
                    continue
            else:
                print(self.my_list)
                break

    @staticmethod
    def _check(num):
        try:
            if re.fullmatch(r'\d+', num):
                return num
            else:
                raise OwnError(num)
        except OwnError as error:
            print(error.txt)
            return None


my_game = TheGame()
my_game.start()
