# Calculadora segura en Python
while True:
    # --- Primer número ---
    while True:
        n1 = input("Ingresa el primer número: ")
        try:
            n1 = float(n1)     # convierte a número (acepta decimales)
            break              # si no hay error, sale del bucle
        except ValueError:
            print("⚠️ Error: debes ingresar solo números.")

    # --- Segundo número ---
    while True:
        n2 = input("Ingresa el segundo número: ")
        try:
            n2 = float(n2)
            break
        except ValueError:
            print("⚠️ Error: debes ingresar solo números.")

    # --- Operación ---
    print("\nOperaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Elige una opción (1-4): ")

    # --- Cálculos ---
    if opcion == "1":
        resultado = n1 + n2
        print(f"\n✅ Resultado: {n1} + {n2} = {resultado}")
    elif opcion == "2":
        resultado = n1 - n2
        print(f"\n✅ Resultado: {n1} - {n2} = {resultado}")
    elif opcion == "3":
        resultado = n1 * n2
        print(f"\n✅ Resultado: {n1} × {n2} = {resultado}")
    elif opcion == "4":
        if n2 != 0:
            resultado = n1 / n2
            print(f"\n✅ Resultado: {n1} ÷ {n2} = {resultado}")
        else:
            print("⚠️ Error: no se puede dividir entre 0.")
    else:
        print("⚠️ Opción no válida.")

    # --- Repetir o salir ---
    repetir = input("\n¿Deseas hacer otra operación? (s/n): ")
    if repetir.lower() != "s":
        print("👋 Gracias por usar la calculadora.")
        break
