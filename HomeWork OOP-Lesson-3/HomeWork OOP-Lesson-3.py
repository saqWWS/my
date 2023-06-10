from pygame import mixer

mixer.init()
mixer.music.set_volume(1)


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
        return mixer.music.load("Donkey_.mp3")

    def _colore(self):
        return self.color


class Monkey(Animal):
    def __init__(self, name, age, foot_count, weight, smell, height):
        super(Monkey, self).__init__(name, age, foot_count, weight, height)
        self.smell = smell

    def sound_animals(self):
        return mixer.music.load("Monkey_.mp3")

    def _smell(self):
        return self.smell


donkey = Donkey("Իշուկ", 8, 4, "189 Կգ․", "Gray", "132 սմ․")
monkey = Monkey("Ռաֆիկի", 7, 2, "73 Կգ․", "Ոչ այդքան հաճելի", "173 սմ․")
print(donkey._name())
print(monkey._smell())
print(donkey._colore())
print(donkey.height)

while True:
    print("------------------------------------------------------------------------------------")
    print("Press 'D' to hear the Donkey.")
    print("Press 'M' to hear the Donkey.")
    print("Press 'E' to exit the program.\n")

    input_sound = input(" Press any of the options:\t").lower()

    if input_sound == 'd':
        print(donkey.sound_animals(), mixer.music.play())
        print("Վայելե՛ք Իշուկի ձայնը։")
    elif input_sound == 'm':
        print(monkey.sound_animals(), mixer.music.play())
        print("Վայելե՛ք Ռաֆիկի ձայնը։")
    elif input_sound == 'e':
        mixer.music.stop()
        print("Pause! you're out of the loop, press again to enjoy again.")
        break


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
