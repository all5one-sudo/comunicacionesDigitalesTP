import serial
import pynmea2

# Configuración del puerto serie para la comunicación con el dispositivo GPS
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5.0)

# Lectura de datos de ubicación del dispositivo GPS
while True:
    line = ser.readline().decode('utf-8')
    if line.startswith('$GPGGA'):
        msg = pynmea2.parse(line)
        lat = msg.latitude
        lon = msg.longitude
        alt = msg.altitude
        print('Latitud:', lat)
        print('Longitud:', lon)
        print('Altitud:', alt)

# Cierre del puerto serie
ser.close()
