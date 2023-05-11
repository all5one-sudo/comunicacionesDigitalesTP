import numpy as np
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr
from scipy import signal

# Se crea el objeto SDR
sdr = RtlSdr()

# Configuración del SDR
sdr.sample_rate = 2.4e6
sdr.center_freq = 88.9e6
sdr.gain = 50

# Se realizan 256*1024 lecturas y se le calcula la PSD con Matplotlib
samples = sdr.read_samples(256*1024)
f, Pxx_den = signal.welch(samples, 10e2, nperseg=1024)
plt.semilogy(f, Pxx_den)
plt.ylim([0.5e-3, 1])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()

sdr.close()
