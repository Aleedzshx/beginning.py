int_positivo = int(input("Ingrese un número positivo\n"))
int_impar = []

for int in range(1,int_positivo):
    if int % 2 == 1:
        int_impar.append(int)

print(int_impar)
