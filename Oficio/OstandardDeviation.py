import numpy as np  
import matplotlib.pyplot as plt
import pandas as pd
import OarmoArrays as ar

# Error instrumental
err_inst = 0.01 # igual para todas las mediciones
# Contar el número de filas en el archivo pesada.csv
file_path = 'csv/Oficio.csv'
data = pd.read_csv(file_path)
num_rows = len(data)


#Ejemplo para mediciones de una magnitud arbitraria
mediciones = np.array([0.99, 0.75, 1.02, 1.38, 1.02, 1.18, 1.23, 1.17, 0.98, 1.27])
N = len(mediciones) # cantidad de mediciones

# Error instrumental
err_inst = 0.01 # igual para todas las mediciones

mean_med = np.mean(mediciones) # Valor medio de mediciones
std_med = np.std(mediciones, ddof = 1) # Desvío estándar (std: standard deviation) de mediciones
# ddof = 1 para que divida por N-1 en vez de N

# Error estadístico
err_est = std_med / np.sqrt(N) # Desvío estandar del promedio

# Error total
err = np.sqrt(err_inst**2 + err_est**2)

print(f"Valor reportado: {mean_med:.2f} ± {err:.2f}")




for i in range(10):
    mediciones = ar.data[i]
    N = len(mediciones) # cantidad de mediciones
    mean_med = np.mean(mediciones) # Valor medio de mediciones
    std_med = np.std(mediciones, ddof = 1) # Desvío estándar (std: standard deviation) de mediciones
    # ddof = 1 para que divida por N-1 en vez de N

    # Error estadístico
    err_est = std_med / np.sqrt(N) # Desvío estandar del promedio
    # Error total
    err = np.sqrt(err_inst**2 + err_est**2)

    ar.data[i][N-1]=err
    # print(ar.data[i])

