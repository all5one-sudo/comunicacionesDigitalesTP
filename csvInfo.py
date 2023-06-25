# Este script se encarga de generar un archivo .csv y otro .xlsx que contengan las columnas solicitadas por el usuario.
# Para ello, se enumerarán por consola las diferentes posibles columnas, y se solicitará al usuario que separe 
# los números de columna por comas

# Se importa la librería necesaria Pandas
import pandas as pd

# Se lee el archivo .csv del Flight Record
csvFile = "flightRecord.csv"  
df = pd.read_csv(csvFile)

# Se enumeran las columnas presentes en el .csv a leer
columnas = df.columns
enumerateColumnas = {indice + 1: columna for indice, columna in enumerate(columnas)}

# Se imprimen las posibles columnas enumeradas
for indice, columna in enumerateColumnas.items():
    print(f"{indice}. {columna}")

# Se solicita al usuario las columnas que quiere extraer
columnasSeleccionadas = input('Ingresa los números de las columnas deseadas (separados por comas): ')
columnasSeleccionadas = [int(c) for c in columnasSeleccionadas.split(",")]

# Se crea un nuevo dataframe con los datos solicitados
dfSeleccionado = df[[enumerateColumnas[c] for c in columnasSeleccionadas]]

# Se convierte ese dataframe a un archivo .csv
csvSeleccionado = "extract.csv"  
dfSeleccionado.to_csv(csvSeleccionado, index=False)
print('Nuevo archivo .csv generado con éxito')

# Se convierte el dataframe a un archivo .xlsx
excelFile = "extract.xlsx"  
dfSeleccionado.to_excel(excelFile, index=False)
print('Nuevo archivo .xlsx generado con éxito')
