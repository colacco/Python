# Hangman program

import random

options = ["python", "linux", "hardware", "kernel", "hacker"]
word = random.choice(options)
len_word = len(word)
count_letters = len(word)
is_running = True
chance = 5
user_word = []
answer = []

def main():
    print("Welcome to Hangman game!")
    print("Try to guess the word until the man die!")
    for x in range(len_word):
        print("_", end=" ")

def wrong_guess(chance):
    chance -= 1
    print("This letter is not in the word")
    print(f"You have more {chance} chance(s)")
    return chance


main()
while is_running:
    guess = input("What is your guess?: ")
    if len(guess) > 1 or not guess.isalpha() or guess in user_word or guess in answer: # Set if is a valid answer
        print("This is not a valid input, try again!")
    else:
        guess = guess.lower()
        if not guess in word: # Set if the letter is in the word
            user_word.append(guess)
            chance = wrong_guess(chance)
            if chance == 0: # Set the end of the game
                print("Oh no! You kill the man.")
                is_running = False
        else:
            answer.append(guess)
            count_letters -= word.count(f"{guess}")
            print(f"Correct! Letter {guess} is in the word")
            print(f"There are {count_letters} letters left.")

            if count_letters == 0:
                print("You won! You are so good in this game.")
                is_running = False

            for x in range(len_word):
                if word[x] in answer:
                    print(word[x], end=" ")
                else:
                    print("_", end=" ")
    print()