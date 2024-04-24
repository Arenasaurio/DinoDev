import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carga de datos
datosnat = pd.read_csv("C:/Users/Csera/Documents/DinoDev_data/PyProjects/natalidad2k18.csv")

# Lista de columnas para las que se calcularán las estadísticas y se generarán los gráficos
columnas = ['ent_resid', 'ent_ocurr', 'sexo', 'edad_madn', 'edad_padn', 'ano_nac', 'mes_nac', 'escol_mad', 'escol_pad']

for columna in columnas:
    # Cálculo de estadísticas
    media = datosnat[columna].mean()
    mediana = datosnat[columna].median()
    varianza = datosnat[columna].var()
    desviacion = datosnat[columna].std()

    # Creación de gráficos de distribución
    plt.figure(figsize=(10, 6))
    sns.histplot(datosnat[columna], kde=True)
    plt.axvline(media, color='r', linestyle='--', label=f'Media: {media:.2f}')
    plt.axvline(mediana, color='g', linestyle='-', label=f'Mediana: {mediana:.2f}')
    plt.axvline(media + desviacion, color='b', linestyle='-.', label=f'Desviación estándar: {desviacion:.2f}')
    plt.legend()
    plt.title(f'Distribución de {columna}')

    # Guardar el gráfico como un archivo .png
    plt.savefig(f"{columna}_distribution.png")

    # Cerrar el gráfico
    plt.close()
