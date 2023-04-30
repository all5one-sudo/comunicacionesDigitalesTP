import matplotlib.pyplot as plt
import numpy as np
from rtlsdr import RtlSdr

sdr = RtlSdr()

# Configuración del SDR
sdr.sample_rate = 2.4e6
sdr.center_freq = 103.7e6
sdr.gain = 50

# Lectura de muestras
samples = sdr.read_samples(256*1024)

# Calculando el espectrograma
plt.specgram(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)

plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia (MHz)')
plt.show()

sdr.close()
