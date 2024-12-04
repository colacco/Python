# Python calculator

number1 = float(input("Enter a number: "))
number2 = float(input("Enter a number: "))
operator = input("What is the operator (+ - * /)?:")

if operator == "+":
    result = round(number1 + number2, 2)
    print(f"The sum between {number1} and {number2} equals to {result}.")

elif operator == "-":
    result = round(number1 - number2, 2)
    print(f"The subtraction between {number1} and {number2} equals to {result}.")

elif operator == "*":
    result = round(number1 * number2, 2)
    print(f"The multiplication between {number1} and {number2} equals to {result}")

elif operator == "/":
    result = round(number1 / number2, 2)
    print(f"The division between {number1} and {number2} equals to {result}")

else:
    print(f"{operator} is not an operator, please try again.")