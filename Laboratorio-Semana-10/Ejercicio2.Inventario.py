#Ejercicio 2: Manejo de Inventario con Listas y Diccionarios

def mostrar_menu():
    print("\n--- Sistema de Inventario ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Buscar producto")
    print("4. Mostrar todos los productos")
    print("5. Salir")

def main():
    inventario = {}

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del producto: ")
            categoria = input("Ingrese la categoría del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            inventario[nombre] = {'categoria': categoria, 'precio': precio, 'cantidad': cantidad}
            print(f"Producto '{nombre}' agregado.")

        elif opcion == '2':
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            if nombre in inventario:
                del inventario[nombre]
                print(f"Producto '{nombre}' eliminado.")
            else:
                print(f"Producto '{nombre}' no encontrado.")

        elif opcion == '3':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            if nombre in inventario:
                producto = inventario[nombre]
                print(f"Producto encontrado: {nombre}, Categoría: {producto['categoria']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
            else:
                print(f"Producto '{nombre}' no encontrado.")

        elif opcion == '4':
            if not inventario:
                print("El inventario está vacío.")
            else:
                print("\n--- Productos en Inventario ---")
                for nombre, info in sorted(inventario.items(), key=lambda x: x[1]['precio']):
                    print(f"Nombre: {nombre}, Categoría: {info['categoria']}, Precio: {info['precio']}, Cantidad: {info['cantidad']}")

        elif opcion == '5':
            print("Saliendo del sistema de inventario.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

    