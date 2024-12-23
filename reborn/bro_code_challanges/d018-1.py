# Python bank program 

total = 0
is_running = True

def menu():
    print("********************")
    print("Banking Program")
    print("********************")
    print("1.Show Balance")
    print("2.Deposite")
    print("3.Withdraw")
    print("4.Exit")
    print("********************")
    
menu()
while is_running:
    choice = input("Enter your choice (1-4): ")
    match choice:
        case "1":
            print(f"Your total now is ${total:.2f}.")
        case "2":
            while True:
                add = input("How many you want input?: ")
                if add.isdigit():
                    total += float(add)
                    print(f"You add ${add}")
                    print(f"Now you have ${total} in your account.")
                    menu()
                    break
                else:
                    print("This is not a valid value, try again.")
        case "3":
            while True:
                retire = input("How many you want input?: ")
                if retire.isdigit():
                    total -= float(retire)
                    print(f"You withdraw ${retire}")
                    print(f"Now you have ${total} in your account.")
                    menu()
                    break
                else:
                    print("This is not a valid value, try again.")
        case "4":
            print("Thanks to visit!")
            is_running = False
        case _:
            print("That number is not in options.")
            choose = int(input("Enter your choice (1-4): "))

# In my way, I think using match&cases help me more for understand. But I don't make with functions because just create more errors. The Bro Code's method is even more easier to understand the essential of the program. I will mantain this page for comparision, the Bro Code's program adapted with my code is in d018-2.py.