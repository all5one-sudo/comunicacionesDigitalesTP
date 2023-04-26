import numpy as np
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr

# Se crea el objeto SDR
sdr = RtlSdr()

# Configuración del SDR
sdr.sample_rate = 2.4e6
sdr.center_freq = 88.9e6
sdr.gain = 50

# Se realizan 256*1024 lecturas y se le calcula la PSD con Matplotlib
samples = sdr.read_samples(256*1024)
f, Pxx = plt.psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)

# Se grafica la PSD
plt.figure(figsize=(10, 5))
plt.plot(f, 10*np.log10(Pxx))
plt.xlabel('Frecuencia (MHz)')
plt.ylabel('PSD (dB/Hz)')
plt.show()

sdr.close()
