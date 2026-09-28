

arr = { 101 : 2500000,
        102: 3200000,
        103: 2800000
}

# amount = int(input("\nIngrese la cantidad de empleados que va registrar  >"))

# for i in range(amount):
#     name = input(f"\nIngrese el codigo del empleado {i + 1}  >")
#     salary = float(input(f"\nIngrese el salario del empleado {i + 1}  >"))
#     arr[name] = salary

suma = 0
for i in arr.values():
    suma +=i


print("Salario promedio: " ,(suma/3))

