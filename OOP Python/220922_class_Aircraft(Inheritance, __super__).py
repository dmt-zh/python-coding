# Объявите базовый класс Aircraft (самолет), объекты которого создаются командой:
# air = Aircraft(model, mass, speed, top)
# где model - модель самолета (строка);
# mass - подъемная масса самолета (любое положительное число);
# speed - максимальная скорость (любое положительное число);
# top - максимальная высота полета (любое положительное число).

# В каждом объекте класса Aircraft должны создаваться локальные атрибуты с именами: _model, _mass, _speed, _top
# и соответствующими значениями. Если передаваемые аргументы не соответствуют указанным критериям
# (строка, любое положительное число), то генерируется исключение командой:
# raise TypeError('неверный тип аргумента')

# Далее, в программе объявите следующие дочерние классы:
# PassengerAircraft - пассажирский самолет;
# WarPlane - военный самолет.

# Объекты этих классов создаются командами:
# pa = PassengerAircraft(model, mass, speed, top, chairs)
# chairs - число пассажирских мест (целое положительное число)

# wp = WarPlane(model, mass, speed, top, weapons)
# weapons - вооружение (словарь); ключи - название оружия, значение - количество

# В каждом объекте классов PassengerAircraft и WarPlane должны формироваться локальные атрибуты с именами
# _chairs и _weapons соответственно. Инициализация остальных атрибутов должна выполняться через инициализатор
# базового класса.

# В инициализаторах классов PassengerAircraft и WarPlane проверять корректность передаваемых аргументов
# chairs и weapons. Если тип данных не совпадает, то генерировать исключение командой:
# raise TypeError('неверный тип аргумента')

# Создайте в программе четыре объекта самолетов со следующими данными:
# PassengerAircraft: МС-21, 1250, 8000, 12000.5, 140
# PassengerAircraft: SuperJet, 1145, 8640, 11034, 80
# WarPlane: Миг-35, 7034, 25000, 2000, {"ракета": 4, "бомба": 10}
# WarPlane: Су-35, 7034, 34000, 2400, {"ракета": 4, "бомба": 7}

# Все эти объекты представить в виде списка planes.




class Aircraft:
    def __init__(self, model, mass, speed, top):
        self._model = self._valid_attr(model, str)
        self._mass = self._valid_attr(mass, (int, float), check_zero=True)
        self._speed = self._valid_attr(speed, (int, float), check_zero=True)
        self._top = self._valid_attr(top, (int, float), check_zero=True)

    def _valid_attr(self, attr, attr_type=None, check_zero=False):
        valid_type = isinstance(attr, attr_type)
        above_zero = attr > 0 if check_zero else True
        if not (valid_type and above_zero):
            raise TypeError('неверный тип аргумента')
        return attr


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs = self._valid_attr(chairs, int)


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._valid_attr(weapons, dict)

        if all(self._valid_attr(value, int, check_zero=True) for value in weapons.values()):
            self._weapons = weapons



planes = [
    PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
    PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
    WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
    WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})
]
