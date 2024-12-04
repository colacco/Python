# Countdown timer

import time

times = int(input("Enter a number: "))

for x in range(times, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600) % 24
    day = int(x / 86400) % 7
    weak = int(x / 604800)
    print(f"{weak} semana(s), {day} days and {hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Wait! They don't love you like I love you")