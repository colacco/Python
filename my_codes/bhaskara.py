

import math
is_running = True
a = 0
b = 0
c = 0

# FUNCTIONS

def main(a, b, c):
    print("Transform your quadratic equation in its standard form as ax² + bx + c = 0")
    a = input("Enter a value for A: ")
    b = input("Enter a value for B: ")
    c = input("Enter a value for C: ")
    return a, b, c

def delta(a, b, c): 
    delta = b**2  - 4 * a * c
    return delta

def bhaskara(a, b, c):
    solution = {}

    if delta(a, b, c) > 0:
        print("Have two real roots")
        solution[0] = (-b + math.sqrt(delta(a, b, c))) / 2 / a
        solution[1] = (-b - math.sqrt(delta(a, b, c))) / 2 / a
        return solution
    
    elif delta(a, b, c) == 0:
        print("Have one real root")
        solution = (-b + math.sqrt(delta(a, b, c))) / 2 / a
        return solution
    
    else:
        return print("There's no real root for this problem.")

def vertex(a,b,c):
    x_vertex = -b / 2 / a
    y_vertex = -1 * delta(a, b, c) / 4 / a
    return x_vertex, y_vertex

# Program

while is_running:
    a, b, c = main(a, b, c)
    print(b.isdigit)
    if a.isdigit and b.isdigit and c.isdigit:
        a, b, c = float(a), float(b), float(c)
        print(bhaskara(a, b, c))
        print(vertex(a, b, c))
    else:
        print("That's not a valid number.")