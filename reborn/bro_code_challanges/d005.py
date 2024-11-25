# Pythagoras Theorem
import math

b = int(input("What's the side b?: "))
a = int(input("What's the side a?: "))

c = round(math.sqrt(pow(a, 2) + pow(b, 2)), 2)

print(f"The side c have {c}")