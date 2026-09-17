print("Bienvenido a tu cuenta de ahorros!")
print("Tenemos un interes anual del 4%")

rate = 0.04 # Tasa de interes al 4%
deposit = int(input("Cuanto dinero desea depositar:\n"))
time = 0

for i in range(0,3,1):
    time += 1
    profit = deposit * (rate + 1) ** time
    print(f"En: {time} años, tu dinero es de: {round(profit, 2)}")




