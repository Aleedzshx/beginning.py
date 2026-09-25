
arr = [25,48,12,36,60,18,54]
# amount = int(input("\nIngresa la cantidad de números que desea ingresar > "))

# for i in range(1, amount+1):
#     temp = int(input(f"\nIngrese su {i} número a la lista > "))
#     arr.append(temp)

for i in range(len(arr)):
    for j in range(0, len(arr)-i-1):
        if arr[j] < arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

if len(arr) >= 2:
    print("El segundo número mayor es >", arr[1])
else:
    print("No hay suficientes números para determinar el segundo mayor")


