#Functions of Program ---------------------------------------------------------------------------------------

def show_total(total):
    print(f"Your total now is ${total:.2f}.")

def menu():
    print("********************")
    print("  Banking Program   ")
    print("********************")
    print("1.Show Balance")
    print("2.Deposite")
    print("3.Withdraw")
    print("4.Exit")
    print("********************")

def deposit():
    amount = float(input("Enter an amout to be deposited: "))
    if amount < 0:
        print("**************************")
        print("That's not a valid amount.")
        print("**************************")
        return 0
    else:
        return amount
    
def withdraw(total):
    amount = float(input("Enter an amout to be withdrawn: "))
    if amount > total:
        print("******************")
        print("Insufficient funds")
        print("******************")
        return 0
    elif amount < 0:
        print("*****************************")
        print("Amount must be greater than 0")
        print("*****************************")
        return 0
    else:
        return amount

# Program ---------------------------------------------------------------------------------------------
def main():
    total = 0
    is_running = True
    
    while is_running:
        menu()
        choice = input("Enter your choice (1-4): ")
        match choice:
            case "1":
                show_total(total)
            case "2":
                total += deposit()
            case "3":
                total -= withdraw(total)
            case "4":
                print("Thanks to visit!")
                is_running = False
            case _:
                print("******************************")
                print("That number is not in options.")
                print("******************************")

if __name__ == '__main__':
    main()