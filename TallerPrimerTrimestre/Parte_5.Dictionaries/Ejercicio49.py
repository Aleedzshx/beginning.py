
arr = {}

amount = int(input("\nIngrese la cantidad de empleados que va registrar  >"))

for i in range(amount):
    name = input(f"\nIngrese el codigo del empleado {i + 1}  >")
    salary = float(input(f"\nIngrese el salario del empleado {i + 1}  >"))
    arr[name] = salary

suma = 0
for i in arr.values():
    suma +=i


print("Salario promedio: " , round((suma/amount)))

