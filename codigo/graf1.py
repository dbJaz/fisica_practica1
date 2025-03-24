import numpy as np  
import matplotlib.pyplot as plt
import pandas as pd
import armoArrays as ar
import standardDeviation as sd

np.random.seed(2) #hace que al repetir la ejecución obtenga los mismos resultados del vector aleatorio

# Parámetros de experimento
dt = 0.1 # Intervalo temporal de medición
T = 1 # tiempo final
N = int(T/dt) # Cantidad de puntos temporales
t = np.linspace(0, T, N) # vector de tiempos
inc_t = 0.05 # Incerteza por resolución instrumental en el tiempo
deltat = np.ones(N) * inc_t # Misma incerteza para todos los tiempos

g = - 9.81 # gravedad (m/s^2) negativa por elección de sist. ref.
H = 2 # altura inicial (m)

# Simulo el vector de alturas con ruido de distribución "Normal"
inc_pos = 0.1 # incerteza de altura (m)
y = H + g * 0.5 * t**2 + np.random.normal(0, inc_pos, len(t))
inc_y = np.ones(N) * inc_pos

plt.figure(figsize=(4, 3))
plt.errorbar(t , y ,
             yerr=inc_y, xerr = inc_t, # error en x y en y
             fmt='o',ms=3,ls='none',capsize=3,zorder=0)
plt.xlabel('Tiempo [s]')
plt.ylabel('Distancia [m]')