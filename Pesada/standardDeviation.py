import numpy as np  
import matplotlib.pyplot as plt
import pandas as pd
import armoArrays as ar

# Error instrumental
err_inst = 0.01 # igual para todas las mediciones
# Contar el número de filas en el archivo pesada.csv
file_path = 'csv/Oficio.csv'
data = pd.read_csv(file_path)

arr1=ar.data[4]
arr2=ar.data[5]
arr3=ar.data[6]
std_arr=[]

for i in range (8):
    mediciones=[arr1[i],arr2[i],arr3[i]]
    N = len(mediciones) # cantidad de mediciones
    mean_med = np.mean(mediciones) # Valor medio de mediciones
    std_med = np.std(mediciones, ddof = 1) # Desvío estándar (std: standard deviation) de mediciones
    # ddof = 1 para que divida por N-1 en vez de N

    # Error estadístico
    err_est = std_med / np.sqrt(N) # Desvío estandar del promedio
    # Error total
    err = np.sqrt(err_inst**2 + err_est**2)

    std_arr =np.append(std_arr,err) 
print(std_arr)

stdl_arr=[]
for i in range (8):
    mediciones=[np.log(arr1[i]),np.log(arr2[i]),np.log(arr3[i])]
    N = len(mediciones) # cantidad de mediciones
    mean_med = np.mean(mediciones) # Valor medio de mediciones
    std_med = np.std(mediciones, ddof = 1) # Desvío estándar (std: standard deviation) de mediciones
    # ddof = 1 para que divida por N-1 en vez de N

    # Error estadístico
    err_est = std_med / np.sqrt(N) # Desvío estandar del promedio
    # Error total
    err = np.sqrt(err_inst**2 + err_est**2)

    stdl_arr =np.append(stdl_arr,err) 
print(std_arr)


