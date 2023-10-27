import machine
import time
import _thread

# Asumiendo que tienes un módulo 'ota' con una función 'check_for_update'
# Si no es así, necesitarás definir la lógica de 'check_for_update' que se ajuste a tus necesidades
import ota

# Configuraciones
FIRMWARE_VERSION = 1.1  # Debe ser un float
UPDATE_URL = "https://nachobeta07.github.io/firmware_microPython.json"
LED_PIN = 18  # GPIO para el LED

# Estableciendo el LED
led = machine.Pin(LED_PIN, machine.Pin.OUT)

# Control para el bucle de parpadeo del LED
stop_blinking = False

def led_blinking_control():
    """
    Controla el parpadeo del LED. Si 'stop_blinking' es True, detiene el parpadeo.
    """
    global stop_blinking
    while not stop_blinking:
        led.value(not led.value())  # Cambia el estado del LED
        time.sleep(0.5)  # Parpadeo cada 0.5 segundos

def main():
    """
    Función principal para gestionar el parpadeo y las actualizaciones del firmware.
    """
    global stop_blinking

    # Iniciar el parpadeo del LED en un nuevo hilo
    _thread.start_new_thread(led_blinking_control, ())

    while True:
        # Verificar si hay actualizaciones disponibles
        update_available = ota.check_for_update()

        if update_available:
            print("Actualización disponible. Aplicando actualización...")
            stop_blinking = True  # Detener el parpadeo del LED
            # Aquí, podrías agregar lógica para aplicar la actualización, si es necesario.
            # Por ejemplo, podrías tener una función en tu módulo 'ota' que maneje el proceso de actualización.
            time.sleep(5)  # Simular tiempo para la actualización (elimina esta línea si aplicas la actualización)
            machine.reset()  # Reiniciar el dispositivo para aplicar la actualización
        else:
            print("No hay actualizaciones disponibles.")

        # Espera 60 segundos antes de la próxima verificación
        time.sleep(60)

# Ejecuta la función principal
if __name__ == '__main__':
    main()
