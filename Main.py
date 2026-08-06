from DiagonAlley import Shop
from Enemies import Enemies
from GameLogic import GameLogic


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
                print("Invalid! Enter command 1-7 to purchase and confirm. ")

def set_wand():
    while True:
        i = 1
        for wand in GameLogic.inventory["wands"]:
            print(f"{i}. {wand}")
        try:
            choice = int(input("Choose your main wand: "))
            if 1 <= choice <= len(GameLogic.inventory["wands"]):
                break
            else:
                print(f"Invalid! Available command are 1-{len(GameLogic.inventory['wands'])}.")
        except ValueError:
            print(f"Invalid! Enter 1-{len(GameLogic.inventory['wands'])} command. ")
def choose_enemy():
    i = 1
    for enemy in Enemies.enemies_list:
        print(f"{i}. {enemy}")
        i += 1

buy_wand()