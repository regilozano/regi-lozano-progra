#Ejercicio 3: Gestión de Contactos con Tuplas y Estructuras Anidadas

def mostrar_menu():
    print("\n--- Gestor de Contactos ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto por nombre")
    print("3. Listar todos los contactos")
    print("4. Salir")

def main():
    agenda = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del contacto: ")
            numero = input("Ingrese el número del contacto: ")
            correo = input("Ingrese el correo del contacto: ")
            contacto = (nombre, numero, correo)
            agenda.append(contacto)
            print(f"Contacto '{nombre}' agregado.")

        elif opcion == '2':
            nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
            encontrado = False
            for contacto in agenda:
                if contacto[0].lower() == nombre_buscar.lower():
                    print(f"Contacto encontrado: Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")
                    encontrado = True
                    break
            if not encontrado:
                print(f"Contacto '{nombre_buscar}' no encontrado.")

        elif opcion == '3':
            if not agenda:
                print("La agenda está vacía.")
            else:
                print("\n--- Contactos en la Agenda ---")
                for contacto in sorted(agenda, key=lambda x: x[0].lower()):
                    print(f"Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")

        elif opcion == '4':
            print("Saliendo del gestor de contactos.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()