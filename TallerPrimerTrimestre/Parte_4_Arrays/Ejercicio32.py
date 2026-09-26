total = 0

grade = []
amount = int(input("Ingresa la cantidad de calificaciones > "))

for i in range(1,amount+1):
    vals = float(input(f"Ingrese su {i} calificacion > "))
    grade.append(vals)

for j in grade:
    total = total + j

print(f"\nSu promedio es {total/amount}")