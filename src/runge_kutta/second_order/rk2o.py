import numpy as np
import matplotlib.pyplot as plt


def rung_kutta_2end_order(f_rk, x0_rk, t_rk):
    return RungKutta(f_rk, x0_rk, t_rk)


def run_example():
    t_of_rk = np.linspace(0, 5, 16)
    y0_of_rk = -1
    function_of_rk = lambda y_eu, t_eu: y_eu ** 2
    y_of_rk = rung_kutta_2end_order(function_of_rk, y0_of_rk, t_of_rk).solve()
    t_true = np.linspace(0, 5, 100)
    y_true = -1 / (t_true + 1)
    plt.plot(t_of_rk, y_of_rk, 'r.-',t_true, y_true)
    plt.legend(['rk2', 'True'])
    plt.grid(True)
    plt.axis([0, 5, -1, 0])
    plt.title("runge kutta order 2 method \n Solution of $y'=y^2 , y(0)=1$")
    plt.show()


class RungKutta:
    def __init__(self, f, y0, t):
        self.t = t
        self.f = f
        self.y0 = y0

    def solve(self):
        n = len(self.t)
        y = np.zeros(len(self.t))
        y[0] = self.y0
        for i in range(n - 1):
            h = self.t[i + 1] - self.t[i]
            y[i + 1] = y[i] + h * self.f(y[i] + self.f(y[i], self.t[i]) * h / 2., self.t[i] + h / 2.)
        return y
