#while = execute some code WHILE condition reamians True

age = int(input("Enter your age: "))

while age < 0:
    print("Your age is invalid, please, try again")
    age = int(input("Enter your age: "))

if age < 16:
    print("You can't drive") 

elif age < 80:
    print("You are able to drive")

else:
    print("Caution! You reflexes are not so good, but you can drive yet.")