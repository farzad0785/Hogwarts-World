class House:
    house = []
    def __init__(self, quote, name, buffs):
        self._quote = quote
        self._name = name
        self._buffs = buffs
        House.house.append(self)
    #Encapsulation
    @property
    def quote(self):
        return self._quote

    @property
    def name(self):
        return self._name

    @property
    def buffs(self):
        return self._buffs

    def add_buffs(self):
        for buff, amount in self.buffs.items():
            if amount != 0:
                pass

    def __str__(self):
        return (f"{self.name:<20}{self.buffs['hp']:<16}{self.buffs['mana']:<15}{self.buffs['coins']:<18}"
                f"{self.buffs['crit chance']}")