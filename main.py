import matplotlib.pyplot as plt
import numpy as np


def beautify_line_chart():
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.xticks([-2, -1, 0, 1, 2])
    plt.yticks([-2, -1, 0, 1, 2])
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


x_array = np.linspace(-2, 2, 101)

fig, ax = plt.subplots(figsize=(4, 4))

y_array = np.sin(x_array**2-x_array)

plt.plot(x_array, y_array)
beautify_line_chart()
