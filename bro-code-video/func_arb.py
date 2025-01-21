# *args    = allows you to pass multiple non-key arguments
# **kwargs = allow you to pass multiple keyword arguments
#            * unpacking operator
#            1. Positional, 2. DEFAULT, 3. Keyword, 4. Arbitrary

def add(*nums): # Create a tuple of arguments
    total = 0
    for num in nums:
        total += num
    return total

print(add(1, 10, 100, 1000, 10000))

def print_address(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "complemento" in kwargs:
        print(f"{kwargs.get('rua')} {kwargs.get('complemento')}")
    else:
        print(f"{kwargs.get('rua')}")
    print(f"{kwargs.get('cidade')} {kwargs.get('uf')} {kwargs.get('cep')}")

print_address("Sir", "Isaac", "Newton", rua='R. Calculiano Infinitesiano',complemento="", cidade="Santa Refração", uf="SP", cep="1999-999")