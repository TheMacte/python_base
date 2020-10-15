from abc import ABC, abstractmethod

all_cloth = 0  # sum of cloth


class Clothes(ABC):
    def __init__(self, input_param, name=None):
        global all_cloth
        self._input_param = input_param
        self.name = name
        all_cloth += self.cloth

    @abstractmethod
    def cloth(self):
        pass


class Topcoat(Clothes):
    @property
    def cloth(self):
        return round(self._input_param / 6.5 + 0.5, 2)


class Suit(Clothes):
    @property
    def cloth(self):
        return 2 * self._input_param + 0.3


my_topcoat = Topcoat(5)
print(my_topcoat.cloth)

my_topcoat2 = Topcoat(13)
print(my_topcoat2.cloth)

my_suit = Suit(3)
print(my_suit.cloth)

print(all_cloth)
