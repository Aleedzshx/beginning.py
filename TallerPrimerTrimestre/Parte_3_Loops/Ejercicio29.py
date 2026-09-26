
int_positivo = int(input("Ingrese un número natural > "))
if 2 > int_positivo:
    print(f"El número {int_positivo} no es primo")
else:
    for i in range(2, int(int_positivo**0.5) + 1):
        if int_positivo % i == 0:
            print(f"El número {int_positivo} no es primo")
            break
    else:
        print(f"El número {int_positivo} es primo")