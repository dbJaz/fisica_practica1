import numpy as np  
import matplotlib.pyplot as plt
import pandas as pd
import OarmoArrays as ar
import OstandardDeviation as sd


diametro = ar.data[7]
inc_diametro = ar.data[7][-1]
diametro=np.delete(diametro, -1)


masa = ar.data[9]
inc_masa = ar.data[9][-1]
masa = np.delete(masa, -1)


plt.figure(figsize=(5, 4))
plt.errorbar(masa,diametro,
             xerr=inc_masa, yerr=inc_diametro,
             fmt='o', ms=4, ls='none', capsize=3, zorder=0)

plt.xlabel("Masa [g]")
plt.ylabel("Diámetro [cm]")
plt.title("Diametro en funcion de la masa, hoja Oficio")
plt.show()
