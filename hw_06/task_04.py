class Car:
    speed_waring = 'Вы превысили скорость'

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Поехали ' + self.name)

    def stop(self):
        print('Остановились ' + self.name)

    def turn(self, direction):
        print('Поворот ' + self.name + ' на ' + direction)

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    speed_limit = 60

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > self.speed_limit:
            print(super().speed_waring)
        else:
            super().show_speed()


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    speed_limit = 40

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > self.speed_limit:
            print(super().speed_waring)
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


town_car = TownCar(50, 'brown', 'kia')
town_car.show_speed()
town_car.speed = 80
town_car.show_speed()
town_car.go()
town_car.stop()
town_car.turn('left')

police_car = PoliceCar(300, 'white', 'Crown Victoria')
print(police_car.is_police)
