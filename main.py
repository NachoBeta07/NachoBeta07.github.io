import machine
import time
import _thread
import ota  # Asegúrate de tener este módulo


# Constantes para la versión del firmware, la URL de actualización y el pin del LED
FIRMWARE_VERSION = 1.1  # Debe ser un float
UPDATE_URL = "https://nachobeta07.github.io/firmware_microPython.json"
LED_PIN = 17  # GPIO para el LED
# Estableciendo el LED
led = machine.Pin(LED_PIN, machine.Pin.OUT)

# Configuración inicial de los dispositivos/actuadores (por ejemplo, LED)
# NOTA: Los usuarios deben modificar estas líneas según sea necesario
pin_device = LED_PIN  # Usamos la constante LED_PIN para el pin GPIO del LED
device = machine.Pin(pin_device, machine.Pin.OUT)
def led_blinking_control():
    """
    Controla el parpadeo del LED. Si 'stop_blinking' es True, detiene el parpadeo.
    """
    global stop_blinking
    while not stop_blinking:
        led.value(not led.value())  # Cambia el estado del LED
        time.sleep(0.5)  # Parpadeo cada 0.5 segundos

def device_control_logic():
    """
    Lógica de control para dispositivos/actuadores (como LEDs, relés, etc.).

    Los usuarios deben modificar esta función según sus necesidades específicas.
    """
    global stop_blinking
    try:
        while True:
            # Iniciar el parpadeo del LED
            stop_blinking = False
            _thread.start_new_thread(led_blinking_control, ())

            # Esperar 5 segundos
            time.sleep(5)

            # Detener el parpadeo del LED
            stop_blinking = True
            time.sleep(0.5)  # Asegurarse de que el parpadeo se detenga antes de continuar

            # Apagar el LED
            led.value(False)
            time.sleep(1)  # Esperar 1 segundo
    except KeyboardInterrupt:
        stop_blinking = True  # Asegurarse de que el parpadeo se detenga antes de salir


def ota_update_check():
    """
    Lógica para verificar y aplicar actualizaciones OTA. 
    Esta función no debe ser modificada por los usuarios para asegurar la integridad de la actualización OTA.
    """
    while True:
        update_available = ota.check_for_update()
        if update_available:
            print("Actualización disponible. Aplicando actualización...")
            # Código para aplicar la actualización aquí
            time.sleep(5)  # Simulación del proceso de actualización
            machine.reset()  # Reiniciar el dispositivo para aplicar la actualización
        else:
            print("No hay actualizaciones disponibles.")
        time.sleep(60)

def main():
    """
    Función principal que inicializa los hilos y procesos necesarios.

    La estructura general de esta función no debe ser modificada por los usuarios.
    """
    # Iniciar la lógica de control del dispositivo en un nuevo hilo
    _thread.start_new_thread(device_control_logic, ())

    # La lógica de actualización OTA se ejecuta en el hilo principal
    ota_update_check()

# Punto de entrada del programa. No se recomienda modificar esta parte.
if __name__ == "__main__":
    main()
