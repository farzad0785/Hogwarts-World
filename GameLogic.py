from DiagonAlley import Shop
import Utils
from Spells import Spell

class GameLogic:
    mage = None
    inventory = {"wands": {},
                 "potions": {}}
    spells = {}
    main_wand = ""
    level = 1
    xp = 0

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

    @staticmethod
    def add_mage(mage_obj):
        GameLogic.mage = mage_obj

    @staticmethod
    def buy_wand(wand_name):
        if GameLogic.mage.coins < Shop.items["wands"][wand_name]["price"]:
            raise ValueError("You don't have enough coins. ")

        if wand_name in GameLogic.inventory["wands"]:
            GameLogic.inventory["wands"][wand_name] += 1
        else:
            GameLogic.inventory["wands"][wand_name] = 1

        GameLogic.mage.coins -= Shop.items["wands"][wand_name]["price"]
        return GameLogic.mage.coins

    @staticmethod
    def sell_wand(wand_name):
        if GameLogic.inventory["wands"][wand_name] == 1:
            GameLogic.inventory["wands"].pop(wand_name)
        else:
            GameLogic.inventory["wands"][wand_name] -= 1
        GameLogic.mage.coins += int(Shop.items["wands"][wand_name]["price"] * 0.8)
        return GameLogic.mage.coins

    @staticmethod
    def set_wand(wand_name):
        if wand_name == GameLogic.main_wand:
            raise ValueError("This wand is already your main wand.")
        GameLogic.main_wand = wand_name


    @staticmethod
    def buy_potion(potion_name):
        if GameLogic.mage.coins < Shop.items["potions"][potion_name]["price"]:
            raise ValueError("You don't have enough coins. ")
        if potion_name in GameLogic.inventory["potions"]:
            GameLogic.inventory["potions"][potion_name] += 1
        else:
            GameLogic.inventory["potions"][potion_name] = 1

        GameLogic.mage.coins -= Shop.items["potions"][potion_name]["price"]
        return GameLogic.mage.coins

    @staticmethod
    def sell_potion(potion_name):
        if GameLogic.inventory["potions"][potion_name] == 1:
            GameLogic.inventory["potions"].pop(potion_name)
        else:
            GameLogic.inventory["potions"][potion_name] -= 1

        GameLogic.mage.coins += int(Shop.items["potions"][potion_name]["price"] * 0.6)
        return GameLogic.mage.coins

    @staticmethod
    def check_storage(f):
        result = []
        inventory_length = len(GameLogic.inventory["wands"]) + len(GameLogic.inventory["potions"])
        maximum_length = GameLogic.level * 4 + 3
        result.append(f"Total inventory: {inventory_length}")
        if inventory_length == maximum_length:
            raise ValueError("Invalid. Inventory is full")
        f()
        if inventory_length > maximum_length:
            raise ValueError("Invalid. Inventory capacity exceeds the maximum.")


    @staticmethod
    def learn_spell(spell):
        if spell in GameLogic.inventory["spells"]:
            raise ValueError("You have already learned this spell. ")
        GameLogic.inventory["spells"] = spell

    @staticmethod
    def level_up():
        base_xp = 10*GameLogic.level^2+405
        if GameLogic.xp >= base_xp:
            GameLogic.xp -= base_xp
            GameLogic.level += 1
            GameLogic.mage.hp += int((1/3)*GameLogic.mage.hp + 2)
            GameLogic.mage.mana += int((1/5)*GameLogic.mage.mana - 2)
