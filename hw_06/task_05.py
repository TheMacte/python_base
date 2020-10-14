class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ШАРИКОВОЙ РУЧКИ')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки КАРАНДАША')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки РУЧКОЙ')


stationery = Stationery('stationery')
pen = Pen('pen')
pencil = Pencil('pencil')
handle = Handle('handle')

stationery.draw()
pen.draw()
pencil.draw()
handle.draw()
