# Lista criada através do ChatGPT, utilizei 128 nomes aleatórios em ordem alfabética para replicar o conceito do livro em minha máquina
# Consegui replicar o código com êxito sem precisar olhar, porém pelo fato de não adicionar o "//" (que não está presente no exemplo do livro) sofri um pouco para descobrir o que era. Tive que recorrer ao chat para entender o que tinha ocorrido. 

minha_lista = ["Abigail", "Adam", "Adrian", "Aiden", "Albert", "Alex", "Alexa", "Alexander", "Alexandra", "Alice", "Alicia", "Allison", "Alyssa", "Amanda", "Amber", "Amy", "Andrea", "Andrew", "Angela", "Anna", "Anthony", "Ashley", "Austin", "Ava", "Barbara", "Benjamin", "Blake", "Brandon", "Brian", "Brianna", "Brittany", "Brooke", "Caleb", "Cameron", "Caroline", "Carter", "Catherine", "Charlotte", "Chloe", "Christian", "Christopher", "Claire", "Colin", "Connor", "Daniel", "David", "Derek", "Diana", "Dylan", "Edward", "Elizabeth", "Ella", "Emily", "Emma", "Eric", "Ethan", "Eva", "Evelyn", "Faith", "Fiona", "Gabriel", "Gavin", "Grace", "Hannah", "Harper", "Henry", "Isabella", "Isaiah", "Jack", "Jackson", "Jacob", "James", "Jasmine", "Jason", "Jayden", "Jennifer", "Jessica", "John", "Jonathan", "Jordan", "Joseph", "Joshua", "Julia", "Julian", "Justin", "Kaitlyn", "Katherine", "Kayla", "Kevin", "Kimberly", "Kyle", "Landon", "Lauren", "Layla", "Liam", "Logan", "Lucas", "Lucy", "Madeline", "Madison", "Marcus", "Maria", "Matthew", "Megan", "Michael", "Mia", "Nathan", "Nicholas", "Noah", "Oliver", "Olivia", "Owen", "Patrick", "Paul", "Rachel", "Rebecca", "Ryan", "Samantha", "Samuel", "Sarah", "Savannah", "Sophia", "Stephanie", "Steven", "Thomas", "Tyler", "Victoria", "William", "Zachary", "Zoe"]

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        elif chute < item:
            baixo = meio + 1
        else:
            alto = meio - 1

    return None


abby_loc = pesquisa_binaria(minha_lista, "Abigail")
mia_loc = pesquisa_binaria(minha_lista, "Mia")
pbi_loc = pesquisa_binaria(minha_lista, "Aprendi pesquisa binária")
print(f"O nome Abigail está na posição { int(abby_loc) + 1}")
print(f"O nome Mia está na posição { int(mia_loc) + 1}")
print(f"A pesquisa binária está na posição {pbi_loc}")