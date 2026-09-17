days = []

amount = int(input("Ingrese la cantidad de dias que desea ingresar > "))

for i in range(1,amount+1):
    temp = int(input(f"Ingrese la venta del día {i}: "))
    days.append(temp)

max_temp = 0
min_temp = days[0]
day_prom = 0
average_temp = sum(days) / len(days)

for j in days:
    if j > max_temp:
        max_temp = j
    if j < min_temp:
        min_temp = j
    if j > average_temp:
        day_prom += 1

print(f"La venta máxima es ${max_temp}")
print(f"La venta mínima es ${min_temp}")
print(f"La venta promedio es ${average_temp:.2f}")
print(f"El total vendido es ${sum(days)}")
print(f"Cantidad de días en los que las ventas fueron superiores al promedio: {day_prom}")
