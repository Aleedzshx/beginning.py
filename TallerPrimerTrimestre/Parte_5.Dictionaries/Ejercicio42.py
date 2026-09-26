
contacts = {}

amount = int(input("\n¿Cuántos contactos quieres registrar? > "))

for i in range(amount):
    name = input(f"\nNombre del contacto {i + 1} > ")
    phone = input(f"\nTeléfono del contacto {i + 1} > ")
    contacts[name] = phone

search = input("\nBuscar contacto > ")
if search in contacts:
    print(f"\n{search} -> {contacts[search]}")
else:
    print("\nNo se encontró el contacto")
