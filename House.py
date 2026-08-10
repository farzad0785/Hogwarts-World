class House:
    def __init__(self, quote, name, buffs):
        self._quote = quote
        self._name = name
        self._buffs = buffs

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