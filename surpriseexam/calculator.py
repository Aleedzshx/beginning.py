
def sum(a,b):
    return(a + b)

def res(a,b):
    return(a - b)

def mul(a,b):
    return(a * b)

def div(a,b):
    return(a/ b)
    
print("~"*30)  
a = int(input("\nIngrese su primer numero  > "))
b = int(input("\nIngrese su segundo numero > "))
    
while  True:
    print("~"*30)
    
    print(f'''
    Sus opciones son...
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir''')

    print("~"*30)

    opcion = int(input("\nIngrese su opcion > "))

    if opcion == 1:
        print(f"Su suma es {sum(a,b)}")
        break
    elif opcion == 2:
            print(f"Su resta es {res(a,b)}")
            break
    elif opcion == 3:
            print(f"Su multiplicacion es {mul(a,b)}")
            break
    elif opcion == 4:
            print(f"Su division es {div(a,b):.2f}")
            break
    elif opcion == 5:
            print("Usted decidio salir del programa...")
            break
    else:
        print("Esa opcion no existe, vuelve a intentarlo.....")



