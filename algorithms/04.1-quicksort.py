
def quicksort(arr):
    if len(arr) < 2: #Caso-base
        return arr
    else:
        pivo = arr[0] # Set pivo
        menores = [i for i in arr[1:] if i <= pivo] # Subarray 1
        maiores = [i for i in arr[1:] if i > pivo] # Subarray 2
        return quicksort(menores) + [pivo] + quicksort(maiores) # recursive
    
print(quicksort([0, 10, 5, 798, 540, 7824, 742, 854, 1000, 41, 32, 82, 18]))