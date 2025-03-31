#Ejercicio 9: Implementación de Múltiples Paradigmas

# mainn.py

from biblioteca import Biblioteca
from libro import Libro

def mostrar_menu():
    print("\n--- Sistema de Gestión de Biblioteca ---")
    print("1. Agregar libro")
    print("2. Listar libros")
    print("3. Buscar libro")
    print("4. Salir")

def main():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            anio = input("Ingrese el año de publicación: ")
            libro = Libro(titulo, autor, anio)
            biblioteca.agregar_libro(libro)
            print("Libro agregado exitosamente.")

        elif opcion == '2':
            biblioteca.listar_libros()

        elif opcion == '3':
            titulo = input("Ingrese el título del libro a buscar: ")
            libro_encontrado = biblioteca.buscar_libro(titulo)
            if libro_encontrado:
                print(f"Libro encontrado: {libro_encontrado}")
            else:
                print("Libro no encontrado.")

        elif opcion == '4':
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()