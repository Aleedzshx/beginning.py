
array = []

amount = int(input('''\nIngresa la cantidad de palabras
    de deseas ingresar > '''))

for i in range(1,amount+1):
    temp = input(f"\nIngrese su {i} palabra > ")
    array.append(temp)

print("Lista invertida")
for e in array[::-1]:
    print(e)
