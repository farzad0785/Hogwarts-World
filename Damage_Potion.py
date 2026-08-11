from Potion import Potion

class DamagePotion(Potion):
    def __init__(self, name, amount, price):
        super().__init__("Damage", name, amount, price, 3)

    def __str__(self):
        return (f"Potion Type: {self.type}"
                f"\nPotion Name: {self.name}"
                f"\nIncrease Damage Amount: {self.amount}"
                f"\nPrice: {self.price}")