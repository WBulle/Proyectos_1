print("=======Cajero BancoCo=======")

while True:
        cuenta = input("\nCuanto dinero tienes en la cuenta? ")
        try:
            cuenta = float(cuenta)   
            break              
        except ValueError:
            print("Error: debes ingresar solo números.")


while True:

    
    print("\n=======Eliga una Opcion=======")
    print("1. Consultar Saldo")
    print("2. Depositar")
    print("3 Retirar")
    print("4. Salir")

    opc = ""

    if not opc:

        opc = input("Ingrese la Opcion: ")

        if opc == "1":
            print("\nSu saldo actual es de $", cuenta)

        elif opc == "2":
            cantidad = input("\n======= Cuanto dinero Depositara: ")
            cantidad = float(cantidad)
            cuenta += cantidad

        elif opc == "3":
            cantidad = input("\n=======Cuanto dinero retirara:  ")
            cantidad = float(cantidad)
            cuenta -= cantidad

        elif opc.lower() == "4":
            break

        else:
            print("Opcion no valida")
            break

       
