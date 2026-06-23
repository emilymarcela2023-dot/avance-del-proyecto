#GENERADOR SEGURO DE CONTRASEÑAS
##AVANCES


import random
import string

contraseñas = []

while True:
    print("\n--- MENÚ ---")
    print("1. Generar contraseña")
    print("2. Evaluar contraseña")
    print("3. Guardar contraseña")
    print("4. Ver contraseñas")
    print("5. Salir")

    opcion = input("Seleccione opción: ")

    # GENERAR
    if opcion == "1":
        longitud = int(input("Ingrese longitud: "))
        caracteres = string.ascii_letters + string.digits

        contraseña = ""
        for i in range(longitud):   # FOR ✅
            contraseña += random.choice(caracteres)

        print("Contraseña:", contraseña)

    # EVALUAR
    elif opcion == "2":
        c = input("Ingrese contraseña: ")

        if len(c) >= 8:
            print("Contraseña fuerte")
        else:
            print("Contraseña débil")

    # GUARDAR
    elif opcion == "3":
        c = input("Ingrese contraseña a guardar: ")
        contraseñas.append(c)
        print("Guardada")

    # VER
    elif opcion == "4":
        print("Contraseñas guardadas:")
        for c in contraseñas:
            print(c)

    # SALIR
    elif opcion == "5":
        print("Fin del programa")
        break

    else:
        print("Opción incorrecta")
        
