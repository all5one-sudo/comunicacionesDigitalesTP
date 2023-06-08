import numpy as np
from rtlsdr import RtlSdr
import pandas as pd
import time

# Configuración del SDR
sdr = RtlSdr()
sdr.sample_rate = 2.4e6
sdr.center_freq = 95e6
sdr.gain = 'auto'

# Lista para almacenar datos
data = []

# Duración en segundos
samplingTime = 60
# Define el intervalo entre muestras en segundos
samplingInterv = 2
# Calcula la cantidad total de muestras
samplesQuant = samplingTime // samplingInterv

# Toma muestras y almacena los datos en la lista
for _ in range(samplesQuant):
    # Obtiene el horario actual
    actualTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    
    # Captura las muestras
    samples = sdr.read_samples(256 * 1024)
    
    # Almacena los datos en la lista
    data.append((actualTime, samples))
    
    # Espera el intervalo de tiempo antes de tomar la siguiente muestra
    time.sleep(samplingInterv)

# Cierra el dispositivo SDR
sdr.close()

# Convierte la lista de datos en un DataFrame de pandas
df = pd.DataFrame(data, columns=['Horario', 'Muestras'])

# Muestra el DataFrame
print(df)
