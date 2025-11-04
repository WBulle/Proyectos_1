empleado = {
    "nombre": "Walter",
    "edad": 25,
    "cargo": "Programador",
    "salario": 1200
}

# Acceder a datos específicos
print("Empleado:", empleado["nombre"])
print("Cargo:", empleado["cargo"])

# Modificar un valor
empleado["salario"] = 1300

# Agregar nuevo dato
empleado["departamento"] = "TI"

# Mostrar todo el diccionario
for clave, valor in empleado.items():
    print(clave, "=>", valor)