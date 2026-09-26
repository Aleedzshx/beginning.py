
amount = int(input("Ingrese la cantidad de numeros > "))
even_list = []
odd_list = []

for i in range(amount):
    num = int(input(f"Ingrese el numero {i+1} > "))
    if num % 2 == 0:
        even_list.append(num)
        break
    else:
        odd_list.append(num)

print(f"Numeros pares: {len(even_list)}")
print(f"Numeros impares: {len(odd_list)}")