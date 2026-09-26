
#ONE  - WAY
# seven_days = []


# for i in range(1, 8):
#     temp = int(input(f"Ingrese la temperatura del día {i}: "))
#     seven_days.append(temp)
    
# average_temp = sum(seven_days) / len(seven_days)

# print(f"La temperatura máxima es {max(seven_days)}°C")
# print(f"La temperatura mínima es {min(seven_days)}°C")
# print(f"La temperatura promedio es {average_temp:.2f}°C")
# print(f"Días por encima del promedio: {len([t for t in seven_days if t > average_temp])}")

#SECOND  - WAY
seven_days = []


for i in range(1, 8):
    temp = int(input(f"Ingrese la temperatura del día {i}: "))
    seven_days.append(temp)

max_temp = 0
min_temp = seven_days[0]
day_prom = 0

suma = 0
for i in seven_days:
    suma += i 

average_temp = suma / len(seven_days)

for j in seven_days:
    if j > max_temp:
        max_temp = j
    if j < min_temp:
        min_temp = j
    if j > average_temp:
        day_prom += 1

mayor = seven_days[0]
for k in seven_days:
    if k > mayor:
        mayor = k 

menor = seven_days[0]
for l in seven_days:
    if menor > l:
        menor = l

print(f"La temperatura máxima es {mayor}°C")
print(f"La temperatura mínima es {menor}°C")
print(f"La temperatura promedio es {average_temp:.2f}°C")
print(f"Dias por encima del promedio: {day_prom}")
