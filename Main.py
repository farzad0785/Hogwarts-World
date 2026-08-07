from DiagonAlley import Shop
from Enemies import Enemies
from GameLogic import GameLogic
from Mage import Mage

def create_mage():
    name = input("Speak thy name, fledgling wizard...")
    mage = Mage(name)
    GameLogic.add_mage(mage)

def buy_wand():
    while True:
        try:
            choice = {}
            i = 1
            for wand_name, wand_attribute in Shop.items["wands"].items():
                print(f"{i}. {wand_name} ")
                for attribute, amount in wand_attribute.items():
                    if amount != 0:
                        print(f"\t{attribute}: {amount}")
                choice[i] = wand_name
                i += 1
            print("0. exit")
            print("="*55)
            confirm = 1
            user_choice = 1
            while confirm == 1:
                try:
                    user_choice = int(input("Pluck thy wand from shadow and light... "))
                    if user_choice == 0:
                        print(GameLogic.sort_inventory("wands"))
                        return
                    if 1 <= user_choice <= 7:
                        while True:
                            confirm = int(input("1. Reconsider \n2. Seal thy pact \nThy decree: "))
                            if confirm in (1, 2):
                                break
                            else:
                                print("Vain attempt! Choose betwixt 1 or 2. ")
                    else:
                        print("Vain attempt! But seven wands grace this realm. Choose betwixt 1 and 7. ")
                except ValueError:
                    print("Thy wit falters, Wizard. Enter a true number to brand this wand as thine own. ")
                print(f"Remaining coins: {GameLogic.buy_wand(choice[user_choice])}")
        except ValueError as e:
            print(e)

def buy_potion():
    while True:
        try:
            choice = {}
            i = 1
            for potion_name, potion_attribute in Shop.items["potions"].items():
                print(f"{i}. {potion_name}: ")
                for attribute, amount in potion_attribute.items():
                    print(f"\t{attribute}: {amount}")
                choice[i] = potion_name
                i += 1
            print("0. exit")
            print("="*55)
            confirm = 1
            user_choice = 0
            while confirm == 1:
                try:
                    user_choice = int(input("Pluck thy potion from heavens and hell... "))
                    if user_choice == 0:
                        print(GameLogic.sort_inventory("potions"))
                        return
                    if 1 <= user_choice <= 9:
                        while True:
                            confirm = int(input("1. Reconsider \n2. Seal thy pact \nThy decree: "))
                            if confirm in (1, 2):
                                break
                            else:
                                print("Vain attempt! Choose betwixt 1 or 2. ")
                    else:
                        print("Vain attempt! But nine potions grace this realm. Choose betwixt 1 and 9. ")
                except ValueError:
                    print("Thy wit falters, Wizard. Enter a true number to brand this potion as thine own. ")
            print(f"Remaining coins: {GameLogic.buy_potion(choice[user_choice])}")
        except ValueError as e:
            print(e)

def sell_wand():
    #Change Old English
    print("ATTENTION! Selling your wand, only gives you 80% of its actual price.")

    while True:
        try:
            choice = {}
            i = 1
            for wand_name in GameLogic.inventory["wands"]:
                print(f"{i}. {wand_name}: {Shop.items['wands'][wand_name]['price']*0.8}")
                choice[i] = wand_name
                i += 1
            print("0. exit")
            print("="*55)
            user_choice = 1
            confirm = 1
            while confirm == 1:
                try:
                    user_choice = int(input("Enter your wand to sell: "))
                    if user_choice == 0:
                        print(GameLogic.sort_inventory("wands"))
                        return
                    elif 1 <= user_choice <= len(GameLogic.inventory["wands"]):
                        GameLogic.sell_wand(choice[user_choice])


def set_wand():
    while True:
        i = 1
        for wand in GameLogic.inventory["wands"]:
            print(f"{i}. {wand}")
        try:
            choice = int(input("Pluck thy wand from shadow and light..."))
            if 1 <= choice <= len(GameLogic.inventory["wands"]):
                break
            else:
                print(f"Vain attempt! But seven wands grace this realm. Choose betwixt 1 and {len(GameLogic.inventory['wands'])}. ")
        except ValueError:
            print(f"Thy wit falters, Tarnished. Enter a true number. ")
def choose_enemy():
    i = 1
    for enemy in Enemies.enemies_list:
        print(f"{i}. {enemy}")
        i += 1

create_mage()
buy_wand()
buy_potion()
