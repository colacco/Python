# Calc a circle area
import math

diameter = int(input("Digit the diameter: "))

radius = diameter * 2
area = round(math.pi * pow(radius, 2), 2)
circ = round(2 * math.pi * radius, 2)

print(f"This circle have {radius} of radius, aproximately {area} of area and {circ} of circumference")