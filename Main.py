from random import randint
from Acromantula import Acromantula
from Dragon import Dragon
from Enemies import Enemies
from Inventory import Inventory
from Potion import Potion
from Heal_Potion import HealPotion
from Mana_Potion import ManaPotion
from Damage_Potion import DamagePotion
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
    house = {
        1: Gryffindor(),
        2: Hufflepuff(),
        3: Ravenclaw(),
        4: Slytherin(),
    }
    i = randint(1, 4)
    return house[i]

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
            for potion_obj in Potion.potions.values():
                print(f"{i:<2}{'.':<4}{potion_obj:}")
                choice[i] = potion_obj
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
                    if 1 <= user_choice <= 9:
                        confirm = confirm_check()
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


def choose_enemy():
    while True:
        try:
            choice = {}
            i = 1
            print(f"{'key':<7}{'Name':<20}{'HP':<8}{'damage':<15}{'XP gain':<12}Coins gain")
            for enemy in Enemies.enemies_list:
                print(f"{i}{'.':<5}{enemy.name:<20}{enemy.hp:<10}{enemy.damage:<15}{enemy.xp:<15}{enemy.coins}")
                choice[i] = enemy.name
                i += 1
            print("0.\t  exit")

            user_choice = 1
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
                    print("Invalid. To choose an enemy enter a number from 1-5. ")

        except ValueError:
            print("Invalid")

def confirm_check():
    while True:
        try:
            confirm = int(input("1. Reconsider \n2. Seal thy pact \nThy decree: "))
            if confirm == 1:
                return True
            elif confirm == 2:
                return False
            else:
                print("Invalid. Enter command 1 or 2. ")
        except ValueError:
            print("Invalid. Enter command 1 or 2. ")

operation_table = {1: ("buy wand", buy_wand),
                   2: ("buy potion", buy_potion),
                   3: ("sell wand", sell_wand),
                   4: ("sell potion", sell_potion),
                   5: ("set wand", set_wand),
                   6: ('Choose enemy', choose_enemy),
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