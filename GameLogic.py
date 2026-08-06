from DiagonAlley import Shop
from Mage import Mage
from Spells import Spell


class GameLogic:
    inventory = {"wands": {},
                 "potions": {},
                 "spells": {}}
    main_wand = ""

    @staticmethod
    def buy_wand(wand_name, mage):
        if mage.coins < Shop.items["wands"][wand_name]["price"]:
            raise ValueError("You don't have enough coins. ")

        if wand_name in GameLogic.inventory["wands"]:
            GameLogic.inventory["wands"][wand_name] += 1
        else:
            GameLogic.inventory["wands"][wand_name] = 1

        mage.coins -= Shop.items["wands"][wand_name]["price"]
        return mage.coins

    @staticmethod
    def sell_wand(wand_name, mage):
        GameLogic.inventory["wands"][wand_name] -= 1
        mage.coins += Shop.items["wands"][wand_name]["price"] * 0.8
        return mage.coins

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
