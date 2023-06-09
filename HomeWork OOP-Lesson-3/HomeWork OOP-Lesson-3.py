class Animal:
    def __init__(self, name, age, foot_count, weight, height):
        self.name = name
        self.age = age
        self.foot_count = foot_count
        self.weight = weight
        self.height = height

    def _name(self):
        return self.name

    def __str__(self):
        return "Donkey and Monkey"


class Donkey(Animal):
    def __init__(self, name, age, foot_count, weight, color, height):
        super(Donkey, self).__init__(name, age, foot_count, weight, height)
        self.color = color

    def sound_animals(self):
        return "https://www.youtube.com/shorts/9g4ZJrHsSTA"

    def _colore(self):
        return self.color


class Monkey(Animal):
    def __init__(self, name, age, foot_count, weight, smell, height):
        super(Monkey, self).__init__(name, age, foot_count, weight, height)
        self.smell = smell

    def sound_animals(self):
        return "https://www.youtube.com/watch?v=_bmcwEK4a1A"

    def _smell(self):
        return self.smell


donkey = Donkey("Իշուկ", 8, 4, "189 Կգ․", "Gray", "132 սմ․")
monkey = Monkey("Ռաֆիկի", 7, 2, "73 Կգ․", "Ոչ այդքան հաճելի", "173 սմ․")
print(donkey._name())
print(donkey.sound_animals())
print(monkey.sound_animals())
print(monkey._smell())
print(donkey._colore())
print(donkey.height)
print(monkey.smell)


class Car():
    def __init__(self, color, horse_power, manufactory):
        self.color = color
        self.horse_power = horse_power
        self.manufactory = manufactory

    def max_speed(self):
        return None


class Subaru(Car):
    def __init__(self, color, horse_power, manufactory):
        super(Subaru, self).__init__(color, horse_power, manufactory)

    def max_speed(self):
        return "\n 280.km/h \n 174.mp/h\n"

    def on_championship(self):
        return "FIA World Rally Championship"

    def most_popular_model(self):
        return "Subaru Impreza WRX STI"

    def where_can_you_drive(self):
        return "On all surfaces.\nAWD is an advantage"


class Alfa_Romeo(Car):
    def __init__(self, color, horse_power, manufactory):
        super(Alfa_Romeo, self).__init__(color, horse_power, manufactory)

    def max_speed(self):
        return "\n307.km/h\n191.mp/h\n"

    def on_championship(self):
        return "The FIA Formula One World Championship"

    def most_popular_model(self):
        return "Alfa Romeo Giulia Quadrifoglio"

    def alfa_romeo_avio(self):
        return ["The Alfa Romeo Avio was an Italian aviation company producing aircraft engines active since 1941"]


subaru = Subaru("Dark Blue", "310 HP.", "Japan")
alfa_romeo = Alfa_Romeo("Red", "505 HP.", "Italy")
print(subaru.max_speed())
print(alfa_romeo.max_speed())
print(subaru.color)
print(alfa_romeo.alfa_romeo_avio())
print(subaru.where_can_you_drive())
for i in range(len(alfa_romeo.alfa_romeo_avio())):
    print(len(alfa_romeo.alfa_romeo_avio()[i]))
