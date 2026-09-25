
list = [1,2,3,4,5,70]

int = int(input("Ingrese un número entero > "))
suma = 0
for i in range(1, int + 1):
    if i % 2 == 1:
        suma += i
print(f"La suma de los números impares es: {suma}")