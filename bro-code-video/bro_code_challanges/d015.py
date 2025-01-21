import random

number = random.randint(1, 100)
counter = 0
lowest_num = 1
highest_num = 100

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while True:
    guess = input("Enter your guess: ")
    counter += 1
    if guess.isdigit():
        guess = int(guess)
        if guess < lowest_num:
            print("Invalid number!")
            print(f"Please, select a number between {lowest_num} and {highest_num}")
        elif guess > highest_num:
            print("Invalid number!")
            print(f"Please, select a number between {lowest_num} and {highest_num}")
        elif guess > number:
            print("Too high! Try again")
        elif guess < number:
            print("Too low! Try again")
        else:
            break
    else:
        print(f"The answer {guess} is invalid!")
        print(f"Please, select a number between {lowest_num} and {highest_num}")
        continue

print(f"Congratulations! The number was {number}, you reach in this value in {counter} times.")

# A little difference between Bro code program, but it's good. In my first time i forgot to add limitation like add a 'str' value or add a number higher/lower than highest/lowest numbers. I'm proud of this, but I can make it better if I train more.