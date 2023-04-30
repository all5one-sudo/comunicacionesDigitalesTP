import plotly.graph_objs as go
from rtlsdr import RtlSdr
import numpy as np

sdr = RtlSdr()

# Configuración del SDR
sdr.sample_rate = 2.4e6
sdr.center_freq = 88.9e6
sdr.gain = 10

# Lectura de muestras
samples = sdr.read_samples(1024)

# Calculo de la FFT
fft = np.fft.fft(samples)

# Graficando la FFT con Plotly
freq = np.fft.fftfreq(len(samples), 1/sdr.sample_rate)
fig = go.Figure(
    go.Scatter(x=freq/1e6, y=20*np.log10(np.abs(fft)))
)
fig.update_xaxes(title_text='Frecuencia (MHz)')
fig.update_yaxes(title_text='Amplitud (dBFS)')
fig.show()

sdr.close()
