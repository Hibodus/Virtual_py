import numpy as np
import matplotlib.pyplot as plt

# Определим функцию y(x)
def y(x):
    if x < 0.1:
        return np.sqrt(2.5 * x**2 + 0.4 * np.sin(x) + 1)
    elif x == 0.1:
        return 2.5 * x + 0.4
    else:
        return np.sqrt(2.5 * x**2 + 0.4 * np.cos(x) + 1)

# Зададим интервал и шаг
x_values = np.arange(0, 0.21, 0.01)
y_values = [y(x) for x in x_values]

# Построим график
plt.plot(x_values, y_values)
plt.title('График функции y(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
