# Gravity calculator

mass = float(input("What is the mass in Kg?: "))
planet = input("Choose one of this celestial body for calculate (sun, jupiter, mars, earth or moon): ")

if planet == "sun":
    result = mass * 273.42
elif planet == "jupiter":
    result = mass * 24.8
elif planet == "mars":
    result = mass * 3.72
elif planet == "earth":
    result = mass * 9.8
elif planet == "moon":
    result = mass * 1.67

print(f"In {planet} the gravity of that body equals to {round(result, 2)}m/s²")