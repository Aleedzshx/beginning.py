pares = []

amount = int(input("Eliga cuaquier numero que desee: "))

for i in range (1,amount):
    if i % 2 == 0:
            pares.append(i)

print(pares)
        