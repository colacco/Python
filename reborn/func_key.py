# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. Positional, 2. DEFAULT, 3. Keyword, 4. Arbitrary

def get_phone(country, ddd, first, last):
    return f"+{country} {ddd} {first}-{last}."

for x in range(1, 11):
    print(x, end=" ")

print()
print("1", "2", "3", "", sep=" indiozinho(s) ")
# sep= = Insert beetween the values
# end= = Insert a string append after the value


isaac_newton_number = get_phone(last=8879, ddd=67, first=99875, country=55) # I know it's weird... But is for wisdom

print(f"Isaac Newton still alive! Your telephone number is: {isaac_newton_number}")

