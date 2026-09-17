
#=============
#values
stored_pin = 1909
user = "alee"
balance = 0
deposit = 0
attempts = 3
#=============
def menu():
    print("~"*30)
    print('''
    Sus opciones son...
    1. Consultar Saldo
    2. Depositar
    3. Retirar
    4. Salir''')
    print("~"*30)
    
    
print("~"*40)#----------------------------
print("Bienvenido a Nuestro App Bank Colombia!")
print("~"*40)#----------------------------


#Login
while True:
    login = int(input("\nIngrese su PIN: "))
    if login == stored_pin:
        print("\nAcceso concedido")
        break
    else:
        attempts -= 1
        print("\nPIN incorrecto, intente de nuevo")
        
        if attempts == 0:
            print("\nDemasiados intentos fallidos, accceso denegado")
            exit()
           
 #----------------------------

#----------------------------


while  True:
    menu()
    opcion = int(input("\nIngrese su opcion > "))
    match opcion:
        case 1:
            print(f"\nSu saldo actual es de {balance}$")
            menu()
        case 2:
            deposit = int(input("\nCuanto desea depositar a su cuenta > "))
            balance += deposit
            print(f"\nEn su cuenta tiene un total de {balance}")
            menu()
        case 3:
            res = int(input("\nCuanto desea retirar a su cuenta > "))
            if res > balance:
                print("\nNo tiene suficiente saldo para realizar esta operacion")
            else:
                balance -= res
                print(f"\nEn su cuenta tiene un total de {balance}")
        case 4:
            print("\nSaliendo del cajero Esperamos verte pronto")
            print("~"*30)
            break
        case _:
            print("\nOpcion invalida, intenta de nuevo")
            print("~"*30)

