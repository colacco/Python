# Quiz game

questions = ("What is the year of French Revolution?", "Who was the first president of EUA?", "How many eggs have in a dozen?", "Where is Berlin?")

options = (("A.1754", "B.1889", "C.1789", "D.1879"), ("A.George Washington", "B.Cristovao Colombo", "C.Joe Biden", "D.Freddy Mercury"), ("A.13", "B.12", "C.15", "D.6"), ("A.Russia", "B.United States", "C.Brazil", "D.Germany"))

answers = ("D", "A", "B", "D")

guesses = []
question_num = 0
score = 0

for question in questions:
    print("----------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Answer: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print(f"{answers[question_num]} is the correct answer!")

    question_num += 1

score = int(score/len(questions)*100)

print("-------------------------------------------")
print(f"Your final score is {score}%")

print("answer: ", end=" ")
for answer in answers:
    print(answer, end=" ")

print()
print("guesses:", end=" ")
for guess in guesses:
    print(guess, end=" ")