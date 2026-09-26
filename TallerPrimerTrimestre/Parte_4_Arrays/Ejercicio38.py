

array1 = []
array2 = []

amount = int(input("\nIngresa la cantidad de numeros queque desea ingresar >"))

for i in range(1,amount+1):
    temp1= int(input(f"\nIngrese su {i} numero a la primera lista > "))
    array1.append(temp1)

    temp2= int(input(f"\nIngrese su {i} numero a la segunda lista > "))
for i in range(1,amount+1):
    array2.append(temp2)

print(f"Su lista combinada es igual a {array1+array2}")
