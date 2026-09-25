
Positivos = 0
Negativos = 0
Ceros = 0

enteros = int(input("Ingrese la cantidad de enteros > "))

for entero in range(enteros):
    valor = int(input(f"Ingrese el entero {entero + 1} > "))
    if valor < 0:
        Negativos += 1
    elif valor == 0:
        Ceros += 1
    else:
        Positivos += 1

print("Positivos:", Positivos)
print("Negativos:", Negativos)
print("Ceros:", Ceros)
