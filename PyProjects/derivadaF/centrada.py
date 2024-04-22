def f(x):
  return x**4

def d1dx(x, h):
  derivada=(f(x+h)-f(x-h))/(2*h)
  return derivada

def alt_d1dx(x, h):
  xa=x+(2*h)
  xb=x+h
  xc=x-h
  xd=x-(2*h)
  a=f(xa)
  b=8*f(xb)
  c=8*f(xc)
  d=f(xd)
  derivada=(-a+b-c+d)/(12*h)
  return derivada

def d2dx(x,h):
  xa=x+h
  xc=x-h
  a=f(xa)
  b=2*f(x)
  c=f(xc)
  derivada2=(a-b+c)/(h**2)
  return derivada2

def alt_d2dx(x, h):
  xa=x+(2*h)
  xb=x+h
  xd=x-h
  xe=x-(2*h)
  a=f(xa)
  b=16*f(xb)
  c=30*f(x)
  d=16*f(xd)
  e=f(xe)
  hi=h**2
  derivada2=(-a+b-c+d-e)/(hi*12)
  return derivada2
##posible fallo al no poseer 3 en adelante derivada
def d3dx(x, h):
  xa=x+(2*h)
  xb=x+h
  xc=x-h
  xd=x-(2*h)
  a=f(xa)
  b=2*f(xb)
  c=2*f(xc)
  d=f(xd)
  hi=h**3
  derivada3=(a-b+c-d)/(hi*2)
  return derivada3

def alt_d3dx(x, h):
  xa=x+(3*h)
  xb=x+(2*h)
  xc=x+h
  xd=x-h
  xe=x-(2*h)
  xf=x-(3*h)
  a=f(xa)
  b=8*f(xb)
  c=13*f(xc)
  d=13*f(xd)
  e=8*f(xe)
  ff=f(xf)
  hi=h**3
  derivada3=(-a+b-c+d-e+ff)/(8*hi)
  return derivada3

def d4dx(x, h):
  xa=x+(2*h)
  xb=x+h
  xd=x-h
  xe=x-(2*h)
  a=f(xa)
  b=4*f(xb)
  c=6*f(x)
  d=4*f(xd)
  e=f(xe)
  derivada4=(a-b+c-d+e)/(h**4)
  return derivada4

def alt_d4dx(x, h):
  xa=x+(3*h)
  xb=x+(2*h)
  xc=x+h
  xe=x-h
  xf=x-(2*h)
  xg=x-(3*h)
  a=f(xa)
  b=12*f(xb)
  c=39*f(xc)
  d=56*f(x)
  e=39*f(xe)
  ff=12*f(xf)
  g=f(xg)
  hi=h**4
  derivada4=(-a+b-c+d-e+ff-g)/(hi*6)
  return derivada4