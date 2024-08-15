import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

'''
Documentacion de una funcion o clase
'''
def generar_distribucion(data, titulo):
    asimetria = skew(data)
    curtosis = kurtosis(data)

    print(f'{titulo}: Asimetria: {asimetria:.2f}, Curtosis: {curtosis:.2f}')

    # Histograma
    sns.histplot(data, kde=False)

    plt.title(titulo)
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.show()

print('todo bien')