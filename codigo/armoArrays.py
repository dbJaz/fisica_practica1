
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#ajuste y a aprtir de la pendiente usar ese valor para reportar el geramaje, es una mejor estimacion 

# Si guardé los datos en un Excel (o Google Sheets) y lo exporté como CSV (comma separated values):
fname = 'csv/Pesada.csv' #llenar nombre correspondiente
# Deben guardar el archivo localmente en la sesión de Colab

# La primera fila debería contener los nombres de las columnas, y el resto de filas debería contener valores numéricos
# genfromtxt transforma el archivo en un np.array
data = np.genfromtxt(fname,
                     delimiter=';',  # separador
                     skip_header=1)  # que ignore la primera fila

# si la línea de arriba tira error por formato pueden usar pandas que es más robusto
# Cambien los argumentos que sea necesario
df = pd.read_csv(fname,
                 skiprows = 1, #que ignore la primera fila
                 sep = ';',  # separados
                 decimal = '.',  # punto decimal ('.' o ',')
                 dtype = float)  # tipo de datos

# para convertirlo a np.array:
data = df.to_numpy()

print(data [0])