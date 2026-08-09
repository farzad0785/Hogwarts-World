from DiagonAlley import Shop
from Enemies import Enemies
from GameLogic import GameLogic
from Mage import Mage

def create_mage():
    name = input("Speak thy name, fledgling wizard... ")
    mage = Mage(name)
    GameLogic.add_mage(mage)
    return mage.coins

def buy_wand():
    while True:
        try:
            choice = {}
            i = 1
            print(f"{'key':<6}{'wand name':<28}{'damage':<17}{'mana fill':<21}{'heal':<18}{'poison':<18}{'crit chance':<21}price")
            for wand_name, wand_attribute in Shop.items["wands"].items():
                print(f"{i}{'.':<5}{wand_name:<30}", end="")
                for amount in wand_attribute.values():
                    print(f"{amount:<18} ", end="")
                choice[i] = wand_name
                i += 1
                print()
            print("0.\t  exit")
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
                            try:
                                confirm = int(input("1. Reconsider \n2. Seal thy pact \nThy decree: "))
                                if confirm in (1, 2):
                                    break
                                else:
                                    print("Vain attempt! Choose betwixt 1 or 2. ")
                            except ValueError:
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
            print(f"{'key':<6}{'potion name':<28}{'amount':<20}price")
            i = 1
            for potion_name, potion_attribute in Shop.items["potions"].items():
                print(f"{i}{'.':<5}{potion_name:<30}", end="")
                for attribute, amount in potion_attribute.items():
                    if attribute == "sort key":
                        continue
                    print(f"{amount:<18} ", end="")
                choice[i] = potion_name
                i += 1
                print()
            print("0. \t  exit")
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
                            try:
                                confirm = int(input("1. Reconsider \n2. Seal thy pact \nThy decree: "))
                                if confirm in (1, 2):
                                    break
                                else:
                                    print("Vain attempt! Choose betwixt 1 or 2. ")
                            except ValueError:
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
            total_wands = len(GameLogic.inventory["wands"])
            i = 1
            print(f"{'key':<6}{'wand name':<28}{'amount':<18}price")
            for wand_name in GameLogic.inventory["wands"]:
                print(f"{i}{'.':<5}{wand_name:<30}{GameLogic.inventory['wands'][wand_name]:<18}{int(Shop.items['wands'][wand_name]['price']*0.8)}")
                choice[i] = wand_name
                i += 1
            print("0. \t  exit")
            print("="*55)

            user_choice = 1
            confirm = 1
            while confirm == 1:
                try:
                    user_choice = int(input("Enter your wand to sell: "))
                    if user_choice == 0:
                        print(GameLogic.sort_inventory("wands"))
                        return
                    elif 1 <= user_choice <= total_wands:
                        while True:
                            try:
                                confirm = int(input("1. Reconsider \n2. Seal thy pact \nThy decree: "))
                                if confirm in (1, 2):
                                    break
                                else:
                                    print("Invalid. Enter command 1 or 2. ")
                            except ValueError:
                                print("Invalid. Command be must a number 1 or 2. ")
                    else:
                        print("Vain attempt! ")
                except ValueError:
                    print(f"Invalid! Enter a command between 1 and {total_wands}")
            print(f"Remaining coins: {GameLogic.sell_wand(choice[user_choice])}")
        except ValueError as e:
            print(e)

def sell_potion():
    print("ATTENTION. Selling potions, only give you 60% of its actual price. ")
    while True:
        total_potions = len(GameLogic.inventory["potions"])
        choice = {}
        i = 1
        print(f"{'key':<6}{'potion name':<28}{'amount':<18}price")
        for potion_name in GameLogic.inventory["potions"]:
            print(f"{i}{'.':<5}{potion_name:<30}{GameLogic.inventory['potions'][potion_name]:<18}{int(Shop.items['potions'][potion_name]['price']*0.6)}")
            choice[i] = potion_name
            i += 1
        print("0. \t  exit")
        print("="*55)

        user_choice = 1
        confirm = 1
        while confirm == 1:
            try:
                user_choice = int(input("Enter you choice: "))
                if user_choice == 0:
                    print(GameLogic.sort_inventory("potions"))
                    return
                elif 0 > user_choice or user_choice > total_potions:
                    print(f"Invalid. Enter a command from 1 to {total_potions}")
                else:
                    while True:
                        try:
                            confirm = int(input("1. Reconsider \n2. Seal thy pact \nThy decree: "))
                            if confirm in (1, 2):
                                break
                            else:
                                print("Invalid. Enter command 1 or 2. ")
                        except ValueError:
                            print("Invalid. Enter command 1 or 2. ")
                    break
            except ValueError:
                print(f"Invalid. Enter a command from 1 to {total_potions}")
        print(f"Remaining coins: {GameLogic.sell_potion(choice[user_choice])}")

def set_wand():
    while True:
        total_wands = len(GameLogic.inventory["wands"])
        i = 1
        for wand in GameLogic.inventory["wands"]:
            print(f"{i}. {wand}")
        try:
            choice = int(input("Pluck thy wand from shadow and light..."))
            if 1 <= choice <= len(GameLogic.inventory["wands"]):
                break
            else:
                print(f"Vain attempt! But seven wands grace this realm. Choose betwixt 1 and {total_wands}. ")
        except ValueError:
            print(f"Thy wit falters, Tarnished. Enter a true number. ")
def choose_enemy():
    i = 1
    for enemy in Enemies.enemies_list:
        print(f"{i}. {enemy}")
        i += 1

operation_table = {1: ("buy wand", buy_wand),
                   2: ("buy potion", buy_potion),
                   3: ("sell wand", sell_wand),
                   4: ("sell potion", sell_potion),
                   5: ("set wand", set_wand),
                   0: ("exit", exit)}
create_mage()
while True:
    for j in operation_table:
        print(j, operation_table[j][0])
    try:
        operation = int(input("Enter command: "))
        if 0 <= operation <= max(operation_table):
            operation_table[operation][1]()
        else:
            print(f"Invalid. Command must be 0-{max(operation_table)}")

    except ValueError:
        print("Invalid. command must be number. ")