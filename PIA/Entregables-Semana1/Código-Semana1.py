#Script semana 1 - PIA

import requests
import socket

def verificar_conexion():
    #Aquí revisamos si hay internet
    try:
        # Intentar conectar al servidor de google
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        # Si no se pudo conectar no hay internet
        return False

def obtener_paises_por_continente(continente):
    #Esta función es como el buscador de países
    
    # Aquí corregir, traducir para hacer que sea lea la decision
    mapeo_continentes = {          #Todas las correcciones para validar que el sistema lea las entradas
        "antartida": "antarctic",  
        "antártida": "antarctic",  
        "america": "americas",     
        "américa": "americas"      
    }
    
    # Limpiar lo que escribió el usuario
    continente = mapeo_continentes.get(continente.lower(), continente.lower())
    
    # Armar la URL para la API
    url = f"https://restcountries.com/v3.1/region/{continente}"
    
    try:
        # Pedir los datos a la API
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()  # Checar que no haya errores
        return respuesta.json()  # Devuelve los países en formato JSON
    except requests.exceptions.RequestException:
        # Si algo sale mal, regresar nada
        return None

def mostrar_info_continente():
    #Esta es la función principal
    
    # Primero checar el internet (no vaya a ser que esté desconectado)
    if not verificar_conexion():
        print(" Error: No hay conexión a Internet.")
        print("Por favor, verifica tu conexión y vuelve a intentarlo.")
        return  # Salir de la función si no hay internet
    
    # Bonito título para que se vea profesional
    print("\n ---Explorador de Países por Continente--- ")
    print("Continentes disponibles:")
    print("- África\n- América\n- Antártida\n- Asia\n- Europa\n- Oceanía")
    
    # Pedir al usuario que elija un continente
    continente = input("\nIngresa el nombre de un continente: ").strip()
    
    # Obtener los países de ese continente
    paises = obtener_paises_por_continente(continente)
    
    if paises:
        # Si encontró países, mostrar bonito
        print(f"\n En {continente.capitalize()} hay {len(paises)} países/territorios:")
        
        print("\n Lista con sus capitales:")
        for i, pais in enumerate(paises, 1):
            nombre = pais['name']['common']  # Nombre común del país
            # Algunos países no tienen capital (como territorios), entonces poner "Sin capital"
            capital = ", ".join(pais.get('capital', ["Sin capital"]))
            print(f"{i}. {nombre}: {capital}")  # Mostrar numerado
        
        # Resumen final para que se vea completo
        print(f"\n Total: {len(paises)} entidades en {continente.capitalize()}")
    else:
        # Si no encontró nada, decir al usuario que pruebe otra cosa
        print(f"\n No se encontraron países para '{continente}' o el continente no existe.")
        print("Prueba con: África, América, Asia, Europa, Oceanía o Antártida")
if __name__ == "__main__":
    mostrar_info_continente()  # Llamar a la función principal