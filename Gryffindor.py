from House import House

class Gryffindor(House):
    def __init__(self, quote, name, buffs):
        super().__init__(quote, name, buffs)

des = ("You might belong in Gryffindor,"
       "\nWhere dwell the brave at heart,"
       "\nTheir daring, nerve and chivalry"
       "\nSet Gryffindors apart.")
house_name = "Gryffindor"
house_buffs = {
    "hp": 100,
    "mana": 13,
    "coins": 200,
    "crit chance": 5,
}

Gryffindor(des, house_name, house_buffs)