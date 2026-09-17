
print(" PRECIOS PARA LA ENTRADA DE VIDEOJUEGOS\n")

print(" 4 años entran gratis\n")
print(" entre 4 y 18 años debe pagar 5€\n ")
print(" 18 años debe pagar 10€\n ")


edad = int(input("Porfavor ingrese su edad : "))

if edad <= 4:
    print("Perfecto tu entrada es gratis!\n")
elif edad <= 18:
    print("Tu entrada sale a 5€\n" )
else: 
    print("Su entrada vale 10€\n")