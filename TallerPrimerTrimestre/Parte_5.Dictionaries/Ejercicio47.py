
arr = {}

best_sale = 0
best_saler = ""

amount = int(input("Ingrese la cantidad de vendedores que va guardar en el diccionario"))

for i in range(amount):
    name = input(f"Ingrese el nombre del {i+1} vendedor")
    sales = float(input(f"ingrese las ventas de {name}"))
    arr[name] = sales


for name , sale in arr.items():
    if best_sale < sale:
        best_sale = sale
        best_saler = name
print(f"El mejor vendedor fue {best_saler} con una venta de {best_sale}")

