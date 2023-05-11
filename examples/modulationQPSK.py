import matplotlib.pyplot as plt
from rtlsdr import RtlSdr
import numpy as np

sdr = RtlSdr()

# Configuración del SDR
sdr.sample_rate = 2.4e6
sdr.center_freq = 100e6
sdr.gain = 50

# Lectura de muestras
samples = sdr.read_samples(256)

# Decodificación de la señal QPSK
bits = np.real(samples) > 0
bits = bits.astype(int)
bits = 2*bits - 1

# Conversión de los bits a símbolos QPSK
symb = np.zeros(len(bits)//2, dtype=complex)
symb.real = (bits[::2] + bits[1::2])/np.sqrt(2)
symb.imag = (bits[::2] - bits[1::2])/np.sqrt(2)

# Graficando la modulación
fig, axs = plt.subplots(2, 1)

axs[0].plot(symb.real)
axs[0].set_ylabel('Amplitud')
axs[0].set_title('Modulación QPSK')

axs[1].plot(np.angle(symb))
axs[1].set_ylabel('Fase')
axs[1].set_xlabel('Muestras')

plt.show()

sdr.close()
