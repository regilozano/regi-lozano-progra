#Ejercicio 9: Implementación de Múltiples Paradigmas

# biblioteca.py

from libro import Libro

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def listar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
            return
        print("Libros en la biblioteca:")
        for libro in self.libros:
            print(libro)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None