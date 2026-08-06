from random import randint

class Mage:
    def __init__(self, name, wand, house_obj, hp=100, mana=50):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.wand = wand
        self.coins = randint(500, 1500)
        self.house = house_obj

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_n):
        self._name = new_n.title()

    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self, amount):
        self._hp = amount
        if self.hp < 0:
            self._hp = 0

    @property
    def mana(self):
        return self._mana
    @mana.setter
    def mana(self, amount):
        self._mana = amount
        if self.mana < 0:
            self._mana = 0

    @property
    def coins(self):
        return self._coins
    @coins.setter
    def coins(self, amount):
        self._coins = amount

    @property
    def house(self):
        return self._house
    @house.setter
    def house(self, new_house):
        self._house = new_house