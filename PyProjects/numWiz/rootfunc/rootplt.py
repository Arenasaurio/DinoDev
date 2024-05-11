import rootf
import matplotlib.pyplot as plt

def gnewtRph(x: float, h: float, f: float, it: int):
    """
    Recibe valores para que funcione newton raphson
    y después itera para sacar un plot
    Input: float x, float h, callable f, int it
    Output: plt.plot
    """
    x_vals =[]
    y_vals =[]
    x_vals.append(x)
    y_vals.append(f(x))
    for i in range(it):
        x=rootf.newtRph(x, h, f)
        y=f(x)
        x_vals.append(x)
        y_vals.append(y)
    plt.plot(x_vals, y_vals, label= f'Raiz newt-raph = {x_vals[-1]}')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Grafico de la funcion")
    plt.grid(True)
    plt.legend()
    plt.show()