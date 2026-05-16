import os
import time
import webbrowser

# --- CONFIGURACIÓN DE COLORES VIBRANTES (ANSI) ---
AZUL_PROFUNDO = '\033[1;34m'
AZUL_NEON = '\033[1;94m'       # Nuevo color para tu nombre gigante, Martin
VERDE_NEON = '\033[1;92m'
MORADO = '\033[1;35m'
FUCSIA = '\033[1;95m'
BLANCO = '\033[1;37m'
ROJO = '\033[1;31m'
RESET = '\033[0m'

def limpiar_pantalla():
    os.system('clear' if os.name != 'nt' else 'cls')

def presentacion():
    limpiar_pantalla()
    # Tu nombre en letras grandes Azul Neón
    print(f"{AZUL_NEON}")
    print(" __  __    _    ____ _____ ___ _   _ ")
    print("|  \/  |  / \\  |  _ \\_   _|_ _| \\ | |")
    print("| |\\/| | / _ \\ | |_) || |  | ||  \\| |")
    print("| |  | |/ ___ \\|  _ < | |  | || |\\  |")
    print("|_|  |_/_/   \\_\\_| \\_\\_| |___|_| \\_|")
    print(f"{AZUL_PROFUNDO}=======================================")
    print(f"{VERDE_NEON}      MUSIC SEARCH & DOWNLOAD BY MARTIN")
    print(f"{AZUL_PROFUNDO}=======================================")
    print(f"{FUCSIA}[+] Descargador & Reproductor Activo - Termux")
    print(f"{BLANCO}Almacenamiento: Carpeta de Descargas (/Download)")
    print(f"{AZUL_PROFUNDO}======================================={RESET}\n")

def obtener_ruta_descarga():
    rutas = ["/sdcard/Download", "/storage/emulated/0/Download", os.getcwd()]
    for r in rutas:
        if os.path.exists(r) and os.access(r, os.W_OK):
            return r
    return os.getcwd()

def buscar_musica_web():
    presentacion()
    print(f"{FUCSIA}--- Buscador de Música en la Web ---{RESET}\n")
    cancion_buscar = input(f"{BLANCO}¿Qué canción o artista deseas buscar?, Martin: {RESET}").strip()
    
    if not cancion_buscar:
        print(f"{ROJO}[!] No escribiste nada.{RESET}")
        input("\nPresiona Enter para continuar...")
        return

    print(f"\n{MORADO}[*] Generando enlace de búsqueda para '{cancion_buscar}'...{RESET}")
    time.sleep(1)
    
    query_formateado = cancion_buscar.replace(" ", "+")
    url_busqueda = f"https://www.youtube.com/results?search_query={query_formateado}"
    
    print(f"\n{VERDE_NEON}[✓] ¡Enlace generado con éxito, Martin!{RESET}")
    print(f"{AZUL_PROFUNDO}---------------------------------------")
    print(f"{BLANCO}🔗 Enlace: {AZUL_NEON}{url_busqueda}{RESET}")
    print(f"{AZUL_PROFUNDO}---------------------------------------")
    input("\nPresiona Enter para regresar...")

def reproducir_musica_web():
    presentacion()
    print(f"{FUCSIA}--- Reproductor de Música Web ---{RESET}\n")
    cancion_reproducir = input(f"{BLANCO}¿Qué canción quieres reproducir?, Martin: {RESET}").strip()
    
    if not cancion_reproducir:
        print(f"{ROJO}[!] Campo vacío.{RESET}")
        input("\nPresiona Enter para continuar...")
        return

    print(f"\n{VERDE_NEON}[*] Conectando con el flujo de streaming...{RESET}")
    time.sleep(1)
    
    query_formateado = cancion_reproducir.replace(" ", "+")
    url_reproducir = f"https://www.youtube.com/results?search_query={query_formateado}"
    
    try:
        os.system(f"am start -a android.intent.action.VIEW -d '{url_reproducir}' > /dev/null 2>&1")
        webbrowser.open(url_reproducir)
    except Exception:
        webbrowser.open(url_reproducir)
        
    print(f"\n{VERDE_NEON}[✓] ¡Lanzando reproducción, Martin! 🎧{RESET}")
    input("\nPresiona Enter para regresar al menú...")

def descargar_musica_web():
    presentacion()
    print(f"{FUCSIA}--- Descargador MP3 Multimedia de Alta Calidad ---{RESET}\n")
    cancion_descargar = input(f"{BLANCO}Escribe el nombre o copia el link de la canción a descargar: {RESET}").strip()
    
    if not cancion_descargar:
        print(f"{ROJO}[!] No especificaste ninguna canción.{RESET}")
        input("\nPresiona Enter para continuar...")
        return
        
    ruta_salida = obtener_ruta_descarga()
    plantilla_guardado = os.path.join(ruta_salida, "%(title)s.%(ext)s")
    
    print(f"\n{MORADO}[*] Iniciando descarga para: {BLANCO}{cancion_descargar}{RESET}")
    print(f"{AZUL_PROFUNDO}[*] Buscando la mejor pista de audio disponible...{RESET}\n")
    
    if "http" in cancion_descargar:
        comando = f'yt-dlp -f "bestaudio/best" -x --audio-format mp3 -o "{plantilla_guardado}" "{cancion_descargar}"'
    else:
        comando = f'yt-dlp -f "bestaudio/best" -x --audio-format mp3 -o "{plantilla_guardado}" "ytsearch1:{cancion_descargar}"'
        
    resultado = os.system(comando)
    
    if resultado == 0:
        print(f"\n{VERDE_NEON}[✓] ¡Descarga exitosa, Martin!{RESET}")
        print(f"{BLANCO}Guardado en: {FUCSIA}{ruta_salida}{RESET}")
    else:
        print(f"\n{ROJO}[X] Ocurrió un error al descargar. Asegúrate de tener conexión a internet y tener 'yt-dlp' actualizado.{RESET}")
        print(f"{MORADO}[i] Si no lo tienes, puedes actualizarlo con: pip install --upgrade yt-dlp{RESET}")
        
    input("\nPresiona Enter para regresar al menú principal...")

def menu():
    while True:
        presentacion()
        print(f"{VERDE_NEON}1. {BLANCO}Buscar música en la Web")
        print(f"{VERDE_NEON}2. {BLANCO}Buscar y REPRODUCIR Audio")
        print(f"{VERDE_NEON}3. {FUCSIA}DESCARGAR canción en MP3")
        print(f"{VERDE_NEON}4. {ROJO}Salir")
        print(f"{AZUL_PROFUNDO}=======================================")
        
        opcion = input(f"{BLANCO}Selecciona una opción, Martin: {RESET}")
        
        if opcion == "1":
            buscar_musica_web()
        elif opcion == "2":
            reproducir_musica_web()
        elif opcion == "3":
            descargar_musica_web()
        elif opcion == "4":
            print(f"\n{FUCSIA}Cerrando el script. ¡Que tengas un gran día, Martin! ✨{RESET}")
            break
        else:
            print(f"\n{ROJO}[!] Opción incorrecta.{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    menu()
