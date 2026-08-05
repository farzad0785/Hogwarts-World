from random import randint

class Mage:
    house = None
    def __init__(self, name, house_obj):
        self.name = name
        self.hp = 100
        self.mana = 50
        self.coins = randint(500, 1500)
        Mage.house = house_obj

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

    @property
    def mana(self):
        return self._mana
    @mana.setter
    def mana(self, amount):
        self._mana = amount

    @property
    def coins(self):
        return self._coins
    @coins.setter
    def coins(self, amount):
        self._coins = amount