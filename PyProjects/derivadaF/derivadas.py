import regresion
import progresion
import centrada

x=float(input('Dame el valor de x:'))
h=float(input('Dame el valor de h(se sugiere uno muy pequeño):'))

d1dxr=regresion.d1dx(x, h)
d1dxp=progresion.d1dx(x, h)


d1dxc=centrada.d1dx(x,h)
d1dxc2=centrada.alt_d1dx(x,h)
d2dxc=centrada.d2dx(x,h)
d2dxc2=centrada.alt_d2dx(x,h)
d3dxc=centrada.d3dx(x,h)
d3dxc2=centrada.alt_d3dx(x,h)
d4dxc=centrada.d4dx(x,h)
d4dxc2=centrada.alt_d4dx(x,h)
print(d1dxc)
print(d1dxc2)
print(d2dxc)
print(d2dxc2)
print(d3dxc)
print(d3dxc2)
print(d4dxc)
print(d4dxc2)