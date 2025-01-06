# 5.5 Lista telefônica
# I literally made this alone!!! I am really happy with results. I know somethings are weird and I can upgrade, but for my own its a good begin. 


is_running = True
tel_lis = {"Esther":"(45) 99999-9999", "Ben":"(13) 88888-8888", "Bob":"(75) 77777-7777", "Dan":"(97) 66666-6666"}

def telephone_list(tel_lis):
    print(f"Name ----------- Number:")
    for key, value in zip(tel_lis.keys(), tel_lis.values()): 
        print(f"{key} ---------- {value}")

def add_num():
    print("This number not exist Yet!")
    question = input("Do you want add a new contact?(y/n): ").lower()
    if question == "y":
        number = input("What's the number of this contact(format: (XX) XXXXX-XXXX)?: ")
        tel_lis.update({name:number})
    else:
        print("Okay!")
        return False


while is_running:
    telephone_list(tel_lis)
    name = input("What the name of people you want a number?(q to quit): ").capitalize()

    if name in tel_lis:
        print(tel_lis.get(name))
    elif name == "Q":
        is_running = False
    else:
        if type(add_num()) == bool:
            is_running = add_num()
        else:
            continue

