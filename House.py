class House:
    def __init__(self, name, w,spells):
        self.name = name
        self.spells = spells

    #Encapsulation
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_n):
        self._name = new_n

    @property
    def spells(self):
        return self._spells
    @spells.setter
    def spells(self, new_spells):
        self._spells = new_spells

    #Methods
    def add_spells(self, spell):
        self.spells.append(spell)
