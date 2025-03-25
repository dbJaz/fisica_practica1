import numpy as np  
import matplotlib.pyplot as plt
import pandas as pd
import armoArrays as ar
import standardDeviation as sd
from scipy import stats


masa = ar.data[9]
inc_masa = ar.data[9][-1]
masa=np.delete(masa, -1)


area = ar.data[2]
inc_area = ar.data[2][-1]
area = np.delete(area, -1)

ajuste = stats.linregress(area, masa)

plt.figure(figsize=(5, 4))
plt.errorbar(area,masa,
             xerr=inc_area, yerr=inc_masa,
             fmt='o', ms=4, ls='none', capsize=3, zorder=0)

y_pred = ajuste.slope * area + ajuste.intercept # Predicción de recta
plt.plot(area, y_pred,c='r')

plt.xlabel("Área [cm^2]")
plt.ylabel("Masa [g]")
plt.title("Masa en funcion del área")
plt.show()
