import random
from Utils import confirm_check
from DiagonAlley import Shop
import Utils
from Inventory import Inventory
from Spells import Spell

class GameLogic:
    mage = None
    spells = {}
    main_wand = ""

    @staticmethod
    def add_mage(mage_obj):
        GameLogic.mage = mage_obj

    @staticmethod
    def buy_wand(wand_obj):
        if GameLogic.mage.coins < wand_obj.price:
            raise ValueError("You don't have enough coins. ")
        try:
            Inventory.add_wand(wand_obj)
            GameLogic.mage.coins -= wand_obj.price
        except ValueError as e:
            return e
        return GameLogic.mage.coins

    @staticmethod
    def sell_wand(wand_obj):
        Inventory.remove_wand(wand_obj)
        GameLogic.mage.coins += int(Inventory.wands[wand_obj].price * 0.8)
        return GameLogic.mage.coins

    @staticmethod
    def set_wand(wand_name):
        if wand_name == GameLogic.main_wand:
            raise ValueError("This wand is already your main wand.")
        GameLogic.main_wand = wand_name


    @staticmethod
    def buy_potion(potion_name, potion_obj):
        if GameLogic.mage.coins < potion_obj.price:
            raise ValueError("You don't have enough coins. ")
        try:
            Inventory.add_potion(potion_name, potion_obj)
            GameLogic.mage.coins -= potion_obj.price
        except ValueError as e:
            return e
        return GameLogic.mage.coins

    @staticmethod
    def sell_potion(potion_obj):
        Inventory.remove_potion(potion_obj)
        GameLogic.mage.coins += int(Shop.items["potions"][potion_obj]["price"] * 0.6)
        return GameLogic.mage.coins

    @staticmethod
    def learn_spell(spell_obj):
        spell_obj.attempts += 1
        if spell_obj.token_cost > GameLogic.mage.tokens:
            raise ValueError("Invalid. You don't have enough tokens to learn this spell.")

        can_learn = True
        learning_chance = spell_obj.learning_chance
        if learning_chance < 100:
            can_learn = GameLogic.check_learning_chance(learning_chance)

        if not can_learn:
            raise ValueError(f"Your tokens lost within the use. You didn't have the chance to learn {spell_obj.name}")


        Inventory.add_spell(spell_obj)
        GameLogic.mage.tokens -= spell_obj.token_cost
        return GameLogic.mage.tokens

    @staticmethod
    def check_learning_chance(chance):
        chance_list = [i for i in range(1, 101)]
        random_num = random.choice(chance_list)

        if random_num > chance:
            return False
        return True

    @staticmethod
    def check_item(item_obj):
        Inventory.check_item(item_obj)

    @staticmethod
    def check_storage(f):
        #Not completed yet
        result = []
        inventory_length = len(Inventory.wands) + len(Inventory.potions) + len(Inventory.spells)
        maximum_length = GameLogic.mage.level * 4 + 3
        result.append(f"Total inventory: {inventory_length}")
        if inventory_length == maximum_length:
            raise ValueError("Invalid. Inventory is full")
        f()
        if inventory_length > maximum_length:
            raise ValueError("Invalid. Inventory capacity exceeds the maximum.")

    @staticmethod
    def level_up():
        base_xp = 10*GameLogic.mage.level+405
        if GameLogic.mage.xp >= base_xp:
            result = []
            GameLogic.mage.xp -= base_xp
            result.append(GameLogic.mage.xp)
            GameLogic.mage.level += 1
            result.append(GameLogic.mage.level)
            GameLogic.mage.hp += int((1/3)*GameLogic.mage.hp + 2)
            result.append(GameLogic.mage.hp)
            GameLogic.mage.mana += int((1/5)*GameLogic.mage.mana - 2)
            result.append(GameLogic.mage.mana)
            GameLogic.mage.tokens += 5
            result.append(GameLogic.mage.tokens)
