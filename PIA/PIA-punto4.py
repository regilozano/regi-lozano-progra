import requests
import socket
import csv

# URL base de la API
API_BASE = "https://restcountries.com/v3.1/region/"

# Mapeo de nombres de continentes en español a los usados por la API
MAPEO_CONTINENTES = {
    "africa": "africa",
    "áfrica": "africa",
    "america": "americas",
    "américa": "americas",
    "antartida": "antarctic",
    "antártida": "antarctic",
    "asia": "asia",
    "europa": "europe",
    "oceania": "oceania",
    "oceanía": "oceania"
}

def verificar_conexion():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

def obtener_paises_por_continente(continente):
    continente_api = MAPEO_CONTINENTES.get(continente.lower())
    if not continente_api:
        return None

    url = f"{API_BASE}{continente_api}"
    try:
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException:
        return None

def limpiar_datos_paises(paises):
    datos_limpios = []
    for pais in paises:
        nombre = pais.get("name", {}).get("common", "Desconocido")
        capital = ", ".join(pais.get("capital", ["Sin capital"]))
        poblacion = pais.get("population", 0)
        poblacion_formateada = f"{poblacion:,}".replace(",", ".")
        idiomas = pais.get("languages", {})
        idioma_principal = list(idiomas.values())[0] if idiomas else "Desconocido"
        divisas = pais.get("currencies", {})
        if divisas:
            codigo_divisa = list(divisas.keys())[0]
            info_divisa = divisas[codigo_divisa]
            nombre_divisa = info_divisa.get("name", "Desconocida")
            divisa = f"{nombre_divisa} ({codigo_divisa})"
        else:
            divisa = "Desconocida"
        datos_limpios.append({
            "nombre": nombre,
            "capital": capital,
            "poblacion": poblacion_formateada,
            "idioma": idioma_principal,
            "divisa": divisa
        })
    return datos_limpios

def guardar_en_csv(nombre_archivo, datos):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        campos = ["nombre", "capital", "poblacion", "idioma", "divisa"]
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        for fila in datos:
            writer.writerow(fila)

def guardar_en_txt(nombre_archivo, datos):
    with open(nombre_archivo, mode='w', encoding='utf-8') as archivo:
        for i, pais in enumerate(datos, 1):
            archivo.write(f"{i}. {pais['nombre']}\n")
            archivo.write(f"   Capital   : {pais['capital']}\n")
            archivo.write(f"   Población : {pais['poblacion']}\n")
            archivo.write(f"   Idioma    : {pais['idioma']}\n")
            archivo.write(f"   Divisa    : {pais['divisa']}\n\n")

def mostrar_info_continente():
    if not verificar_conexion():
        print(" Error: No hay conexión a Internet.")
        print("Por favor, verifica tu conexión y vuelve a intentarlo.")
        return

    print("\n--- Explorador de Países por Continente ---")
    print("Continentes disponibles:")
    print("- África\n- América\n- Antártida\n- Asia\n- Europa\n- Oceanía")

    continente_usuario = input("\nIngresa el nombre de un continente: ").strip().lower()

    if continente_usuario not in MAPEO_CONTINENTES:
        print(f"\n '{continente_usuario}' no es un continente reconocido.")
        print("Prueba con: África, América, Asia, Europa, Oceanía o Antártida")
        return

    paises = obtener_paises_por_continente(continente_usuario)
    
    if paises:
        paises_limpios = limpiar_datos_paises(paises)
        print(f"\n En {continente_usuario.capitalize()} hay {len(paises_limpios)} países/territorios:")
        print("\n Lista con sus detalles:")

        for i, pais in enumerate(sorted(paises_limpios, key=lambda x: x['nombre']), 1):
            print(f"{i}. {pais['nombre']}")
            print(f"   Capital   : {pais['capital']}")
            print(f"   Población : {pais['poblacion']}")
            print(f"   Idioma    : {pais['idioma']}")
            print(f"   Divisa    : {pais['divisa']}\n")

        nombre_csv = f"{continente_usuario}_paises.csv"
        nombre_txt = f"{continente_usuario}_paises.txt"

        guardar_en_csv(nombre_csv, paises_limpios)
        guardar_en_txt(nombre_txt, paises_limpios)

        print(f"Datos guardados en los archivos: {nombre_csv} y {nombre_txt}")
    else:
        print(f"\n No se encontraron países para '{continente_usuario}' o el continente no existe.")
        print("Asegúrate de escribirlo correctamente.")

if __name__ == "__main__":
    mostrar_info_continente()

