
invest = float(input("Ingrese la cantidad de dinero a invertir: "))
annual_interest_rate = float(input("Ingrese la tasa de interés anual (en porcentaje): "))
years = int(input("Ingrese la cantidad de años a invertir: "))

for year in range(1, years + 1):
    invest += invest * (annual_interest_rate / 100)
    print(f"Año {year}: ${invest:.2f}")