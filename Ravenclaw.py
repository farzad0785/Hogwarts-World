from House import House

class Ravenclaw(House):
    def __init__(self):
        quote = ("Or yet in wise old Ravenclaw"
                "\nIf you’ve a ready mind"
                "\nWhere those of wit and learning"
                "\nWill always find their kind.")
        name = "Ravenclaw"
        buffs = {"hp": 0,
                "mana": 0,
                "coins": 500,
                "crit chance": 0,}
        super().__init__(quote, name, buffs)