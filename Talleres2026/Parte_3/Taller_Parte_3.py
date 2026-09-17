


#TALLER_PYTHON_PARTE_3
# LOOPS

# Ejercicio 21
#
# n = int(input("Ingrese un número natural > "))

# suma = 0
# for n in range(1, n + 1):
#     suma+= n
# print("La suma de los primeros", n, "números naturales es", suma)



# Ejercicio 22
#
# n = int(input("Ingrese un número natural > "))
# i = 1

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         continue
#     print(i)


# Ejercicio 23

# n = int(input("Ingrese un número natural > "))
# for i in range(1, 11 ):
#     print(f"{i}x{n} = {i * n}")


# Ejercicio 24
#
# n = int(input("Ingrese un número natural > "))

# multi = 1

# for i in range(1, n + 1):
#     multi *= i
# print("El factorial de", n, "es", multi)
#


#Ejercicio 25
#
# n = int(input('''Ingrese la cantidad de notas que
#     quiera registrar   > '''))

# nota = 0
# promedio = 0
# for i in range(n):
#     nota += float(input(f"Ingrese la nota {i + 1} > "))
#     promedio = nota / n
#     print("El promediode las notas es:", promedio)


# Ejercicio 26
#
# Positivos = 0
# Negativos = 0
# Ceros = 0

# enteros = int(input("Ingrese la cantidad de enteros > "))

# for entero in range(enteros):
#     valor = int(input(f"Ingrese el entero {entero + 1} > "))
#     if valor < 0:
#         Negativos += 1
#     elif valor == 0:
#         Ceros += 1
#     else:
#         Positivos += 1

# print("Positivos:", Positivos)
# print("Negativos:", Negativos)
# print("Ceros:", Ceros)


#Ejercicio 27
#

# list = [1,2,3,4,5,70]

# int = int(input("Ingrese un número entero > "))
# for i in range(1, int + 1):
#     if i % 2 == 0:




# print("La suma de los primeros", int, "números impares", suma)


#Ejercicio 28
#
# vowels = "aeiou"
# vowel = 0
# word = input("Ingrese una palabra > ")

# for i in range(len(word)):
#     if word[i] in vowels:
#         vowel += 1

# print("La palabra ", word, "tiene ", vowel, "vocales")


# #Ejercicio 29
#
# int_positivo = int(input("Ingrese un número natural > "))
# if 2 > int_positivo:
#     print(f"El número {int_positivo} no es primo")
# else:
#     for i in range(2, int(int_positivo**0.5) + 1):
#         if int_positivo % i == 0:
#             print(f"El número {int_positivo} no es primo")
#             break
#     else:
#         print(f"El número {int_positivo} es primo")

#Ejercicio 30
#

 #Casos Base..
# serie0 = 0
# serie1 = 1

# Fibona = int(input('''\ncantidad de términos que
#     desea generar de la serie de Fibonacci > '''))

# for i in range(Fibona):
#     print(serie0)
#     temp = serie0 + serie1   # suma de los dos anteriores
#     serie0 = serie1          # el siguiente número
#     serie1 = temp     # actualiza el nuevo valor


