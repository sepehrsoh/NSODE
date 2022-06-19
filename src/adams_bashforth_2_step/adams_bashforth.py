import numpy as np
import matplotlib.pyplot as plt


def adams_bashforth(f_ab, y0_ab, t_ab):
    return AdamsBashforth(f_ab, y0_ab, t_ab)


def run_example():
    t_of_ab = np.linspace(0, 5, 16)
    y0_of_ab = -1
    function_of_ab = lambda y_ab, t_ab: y_ab ** 2
    y_of_ab = adams_bashforth(function_of_ab, y0_of_ab, t_of_ab).solve()
    t_true = np.linspace(0, 5, 100)
    y_true = -1 / (t_true + 1)
    plt.plot(t_of_ab, y_of_ab, 'r.-', t_true, y_true)
    plt.legend(['abo2', 'True'])
    plt.grid(True)
    plt.axis([0, 5, -1, 0])
    plt.title("adams bashforth method \n Solution of $y'=y^2 , y(0)=1$")
    plt.show()


class AdamsBashforth:
    def __init__(self, f, y0, t):
        self.f = f
        self.y0 = y0
        self.t = t

    def solve(self):
        n = len(self.t)
        y = np.zeros(len(self.t))
        y[0] = y[1] = self.y0
        for i in range(n - 2):
            h = self.t[i + 1] - self.t[i]
            y[i + 2] = y[i + 1] + h * (3 * self.f(y[i + 1], self.t[i + 1]) - self.f(y[i], self.t[i])) / 2.
        return y
