
products = {}
amount = int(input("\n¿Cuántos productos quieres registrar? > "))

for i in range(amount):
    name = input(f"\nNombre del producto {i + 1} > ")
    quantity = float(input(f"\nCantidad de {name} > "))
    products[name] = quantity

search = input("\nBuscar producto > ")
if search in products:
    print(f"\n{search} -> {products[search]}")
else:
    print("\nNo se encontró el producto")
