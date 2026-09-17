#=============
#values
deportistas = []
tiempos = []
amount_deportistas = 0
#=============


print("~"*40)#----------------------------
print("Bienvenido a Nuestro Sistema de Registro de Deportistas !")
print("~"*40)#----------------------------


def menu():  
    print("~"*30)
    print('''
Sus opciones son...
1. Registrar deportista
2. Mostrar deportistas
3. Buscar deportista
4. Mostrar mejor tiempo
5. Mostrar tiempo promedio
6. Salir''')
print("~"*30)


while  True:
    menu()
    opcion = int(input("\nIngrese su opcion > "))
    match opcion:
        
        case 1:
            print("Recuerde que tiene que ingresar el nombre y su tiempo obtenido\n")
            amount = int(input("Ingrese la cantidad de deportistas que desea ingresar  > "))

            for i in range(1,amount+1):
                amount_deportistas += 1
                temp_name = input("Ingrese el Primer Nombre y Primer Apellido  >")
                deportistas.append(temp_name)
                temp_time = float(input("Ingrese el tiempo en segundos  > "))
                tiempos.append(temp_time)

        case 2:
            if amount_deportistas == 0:
                print("No hay deportistas registrados")
            else:
                print("Los deportistas registrados son ...")
            for i in range(len(deportistas)):
                print(f"El deportista {deportistas[i]} y su mejor tiempo {tiempos[i]}")
                
        case 3:
            find_name = input("Ingrese el deportista que quiera buscar >")
            encontrado = "No se encontro el usuario"
            for i in range(len(deportistas)):
                if deportistas[i] == find_name:
                    encontrado = f"El deportista {deportistas[i]} y su mejor tiempo {tiempos[i]}"   
                    
            print(encontrado)
            
        case 4:
            mayor = tiempos[0]
            pos = 0
            for i in range(len(deportistas)):
                if tiempos[i] < mayor:
                    mayor = tiempos[i]
                    pos = i
            print(f"El deportista {deportistas[pos]} y su mejor tiempo {tiempos[pos]}")
            
        case 5 :
            suma = 0
            for i in range(len(deportistas)):
                suma += tiempos[i]
            print(f"Promedio = {suma / len(tiempos)}")
        case 6 :
            print("Decidio Salir vuelva pronto")
            break
        case _:
            print("spcion no valida")
