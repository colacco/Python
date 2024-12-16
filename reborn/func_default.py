# default arguments = A default value for certain parameters
#                     defaultis used when that atgument is ommited
#                     make your functions more flexible, reduces # of arguments
#                     1. Positional, 2. DEFAULT, 3. Keyword, 4. Arbitrary

import time

def count(end, start=0):
    for x in range(start, end+1): # +1 is used because the counter stops one number earlier.
        print(x)
        time.sleep(1)
    print("Done!")

print("Let's count numbers!")  
end = input("Please enter a number:")

while not end.isnumeric():
    print("This is not a number, please, try again!")
    end = input("Please enter a number:")

count(int(end))