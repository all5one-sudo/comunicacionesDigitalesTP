import matplotlib.pyplot as plt
import numpy as np
from rtlsdr import RtlSdr

# Configuración del RTL-SDR
sdr = RtlSdr()
sdr.sample_rate = 2.4e6
sdr.center_freq = 88.9e6
sdr.gain = 40

# Configuración del espectrograma
fig, ax = plt.subplots()
ax.set_title('Espectrograma en tiempo real')
ax.set_xlabel('Tiempo')
ax.set_ylabel('Frecuencia')
im = ax.imshow(np.zeros((512, 1024)), cmap='jet', origin='lower', aspect='auto')

# Función para actualizar el espectrograma en cada iteración
def update_spectrogram(samples):
    global im
    spec, _, _ = ax.specgram(samples, NFFT=512, Fs=sdr.sample_rate, noverlap=256, cmap='jet', mode='magnitude')[0:3]
    im.set_data(spec)
    return im,

# Bucle de adquisición de muestras y actualización del espectrograma
while True:
    samples = sdr.read_samples(1024 * 16)
    update_spectrogram(samples)
    plt.pause(0.01)

# Cierre del RTL-SDR
sdr.close()
