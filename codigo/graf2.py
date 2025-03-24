import numpy as np  
import matplotlib.pyplot as plt
import pandas as pd
import armoArrays as ar
import standardDeviation as sd

array=ar.data
masa=array[3]
inc_peso=array[3][-1]
masa=np.delete(masa, -1)

diametro=array[7]
inc_diametro=array[7][-1]
print(inc_diametro)
inc_dc = inc_diametro * 2 *diametro
diametro=np.delete(diametro, -1)
print("VALOR")
print(diametro)
print(inc_diametro)


plt.figure(figsize=(4, 3))
plt.errorbar(masa**2, diametro, xerr=inc_peso, yerr=inc_diametro, fmt='o',ms=3,ls='none',capsize=3,zorder=0)

plt.xlabel('Peso [g]')
plt.ylabel('Diámetro [cm]')
plt.show()

