
list = []
numbers = int(input('''Ingrese la cantidad de los valores
    que desea guardar en la lista> '''))

for num in range(numbers):
    user_input = int(input("Ingresa el numero a la lista > " ))
    list.append(user_input)

print(f"Mayor > {max(list)}")
print(f"Menor > {min(list)}")


















