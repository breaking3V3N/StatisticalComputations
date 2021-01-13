import sympy as sym

"""
Objectives of program can be expressed as follows
    X(1) WE ARE GIVEN TWO FUNCTIONS: f,g with their respective domains
    
    X(2) We need to solve for x given an expression of the form y =
    
    X(3) plug inverse obtained from (2) into (f).[function composition]
    
    (4) Compute derivative ABS VAL
    
    (5) We now need to compute our new bounds for the equation i.e if dom(x) = [a,b], 
    then what domain can we equip to y so that our range of y is consistent with our dom(x)
    
    (6) Verify Monotonicity
"""
# initializes required symbols needed for computation
x, y = sym.symbols("x y", real=True)


class function_manip:

    def __init__(self, x_bounds: list, x_function: sym.exp, y_function: sym.exp):
        self.f_function = x_function
        self.xlb = x_bounds[0]
        self.xub = x_bounds[1]
        self.g_function = y_function
        self.g_inverse = self.inverse_solve()
        self.f_o_g = self.function_composition()
        self.dx_dy = sym.diff(self.g_inverse, y)
        self.ylb = self.compute_new_bounds()[0]
        #self.ismonotonic = self.monotonicity_check()
        self.yub = self.compute_new_bounds()[1]
        # This function inputs a function and solves for its inverse.
        # function inputs some expression y = g(x)
        # outputs x= g^-1(y)

    def monotonicity_check(self):
        return sym.solve(sym.diff(self.g_function,x),x)

    def inverse_solve(self) -> sym.exp:
        """
        THIS IS STEP(2) of the process.
        :return:
        """
        eq1 = sym.Eq(self.g_function - y, 0)
        sol = sym.solve(eq1, x)[0]
        return sol

    """
    Step three of process
    """

    def function_composition(self):
        return self.f_function.xreplace({x: self.g_inverse})

    # need to implement dx/dy component\\\DONE
    def compute_new_bounds(self):
        return [sym.solve(self.g_inverse - self.xlb, y),sym.solve(self.xub - self.g_inverse,y)]
        #return sym.solve(self.f_o_g * self.dx_dy - self.xlb,y)



    def print_inverse(self):
        print(self.g_inverse)

    def print_composition(self):
        print(self.f_o_g)


a = function_manip([0, 3], (x+1)/8, x**2)
a.print_inverse()
a.print_composition()
print(sym.simplify(a.dx_dy * a.f_o_g))#PDF for y
print(a.ylb)#new bounds
print(a.monotonicity_check())
"""

x, y = symbols('x y') 
  
f = sin(x) + cos(2 * x) 
# Use sympy.xreplace() method 
gfg = f.xreplace({2 * x : y}) 
     
print(gfg) 

"""
