# Python compound interest calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter your principle amount: "))
    if principle <= 0:
        print("The principle must be a positive number. Please, try again.")
    else:
        break

while rate <= 0:
    rate = float(input("Enter a rate of your investiment (a.m.): "))
    if rate <= 0:
        print("The rate must be positive. Please, try again.")

while time <= 0:
    time = float(input("Enter the time of investiment (month): "))
    if time <= 0:
        print("The can't be retroced. Please try again!")

total = principle * (1 + rate / 100)**time
time = int(time)

print(f"The total amount you will have in {time} month(s) is {total:.2f}")