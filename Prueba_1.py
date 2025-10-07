while True:
    cuenta = input("\n¿Cuánto dinero tienes en la cuenta? ")

    try:
        cuenta = float(cuenta)   # Intentamos convertir a número

        if cuenta >= 0:          # Verificamos que sea mayor o igual a 0
            break                # Si cumple, salimos del bucle
        else:
            print("Error: el valor no puede ser negativo. Intenta de nuevo.")
            
    except ValueError:
        print("Error: debes ingresar solo números.")