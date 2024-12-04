# Building

numbers1 = ["1", "2", "3"]
numbers2 = ["4", "5", "6"]
numbers3 = ["7", "8", "9"]
addition = ["*", "0", "#"]

matrix = [numbers1, numbers2, numbers3, addition]

for rows in matrix:
    for num in rows:
        print(num, end=" ")
    print()