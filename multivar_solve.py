import sympy as sym
import scipy


class m_function:
    def __init__(self, function: sym.exp,bound_list: list):
        self.func = function
        self.bounds = bound_list

    def compute_bounds(self):
