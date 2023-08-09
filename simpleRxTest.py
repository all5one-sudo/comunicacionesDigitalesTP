# Se grafican los resultados obtenidos de transmitir con SDR Pluto a una frecuencia de 900 MHz
# y recibir con un RTL - SDR a diferentes distancias

import matplotlib.pyplot as plt

dist = [70,80,90,100,112,130]
peak = [-13.92,-18.92,-25.57,-29.07,-32.53,-40.09]

plt.plot(dist,peak)
plt.title('Relación distancia - pico de FFT')
plt.ylabel('Pico FFT [dB]')
plt.xlabel('Distancia al SDR [cm]')
plt.grid()
plt.show()