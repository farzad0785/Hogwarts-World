from Potion import Potion

class HealPotion(Potion):
    def __init__(self, description, name, heal, price):
        super().__init__(description, "Heal", name, heal, price,1)
        Potion.potions[name] = self

    def __str__(self):
        return f"{self.type:<20}{self.name:<37}{self.amount:<19}{self.price}"

des = ("A pale, watery concoction. Scarce more than a whisper of true healing. "
       "\nMends the most trivial of wounds, yet offers little solace to the gravely injured.")
HealPotion(des, "Diluted Wiggenweld Draught", 20, 30)

des = ("A vibrant emerald brew, bubbling with latent vitality. Restores the flesh "
       "\nto a moderate state of wholeness—a staple in the satchel of any prudent wizard.")
HealPotion(des, "Pure Wiggenweld Elixir", 50, 100)

des = ("A shimmering, golden liquid, warm to the touch. Infused with the "
       "\nessence of the immortal bird, it weeps life back into the dying with fervent haste.")
HealPotion(des, "Phoenix Tear Infusion", 100, 250)

des = ("A cursed silver ichor, gleaming with forbidden allure. "
       "\nGrants tremendous restoration, yet stains the soul with a foul taint. "
       "\nOnly the desperate or the foolish partake.")
HealPotion(des, "Essence of Unicorn Blood", 200, 500)

des = ("A legendary draught, its recipe lost to the ages. "
       "\nSaid to be brewed by the four great founders themselves. "
       "\nFully restores the drinker, as if blessed by Hogwarts itself.")
HealPotion(des, "Elixir of the Founders", 500, 1000)