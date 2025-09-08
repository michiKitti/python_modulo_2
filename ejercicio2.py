"""Intérprete de Comandos Sencillo
Desarrolla un programa que simule un menú de consola usando la estructura match-case. El programa mostrará una lista de comandos disponibles ("guardar", "cargar", "salir") y el usuario ingresará uno
•	El programa debe ejecutar una acción simulada para cada comando (ej. imprimir "Guardando archivo...").
•	Si el comando no es válido, debe mostrar un mensaje de error.
•	El programa debe seguir pidiendo comandos hasta que el usuario escriba "salir".
"""
def interprete_comandos():
    print("=== Intérprete de Comandos ===")
    print("Comandos disponibles: guardar, cargar, salir")

    while True:
        comando = input("Ingresa un comando: ").lower()

        match comando:
            case "guardar":
                print("Guardando archivo...")
            case "cargar":
                print("Cargando archivo...")
            case "salir":
                print("Saliendo del programa. ¡Adiós!")
                break
            case _:
                print("Error: comando no reconocido. Intenta de nuevo.")

# Ejecutar el intérprete
interprete_comandos()
