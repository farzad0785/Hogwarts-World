from House import House

class Hufflepuff(House):
    def __init__(self):
        quote = ("You might belong in Hufflepuff"
                 "\nWhere they are just and loyal"
                 "\nThose patient Hufflepuffs are true"
                 "\nAnd unafraid of toil.")
        name = "Hufflepuff"
        buffs = {"hp": 0,
                "mana": 20,
                "coins": 0,
                "crit chance": 0,}
        super().__init__(quote, name, buffs)