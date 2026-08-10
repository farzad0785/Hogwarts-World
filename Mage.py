#from random import randint

class Mage:
    def __init__(self, name, house_obj = None, hp=100, mana=50, crit_chance=0.1, level=1, xp=0):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.coins = 10000
        self._crit_chance = crit_chance
        self.house = house_obj
        self.level = level
        self.xp = xp

        self._status = {}

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_n):
        self._name = new_n.title()
        self.add_status("Name", self.name)

    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self, amount):
        self._hp = amount
        if self.hp < 0:
            self._hp = 0
        self.add_status("HP", self.hp)

    @property
    def mana(self):
        return self._mana
    @mana.setter
    def mana(self, amount):
        self._mana = amount
        if self.mana < 0:
            self._mana = 0
        self.add_status("Mana", self.mana)

    @property
    def coins(self):
        return self._coins
    @coins.setter
    def coins(self, amount):
        self._coins = amount
        if self.coins < 0:
            self.coins = 0
        self.add_status("Coins", self.coins)

    @property
    def house(self):
        return self._house
    @house.setter
    def house(self, new_house):
        self._house = new_house
        self.add_status("House", self._house.name)

    @property
    def level(self):
        return self._level
    @level.setter
    def level(self, new_l):
        self._level = new_l
        self.add_status("Level", self.level)

    @property
    def xp(self):
        return self._xp
    @xp.setter
    def xp(self, new_xp):
        self._xp = new_xp
        self.add_status("XP", self.xp)

    @property
    def status(self):
        return self._status

    def add_status(self, att_name, att_amount):
        self._status[att_name] = att_amount