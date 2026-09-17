#Dictionaries
#
#Ejercicio 41

# students = {}
# amount = int(input("\n¿Cuántos estudiantes quieres registrar? > "))

# for i in range(amount):
#     id = int(input(f"\nCodigo del estudiante {i + 1} > "))
#     name = input(f"\nNombre del estudiante {i + 1} > ")
#     students[id] = name

# print("Listado de estudiantes")
# for i in students:
#     print(f"\n{i} -> {students[i]}")


#Ejercicio 42
#
# contacts = {}

# amount = int(input("\n¿Cuántos contactos quieres registrar? > "))

# for i in range(amount):
#     name = input(f"\nNombre del contacto {i + 1} > ")
#     phone = input(f"\nTeléfono del contacto {i + 1} > ")
#     contacts[name] = phone

# search = input("\nBuscar contacto > ")
# if search in contacts:
#     print(f"\n{search} -> {contacts[search]}")
# else:
#     print("\nNo se encontró el contacto")


#Ejercicio 43
#
# products = {}
# amount = int(input("\n¿Cuántos productos quieres registrar? > "))

# for i in range(amount):
#     name = input(f"\nNombre del producto {i + 1} > ")
#     quantity = float(input(f"\nCantidad de {name} > "))
#     products[name] = quantity

# search = input("\nBuscar producto > ")
# if search in products:
#     print(f"\n{search} -> {products[search]}")
# else:
#     print("\nNo se encontró el producto")


#Ejercicio 44
#
# bypieces = {}

# phrase = input("\nIngresa una frase > ").lower()

# words = phrase.split()
# for word in words:
#     if word in bypieces:
#         bypieces[word] += 1
#     else:
#         bypieces[word] = 1
# print("\nContador de palabras")
# for word in bypieces:
#     print(f"\n{word} -> {bypieces[word]}")

#Ejercicio 45
# 
# count = {}

# word = input("\nIngresa una palabra > ")
# for letter in word:
#     if letter in count:
#         count[letter] += 1
#     else:
#         count[letter] = 1

# print("\nContador de letras")
# for letter in count:
#     print(f"\n{letter} -> {count[letter]}")


#Ejercicio 46
#
# students = {}
# amount = int(input("\n¿Cuántos estudiantes quieres registrar? > "))

# for i in range(amount):
#     name = (input(f"\nPrimer nombre del {i + 1} estudiante  > "))
#     grade = float(input(f"\nNotas de {name} > "))
#     students[name] = grade

# best_student = max(students, key=students.get)
# print(f"La mejor nota fue del estudiante {best_student} -> {students[best_student]}")

#Ejercicio 47
# 
