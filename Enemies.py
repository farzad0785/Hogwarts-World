class Enemies:
    enemies_list = []
    def __init__(self, name, hp, damage, xp, coins):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.xp = xp
        self.coins = coins
        Enemies.enemies_list.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_n):
        self._name = new_n

    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self, amount):
        self._hp = amount
        if self.hp < 0:
            self._hp = 0

    @property
    def damage(self):
        return self._damage
    @damage.setter
    def damage(self, amount):
        self._damage = amount

    @property
    def xp(self):
        return self._xp
    @xp.setter
    def xp(self, amount):
        self._xp = amount

    @property
    def coins(self):
        return self._coins
    @coins.setter
    def coins(self, amount):
        self._coins = amount

    def __str__(self):
        return f"{self.name:<20}{self.hp:<10}{self.damage:<15}{self.xp:<15}{self.coins}"