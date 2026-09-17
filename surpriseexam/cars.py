
# ==================================
# Values
plate_number= []
brand = []
model_year = []
amount_cars = 0
# ==================================


def menu():
    print("============== MENÚ ==============")
    print('''
    -1. Registrar vehículo
    -2. Mostrar vehículos
    -3. Buscar vehículo
    -4. Mostrar vehículo más antiguo
    -5. Mostrar año promedio de fabricación
    -6. Salir 
        ''')
    print("="*40)

while True:
    menu()

    option = int(input("Ingrese la opcion\n"))

    match option:
        case 1:
            amount = int(input("Cuantos registros va realizar >\n"))

            for i in range(1,amount+1):
                plate = (input(f"Ingrese el numero de placa del {i}º  vehículo  \n"))
                car_brand = (input("Ingrese la marca \n"))
                year_model = int(input("Ingrese el modelo\n "))
                plate_number.append(plate)
                brand.append(car_brand)
                model_year.append(year_model)
                amount_cars += 1

            print("Se registro correctamente ! ")

        case 2 :
           if amount_cars == 0:
               print("No hay vehículos registrados...\n")
               break
           else:
                print("="*40)
                print("Los vehículos son los siguientes...\n ")
                for i in range(len(plate_number)):
                     print(f"-El vehículo con placa {plate_number[i]}, de marca {brand[i]} , modelo {model_year[i]}\n ")

        case 3 :
            if amount_cars == 0:
                print("No hay vehículos registrados...\n")
                break
            else:
                find_car = input("Ingrese la placa de su vehiculo > ")
            for i in range(len(plate_number)):
                if find_car == plate_number[i]:
                    find = f"La placa {find_car} , modelo {model_year[i]} , marca {brand[i]}"
                    print(find)
                else:
                    print("No se encontró el vehículo...\n")
            
        case 4 :
            if amount_cars == 0:
                print("No hay vehículos registrados...\n")
                break
            else:
                antiques = model_year[0]
                for i in range(len(plate_number)):
                    if antiques > model_year[i]:
                        antiques = model_year[i]
                print(f"El vehículo más antiguo es de {antiques}")
            
        case 5 :
            if amount_cars == 0:
                print("No hay vehículos registrados...\n")
                break
                suma = 0 
                for i in year_model:
                    suma+= i
                    print(f"El promedio de los años de los vehículos es {suma / len(plate_number)}")
                
            # print(f"El promedio de los años de los vehículos es {sum(model_year) / len(plate_number)}")

        case 6 :
            print("Saliendo...")
            break

        case _ :
            print("Opción no válida...")
