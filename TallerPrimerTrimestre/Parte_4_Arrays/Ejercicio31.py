#ARRAYS
#Ejercicio 31
#

# list = []
# numbers = int(input('''Ingrese la cantidad de los valores
#     que desea guardar en la lista> '''))

# for num in range(numbers):
#     user_input = int(input("Ingresa el numero a la lista > " ))
#     list.append(user_input)

# print(f"Mayor > {max(list)}")
# print(f"Menor > {min(list)}")

#Ejercicio 32
#
# total = 0

# grade = []
# amount = int(input("Ingresa la cantidad de calificaciones > "))

# for i in range(1,amount+1):
#     vals = float(input(f"Ingrese su {i} calificacion > "))
#     grade.append(vals)

# for j in grade:
#     total = total + j

# print(f"\nSu promedio es {total/amount}")

#Ejercicio 33
#
# amount = int(input("Ingrese la cantidad de numeros > "))
# even_list = []
# odd_list = []

# for i in range(amount):
#     num = int(input(f"Ingrese el numero {i+1} > "))
#     if num % 2 == 0:
#         even_list.append(num)
#         break
#     else:
#         odd_list.append(num)

# print(f"Numeros pares: {len(even_list)}")
# print(f"Numeros impares: {len(odd_list)}")
#
# Ejercicio 34
#


# lista = []
# amount = int(input('''\nIIngrese la cantidad de
#     numero que desea guardar > '''))


# for num in range(1,amount+1):
#     temp = int(input(f"\nIngrese su {num} numero > "))
#     lista.append(temp)

# print(f"\nEstos son los numeros que guardaste en la lista {lista}")
# find = int(input('''\nIngrese el numero que desea
#     buscar en la lista  > '''))

# if find in lista:
#     print(f'''\nIEl numero {find} se encuentra
#         en la posicion { lista.index(find) + 1}''')
# else:
#     print("\nIEste numero no se encuentra en la lista")

#Ejercicio 35
#
#
# array = []
# amount = int(input('''\nIngresa la cantidad de palabras
#     de deseas ingresar > '''))

# for i in range(1,amount+1):
#     temp = input(f"\nIngrese su {i} palabra > ")
#     array.append(temp)

# print(f'''\nLista invertida >
# ''')
# array.reverse()
# print(array)


# Ejercicio 36
#
# array = []
# amount = int(input('''\nIngresa la cantidad de numeros que
#    que desea ingresar > '''))

# for i in range(1,amount+1):
#     temp = int(input(f"\nIngrese su {i} numero a la lista> "))
#     array.append(temp)

# print(set(array))

#Ejercicio 37
#
# array = []
# amount = int(input('''\nIngresa la cantidad de numeros que
#    que desea ingresar > '''))

# for i in range(1,amount+1):
#     temp = int(input(f"\nIngrese su {i} numero a la lista> "))
#     array.append(temp)

# new_arr = sorted(array)

# print(f" Lista ordenada > {new_arr}")


#Ejercicio 38
#
# array1 = []
# array2 = []

# amount = int(input('''\nIngresa la cantidad de numeros que
#    que desea ingresar > '''))

# for i in range(1,amount+1):
#     temp1= int(input(f"\nIngrese su {i} numero a la primera lista > "))
#     array1.append(temp1)

#     temp2= int(input(f"\nIngrese su {i} numero a la segunda lista > "))
# for i in range(1,amount+1):
#     array2.append(temp2)

# print(f"Su lista combinada es igual a {array1+array2}")


#Ejercicio 39
#


# lista = []
# amount = int(input("\nIngresa la cantidad de números que desea ingresar > "))

# for i in range(1, amount+1):
#     temp = int(input(f"\nIngrese su {i} número a la lista > "))
#     lista.append(temp)

# # Ordenamos la lista de mayor a menor
# lista.sort(reverse=True)

# # Mostramos el segundo número mayor
# if len(lista) >= 2:
#     print("El segundo número mayor es >", lista[1])
# else:
#     print("No hay suficientes números para determinar el segundo mayor")



#Ejercicio 40
#
# array = []
# amount = int(input('''\nIngresa la cantidad de productos que
#    desea guardar en la lista > '''))

# for i in range(1,amount+1):
#     temp = input(f"\nIngrese su{i} articulo ")
#     array.append(temp)

# print("\n Lista de compras > ")

# count= 1

# for j in array:
#     print(f"{count}.{j}")
#     count+=1
