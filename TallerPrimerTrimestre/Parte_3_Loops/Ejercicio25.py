
n = int(input('''Ingrese la cantidad de notas que
    quiera registrar   > '''))

nota = 0
promedio = 0
for i in range(n):
    nota += float(input(f"Ingrese la nota {i + 1} > "))
    promedio = nota / n
    print("El promediode las notas es:", promedio)