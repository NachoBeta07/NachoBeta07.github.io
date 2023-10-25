import network

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Conectando a la red:', ssid)
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass  # puedes manejar el tiempo de espera o agregar una lógica de reintento
    print('Configuración de red:', wlan.ifconfig())

# reemplaza con tus datos de la red
connect_wifi('XTRIM VERA', 'Oe241298*')