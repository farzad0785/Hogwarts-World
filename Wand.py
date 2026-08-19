class Wand:
    wands = {}
    def __init__(self, name, damage, mana_fill, heal, poison, crit_chance, price, description):
        self.name = name
        self.damage = damage
        self.mana_fill = mana_fill
        self.heal = heal
        self.poison = poison
        self.crit_chance = crit_chance
        self.price = price
        self.description = description
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

    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, prompt):
        self._description = prompt

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Damage: {self.damage}", end=" | ")
        if self.poison != 0:
            print(f"Poison Damage: {self.poison}")
        if self.mana_fill != 0:
            print(f"Mana Fill: {self.mana_fill}", end=" | ")
        if self.heal != 0:
            print(f"Heal: {self.heal}")
        if self.crit_chance != 0:
            print(f"Crit Chance: {self.crit_chance}")

    def __str__(self):
        return (f"{self.name:<30}{self.damage:<18}{self.mana_fill:<18}{self.heal:<18}{self.poison:<18}"
                f"{self.crit_chance:<18}{self.price:<18}")

    def __ge__(self, other):
        return self.price >= other.price
    def __lt__(self, other):
        return self.price < other.price

des = ("A frail splinter of forgotten wood. "
       "\nScarcely worthy of the lowliest acolyte. Its magic flickers, frail as a dying candle's flame.")
Wand("Weak Wand", 5, 0, 0, 0, 0, 20, des)

des = ("A wand of modest make. "
       "\nSufficient for the common practitioner, yet bereft of any spark of greatness or renown.")
Wand("Regular Wand", 10, 0, 0, 0, 0,50, des)

des = ("A wand hewn with purpose. "
       "\nIt hums with latent puissance—prized by those who have delved deep into the arcane arts.")
Wand("Advanced Wand", 20, 0, 0, 0, 0, 200, des)

des = ("Yew and malice, bound in cursed union. "
       "\nIt bestows ruinous might upon its master, yet the soul forfeits a fragment of itself with every casting.")
Wand("Lord Voldemort Wand", 20, 7, 0, 0, 0, 400, des)

des = ("The fabled Deathstick. "
       "\nHewn from the bough of an ancient elder, it bendeth the very laws of magic to the wielder's will.")
Wand("The Elder Wand", 20, 0, 13, 0, 0.1, 1000, des)

des = ("A wand of subtle grace. "
       "\nCrafted for precision and shadow, its sorcery flows like silent venom—lethal and unseen.")
Wand("Severus Wand", 10, 3, 0, 20, 0, 1500, des)

des = ("A twisted branch of darkness incarnate. "
       "Forged amid despair, it hungers for chaos and rewards its bearer with ruinous, volatile fury.")
Wand("Death Eater Wand", 50, 5, 10, 5, 0.2, 5000, des)