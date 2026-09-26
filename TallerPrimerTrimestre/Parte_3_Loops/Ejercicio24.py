
n = int(input("Ingrese un número natural > "))

multi = 1

for i in range(1, n + 1):
    multi *= i
print("El factorial de", n, "es", multi)
