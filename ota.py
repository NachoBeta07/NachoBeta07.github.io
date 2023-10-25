# ota.py
import urequests
import ujson
import machine
from main import FIRMWARE_VERSION, UPDATE_URL
# # Configuración y variables globales
# firmware_version = 1.0  # Debe ser el mismo que está actualmente cargado en tu dispositivo
# update_info_url = 'http://mi-servidor.com/updateinfo.json'  # URL que contiene la información de la última versión

def update_script(new_script_url):
    """
    Función para actualizar el script de MicroPython.
    """
    print("Updating script from:", new_script_url)
    
    try:
        # Descargar el script
        response = urequests.get(new_script_url)
        if response.status_code == 200:
            # Sobrescribir el script actual
            with open('main.py', 'w') as file:
                file.write(response.text)
            print("Script updated, restarting...")
            machine.reset()
        else:
            print("Failed to download the update.")
    except Exception as e:
        print("Update error:", e)

def check_for_update():
    """
    Función para verificar la necesidad de una actualización y ejecutarla.
    """
    print("Checking for update...")
    current_version = FIRMWARE_VERSION
    update_url = UPDATE_URL
    
    try:
        # Obtener información de la versión más reciente
        response = urequests.get(update_url)
        if response.status_code == 200:
            update_info = response.json()
            latest_version = float(update_info['version'])  # Convierte el número de versión a float
            new_script_url = update_info['url']

            print("Current version:", current_version)
            print("Latest version:", latest_version)

            # Comprobar si la versión actual es antigua
            if latest_version != current_version:
                # Actualizar el script
                update_script(new_script_url)
            else:
                print("Already up to date.")
        else:
            print("Failed to retrieve update information.")
    except Exception as e:
        print("Error checking for update:", e)

# Puedes llamar a check_for_update() desde aquí si quieres que se ejecute cuando se importe este módulo,
# o podrías llamarlo desde otro lugar en tu código dependiendo de tus preferencias de flujo de trabajo.
if __name__ == '__main__':
    check_for_update()