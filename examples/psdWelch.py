import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
from rtlsdr import RtlSdr

# Configuración del RTL-SDR
sdr = RtlSdr()
sdr.sample_rate = 2.4e6
sdr.center_freq = 100e6
sdr.gain = 'auto'

# Muestreo
samples = sdr.read_samples(1024 * 20) 

# Parámetros para la PWelch
fs = sdr.sample_rate
nperseg = 1024
noverlap = nperseg // 2

# Se calcula la PSD
f, Pxx = welch(samples, fs=fs, nperseg=nperseg, noverlap=noverlap)

# Gráfico
plt.figure()
plt.semilogy(f, Pxx)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Densidad espectral de potencia')
plt.title('PSD (pwelch)')
plt.grid(True)
plt.show()
