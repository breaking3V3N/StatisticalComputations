import sympy as sym
import math

#function that intializes symbols needed
def init_symbols(vars: list)-> list:
    emp_list = []
    for var in vars:
        var = sym.symbols(str(var), real=True)
        emp_list.append(var)
    return emp_list

class multi_cts_pf:

    def __init__(self,function ,variable_list:list):
        self.function = function
        self.variables = init_symbols(variable_list)
        self.total_var = len(self.variables)
        self.partial_equations = []

    #def is_independent(self)->bool:


    def partial_functions(self):
        for var in self.variable:
            sm_partial = sym.diff((y**2)*4*x*sym.exp(-x-2*y),var)
            self.partial_equations.append(sm_partial)
    def get_partial_functions(self):
        for x in range (0,len(self.partial_equations)):
            print("Partial of f, w.r.t({})  -> {}".format(self.variables[x],self.partial_equations[x]))


    def marginal_probabilities(self):
    """
    This function will be mildly complicated. We break it down into the following steps:
    (1) we first determine how many variables we are computing for. We will begin with base case n=2

    """


#a = multi_cts_pf("abc",['x','y'])

x,y = sym.symbols("x y",real =True)


int_partial_x = sym.integrate(4*x*y,y)
int_partial_y = sym.integrate(4*x*y,x)


print(int_partial_x)
print(int_partial_y)


print()

"""
def function_parser(function: str):
    for char in function:
        if
"""