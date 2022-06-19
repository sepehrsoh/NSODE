import numpy as np
import matplotlib.pyplot as plt


def rung_kutta_o4(f_rk4,y0_rk4,t_rk4):
    return RungKuttaO4(f_rk4,y0_rk4,t_rk4)


def run_example():
    t_of_rk4 = np.linspace(0, 5, 16)
    y0_of_rk4 = -1
    function_of_rk4 = lambda y_rk4, t_rk4: y_rk4 ** 2
    y_of_rk4 = rung_kutta_o4(function_of_rk4, y0_of_rk4, t_of_rk4).solve()
    t_true = np.linspace(0, 5, 100)
    y_true = -1 / (t_true + 1)
    plt.plot(t_of_rk4, y_of_rk4, 'r.-', t_true, y_true)
    plt.legend(['rko4', 'True'])
    plt.grid(True)
    plt.axis([0, 5, -1, 0])
    plt.title("runge kutta order 4 method \n Solution of $y'=y^2 , y(0)=1$")
    plt.show()

class RungKuttaO4:
    def __init__(self, f, y0, t):
        self.f = f
        self.y0 = y0
        self.t = t

    def solve(self):
        n = len(self.t)
        y = np.zeros(len(self.t))
        y[0] = self.y0
        for i in range(n - 1):
            h = self.t[i + 1] - self.t[i]
            k1 = h * self.f(y[i], self.t[i])
            k2 = h * self.f(y[i] + 0.5 * k1, self.t[i] + 0.5 * h)
            k3 = h * self.f(y[i] + 0.5 * k2, self.t[i] + 0.5 * h)
            k4 = h * self.f(y[i] + k3, self.t[i + 1])
            y[i + 1] = y[i] + (k1 + 2.0 * (k2 + k3) + k4) / 6.0
        return y