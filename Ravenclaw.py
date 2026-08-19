from House import House

class Ravenclaw(House):
    def __init__(self, quote, name, buffs):
        super().__init__(quote, name, buffs)

des = ("Or yet in wise old Ravenclaw"
         "\nIf you’ve a ready mind"
         "\nWhere those of wit and learning"
         "\nWill always find their kind.")
house_name = "Ravenclaw"
house_buffs = {
    "hp": 16,
    "mana": 7,
    "coins": 800,
    "crit chance": 5,
}

Ravenclaw(des, house_name, house_buffs)