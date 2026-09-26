
array = []
amount = int(input("\nIngresa la cantidad de productos quedesea guardar en la lista >"))

for i in range(1,amount+1):
    temp = input(f"\nIngrese su{i} articulo ")
    array.append(temp)

print("\n Lista de compras > ")

count= 1

for j in array:
    print(f"{count}.{j}")
    count+=1
