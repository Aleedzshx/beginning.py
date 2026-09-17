# =============
deportistas = []
tiempos = []
amount_deportistas = 0
# =============

print("~" * 40)
print("Bienvenido a Nuestro Sistema de Registro de Deportistas !")
print("~" * 40)

def menu():
    print("~" * 30)
    print('''
    Sus opciones son...
    1. Registrar deportista
    2. Mostrar deportistas
    3. Buscar deportista
    4. Mostrar mejor tiempo
    5. Mostrar tiempo promedio
    6. Salir''')
    print("~" * 30)

while True:
    menu()

    opcion = int(input("Ingrese su opcion >\n "))

    match opcion:
        case 1:
            print("Recuerde que tiene que ingresar el nombre y su tiempo obtenido\n")
            amount = int(input("Ingrese la cantidad de deportistas que desea ingresar > "))
            for i in range(1, amount + 1):
                amount_deportistas += 1
                temp_name = input(f"Ingrese el Primer Nombre y Primer Apellido del deportista {i} > ")
                deportistas.append(temp_name)
                temp_time = float(input("Ingrese el tiempo en segundos > "))
                tiempos.append(temp_time)
                print(f"Se ingresaron {amount} deportista(s   ) a la lista... ")


        case 2:
            if amount_deportistas == 0:
                print("No hay deportistas registrados.\n")
            else:
                print("Los deportistas registrados son:\n")
                for i in range(len(deportistas)):
                    print(f"- El deportista {deportistas[i]} tiene un tiempo de {tiempos[i]}s")

        case 3:
            if amount_deportistas == 0:
                print("No hay deportistas registrados para buscar.\n")
            else:
                find_name = input("Ingrese el deportista que quiera buscar > ").strip().lower()
                encontrado = "No se encontró el usuario."
                for i in range(len(deportistas)):
                    if deportistas[i].lower() == find_name:
                        encontrado = f"El deportista {deportistas[i]} tiene un tiempo de {tiempos[i]}s"
                        break
                print(encontrado)

        case 4:
            if amount_deportistas == 0:
                print("No hay deportistas registrados.\n")
            else:
                mejor_tiempo = tiempos[0]
                pos = 0
                for i in range(len(tiempos)):
                    if tiempos[i] < mejor_tiempo:
                        mejor_tiempo = tiempos[i]
                        pos = i
                print(f"El mejor tiempo es de {deportistas[pos]} con {tiempos[pos]}s\n")
      
        case 5:
            if amount_deportistas == 0:
                print("No hay deportistas registrados para calcular el promedio.\n")
            else:
                promedio = sum(deportistas) / len(tiempos)
                print(f"Tiempo promedio del grupo = {promedio:.2f}s\n")

        case 6:
            print("Decidió salir. ¡Vuelva pronto!\n")
            print("~" * 40)
            break

        case _:
            print("Opción inválida. Por favor, intente de nuevo.\n")




     
