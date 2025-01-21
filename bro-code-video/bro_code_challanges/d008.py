# validate user input exercise
# 1. username is no more than 12 characters 
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username:")

validate = username.isalpha()
count = len(username)


if validate and count < 13:
    print("Seu nome é válido")

elif not validate and not count < 13:
    print("Seu nome deve conter apenas letras do alfabeto e no máximo 12 caracteres")

elif not count < 13:
    print("Seu nome deve conter no máximo 12 letras")

else: 
    print("Seu nome deve conter apenas letras do alfabeto")