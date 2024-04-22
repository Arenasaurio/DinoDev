import pandas as pd
import math
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np
#al ser un metodo rapido probablemente tenga casos donde la division por cero se de
def evaluateEfe(x):
    return x**3 +2

##muller el mulas
def hZero(x1,x0):
    return x1-x0

def hOne(x2,x1):
    return x2-x1

def deltZero(x1, x0):
    d0=(evaluateEfe(x1)-evaluateEfe(x0))/hZero(x1,x0)
    return d0

def deltOne(x2, x1):
    d1=(evaluateEfe(x2)-evaluateEfe(x1))/hOne(x2,x1)
    return d1

def sacarA(x0,x1,x2):
    A=(deltOne(x2,x1)-deltZero(x1,x0))/(hOne(x2,x1)+hZero(x1,x0))
    return A

def sacarB(x0,x1,x2):
    B=sacarA(x0,x1,x2) * hOne(x2,x1) + deltOne(x2,x1)
    return B

def sacarC(x2):
    return evaluateEfe(x2)

def denRaiz(x0,x1,x2):
    raiz=((sacarB(x0,x1,x2)**2)-4*sacarA(x0,x1,x2)*sacarC(x2))**(1/2)
    return raiz

def denominador(x0,x1,x2):
    if abs(sacarB(x0,x1,x2) + denRaiz(x0,x1,x2)) > abs(sacarB(x0,x1,x2) - denRaiz(x0,x1,x2)):
        den = sacarB(x0,x1,x2) + denRaiz(x0,x1,x2)
    else:
        den = sacarB(x0,x1,x2) - denRaiz(x0,x1,x2)
    return den

def sacarX3(x0,x1,x2):
    x3 = x2 - 2 * sacarC(x2) / denominador(x0,x1,x2)
    return x3

##fin del mullas psdt. facilmente se puede unificar en una sola funcion pero me dio flojera
def errorRelativo(xi,x):
    res=math.fabs((xi-x)/xi)
    return res

x0=float(input('Puedes darme el valor para x0? : '))
x1=float(input('Puedes darme el valor para x1? : '))
x2=float(input('Puedes darme el valor para x2? : '))
x=0
errR=1
errP=errorRelativo(x2,x)*100
x_vals=[]
fx_vals=[]
erR_vals=[]

tabla=[["xi", "f(xi)", "erR", "errRP"]]
tabla.append([x0,evaluateEfe(x0), errR, errP])
x_vals.append(x0)
fx_vals.append(evaluateEfe(x0))
tabla.append([x1,evaluateEfe(x1), errR, errP])
x_vals.append(x1)
fx_vals.append(evaluateEfe(x1))
powError=int(input("Dame la potencia del error maximo del programa 1.2x*10^?(por favor ten en cuenta que para un error pequeño es negativo)"))
notCien= np.float_power(10, powError)
while errR>(1.2*notCien):
    
    x_vals.append(x2)
    fx_vals.append(evaluateEfe(x2))
    erR_vals.append(errR)
    tabla.append([x2,evaluateEfe(x2), errR, errP])
    x3=sacarX3(x0,x1,x2)
    errR=errorRelativo(x3,x2)
    errP=errR*100
    x0, x1, x2 = x1, x2, x3


grafX=np.linspace(min(x_vals), max(x_vals), 1000)

plt.plot(grafX, evaluateEfe(grafX))
plt.legend([f'Con raíz aprox en: {x_vals[-1]:.4f}'])
plt.scatter(x_vals, np.vectorize(evaluateEfe)(x_vals), color='red', label='Puntos usados')
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlim(int(min(x_vals)), int(max(x_vals))+1)
plt.ylim(int(min(fx_vals)), int(max(fx_vals))+1)
plt.show()


plt.plot(range(1,len(erR_vals)+1), erR_vals, label=f'Con error minimo en la iteración:{len(erR_vals)}')
plt.xlabel('Iteración')
plt.ylabel('Error Relativo Porcentual')
plt.title('Error en el Método de muller')
plt.grid(True)
plt.legend()
plt.show()

tabla1=tabulate(tabla)

df=pd.DataFrame(tabla)
df.to_csv('metMuller.csv', header=False, index=True)
print(tabla1)


    ##x0, x1, x2 = 4.5, 5.5, 5.0
    