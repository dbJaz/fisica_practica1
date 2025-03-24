import numpy as np  
import matplotlib.pyplot as plt
import pandas as pd
import armoArrays as ar
import standardDeviation as sd

array=ar.data
peso=array[3]
peso=np.delete(peso, -1)
inc_peso=array[3][-1]
inc_diametro=array[7][-1]
diametro=array[7]
diametro=np.delete(diametro, -1)
#print("el peso es", peso)
plt.figure(figsize=(4, 3))
plt.errorbar(peso, diametro, xerr=inc_peso, yerr=inc_diametro, fmt='o',ms=3,ls='none',capsize=3,zorder=0)

plt.xscale('log')
plt.yscale('log')

plt.xlabel('Peso [g]')
plt.ylabel('Diámetro [cm]')
plt.show()