# WE first begin by just doing some examples
import scipy.integrate
import math
from scipy import interpolate
import numpy as np
import matplotlib as plt
from matplotlib import pyplot
import sympy as sym
from scipy.integrate import simps

x = sym.symbols("x",real = True)


def percentile_data(variance: float, nth_percentile: int):
    for x in range(1, nth_percentile + 1):
        percentile = scipy.integrate.quad(Normal_standard, 0 - x * 1, 0 + x * 1)[0]
        print("Quartile {}: {}".format(x, percentile))


def graph_function():
    # x = np.linspace(0, 200, 400)
    y = Normal(x)
    pyplot.plot(x, y)
    pyplot.show()


"""NORMAL FUNCTIONS"""


def Normal_standard(x):
    return (np.e ** (-(x ** 2) / 2)) / (np.sqrt(2 * np.pi))


# need to make general normal
# need to figure out how to change expected and variance whenever
# 100 = expected, 2 parameters
# 15 = variance
def Normal(x):
    return (sym.e ** -((x - 100) / (15 * 2)) ** 2 / (15 * (np.sqrt(2 * np.pi))))


"""EXPONENTIAL FUNCTION"""

#again need to find a way to generalize
#.278 = lambda,1 parameter
def exponential_distribution(x):
    return .278 * math.exp(-.278 * x)

x = sym.symbols("x",real = True)
"""GAMMA FUNCTION"""
#generalize; 2 parameteres alpha;beta
#need to define 2 functions for this computation
def gamma_function(alpha:float):
    return sym.integrate((x**(alpha-1))*np.exp(-x),x,(0,sym.oo))
def cts_gamma_distribution(alpha:float,lambda_:float)->sym.exp:
    return lambda_**alpha/gamma_function(alpha) * x**(alpha-1)*sym.exp(-lambda_*x)
#def gamma_distribution(x):
    

# want to incorporate bounds in the function additionally the quantile would be good as well
def Compute_integration():
    x = np.linspace(0, 200, 300)
    I2 = scipy.integrate.quad(exponential_distribution, 9, np.infty)[0]
    return I2

def sym_integrate():
    return sym.integrate(cts_gamma_distribution(2,.5),(x,4,sym.oo))

print(sym.gamma(2))
"""
class Integral:
    
    #Constructor allows us to initalize the following:
    (1) variable of integration
    (2) lower bound
    (3) upper_bound
    

    # We begin with 1 dimensional case:
    def __init__(self, variable, lower_bounds, upper_bounds):
        Integral.variable = variable
        Integral.lower_bounds = lower_bounds
        Integral.upper_bounds = upper_bounds

    # here is the particular equation of integration
   # def Normal_distribution(self,expected_value:float, standard_deviation_value:float, x):
        #return math.exp(-.5*(((x-expected_value)/standard_deviation_value)**2))/(standard_deviation_value*math.sqrt(2*math.pi))
def Normal_distribution(self,expected_value:float, standard_deviation_value:float, variable):
    return math.exp(-.5*(((variable-expected_value)/standard_deviation_value)**2))/(standard_deviation_value*math.sqrt(2*math.pi))

a = numpy.array([-numpy.infty,numpy.infty])
I2 = scipy.integrate.simps(Normal_distribution(0,1-+),x)


print(result)
"""
