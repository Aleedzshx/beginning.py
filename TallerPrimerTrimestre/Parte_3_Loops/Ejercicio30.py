
serie0 = 0
serie1 = 1

Fibona = int(input('''\ncantidad de términos que
    desea generar de la serie de Fibonacci > '''))

for i in range(Fibona):
    print(serie0)
    temp = serie0 + serie1   # suma de los dos anteriores
    serie0 = serie1          # el siguiente número
    serie1 = temp     # actualiza el nuevo valor

