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
        inventory = []
        for category, items in GameLogic.inventory.items():
            inventory.append(f"{category}:")
            for item, amount in items.items():
                inventory.append(f"\t{item}: {amount}")

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
        GameLogic.mage.coins += Shop.items["wands"][wand_name]["price"] * 0.8
        return GameLogic.mage.coins

    @staticmethod
    def set_wand():
        #Not completed
        i = 1
        for wand in GameLogic.inventory["wands"]:
            print(f"{i}. {wand}")

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

        GameLogic.mage.coins += Shop.items["potions"][potion_name]["price"] * 0.6
        return GameLogic.mage.coins

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
