class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self, depth):
        return self._length * self._width * 25 * depth


my_road = Road(20, 5000)
print(my_road.calc(5))
