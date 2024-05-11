def alt_d1dx(x: float, h: float, f: float)->float:
  """
  Usa el metodo centrado para la derivada.
  Input: float x, float h, func f
  Output: float derivada
  """
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

def newtRph(x: float, h: float, f: float)->float:
  """
  Usa el metodo de newton-raphson para sacar raiz de una funcion dada
  logrando una aproximacion en n iteraciones
  Input: float x, float alt_d1dx, float f
  Output: float xi
  """
  xi = x-(f(x)/alt_d1dx(x, 0.000000001, f))
  return xi

