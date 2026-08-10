from House import House

class Slytherin(House):
    def __init__(self):
        quote = ("Or perhaps in Slytherin"
                 "You’ll make your real friends"
                 "Those cunning folk use any means"
                 "To achieve their ends.")
        name = "Slytherin"
        buffs = {"hp": 0,
                "mana": 0,
                "coins": 0,
                "crit chance": 0.2,}
        super().__init__(quote, name, buffs)