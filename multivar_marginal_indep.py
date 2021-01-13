import sympy as sym
import math
import scipy.integrate
import math
from scipy import interpolate
import numpy as np
import matplotlib as plt
from matplotlib import pyplot

x,y = sym.symbols("x y", real = True)

class multivar_marginal:

    def __init__(self,input_function,x_bounds,y_bounds):
        self.function = input_function
        self.x_lower_bound = x_bounds[0]
        self.x_upper_bound = x_bounds[1]
        self.y_lower_bound = y_bounds[0]
        self.y_upper_bound = y_bounds[1]


    def compute_marginals(self):
        marginal_x = sym.integrate(self.function,(y,self.y_lower_bound, self.y_upper_bound))
        marginal_y = sym.integrate(self.function, (x, self.x_lower_bound, self.x_upper_bound))


def integrand(function):
    return 3*x


# want to incorporate bounds in the function additionally the quantile would be good as well
#close but not ther eyet
def Compute_integration():
    #x = np.linspace(0, 200, 300)
    I2 = scipy.integrate.dblquad(lambda x, y:3*x,.25,1,lambda x:0,lambda x: .5)[0]
    return I2


def is_independent(function, x_bounds:list, y_bounds:list):
    marginal_x = sym.integrate(4*x*y,(y,y_bounds[0],y_bounds[1]))
    marginal_y = sym.integrate(4*x*y,(x,x_bounds[0],x_bounds[1]))
    print(marginal_x)
    print(marginal_y)