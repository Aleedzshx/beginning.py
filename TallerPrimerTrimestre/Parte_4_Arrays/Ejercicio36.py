
array = []
array_organized = []

amount = int(input("\nIngresa la cantidad de numeros queque desea ingresar >"))

for i in range(1,amount+1):
    temp = int(input(f"\nIngrese su {i} numero a la lista> "))
    array.append(temp)

for num in array:
    repetido = False
    for j in array_organized:
        if i == j:
            repetido = True
            break
    if not repetido:
        array_organized.append(i)

print(array_organized)
