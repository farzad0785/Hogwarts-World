from Spells import Spell
from Utils import merge_sort

class Inventory:
    wands = []
    potions = {}
    spells = []

    @staticmethod
    def add_wand(wand_obj):
        if wand_obj in Inventory.wands:
            raise ValueError(f"Invalid. You already have {wand_obj.name}. ")
        Inventory.wands.append(wand_obj)

    @staticmethod
    def add_potion(potion_name, potion_obj):
        if potion_name in Inventory.potions:
            Inventory.potions[potion_name]["amount"] += 1
        else:
            Inventory.potions[potion_name] = {
                "object": potion_obj,
                "amount": 1,
            }

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
        Inventory.wands = merge_sort(Inventory.wands, "wands")
        Inventory.potions = dict(merge_sort(list(Inventory.potions.items()), "potions"))
        Inventory.spells = merge_sort(Inventory.spells, "spell")
        return Inventory.show_inventory()

    @staticmethod
    def show_inventory():
        inventory = ["=========================WANDS=========================", f"{'wand name':<35}"]
        for wand in Inventory.wands:
            inventory.append(f"{wand.name:<35}")
        inventory.append("-"*55)

        inventory.append("=========================POTIONS========================")
        inventory.append(f"{'potion name':<35}quantity")
        for potion_name, amount in Inventory.potions.items():
            inventory.append(f"{potion_name:<38}{amount['amount']}")
        inventory.append("-"*55)

        inventory.append("=========================SPELLS=========================")
        inventory.append(f"{'spell name':<35}kind")
        for spell in Inventory.spells:
            inventory.append(f"{spell.name:<35}{spell.kind}")
        inventory.append("-"*55)

        return "\n".join(inventory)

    @staticmethod
    def check_item(item_obj):
        item_obj.show_info()