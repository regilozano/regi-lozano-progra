#Ejercicio 5: Módulo para Conversión de Unidades

# main.py

import conversor

def mostrar_menu():
    print("\n--- Conversor de Unidades ---")
    print("1. Kilómetros a Millas")
    print("2. Celsius a Fahrenheit")
    print("3. Litros a Galones")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            km = float(input("Ingrese la cantidad de kilómetros: "))
            millas = conversor.km_a_millas(km)
            print(f"{km} kilómetros son {millas:.2f} millas.")

        elif opcion == '2':
            celsius = float(input("Ingrese la temperatura en Celsius: "))
            fahrenheit = conversor.celsius_a_fahrenheit(celsius)
            print(f"{celsius} grados Celsius son {fahrenheit:.2f} grados Fahrenheit.")

        elif opcion == '3':
            litros = float(input("Ingrese la cantidad de litros: "))
            galones = conversor.litros_a_galones(litros)
            print(f"{litros} litros son {galones:.2f} galones.")

        elif opcion == '4':
            print("Saliendo del conversor.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()