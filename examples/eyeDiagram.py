import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import rtlsdr

# Configuración del SDR
sdr = rtlsdr.RtlSdr()
sdr.sample_rate = 2.4e6
sdr.center_freq = 100e6
sdr.gain = 'auto'

# Captura de la señal de muestra
samples = sdr.read_samples(256*1024)

# Resampling para trabajar con menos carga
downsampled = signal.resample(samples, len(samples)//10)

# Espectrograma de la señal
f, t, Sxx = signal.spectrogram(downsampled, fs=sdr.sample_rate/10, window='hamming', nperseg=1024, noverlap=512)

# Espectro de ojo
eye = np.abs(Sxx[:, int(len(t)/2)])
eye /= np.max(eye)

# Grafico
plt.plot(f, eye)
plt.title('Espectro de ojo')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud normalizada')
plt.show()

sdr.close()
