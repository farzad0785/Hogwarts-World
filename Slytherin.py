from House import House

class Slytherin(House):
    def __init__(self, quote, name, buffs):
        super().__init__(quote, name, buffs)

des = ("Or perhaps in Slytherin"
         "You’ll make your real friends"
         "Those cunning folk use any means"
         "To achieve their ends.")
house_name = "Slytherin"
house_buffs = {
    "hp": 20,
    "mana": 10,
    "coins": 200,
    "crit chance": 15,
}

Slytherin(des, house_name, house_buffs)