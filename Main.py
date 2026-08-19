from random import randint
from Acromantula import Acromantula
from Dragon import Dragon
from Enemies import Enemies
from House import House
from Inventory import Inventory
from Potion import Potion
from Heal_Potion import HealPotion
from Mana_Potion import ManaPotion
from Damage_Potion import DamagePotion
from Spells import Spell
from Wand import Wand
from GameLogic import GameLogic
from Goblin import Goblin
from Gryffindor import Gryffindor
from Hufflepuff import Hufflepuff
from Mage import Mage
from Oni import Oni
from Ravenclaw import Ravenclaw
from Slytherin import Slytherin
from Wolf import Wolf
from Utils import confirm_check

def create_mage():
    name = input("Speak thy name, fledgling wizard... ")
    house_obj = create_house()
    mage = Mage(name, house_obj)
    GameLogic.add_mage(mage)
    Dragon()
    Acromantula()
    Oni()
    Wolf()
    Goblin()
    return mage.coins

def create_house():
    print(f"{'name':<17}{'bonus HP':<15}{'bonus Mana':<15}{'bonus coins':<15}"
          f"{'bonus crit chance'}")
    for house in House.house:
        print(house)

#=====SHOP=====
def buy_wand():
    while True:
        try:
            choice = {}
            i = 1
            print(f"{'key':<6}{'wand name':<28}{'damage':<16}{'mana fill':<21}{'heal':<17}{'poison':<16}{'crit chance':<20}price")
            for wand_obj in Wand.wands.values():
                print(f"{i}{'.':<5}{wand_obj}")
                choice[i] = wand_obj
                i += 1
            print("0.\t  exit")
            print("="*55)

            confirm = True
            user_choice = 1
            while confirm:
                try:
                    user_choice = int(input("Pluck thy wand from shadow and light... "))
                    if user_choice == 0:
                        print(Inventory.sort_inventory())
                        return
                    if 1 <= user_choice <= 7:
                        confirm = confirm_check()
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
            print(f"{'Key':<6}{'Potion type':<20}{'Potion Name':<35}{'Amount':<20}Price")
            i = 1
            for potion_name, potion_obj in Potion.potions.items():
                print(f"{i:<2}{'.':<4}{potion_obj:}")
                choice[i] = [potion_name, potion_obj]
                i += 1
            print("0 .\t  exit")
            print("="*55)

            confirm = True
            user_choice = 0
            while confirm:
                try:
                    user_choice = int(input("Pluck thy potion from heavens and hell... "))
                    if user_choice == 0:
                        print(Inventory.sort_inventory())
                        return
                    if 1 <= user_choice <= 15:
                        confirm = confirm_check()
                    else:
                        print("Vain attempt! But nine potions grace this realm. Choose betwixt 1 and 15. ")

                except ValueError:
                    print("Thy wit falters, Wizard. Enter a true number to brand this potion as thine own. ")

            print(f"Remaining coins: {GameLogic.buy_potion(choice[user_choice][0], choice[user_choice][1])}")
        except ValueError as e:
            print(e)

def learn_spell():
    while True:
        try:
            choice = {}
            i = 1

            print(f"\t\t{'Name':<20}{'Type':<10}{'Kind':<15}{'Amount':<10}{'Required Level':<21}"
                  f"{'Learning Chance':<20}{'Token Cost':<17}{'Attempts':<10}")
            for spell_obj in Spell.spells.values():
                print(f"{i:<2}{'.':<4}{spell_obj}")
                choice[i] = spell_obj
                i += 1
            print("0 .\t  Exit")

            user_choice = 1
            confirm = True
            while confirm:
                try:
                    user_choice = int(input("Enter command: "))
                    if user_choice == 0:
                        print(Inventory.sort_inventory())
                        return
                    elif 1 <= user_choice <= 20:
                        confirm = confirm_check()
                    else:
                        print("Invalid command. Command must be 0-20. ")
                except ValueError:
                    print("Invalid. Command must be a number. ")

            print(f"This spell costs {choice[user_choice].token_cost} tokes. \nSpend? ")
            confirm = confirm_check()
            if not confirm:
                print(f"Remaining tokens: {GameLogic.learn_spell(choice[user_choice])}")
                print(f"Successful learning! You now have {choice[user_choice].name}, and can use it in combats. ")
        except ValueError as e:
            print(e)
            print("You could not learn the spell. ")

def sell_wand():
    #Change to Old English
    print("ATTENTION! Selling your wand, only gives you 80% of its actual price.")

    while True:
        choice = {}
        total_wands = len(Inventory.wands)
        i = 1
        print(f"{'key':<6}{'wand name':<28}price")
        for wand_obj in Inventory.wands:
            print(f"{i}{'.':<5}{wand_obj.name:<30}{int(Inventory.wands[wand_obj].price*0.8)}")
            choice[i] = wand_obj
            i += 1
        print("0.  \texit")
        print("="*55)

        user_choice = 1
        confirm = True
        while confirm:
            try:
                user_choice = int(input("Enter your wand to sell: "))
                if user_choice == 0:
                    print(Inventory.sort_inventory())
                    return
                elif 1 <= user_choice <= total_wands:
                    confirm = confirm_check()
                else:
                    print(f"Vain attempt! Command must be between 0-{total_wands}")
            except ValueError:
                print(f"Invalid! Enter a command between 0 and {total_wands}")
        print(f"Remaining coins: {GameLogic.sell_wand(choice[user_choice])}")

def sell_potion():
    print("ATTENTION. Selling potions, only give you 60% of its actual price. ")
    while True:
        total_potions = len(Inventory.potions)
        choice = {}
        i = 1
        print(f"{'key':<6}{'potion name':<28}{'amount':<18}price")
        for potion_obj in Inventory.potions:
            print(f"{i:<2}{'.':<4}{potion_obj.name:<30}{Inventory.potions[potion_obj]:<18}{int(potion_obj.price*0.6)}")
            choice[i] = potion_obj
            i += 1
        print("0.   \texit")
        print("="*55)

        user_choice = 1
        confirm = True
        while confirm == 1:
            try:
                user_choice = int(input("Enter your choice: "))
                if user_choice == 0:
                    print(Inventory.sort_inventory())
                    return
                elif 0 <= user_choice <= total_potions:
                    confirm = confirm_check()
                else:
                    print(f"Invalid. Enter a command from 0 to {total_potions}")
            except ValueError:
                print(f"Invalid. Enter a command from 0 to {total_potions}")
        print(f"Remaining coins: {GameLogic.sell_potion(choice[user_choice])}")

#=====INVENTORY=====
def set_wand():
    while True:
        try:
            choice = {}
            total_wands = len(Inventory.wands)
            i = 1
            print(f"{'key':<6}{'wand name':<28}")
            for wand_obj in Inventory.wands:
                print(f"{i}{'.':<5}{wand_obj.name:<30}")
                choice[i] = wand_obj
                i += 1
            print("0. \t  exit")
            print("="*55)

            user_choice = 1
            confirm = True
            while confirm:
                try:
                    user_choice = int(input("Pluck thy wand from shadow and light..."))
                    if user_choice == 0:
                        return
                    elif 1 <= user_choice <= total_wands:
                        confirm = confirm_check()
                    else:
                        print(f"Vain attempt! But seven wands grace this realm. Choose betwixt 1 and {total_wands}. ")
                except ValueError:
                    print(f"Thy wit falters, Tarnished. Enter a true number. ")
            GameLogic.set_wand(choice[user_choice])
            break
        except ValueError as e:
            print(e)


def check_item():
    while True:
        try:
            choice = {}
            i = 1
            for wand_obj in Inventory.wands:
                print(f"{i:<2}{'.':<4}{wand_obj.name}")
                choice[i] = wand_obj
                i += 1
            for potion_name, potion_obj in Inventory.potions.items():
                print(f"{i:<2}{'.':<4}{potion_name}")
                choice[i] = potion_obj["object"]
                i += 1
            for spell_obj in Inventory.spells:
                print(f"{i:<2}{'.':<4}{spell_obj.name}")
                choice[i] = spell_obj
            print("0.\t  Exit")

            total_items = len(Inventory.wands) + len(Inventory.potions) + len(Inventory.spells)

            user_choice = 1
            confirm = True
            while confirm:
                try:
                    user_choice = int(input(f"Enter your choice 0-{total_items}"))
                    if user_choice == 0:
                        return
                    elif 1 <= user_choice <= total_items:
                        break
                    else:
                        print(f"Invalid. Entered command must between 0-{total_items}")
                except ValueError:
                    print("Invalid. Command must be a number. ")
            GameLogic.check_item(choice[user_choice])
        except ValueError as e:
            print(e)

#=====STATUS=====
def status():
    pass

#=====CHOOSE ENEMY=====
def choose_enemy():
    try:
        choice = {}
        i = 1
        print(f"{'key':<7}{'Name':<20}{'HP':<8}{'damage':<15}{'XP gain':<12}Coins gain")
        for enemy in Enemies.enemies_list:
            print(f"{i}{'.':<5}{enemy}")
            choice[i] = enemy
            i += 1
        print("0.\t  exit")

        confirm = True
        while confirm:
            try:
                user_choice = int(input())
                if user_choice == 0:
                    return
                elif 0 <= user_choice <= 5:
                    confirm = confirm_check()
                else:
                    print("Invalid. Enter a command from 0-5. ")
            except ValueError:
                print("Invalid. To choose an enemy enter a number from 0-5. ")

    except ValueError:
        print("Invalid. Command must be a number")

shop = {
    1: ("Buy Wand", buy_wand),
    2: ("Buy Potion", buy_potion),
    3: ("Sell Wand", sell_wand),
    4: ("Sell Potion", sell_potion),
    5: ("Learn Spell", learn_spell),
    0: "Exit"
}

inventory = {
    1: ("Items Status", check_item),
    2: ("Set Wand", set_wand),
    0: "Exit"
}

main_menu = {
    1: ("Shop", shop),
    2: ("Inventory", inventory),
    3: ("Status", status),
    4: ('Choose enemy', choose_enemy),
    0: ("exit", exit)
}

create_house()
while True:
    for menu in main_menu:
        print(f"{menu}. {main_menu[menu][0]}")
    try:
        op = int(input("Enter command: "))
        if op == 0:
            exit()
        elif 1 <= op <= max(main_menu):
            new_menu = main_menu[op][1]
            for new_op in new_menu:
                print(f"{new_op}. {new_menu[new_op][0]}")
            op = int(input("Enter command: "))
            if op == 0:
                continue
            new_menu[op][1]()
        else:
            print(f"Invalid. Command must be 0-{max(main_menu)}")

    except ValueError:
        print("Invalid. command must be number. ")