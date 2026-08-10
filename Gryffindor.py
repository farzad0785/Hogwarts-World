from House import House

class Gryffindor(House):
    def __init__(self):
        quote = ("You might belong in Gryffindor,"
                 "\nWhere dwell the brave at heart,"
                 "\nTheir daring, nerve and chivalry"
                 "\nSet Gryffindors apart.")
        name = "Gryffindor"
        buffs = {"hp": 100,
                "mana": 0,
                "coins": 0,
                "crit chance": 0,}
        super().__init__(quote, name, buffs)