from Potion import Potion

class ManaPotion(Potion):
    def __init__(self, description, name, amount, price):
        super().__init__(description, "Mana", name, amount, price, 2)
        Potion.potions[name] = self

    def show_info(self):
        print(f"Potion type: {self.type} | Name: {self.name} \n"
              f"Info: {self.description}\n"
              f"Mana fill: {self.amount} | Price: {self.price} \n")

    def __str__(self):
        return f"{self.type:<20}{self.name:<37}{self.amount:<19}{self.price}"

des = ("A murky brew of crushed moonstone. Soothes the "
       "\nfrayed mind, replenishing a sliver of arcane vigor.")
ManaPotion(des, "Cloudy Moonstone Draught", 10, 20)

des = ("Distilled from the resilient beast. Sharpens the weary mind"
       "\nand restores a moderate wellspring of concentration.")
ManaPotion(des, "Essence of Murtlap Tentacles", 20, 50)

des = ("A swirling silver nectar. Clears the fog of battle, "
       "\nflooding the caster with a surging tide of magical stamina.")
ManaPotion(des, "Potion of Unbridled Clarity", 50, 200)

des = ("A forbidden brew that borders on divination. Restores vast reservoirs of focus, "
       "\nallowing the caster to perceive the weave of magic itself.")
ManaPotion(des, "Elixir of the Inner Eye", 100, 500)

des = ("Impossibly rare. Only those who have witnessed death can harvest it. "
       "\nFully saturates the soul with unlimited, fleeting arcane power.")
ManaPotion(des, "Tears of a Dying Thestral", 200, 1000)