class Enemies:
    enemies_list = ["Dragon", "Acromantula", "Oni", "Wolf", "Goblin"]
    def __init__(self, hp, damage, exp, coins):
        self.hp = hp
        self.damage = damage
        self.exp = exp
        self.coins = coins

    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self, amount):
        self._hp = amount

    @property
    def damage(self):
        return self._damage
    @damage.setter
    def damage(self, amount):
        self._damage = amount

    @property
    def exp(self):
        return self._exp
    @exp.setter
    def exp(self, amount):
        self._exp = amount

    @property
    def coins(self):
        return self._coins
    @coins.setter
    def coins(self, amount):
        self._coins = amount