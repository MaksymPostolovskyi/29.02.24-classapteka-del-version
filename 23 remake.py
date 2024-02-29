class Аптека():
    population = 0
    def __init__(self, name, location):
        self.location = location
        self.name = name
        Аптека.population = 0

    def __del__(self):
        print(f"{self.name} destroyed")
        Аптека.population -= 1
        if Аптека.population == 0:
            print(f"{self.name} was last")
        else:
            print(f"Still {Аптека.population}".format(Аптека.population))

    def add_apteka(self, name):
        Аптека.population += 1
        print(f"Initialization {name}")

    def how_many(self):
        print(f"City have {Аптека.population}".format(Аптека.population))

Аптека1 = Аптека("Подорожник", "Івано-Франківськ")
Аптека.how_many
Аптека2 = Аптека("Сімейна", "Тисмениця")
Аптека.how_many

Аптека1.add_apteka("Подорожник")
Аптека2.add_apteka("Сімейна")


del Аптека1
del Аптека2

print(Аптека.__doc__)