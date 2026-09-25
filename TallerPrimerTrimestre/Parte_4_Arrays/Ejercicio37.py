
arr = []
amount = int(input("\nIngresa la cantidad de numeros que desea ingresar > "))

for i in range(1,amount+1):
    temp = int(input(f"\nIngrese su {i} numero a la lista> "))
    arr.append(temp)

for i in range(len(arr)):
    for j in range(0, len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            
print("Lista ordenada:", arr)