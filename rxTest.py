import numpy as np
from rtlsdr import RtlSdr

# Configuración del RTL-SDR
sdr = RtlSdr()
sdr.sample_rate = 2.4e6  # Frecuencia de muestreo en Hz
sdr.center_freq = 500e6  # Frecuencia central en Hz
sdr.gain = 'auto'  # Ganancia automática

# Captura de muestras de la señal con RTL-SDR
muestras = sdr.read_samples(1024 * 10)  # Lee 10240 muestras (puedes ajustar este valor)

# Aplicar una transformada de Fourier (FFT) a las muestras
espectro = np.fft.fft(muestras)

# Calcular la densidad espectral de potencia
densidad_potencia = np.abs(espectro) ** 2 / len(muestras)

# Calcular la potencia promedio
potencia_promedio = np.mean(densidad_potencia)

print("Potencia promedio:", potencia_promedio)

# Liberar el RTL-SDR
sdr.close()
