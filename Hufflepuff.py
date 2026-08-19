from House import House

class Hufflepuff(House):
    def __init__(self, quote, name, buffs):
        super().__init__(quote, name, buffs)

des = ("You might belong in Hufflepuff"
       "\nWhere they are just and loyal"
       "\nThose patient Hufflepuffs are true"
       "\nAnd unafraid of toil.")
house_name = "Hufflepuff"
house_buffs = {
    "hp": 16,
    "mana": 25,
    "coins": 300,
    "crit chance": 5,
}

Hufflepuff(des, house_name, house_buffs)