print("=======Cajero BancoCo=======")

# Leer saldo inicial (>= 0) con try/except
while True:
    cuenta = input("\nCuánto dinero tienes en la cuenta? ")
    try:
        cuenta = float(cuenta)
        if cuenta >= 0:
            break
        else:
            print("Error: el valor no puede ser negativo. Intenta de nuevo.")
    except ValueError:
        print("Error: debes ingresar solo números.")

while True:
    print("\n=======Elija una Opción=======")
    print("1. Consultar Saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")

    opc = input("Ingrese la Opción: ").strip()

    if opc == "1":
        print("\nSu saldo actual es de $", f"{cuenta:,.2f}")

    elif opc == "2":
      
        cantidad = input("\n======= ¿Cuánto dinero depositarás?: ")
        try:
            cantidad = float(cantidad)
            if cantidad >= 0:
                cuenta += cantidad
                print("Saldo depositado.")
                print(f"Saldo actual: ${cuenta:,.2f}")
            else:
                print("Error: cantidad no puede ser negativa.")
        except ValueError:
            print("Error: ingrese solo números.")

    elif opc == "3":
    
        cantidad = input("\n======= ¿Cuánto dinero retirarás?: ")
        try:
            cantidad = float(cantidad)
            if cantidad < 0:
                print("Error: la cantidad no puede ser negativa.")
            elif cantidad <= cuenta:
                cuenta -= cantidad
                print(f"Cantidad retirada: ${cantidad:,.2f}")
                print(f"Saldo actual: ${cuenta:,.2f}")
            else:
                print("No tienes fondos suficientes.")
        except ValueError:
            print("Error: ingrese solo números.")

    elif opc == "4":
        break

    else:
        print("Opción no válida. Intenta de nuevo.")