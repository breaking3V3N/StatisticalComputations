import scipy.integrate
import math
from scipy import interpolate
import numpy as np
import matplotlib as plt
from matplotlib import pyplot
import sympy as sym

x,t,lam = sym.symbols("x t lam", real = True)

sigma,mu =sym.symbols("sigma mu", real = True)
class continuous_pdf:

    def __init__(self, function: sym.exp, x_bounds: list):
        self.function = function
        self.xlb = x_bounds[0]
        self.xub = x_bounds[1]
        self.expected = self.cts_expected_value()
        self.varaince = self.cts_varaince_value()

    def cts_expected_value(self):
        return sym.integrate(self.function * x,(x,self.xlb,self.xub))


    def cts_varaince_value(self):
        return sym.integrate(self.function * (x - self.expected)**2, (x,self.xlb,self.xub))

    def moment_generating_function(self):
        return sym.integrate(self.function * sym.exp(-t*x),(x,self.xlb,self.xub))
a = continuous_pdf(lam * sym.exp(-lam * x),[0,sym.oo])
print(a.moment_generating_function())