#Ejercicio 6: Sistema de Gestión de Vehículos

class Vehiculo:
    def __init__(self, marca, modelo, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def mostrar_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Precio: {self.precio}"

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, precio, numero_puertas):
        super().__init__(marca, modelo, anio, precio)
        self.numero_puertas = numero_puertas

    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        return f"{info_base}, Número de puertas: {self.numero_puertas}"

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, precio, cilindrada):
        super().__init__(marca, modelo, anio, precio)
        self.cilindrada = cilindrada

    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        return f"{info_base}, Cilindrada: {self.cilindrada} cc"

def main():
    # Crear instancias de Automovil y Motocicleta
    auto1 = Automovil("Toyota", "Corolla", 2020, 20000, 4)
    moto1 = Motocicleta("Yamaha", "MT-07", 2021, 7500, 689)

    # Mostrar información de los vehículos
    print(auto1.mostrar_informacion())
    print(moto1.mostrar_informacion())

if __name__ == "__main__":
    main()