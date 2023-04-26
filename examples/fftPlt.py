import matplotlib.pyplot as plt
import numpy as np
from rtlsdr import RtlSdr

sdr = RtlSdr()

# Configuración del SDR
sdr.sample_rate = 2.4e6
sdr.center_freq = 95e6
sdr.gain = 50

# Lectura de muestras
samples = sdr.read_samples(256*1024)

# Calculo de la FFT
fft = np.fft.fft(samples)

# Grafico de la FFT
freq = np.fft.fftfreq(len(samples), 1/sdr.sample_rate)
plt.plot(freq/1e6, 20*np.log10(np.abs(fft)))
plt.xlabel('Frecuencia (MHz)')
plt.ylabel('Amplitud (dBFS)')
plt.show()

sdr.close()
