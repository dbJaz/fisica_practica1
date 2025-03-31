import numpy as np  
import matplotlib.pyplot as plt
import pandas as pd
import OarmoArrays as ar
import OstandardDeviation as sd
from scipy import stats

masa = ar.data[9]
inc_masa = 0.1#la incertidumbre instrumental

area = ar.data[2]
inc_area = []
for i in range(8):
    area=ar.data[2][i]
    lado1=ar.data[0][i]
    lado2=ar.data[1][i]
    incerteza = area*((0.5/lado1)+(0.5/lado2))
    inc_area = np.append(inc_area,incerteza)

print(inc_area)
print(type(area), type(masa))
print(area, masa)

ajuste = stats.linregress(area, masa)

plt.figure(figsize=(5, 4))
plt.errorbar(area,masa,
             xerr=inc_area, yerr=inc_masa,
             fmt='o', ms=4, ls='none', capsize=3, zorder=0)

y_pred = ajuste.slope * area + ajuste.intercept # Predicción de recta
plt.plot(area, y_pred,c='r')

plt.xlabel("Área [cm^2]")
plt.ylabel("Masa [g]")
plt.title("Masa en funcion del área, hoja Oficio")
plt.show()