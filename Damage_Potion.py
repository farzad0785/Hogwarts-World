from Potion import Potion

class DamagePotion(Potion):
    def __init__(self, description, name, amount, price):
        super().__init__(description, "Damage", name, amount, price, 3)
        Potion.potions[name] = self

    def show_info(self):
        print(f"Potion type: {self.type} | Name: {self.name} \n"
              f"Info: {self.description}\n"
              f"Damage incremental: {self.amount} | Price: {self.price}")

    def __str__(self):
        return f"{self.type:<20}{self.name:<37}{self.amount:<19}{self.price}"

des = ("A sharp, bitter concoction. Ignites a faint, feral rage "
       "\nwithin the veins, slightly bolstering offensive might.")
DamagePotion(des, "Fanged Fury Brew", 5, 10)

des = ("Infused with the ground talons of a Welsh Green. "
       "\nLends the drinker a savage, bestial strength for a time.")
DamagePotion(des, "Dragon Claw Essence", 10, 30)

des = ("Fiery and volatile. This dangerous brew amplifies "
       "\nthe caster's destructive output to a formidable degree.")
DamagePotion(des, "Extract of the Hungarian Horntail", 20, 100)

des = ("A bubbling crimson potion that calls to the primal mind. "
       "\nGreatly magnifies offensive prowess, yet whispers of reckless abandon.")
DamagePotion(des, "Draught of the Berserker", 50, 500)

des = ("A cursed, gleaming venom. Drinking it grants ruinous power akin to the "
       "\nserpent's deadly gaze—though it is not meant for mortal tongues.")
DamagePotion(des, "Blood of the Basilisk", 100, 1000)