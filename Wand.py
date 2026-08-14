class Wand:
    wands = {}
    def __init__(self, name, damage, mana_fill, heal, poison, crit_chance, price):
        self.name = name
        self.damage = damage
        self.mana_fill = mana_fill
        self.heal = heal
        self.poison = poison
        self.crit_chance = crit_chance
        self.price = price
        Wand.wands[name] = self

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_n):
        self._name = new_n

    @property
    def damage(self):
        return self._damage
    @damage.setter
    def damage(self, amount):
        self._damage = amount

    @property
    def mana_fill(self):
        return self._mana_fill
    @mana_fill.setter
    def mana_fill(self, amount):
        self._mana_fill = amount

    @property
    def heal(self):
        return self._heal
    @heal.setter
    def heal(self, amount):
        self._heal = amount

    @property
    def poison(self):
        return self._poison
    @poison.setter
    def poison(self, amount):
        self._poison = amount

    @property
    def crit_chance(self):
        return int(self._crit_chance * 100)
    @crit_chance.setter
    def crit_chance(self, amount):
        self._crit_chance = amount

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, amount):
        self._price = amount

    def __str__(self):
        return (f"{self.name:<30}{self.damage:<18}{self.mana_fill:<18}{self.heal:<18}{self.poison:<18}"
                f"{self.crit_chance:<18}{self.price:<18}")

    def __ge__(self, other):
        return self.price >= other.price
    def __lt__(self, other):
        return self.price < other.price

Wand("Weak Wand", 5, 0, 0, 0, 0, 20)
Wand("Regular Wand", 10, 0, 0, 0, 0,50)
Wand("Advanced Wand", 20, 0, 0, 0, 0, 200)
Wand("Lord Voldemort Wand", 20, 7, 0, 0, 0, 400)
Wand("The Elder Wand", 20, 0, 13, 0, 0.1, 1000)
Wand("Severus Wand", 10, 3, 0, 20, 0, 1500)
Wand("Death Eater Wand", 50, 5, 10, 5, 0.2, 5000)