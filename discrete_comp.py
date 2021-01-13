"""
This file will be our discrete computations file
THIS IS FOR NUMERICAL COMPUTATIONS
"""
import math
import sympy as sym
from scipy import stats
"""
Core computations. Need to include permuations.
"""
lam ,x, k = sym.symbols("lam x k",real = True)

def factorial(n: int)->int:
    if n==1:
        return n
    else:
        return n*factorial(n-1)

def combinations(total_trials: int, specific_outcomes: int)->int:
    return factorial(total_trials)/(factorial(total_trials-specific_outcomes)*factorial(specific_outcomes))

def square_list(values: list):
    squared_list = []
    for element in values:
        squared_list.append(element**2)
    return squared_list

def discrete_expected_value(values: list, probabilities: list)->float:
    expected = 0
    for x in range (0,len(values)):
        expected += values[x] * probabilities[x]
    return expected
#integrate in class form
def discrete_variance_one(values: list, probabilities: list)->float:
    variance = 0
    expect = discrete_expected_value(values,probabilities)
    for x in range(0,len(values)):
        variance += ((expect-values[x])**2) * probabilities[x]
    return variance
def discrete_variance_two(values: list, probabilities: list)->float:
    variance = 0
    expect = discrete_expected_value(values,probabilities)
    expect_squared = discrete_expected_value(square_list(values),probabilities)
    variance = expect_squared - expect**2
    return variance

"""
Discrete distributions:
"""
def discrete_bernoulli_distribution(probability_p: float, num_trials: int):
    return (probability_p**num_trials) * (1-probability_p)**(1-num_trials)

#bernouilli or binomial
def discrete_binomial_distributiion(total_trials: int, specific_outcomes:int, probability_p: float):
    return combinations(total_trials,specific_outcomes) * probability_p**specific_outcomes * \
           (1-probability_p)**(total_trials-specific_outcomes)
#do
def discrete_geometric_distribution(k: int, probability_p: float):
    return (1-probability_p)**(k-1) * probability_p

def discrete_negative_binomial(probability_p: float, r_attepts_tried, k_total_attepts):
    return combinations(k_total_attepts,r_attepts_tried) * probability_p**r_attepts_tried *(1-probability_p)**(k_total_attepts-r_attepts_tried)
#look into below
def discrete_hypergeometric(r,k,m,n):
    return combinations(r,k)*combinations(n-r,m-k)/combinations(n,m)
#positive
def discrete_poission_distribution(parameter_lambda: int, k_num_times_event_occurs: int):
    return parameter_lambda**k_num_times_event_occurs*math.exp(-parameter_lambda)/factorial(k_num_times_event_occurs)

print(discrete_poission_distribution(.6,3))