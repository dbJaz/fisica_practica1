import numpy as np  
import matplotlib.pyplot as plt
import pandas as pd
import OarmoArrays as ar
import OstandardDeviation as sd


volumen = ar.data[7]
inc_volumen = ar.data[7][-1]
volumen=np.delete(volumen, -1)


masa = ar.data[9]
inc_masa = 0.01
masa = np.delete(masa, -1)


plt.figure(figsize=(5, 4))
plt.errorbar(masa,volumen,
             xerr=inc_masa, yerr=inc_volumen,
             fmt='o', ms=4, ls='none', capsize=3, zorder=0)

plt.xlabel("Masa [g]")
plt.ylabel("Diámetro [cm]")
plt.title("Diametro en funcion de la masa, hoja Oficio")
plt.show()
