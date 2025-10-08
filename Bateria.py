print ("Cargando.... ") 

while True:
    bateria = input("Ingrese el nivel de bateria (0-100): ")
    try:
        bateria = int(bateria)
        if 0 <= bateria <= 100:
            break
        else:
            print("Error: el nivel de bateria debe estar entre 0 y 100.")
    except ValueError:
        print("Error: debe ingresar un número entero.")



if bateria >= 80:
        print("Bateria Alta")
        print ("\n0% [▄ ▄ ▄ ▄ ▄] 100%")
        
elif 60 <= bateria < 80:
        print("Bateria Media")
        print ("\n0% [▄ ▄ ▄ ▄  ] 100%")
        
elif 40 <= bateria < 60:
        print("Bateria Media baja")
        print ("\n0% [▄ ▄ ▄    ] 100%")  
        
elif 20 <= bateria < 40:
        print("Bateria Baja")
        print ("\n0% [▄ ▄      ] 100%")
        
elif 1 <= bateria < 20:
        print("Bateria Baja")
        print ("\n0% [▄        ] 100%")   
        
else:
        print("Error: el nivel de bateria debe estar entre 0 y 100.")
        bateria = input("Ingrese el nivel de bateria (0-100): ")
        try:
            bateria = int(bateria)
        except ValueError:
            print("Error: debe ingresar un número entero.")