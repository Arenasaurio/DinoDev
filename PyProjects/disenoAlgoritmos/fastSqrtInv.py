import matplotlib.pyplot as plt
import numpy as np

def fast_invsqrt(x):
    xhalf = 0.5 * x
    i = int(x)
    i = 0x5f3759df - (i >> 1)
    x = float(i)
    x = x * (1.5 - (xhalf * x * x))
    return x

# Generar datos para graficar
x_values = np.linspace(0.01, 100, 1000)
y_values = [fast_invsqrt(x) for x in x_values]

# Graficar la función
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label="Fast InvSqrt")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Función Fast InvSqrt")
plt.grid(True)
plt.legend()
plt.show()
