from Spells import Spell
from Utils import merge_sort

class Inventory:
    wands = {}
    potions = {}
    spells = []

    @staticmethod
    def add_wand(wand_obj):
        if wand_obj in Inventory.wands:
            raise ValueError(f"Invalid. You already have {wand_obj.name}. ")
        Inventory.wands[wand_obj] = 1

    @staticmethod
    def add_potion(potion_obj):
        if potion_obj in Inventory.potions:
            Inventory.potions[potion_obj] += 1
        else:
            Inventory.potions[potion_obj] = 1

    @staticmethod
    def add_spell(spell_obj):
        if spell_obj in Inventory.spells:
            raise ValueError("Invalid. You have already learned this spell. ")
        Inventory.spells.append(spell_obj)

    @staticmethod
    def remove_wand(wand_obj):
        Inventory.wands.pop(wand_obj)

    @staticmethod
    def remove_potion(potion_obj):
        if Inventory.potions[potion_obj] == 1:
            Inventory.potions.pop(potion_obj)
        else:
            Inventory.potions[potion_obj] -= 1

    @staticmethod
    def sort_inventory():
        Inventory.wands = dict(merge_sort(list(Inventory.wands.items()), "wands"))
        Inventory.potions = dict(merge_sort(list(Inventory.potions.items()), "potions"))
        Inventory.spells = merge_sort(Inventory.spells, "spell")
        return Inventory.show_inventory()

    @staticmethod
    def show_inventory():
        inventory = ["=========================WANDS=========================", f"{'wand name':<27}quantity"]
        for wand, amount in Inventory.wands.items():
            inventory.append(f"{wand.name:<30}{amount}")
        inventory.append("-"*55)

        inventory.append("=========================POTIONS========================")
        inventory.append(f"{'potion name':<27}quantity")
        for potion, amount in Inventory.potions.items():
            inventory.append(f"{potion.name:<30}{amount}")
        inventory.append("-"*55)

        inventory.append("=========================SPELLS=========================")
        inventory.append(f"{'spell name':<28}kind")
        for spell in Inventory.spells:
            inventory.append(f"{spell.name:<28}{spell.kind}")
        inventory.append("-"*55)

        return "\n".join(inventory)

    @staticmethod
    def check_item(key, name):
        pass