#Problema 10 
#Leer, escribir y modificar un archivo de texto.


def escribir_archivo (nombre, contenido): 
    with open(nombre, 'w', encoding='utf-8') as f :
        f.write(contenido)

def leer_archivo(nombre): 
    with open (nombre, 'r', encoding= 'utf-8') as f: 
        return f.read()
    
def modificar_archivo (nombre, buscar, reemplazar): 
    contenido = leer_archivo(nombre)
    contenido_modificado = contenido.replace (buscar, reemplazar)
    escribir_archivo(nombre, contenido_modificado)

if __name__ == '__main__': 
    archivo = 'archivo.txt'   

    contenido_inicial = "Hola todos\nEsta es la tarea."
    escribir_archivo(archivo,contenido_inicial)
    print("Contenido inicial:")
    print(leer_archivo(archivo))

    modificar_archivo(archivo,"todos","Python" )
    print("\nContenido modificado:")
    print(leer_archivo(archivo))