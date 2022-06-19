from src.euler_method.euler import euler
from src.runge_kutta.second_order import rk2o
from src.runge_kutta.forth_order import rk4o
from src.adams_bashforth_2_step import adams_bashforth
from src.adams_bashforth_moulton import abmo4

if __name__ == '__main__':
    # example of euler method
    euler.run_example()
    # example of rung kutta 2nd order method
    rk2o.run_example()
    rk2o.rung_kutta_2end_order()
    # example of rung kutta 4nd order method
    rk4o.run_example()
    # example of rung adams bashforth predictor-corrector method
    abmo4.run_example()
    # example of adams bashforth 2nd order method
    adams_bashforth.run_example()
