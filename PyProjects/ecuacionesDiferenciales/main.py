import edo
from tabulate import tabulate
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tabla=[["i", "Xi", "Y euler", "Y 2nd Orden", "Y 3rd Orden", "Y 4to Orden", "Y 5to orden"]]

x=float(input('Dame el valor inicial de x(x0): '))
y=float(input('Dame el valor inicial de y(y0): '))
h=float(input('Dame el valor de h por favor: '))
tabla.append([0, x, y, y, y, y, y])
ypp1=y
ypp2=y
ypp3=y
ypp4=y
ypp5=y
iteraciones=int(input('Dame el numero de iteraciones a realizar: '))

y1arr = []
y2arr = []
y3arr = []
y4arr = []
y5arr = []

for i in range(0,iteraciones):
    ypp1=edo.euler(x,ypp1,h)
    ypp2=edo.rungekutta2(x, ypp2, h)
    ypp3=edo.rungekutta3(x, ypp3, h)
    ypp4=edo.rungekutta4(x, ypp4, h)
    ypp5=edo.rungekutta5(x, ypp5, h)
    x+=h
    tabla.append([i+1, x, ypp1, ypp2, ypp3, ypp4, ypp5])

    y1arr.append(ypp1)
    y2arr.append(ypp2)
    y3arr.append(ypp3)
    y4arr.append(ypp4)
    y5arr.append(ypp5)

tablai=tabulate(tabla)
print(tablai)


plt.scatter(range(len(y5arr)), y5arr)
plt.xlabel('Indice')
plt.ylabel('Valor')
plt.title('Grafico de Runge')
plt.show()