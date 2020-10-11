import time


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self, infinite=True):
        while infinite:
            my_timer = [7, 2, 5]
            for i in range(3):
                print(self.__color[i])
                time.sleep(my_timer[i])


my_tl = TrafficLight()
my_tl.running()
