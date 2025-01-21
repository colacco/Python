# for loop = execute a block of code a fixed number of times.
#            You can iterate over a range, string, sequence, etc.

for x in range(1, 11, 3):
    print(x) 

# nested loop = A loop within another loop (outer, inner)

collumns = int(input("Enter a number of collumns: "))
rows = int(input("Enter a number of rows: "))
symbol = input("Write the symbol you want: ")

for x in range(collumns):
    for y in range(rows):
        print(symbol, end="")    
    print()