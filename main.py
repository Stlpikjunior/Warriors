class Komplex:  #
    def __init__(self, real,
                 img):  # toto je konstruktor a vola sa presane vtedy ked vytvaras instanciu objektu/ objekt# #tieto metody budeme pouzivat na pretazenie operatorov, budem donho posielat dve zlozky - real, img
        # syntakticky shit pretoze v definicii su tri premenne a nikdy tam nebudem posielat self, takze vzdy budem posielat len dve-
        self.real = real
        self.img = img

    def __str__(self):  # terminus technicus - override methods, pozriem ktora robi co
        if self.img >= 0:
            return str(self.real) + '+' + str(self.img) + 'i'
        else:
            return str(self.real) + str(self.img) + 'i'

    def abs(self):
        return (self.real ** 2 + self.img ** 2) ** 0.5

    def __add__(self, other):
        return Komplex(self.real + other.real, self.img + other.img)

    def __mul__(self, other):
        return Komplex(self.real * other.real - self.img * other.img, self.real * other.img + self.img * other.real)


k1 = Komplex(6, 5)
k2 = Komplex(3, -2)
k3 = k1 + k2
k4 = k1 * k2
# print(k1, k2, k3, k4)  # napise mi ze to je len nejaky objekt absolutne hujujuju bujujuju


class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack
        self.state = True


class Knight:  # vdaka vlastnosti OOP toto cele nemusime pisat, knight bude mat vsetko to co mal warrior
    def __init__(self, health=50, attack=7):
        self.health = health
        self.attack = attack
        self.state = True

class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit_class, count):
        for i in range(count):
            unit = unit_class()
            self.units.append(unit)


def fight(w1, w2):
    while w1.health > 0 and w2.health > 0:
        w2.health -= w1.attack
        # print(w2.health)
        if w2.health > 0:
            w1.health -= w2.attack
            # print(w1.health)
    if w1.health > 0:
        return True  # vyhral bojovnik 1
    else:
        return False


class Battle:
    def __init__(self):
        pass

    def fight_arm(self, army_1, army_2):
        while len(army_1.units) > 0 and len(army_2.units) > 0:
            if fight(army_1.units[0], army_2.units[0]):
                army_2.units.pop(0)
            else:
                army_1.units.pop(0)
        if len(army_1.units) > 0:
            # print('army 1 won')
            return 'army 1 won'
        else:
            # print('army 2 won')
            return 'army 2 won'


#
# #test
# chuck = Warrior()
# bruce = Warrior()
# carl = Knight()
# print(carl.attack)

# fight(bruce,carl)
# fight(carl,bruce)


my_army = Army()
my_army.add_units(Knight, 4)

enemy_army = Army()
enemy_army.add_units(Warrior, 5)

army_3 = Army()
army_3.add_units(Warrior, 7)
army_3.add_units(Knight, 2)

army_4 = Army()
army_4.add_units(Warrior, 12)

battle = Battle()
print(battle.fight_arm(my_army, enemy_army))
print(battle.fight_arm(army_3, army_4))
