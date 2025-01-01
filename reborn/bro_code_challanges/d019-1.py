# slot machine game
#Variables and Imports ---------------------------------------------------------------------------------------
import random
import time
balance = 100
is_running = True
symbols = ("❤️", "🍓", "🍒", "⚜️", "🍋")

#Functions of Program ---------------------------------------------------------------------------------------

def spin_again(is_running):
    another = input("Do you want to spin again? (Y/N): ").lower()
    if another == "y":
        return True
    elif another == "n":
        return False
    else:
        print("This is not acceptable!")
        spin_again(is_running)

def start():
    print("***************************")
    print("Welcome to Python Slots")    
    print("Symbols: ❤️ 🍓 🍒 ⚜️ 🍋")
    print("***************************")

def bet_analyse():
    print(f"Current balance: ${balance}")
    bet = int(input(f"Place your bet amount:"))
    if bet <= 0:
        print("Essa quantia não é valida")
        bet_analyse()
    else:
        return bet

def spinning():
    print("Spinning...")
    for x in range(3):
        time.sleep(1)
        print(x+1, end="... ")
    print()

# Program ---------------------------------------------------------------------------------------------

start()
while is_running:
    bet = int(bet_analyse())
   
    spinning()
    fir_house = random.choices(symbols)
    sec_house = random.choices(symbols)
    thi_house = random.choices(symbols)

    print("****************************************")
    print(f"{fir_house} | {sec_house} | {thi_house}")
    print("****************************************")

    if fir_house == sec_house == thi_house:
        balance += bet
        print("You win!")
        is_running = spin_again(is_running)
    else:
        balance -= bet
        print("Soory you lost this round")
        is_running = spin_again(is_running)

    if balance <= 0:
        print("You don't have more money.")
        is_running = False
    