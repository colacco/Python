# Consegui fazer sozinho apenas o 4.2 e o Fibonacci
# 4.1 sum funtion with recursive:

def sum(lista):
    if lista == []:
        return 0
    
    return lista[0] + sum(lista[1:])

print(sum([2,4,6]))

# 4.2 count funtion with recursive:

def count(array):
    if array == []:
        return 0

    total = 1 + count(array[1:])
    return total

print(count([5, 5, 6, 204, 4, 1, 79, 704]))

# 4.3 max

def max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

    
    

print(max([5, 1080, 6, 204, 4, 1, 79, 704]))

# Extra: Fibonacci

def fibonacci(posicao):
    if posicao == 1:
        return 0
    elif posicao == 2:
        return 1
    
    return fibonacci(posicao - 1) + fibonacci(posicao - 2)

print(fibonacci(7))
# 1:0, 2:1, 3:1, 4:2, 5:3, 6:5, 7:8