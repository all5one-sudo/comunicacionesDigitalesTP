import numpy as np
from rtlsdr import RtlSdr

# Configuración SDR
sdr = RtlSdr()
sdr.sample_rate = 2.4e6
sdr.center_freq = 98.9e6
sdr.gain = 'auto' # Ganancia en dB

# Se mide la intensidad para las muestras tomadass
samples = sdr.read_samples(256*1024)
power = np.abs(samples)**2              #Potencia de cada valor, promedio
power_db = 10*np.log10(np.mean(power))
print('Intensidad de campo electromagnético: %0.2f dBFS' % power_db)

# Se cierra el objeto sdr
sdr.close()

# Construir Soporte del Drone (3D) con SDR DE jupyter 