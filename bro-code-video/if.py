# if = Do some code only IF some condition is True
# ELSE do somtihing else

age = int(input("Enter your age: "))

if age >= 16:
    print("You can get your driver's licence!")
elif 0 > age:
    print("How can you answer if you don't born yet?")
else:
    print("You don't have age enough for your driver's licence")