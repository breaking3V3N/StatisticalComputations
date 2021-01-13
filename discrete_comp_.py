import sympy as sym


def poission_distribution(lambda_param: sym.symbols, k_times: sym.symbols):
    sum = sym.Sum(lambda_param ** k_times * sym.exp(-k_times)/sym.factorial(k_times))
    return sum.doit()
print(poission_distribution(.6,3))