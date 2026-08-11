from Utils import merge_sort

class Inventory:
    wands = {"Weak wand": 10,
             "Death Eater Wand": 2}
    potions = {"Healing potion #1": 2,
               "Mana potion #1": 1}
    spells = ["Avada Kedavra"]

    @staticmethod
    def sort_inventory():
        Inventory.wands = dict(merge_sort(list(Inventory.wands.items()), "wands"))
        Inventory.potions = dict(merge_sort(list(Inventory.potions.items()), "potions"))
        Inventory.spells = merge_sort(Inventory.spells, "spell")
        return Inventory.show_inventory()

    @staticmethod
    def show_inventory():
        inventory = [f"{'category':<15}{'item_name':<28}amount"]
        for item, amount in Inventory.wands.items():
            inventory.append(f"{'wand':<15}{item:<30}{amount}")
            inventory.append("-"*55)

        return "\n".join(inventory)
"""
    @staticmethod
    def sort_inventory(key):
        if key == "wands":
            GameLogic.inventory[key] = dict(Utils.merge_sort(list(GameLogic.inventory[key].items()), key))
        else:
            GameLogic.inventory[key] = dict(Utils.merge_sort(list(GameLogic.inventory[key].items()), key))
        return GameLogic.show_inventory()

    @staticmethod
    def show_inventory():
        inventory = [f"{'category':<15}{'item_name':<28}amount"]
        for category, items in GameLogic.inventory.items():
            for item, amount in items.items():
                inventory.append(f"{category:<15}{item:<30}{amount}")
            inventory.append("-"*55)

        return "\n".join(inventory)
"""

print(Inventory.sort_inventory())