import numpy as np
import matplotlib.pyplot as plt


def adams_bashforth_moulton(f_abm, y0_abm, t_abm):
    return ABM(f_abm, y0_abm, t_abm)


def run_example():
    t_of_abm = np.linspace(0, 5, 16)
    y0_of_abm = -1
    function_of_abm = lambda y_abm, t_abm: y_abm ** 2
    y_of_abm = adams_bashforth_moulton(function_of_abm, y0_of_abm, t_of_abm).solve()
    t_true = np.linspace(0, 5, 100)
    y_true = -1 / (t_true + 1)
    plt.plot(t_of_abm, y_of_abm, 'r.-', t_true, y_true)
    plt.legend(['abmo4', 'True'])
    plt.grid(True)
    plt.axis([0, 5, -1, 0])
    plt.title("adams bashforth moulton method \nSolution of $y'=y^2 , y(0)=1$")
    plt.show()

class ABM:
    def __init__(self, f, y0, t):
        self.t = t
        self.f = f
        self.y0 = y0

    def solve(self):
        y = np.zeros(len(self.t))
        y[0] = self.y0
        f1 = f2 = f3 = 0
        for i in range(min(3, len(self.t) - 1)):
            h = self.t[i + 1] - self.t[i]
            f0 = self.f(y[i], self.t[i])
            k1 = h * f0
            k2 = h * self.f(y[i] + 0.5 * k1, self.t[i] + 0.5 * h)
            k3 = h * self.f(y[i] + 0.5 * k2, self.t[i] + 0.5 * h)
            k4 = h * self.f(y[i] + k3, self.t[i + 1])
            y[i + 1] = y[i] + (k1 + 2.0 * (k2 + k3) + k4) / 6.0
            f1, f2, f3 = (f0, f1, f2)

        for i in range(3, len(self.t) - 1):
            h = self.t[i + 1] - self.t[i]
            f0 = self.f(y[i], self.t[i])
            w = y[i] + h * (55.0 * f0 - 59.0 * f1 + 37.0 * f2 - 9.0 * f3) / 24.0
            fw = self.f(w, self.t[i + 1])
            y[i + 1] = y[i] + h * (9.0 * fw + 19.0 * f0 - 5.0 * f1 + f2) / 24.0
            f1, f2, f3 = (f0, f1, f2)

        return y
