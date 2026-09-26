
lista = []
amount = int(input('''\nIIngrese la cantidad de
    numero que desea guardar > '''))


for num in range(1,amount+1):
    temp = int(input(f"\nIngrese su {num} numero > "))
    lista.append(temp)

print(f"\nEstos son los numeros que guardaste en la lista {lista}")
find = int(input('''\nIngrese el numero que desea
    buscar en la lista  > '''))

if find in lista:
    print(f'''\nIEl numero {find} se encuentra
        en la posicion { lista.index(find) + 1}''')
else:
    print("\nIEste numero no se encuentra en la lista")
