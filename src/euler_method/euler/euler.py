import numpy as np
import matplotlib.pyplot as plt


def euler(f_e, y_e, h_e):
    return Euler(f_e, y_e, h_e)


def run_example():
    t_of_eu = np.linspace(0, 5, 16)
    y0_of_eu = -1
    function_of_eu = lambda y_eu, t_eu: y_eu ** 2
    y = euler(function_of_eu, y0_of_eu, t_of_eu).solve()
    t_true = np.linspace(0, 5, 100)
    y_true = -1 / (t_true + 1)
    plt.plot(t_of_eu, y, 'r.-', t_true, y_true)
    plt.legend(['Euler', 'True'])
    plt.grid(True)
    plt.axis([0, 5, -1, 0])
    plt.title("euler method \n Solution of $y'=y^2 , y(0)=1$")
    plt.show()


class Euler:
    def __init__(self, f, y0, t):
        self.function = f
        self.y0 = y0
        self.h = t

    def solve(self):
        y = np.zeros(len(self.h))
        y[0] = self.y0
        for n in range(0, len(self.h) - 1):
            y[n + 1] = y[n] + self.function(y[n], self.h[n]) * (self.h[n + 1] - self.h[n])
        return y
