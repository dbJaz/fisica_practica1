import numpy as np  
import matplotlib.pyplot as plt
import pandas as pd
import OarmoArrays as ar
import OstandardDeviation as sd
from scipy import stats
from scipy.optimize import curve_fit


array=ar.data
masa=ar.data[3]
inc_masa=0.1
masa=np.delete(masa, -1)
inc_mc = inc_masa * 2 * masa
print("valor ")
print(inc_mc)
diametro=array[7]
inc_diametro=array[7][-1]
diametro=np.delete(diametro, -1)


# plt.figure(figsize=(4, 3))
# plt.errorbar(masa**2, diametro, yerr=inc_diametro, xerr=inc_mc,fmt='o',ms=3,ls='none',capsize=3,zorder=0)

ajuste = stats.linregress(masa**2, diametro)
# Accedo a los parámetros óptimos a traves de ajuste
print(f"Pendiente: {ajuste.slope:.2f} ± {ajuste.stderr:.2f}") #stderr devuelve el error de la pendiente
# :.2f para redondear a 2 decimales
print(f"Ordenada al origen: {ajuste.intercept:.2f} ± {ajuste.intercept_stderr:.2f}") # intercept_stderr
#devuelve el error de la ordenada

# Grafico los datos junto con la recta ajustada
# y_pred = ajuste.slope * masa**2 + ajuste.intercept # Predicción de recta
# plt.plot(masa**2, y_pred,c='r')

# curve_fit requiere como argumento la función que se quiere ajustar
def cuadratica(x,a,b): # x debe ser el primer argumento y después los parámetros a ajustar
    return a*np.log(x) + b

# usamos curve_fit
popt, pcov = curve_fit(f = cuadratica,  # la función que va a usar
                      xdata = masa,        # data en x
                      ydata = diametro,        # data en y
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
y_pred = cuadratica(masa,a,b)  # predicciones del modelo con los parámetros óptimos

plt.figure(figsize = (5,4))
plt.errorbar(masa**2, diametro, yerr=inc_diametro, xerr = inc_mc, fmt='o',ms=3,ls='none',capsize=3)
plt.plot(masa**2, y_pred,c='r')
plt.xlabel('Masa [g^2]')
plt.ylabel('Diametro [cm]')
plt.title('Diametro en función de la masa^2, hoja oficio'
'')
plt.show()