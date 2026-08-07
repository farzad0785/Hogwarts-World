from DiagonAlley import Shop
from Mage import Mage
from Spells import Spell


class GameLogic:
    mage = None
    inventory = {"wands": {},
                 "potions": {},
                 "spells": {}}
    main_wand = ""
    level = 1
    xp = 0

    @staticmethod
    def show_inventory():
        for item in GameLogic.inventory.values():
            print(item)

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
    def sell_wand(wand_name, mage):
        GameLogic.inventory["wands"][wand_name] -= 1
        mage.coins += Shop.items["wands"][wand_name]["price"] * 0.8
        return mage.coins

    @staticmethod
    def set_wand():
        i = 1
        for wand in GameLogic.inventory["wands"]:
            print(f"{i}. {wand}")

    @staticmethod
    def buy_potion(potion, mage):
        if potion in GameLogic.inventory["potions"]:
            GameLogic.inventory["potions"][potion] += 1
        else:
            GameLogic.inventory["potions"][potion] = 1

        mage.coins -= Shop.items["potions"][potion]
        return mage.coins

    @staticmethod
    def sell_potion(potion, mage):
        if potion in GameLogic.inventory["potions"]:
            GameLogic.inventory["potions"][potion] += 1
        else:
            GameLogic.inventory["potions"][potion] = 1

        mage.coins += Shop.items["potions"][potion] * 0.8
        return mage.coins

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
