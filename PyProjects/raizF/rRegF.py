import pandas as pd
import math
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np

def evaluateEfe(x):
  num=math.sin(x-3)
  den=x-(1/2)
  coci=num/den
  return coci

def sacarM(a,b):
  numerador=evaluateEfe(b)*(b-a)
  denominador=evaluateEfe(b)-evaluateEfe(a)
  m=b-(numerador/denominador)
  return m


a=float(input('dame a: '))
b=float(input('dame b: '))
fA=evaluateEfe(a)
fB=evaluateEfe(b)

while(fA*fB>0):
  a=float(input('dame a: '))
  b=float(input('dame b: '))
  fA=evaluateEfe(a)
  fB=evaluateEfe(b)
  
if(fA>fB):
  swap=a
  a=b
  b=swap
print(a)
print(b)



m=sacarM(a,b)
fM=evaluateEfe(m)
errR=1
x_vals = np.linspace(a, b, 1000)
y_vals = np.vectorize(evaluateEfe)(x_vals)     
m_vals = []
eR_vals = []
tabla=[["a", "b", "m", "f(a)", "f(b)", "f(m)", "erR", "errRP"]]
i=1
powError=int(input("Dame la potencia del error maximo del programa 1.2x*10^?(por favor ten en cuenta que para un error pequeño es negativo)"))
notCien= np.float_power(10, powError)
while errR>(1.2*notCien):
    n=m
    m_vals.append(n)
    eR_vals.append(errR)
    errRP=errR*100
    tabla.append([a,b,m,fA, fB, fM, errR, errRP])
    if(fM*fA>0):
        a=m
    else:
        b=m
    if(fM==0):
        break
    if(fM==0):
        i+=1
        break
    if(fA*fB>0):
       i+=1
       break
    m=sacarM(a,b)
    fM=evaluateEfe(m)
    errR=(m-n)/m
    errR=math.fabs(errR)
    fA=evaluateEfe(a)
    fB=evaluateEfe(b)
    i+=1
plt.plot(x_vals, y_vals, label='f(x)=cos(x)')
plt.scatter(m_vals, np.vectorize(evaluateEfe)(m_vals), color='red', label='Puntos medios')
plt.legend([f'Con raiz aprox en:{m_vals[-1]:-4f}'])
plt.figure()

plt.plot(range(1,len(eR_vals)+1), eR_vals, label=f'Con error minimo en la iteración:{len(eR_vals)}')
plt.legend([f'Con error minimo en la iteración:{len(eR_vals)}'])
plt.xlabel('Iteración')
plt.ylabel('Error Relativo Porcentual')
plt.title('Error en el Método de regla falsa')
plt.grid(True)
plt.legend()
plt.show()
tabla1=tabulate(tabla)
df=pd.DataFrame(tabla)
df.to_csv('reglaFalsa.csv', header=False, index=True)
print(tabla1)