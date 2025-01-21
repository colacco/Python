# Rock, paper, scissor game

import random

options = ("rock", "paper", "scissor")
player = None
is_running = True

print("Let's play rock, paper scissor game!")
while is_running:
    pc = random.choice(options)
    player = input("What is your play (rock, paper or scissor)?").lower()
    if player not in options:
        print(f"The value {player} is invalid!")
    else:
        if player == pc:
            print("Draw!")
            print(f"You and computer select {pc}")
        elif pc == "rock" and player == "scissor" or pc == "paper" and player == "rock" or pc == "scissor" and player == "paper":
            print("You loose!")
            print(f"Computer choose {pc} and you choose {player}.")
        else:
            print("You win!")
            print(f"Computer choose {pc} and you choose {player}.")

    play = input("You wanna play again (y/n)?: ")
    if play == "n":
        is_running = False
    elif play is not "n":
        is_running = True

print("Ok, see you next time!")

# This is a second version.. In my first, I couldn't make the right way. I think this happen because I thought about the whole process... I see one time Bro Code and he starts from the basics. He don't thinks in the looping for now, but thinks about the essence of the thing.
# I couldn't make this project on my own, but this idea for now will be increnible for my next projects!