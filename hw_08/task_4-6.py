import re


class OwnError(Exception):
    def __init__(self, num):
        self.num = num
        self.txt = f'Мне нужны цифры... А это... ' \
                   f'В общем я не знаю, что это, но это не то, что я ожидал, что это вообще такое "{num}"'


class Storage:
    def __init__(self):
        self.storage_lib = {}

    def __add__(self, other):
        if type(other) is dict:
            name_element = [x for x in other][0]
            if self.storage_lib.get(name_element):
                other[name_element] += self.storage_lib.get(name_element)
            self.storage_lib.update(other)
        else:
            print('Что-то с элементом не то...')  # Осталось (отладка)
        print(self.storage_lib) # Аварийное (оставить)

    def __sub__(self, other):
        if type(other) is dict:
            name_element = [x for x in other][0]
            if self.storage_lib.get(name_element) and self.storage_lib[name_element] - other[name_element] >= 0:
                self.storage_lib[name_element] -= other[name_element]
                print(self.storage_lib)  # Осталось (отладка)
                return other
            else:
                print('Слишком большой расход, на складе стольо нет. Операция отклонена')  # Аварийное (оставить)
        else:
            print('Что-то с элементом не то...') # Аварийное (оставить)
        print(self.storage_lib)  # Осталось (отладка)


class OfficeEquipment:
    def __init__(self, count, name='def element'):
        self.name = name
        if type(count) is not int:
            self.count = int(self._check(str(count)))
        else:
            self.count = count

    @staticmethod
    def _check(num):
        """
        :param num: any string for integer check
        :return: number or None
        """
        try:
            if re.fullmatch(r'\d+', num):
                return num
            else:
                raise OwnError(num)
        except OwnError as error:
            print(error.txt)
            return 0

    @property
    def element(self):
        return {self.name: self.count}


class Printer(OfficeEquipment):
    def __init__(self, count, name='Printer'):
        super().__init__(count, name)

    def __str__(self):
        return 'Принтер цветной, не дорогой, не работает'


class Scanner(OfficeEquipment):
    def __init__(self, count, name='Scanner'):
        super().__init__(count, name)

    def __str__(self):
        return '1 000 000 страниц в минуту, а ещё он жу-утко дорогой'


class Xerox(OfficeEquipment):
    def __init__(self, count, name='Xerox'):
        super().__init__(count, name)

    def __str__(self):
        return 'МФУ, сканирует, печатает, жарит парит, рассылает факсы. Надо брать!'


main_storage = Storage()
shop_storage = Storage()  # Create storages
printers_supply = Printer(100)  # supply 100 printers
main_storage + printers_supply.element  #  posting of goods
printers_to_shop = Printer(10)  # printers for shop
shop_storage + (main_storage - printers_to_shop.element)  # supply 10 printers to shop from main storage



