#Ejercicio 9: Implementación de Múltiples Paradigmas

# libro.py

class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def __str__(self):
        return f"{self.titulo} por {self.autor} ({self.anio})"