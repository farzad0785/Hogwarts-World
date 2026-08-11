from Potion import Potion

class HealPotion(Potion):
    def __init__(self, name, heal, price):
        super().__init__("Heal", name, heal, price,1)

    def __str__(self):
        return (f"Potion Type: {self.type}"
                f"\nPotion Name: {self.name}"
                f"\nHeal Amount: {self.amount}"
                f"\nPrice: {self.price}")