
arr = {}

amount = int(input("Ingrese la cantidad de libros que va registrar"))
for i in range(amount):
    id = input(f"Ingrese el codigo del libro {i+1}")
    arr[id] = int(input(f"Ingrese el titulo del libro {i+1}"))

find = input("Ingrese el codigo del libro que desea buscar")
if find in arr:
    print("\nLibro encontrado:")
    print(f"El libro con codigo {find} tiene titulo {arr[find]}")
else:
    print("\nLibro No encontrado:")
    print(f"El libro con codigo {find} no se encuentra en el diccionario")
