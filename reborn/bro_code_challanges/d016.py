# Rock, paper, scissors game

import random

print("Let's play rock, paper , scissor game!")

while True:
    guess = input("What's your  play?(q to quit): ").lower()
    if guess == "scissor":
        print("you play a scissor!")
    elif guess == "rock":
        print("you play a rock!")
    elif guess == "paper":
        print("you play a paper!")
    else:
        print(f"The value {guess} is invalid, please try again!")