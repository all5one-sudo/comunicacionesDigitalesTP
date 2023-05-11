import matplotlib.pyplot as plt
from rtlsdr import RtlSdr
import numpy as np

sdr = RtlSdr()

# Configuración del SDR
sdr.sample_rate = 2.4e6
sdr.center_freq = 100e6
sdr.gain = 50

# Muestreo
samples = sdr.read_samples(256*1024)

# Se decodifica la señal BPSK
bits = np.real(samples) > 0
bits = bits.astype(int)
bits = 2*bits - 1

# Conversión de los bits a símbolos BPSK
symb = np.zeros(len(bits)//2, dtype=complex)
symb.real = bits[::2]
symb.imag = bits[1::2]

# Graficando el diagrama de constelaciones
plt.scatter(symb.real, symb.imag)
plt.xlabel('I')
plt.ylabel('Q')
plt.title('Diagrama de constelaciones BPSK')
plt.show()

sdr.close()
