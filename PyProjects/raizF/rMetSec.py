import math
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def evaluateEfe(x):
  num=math.sin(x-3)
  den=x-(1/2)
  coci=num/den
  return coci

def nuevaEquisi(x0,x1):
    res=x1-((evaluateEfe(x1)*(x0-x1))/evaluateEfe(x0)-evaluateEfe(x1))
    return res


def errorRelativo(xi,x):
    res=math.fabs((xi-x)/xi)
    return res


xi=float(input('dame xi: '))
x=0
a=-100
b=100
xim1=float(input('dame xi-1: '))
x_vals = np.linspace(a, b, 1000)
y_vals = np.vectorize(evaluateEfe)(x_vals)     
xi_vals = []
eR_vals = []
i=1
errR=errorRelativo(xi,x)
fXi=evaluateEfe(xi)
fX0=evaluateEfe(xim1)
errRP=errR*100
tabla=[["xi-1", "xi", "f(xi-1)", "f(xi)", "errR", "errRP"]]

powError=int(input("Dame la potencia del error maximo del programa 1.2x*10^?(por favor ten en cuenta que para un error pequeño es negativo)"))
notCien= np.float_power(10, powError)
while errR>(1.2*notCien):
    x=xi
    xi_vals.append(xi)
    eR_vals.append(errR)
    tabla.append([xim1, xi, fX0, fXi, errR, errRP])
    xim1=xi
    xi=nuevaEquisi(xim1, xi)
    fXi=evaluateEfe(xi)
    
    fX0=evaluateEfe(xim1)
    errR=errorRelativo(xi,x)
    errRP=errR*100
    i+=1

plt.plot(x_vals, y_vals, label='f(x)=cos(x)')
plt.legend([f'Con raíz aprox en: {xi_vals[-1]:.4f}'])
plt.scatter(xi_vals, np.vectorize(evaluateEfe)(xi_vals), color='red', label='Puntos medios')
plt.figure()
plt.plot(range(1,i), eR_vals, label=f'Con error minimo en la iteración:{len(eR_vals)}')
plt.xlabel('Iteración')
plt.ylabel('Error Relativo Porcentual')
plt.title('Error en el Método por Secante')
plt.grid(True)
plt.legend()
plt.show()
tabla1=tabulate(tabla)
df=pd.DataFrame(tabla)
df.to_csv('MetdoSecante.csv', header=False, index=True)
print(tabla1)