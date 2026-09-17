


print('"Bank Colombia"')
print('"Tenemos un interes anual del 12,0%"')

Invest = int(input("Cuanto dinero deseas invertir:\n"))

time = float(input("Por cuanto años desea mantener su inversion?:\n"))

rate= float(input("Por cual interes anual esta interesado?:\n"))

final_amount = Invest * (1 + rate) ** time # Fórmula de interés compuesto: Monto = Capital * (1 + tasa) ^ tiempo


profit = f"{(final_amount - Invest):.2f}"
print(f"Tu ganancia seria de : {profit}")