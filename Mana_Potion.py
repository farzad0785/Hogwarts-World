from Potion import Potion

class ManaPotion(Potion):
    def __init__(self, name, amount, price):
        super().__init__("Mana", name, amount, price, 2)

    def __str__(self):
        return (f"Potion Type: {self.type}"
                f"\nPotion Name: {self.name}"
                f"\nMana Fill Amount: {self.amount}"
                f"\nPrice: {self.price}")