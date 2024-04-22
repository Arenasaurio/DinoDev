import math
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def evaluateEfe(x):
    cociente=x/4
    cociente = cociente**2
    return cociente-6

def evaluateEfePrima(x):
    return x/8

def sacarxi(x):
    res=x-(evaluateEfe(x)/evaluateEfePrima(x))
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
fpXi=evaluateEfePrima(xi)
errRP=errR*100
tabla=[["xi", "f(xi)", "f'(xi)", "errR", "errRP"]]
i=1
powError=int(input("Dame la potencia del error maximo del programa 1.2x*10^?(por favor ten en cuenta que para un error pequeño es negativo)"))
notCien= np.float_power(10, powError)
while errR>(1.2*notCien):
    x=xi
    xi_vals.append(x)
    eR_vals.append(errR)
    tabla.append([xi, fXi, fpXi, errR, errRP])
    xi=sacarxi(xi)
    fXi=evaluateEfe(xi)
    fpXi=evaluateEfePrima(xi)
    errR=errorRelativo(xi,x)
    errRP=errR*100
    i+=1

plt.plot(x_vals, y_vals, label='f(x)=cos(x)')
plt.scatter(xi_vals, np.vectorize(evaluateEfe)(xi_vals), color='red', label='Puntos medios')
plt.legend(['f(x)=(x/4)^2 -6', f'Con raíz aprox en: {xi_vals[-1]:.4f}'])
plt.figure()
plt.plot(range(1,i), eR_vals, label='Error Relativo Porcentual (%)')
plt.legend([f'Error menor en la iteración: {len(eR_vals)}'])
plt.xlabel('Iteración')
plt.ylabel('Error Relativo Porcentual')
plt.title('Error en el Método de Newton Raphson')
plt.grid(True)


plt.show()
tabla1=tabulate(tabla)
df=pd.DataFrame(tabla)
df.to_csv('NewtRaph.csv', header=False, index=True)
print(tabla1)