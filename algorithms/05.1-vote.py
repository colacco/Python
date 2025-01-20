# I just fix some things, but this is an example of book.

voted = {"John", "Yasuo", "Zariel"}

def verifica_eleitor(name):
    if name in voted:
        print("Get out!")
    else:
        voted.add(name)
        print("Let vote!") 

verifica_eleitor("John")
verifica_eleitor("Caio")
verifica_eleitor("Jason")
verifica_eleitor("Zariel")
print(voted)