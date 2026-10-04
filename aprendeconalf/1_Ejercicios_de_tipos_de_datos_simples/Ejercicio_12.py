
print("~"*35)
print("Las barras de pan se venden a 3.49€")
print("~"*35)

price = 3.49
discount = 0.6  # 60%

stalebread = int(input("Ingrese el pan vendido que no esté fresco > "))

print("~"*35)
if stalebread == 1:
    print(f"Usted pidió solamente {stalebread} barra de pan")
elif stalebread >= 2:
    print(f"Usted pidió {stalebread} barras de pan")
else:
    print("Este valor es incorrecto")

Total = price * stalebread * (1 - discount)
print(f"El valor por una barra de pan fresca es de {price} €")
print("El descuento aplicado es del 60%")
print(f"El coste final a pagar es: {round(Total, 2)} €")
