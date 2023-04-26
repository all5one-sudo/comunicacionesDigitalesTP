import geopandas as gpd
from shapely.geometry import Point
import numpy as np
import matplotlib.pyplot as plt

# Simular coordenadas GPS
n_points = 10000
lat = np.random.uniform(50.0, 51.0, n_points)
lon = np.random.uniform(-1.0, 1.0, n_points)

# Crear un GeoDataFrame con los datos simulados
geometry = [Point(xy) for xy in zip(lon, lat)]
df = gpd.GeoDataFrame({'intensidad': np.random.rand(n_points)}, geometry=geometry)

# Crear una figura y los ejes utilizando la función subplots de Matplotlib
fig, ax = plt.subplots(figsize=(10, 10))

# Crear un mapa de calor utilizando la función plot de GeoPandas
df.plot(column='intensidad', cmap='Reds', markersize=5, alpha=1, legend=True, 
        ax=ax, legend_kwds={'shrink': 0.5})

# Agregar un grid al mapa de calor
ax.grid(True, linestyle=':', linewidth=0.5, color='gray')

# Agregar etiquetas a los ejes
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')
ax.set_title('Mapa de Calor Intensidad de Campo Electromagnético')

# Mostrar el mapa de calor utilizando la función show de Matplotlib
plt.show()