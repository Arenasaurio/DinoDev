import pandas as pd
import math
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np

def evaluateEfe(x):
    cociente=x/4
    cociente = cociente**2
    return cociente-6
#puede o no necesitar derivada, segun sea una funcion trigonometrica
def derivada(x):
    cociente=x/8
    return cociente

def evaluateGe(x):
    res=x-(evaluateEfe(x)/derivada(x))
    return res

def errorRelativo(xi,x):
    res=math.fabs((xi-x)/xi)
    return res


xi=float(input('dame xi: '))
x=0
a=-2*xi
b=2*xi
x_vals = np.linspace(a, b, 1000)
y_vals = np.vectorize(evaluateEfe)(x_vals)     
xi_vals = []
eR_vals = []
errR=errorRelativo(xi,x)
fXi=evaluateEfe(xi)
gXi=evaluateGe(xi)
errRP=errR*100
tabla=[["xi", "f(xi)", "g(xi)", "errR", "errRP"]]
i=1
powError=int(input("Dame la potencia del error maximo del programa 1.2x*10^?(por favor ten en cuenta que para un error pequeño es negativo)"))
notCien= np.float_power(10, powError)
while errR>(1.2*notCien):
    x=xi
    xi_vals.append(x)
    eR_vals.append(errR)
    tabla.append([xi, fXi, gXi, errR, errRP])
    xi=gXi
    fXi=evaluateEfe(xi)
    gXi=evaluateGe(xi)
    errR=errorRelativo(xi,x)
    errRP=errR*100
    i+=1



plt.plot(x_vals, y_vals, label='f(x)=x^2/16 -6')
plt.scatter(xi_vals, np.vectorize(evaluateEfe)(xi_vals), color='red', label='Puntos medios')
plt.legend([f'Con raíz aprox en: {xi_vals[-1]:.4f}'])
plt.figure()
plt.plot(range(1,len(eR_vals)+1), eR_vals, label=f'Con error minimo en la iteración:{len(eR_vals)}')
plt.xlabel('Iteración')
plt.ylabel('Error Relativo Porcentual')
plt.title('Error en el Método del Punto fijo')
plt.grid(True)
plt.legend()
plt.show()
tabla1=tabulate(tabla)
df=pd.DataFrame(tabla)
df.to_csv('puntoFijo.csv', header=False, index=True)
print(tabla1)