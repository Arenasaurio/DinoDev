import rootf
import rootplt
def f(x):
    return x**2

equis = float(input("Dame el valor de x: "))

print(rootf.alt_d1dx(equis, 0.001, f))
rut = rootf.newtRph(equis, 0.001, f)
print(rut, f(rut))
iteraciones = int(input("Dime cuantas iteraciones quieres hacer?"))
rootplt.gnewtRph(equis, 0.001, f, iteraciones)