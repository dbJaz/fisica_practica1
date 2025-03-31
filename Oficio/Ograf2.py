import numpy as np  
import matplotlib.pyplot as plt
import pandas as pd
import OarmoArrays as ar
import OstandardDeviation as sd
from scipy import stats
from scipy.optimize import curve_fit


array=ar.data
log_masa=ar.data[11]
inc_masa=0.05



log_diametro=array[10]
inc_diametro=sd.stdl_arr
inc_diametro= np.abs(inc_diametro)



# plt.figure(figsize=(4, 3))
# plt.errorbar(masa**2, diametro, yerr=inc_diametro, xerr=inc_mc,fmt='o',ms=3,ls='none',capsize=3,zorder=0)

# ajuste = stats.linregress(log_masa, log_diametro)
# # Accedo a los parámetros óptimos a traves de ajuste
# print(f"Pendiente: {ajuste.slope:.2f} ± {ajuste.stderr:.2f}") #stderr devuelve el error de la pendiente
# # :.2f para redondear a 2 decimales
# print(f"Ordenada al origen: {ajuste.intercept:.2f} ± {ajuste.intercept_stderr:.2f}") # intercept_stderr
# #devuelve el error de la ordenada

# Grafico los datos junto con la recta ajustada
# y_pred = ajuste.slope * masa**2 + ajuste.intercept # Predicción de recta
# plt.plot(masa**2, y_pred,c='r')

# curve_fit requiere como argumento la función que se quiere ajustar
def cuadratica(x,a,b): # x debe ser el primer argumento y después los parámetros a ajustar
    return a*(x) + b

# usamos curve_fit
popt, pcov = curve_fit(f = cuadratica,  # la función que va a usar
                      xdata = log_masa,        # data en x
                      ydata = log_diametro,        # data en y
                      sigma = inc_diametro,    # incertidumbre en y
                      p0 = (-5,6))      # estimación inicial de los parámetros a y b

# popt serán los parámetros óptimos
a, b = popt[0], popt[1]
# pcov es la matriz de covarianzas de la cual obtenemos las desviaciones

# estándar de los parámetros
perr = np.sqrt(np.diag(pcov)) # desviaciones estándar / incertidumbres de los parámetros a y b
inc_a, inc_b = perr[0], perr[1]

print(f"a: {a:.2f} ± {inc_a:.2f}")
print(f"b: {b:.2f} ± {inc_b:.2f}") # intercept_stderr

# Graficamos
y_pred = cuadratica(log_masa,a,b)  # predicciones del modelo con los parámetros óptimos

plt.figure(figsize = (5,4))
plt.errorbar(log_masa, log_diametro, yerr=inc_diametro, xerr = inc_masa, fmt='o',ms=3,ls='none',capsize=3)
plt.plot(log_masa, y_pred,c='r')
plt.xlabel('Log(masa) [g]')
plt.ylabel('Log(diametro) [cm]')
plt.title('Gráfico diametro y masa en escala logarítmica, hoja oficio'
'')
plt.show()