import numpy as np
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr

sdr = RtlSdr()

# Configuración de la frecuencia y el ancho de banda
sdr.sample_rate = 2.4e6
sdr.center_freq = 100e6
sdr.freq_correction = 60
sdr.gain = 'auto'

# Muestreo y procesamiento de datos
samples = sdr.read_samples(256*1024)
spectrum = np.fft.fft(samples)
spectrum = np.abs(spectrum)

# Gráfico del espectro
plt.figure(figsize=(10, 5))
plt.plot(np.linspace(0, sdr.sample_rate/2, len(spectrum)//2), spectrum[:len(spectrum)//2])
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.show()

sdr.close()
