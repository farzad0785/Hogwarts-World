from Diagon_alley import Shop
from Enemies import Enemies

def buy_wand():
    while True:
        choice = {}
        i = 1
        for wand_name, wand_attribute in Shop.items["wands"].items():
            print(f"{i}. {wand_name} ")
            for attribute, amount in wand_attribute.items():
                if amount != 0:
                    print(f"\t{attribute}: {amount}")
            choice[wand_name] = i
            i += 1
        print("0. exit")
        print("="*55)
        confirm = 1
        while confirm == 1:
            try:
                user_choice = int(input("Choose your wand: "))
                if user_choice == 0:
                    return
                if 1 <= user_choice <= 7:
                    confirm = int(input("1. Choose again \n2. confirm \nEnter command: "))
                else:
                    print("Invalid! Available wands have command 1-7.")

            except ValueError:
                print("Invalid. Enter integer to purchase and confirm. ")

def buy_potion():
    while True:
        choice = {}
        i = 1
        for item, price in Shop.items["wands"].items():
            print(f"{i}. {item}| {price} coins")
            choice[item] = i
            i += 1
        print("="*55)
        confirm = 1
        while confirm == 1:
            try:
                user_choice = int(input("Choose your wand: "))
                if 1 <= user_choice <= 7:
                    confirm = int(input("1. Choose again \n2. confirm \nEnter command: "))
                else:
                    print("Invalid! Available wands have command 1-7.")

            except ValueError:
                print("Invalid. Enter integer to purchase and confirm. ")

def choose_enemy():
    i = 1
    for enemy in Enemies.enemies_list:
        print(f"{i}. {enemy}")
        i += 1

buy_wand()