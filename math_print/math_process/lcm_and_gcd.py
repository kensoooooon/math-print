"""
import math

import sympy as sy

def divisors(x, y):
    gcd = math.gcd(x, y)
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= gcd:
        if gcd % i == 0:
            lower_divisors.append(i)
            if i != gcd // i:
                upper_divisors.append(gcd // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def lcms(x, y):
    lst = [((x * y) // math.gcd(x, y)) * i for i in range(1, 6)]
    return lst

def max_indexer(now_num, base_candidate):
    x = sy.Symbol("x", real=True)
    max_value = sy.solve(now_num * base_candidate ** x - 100, x)[0]
    max_index = math.floor(max_value)
    return max_index

for _ in range(5):
    bases = [2, 3, 4, 5, 6, 7, 8]
    num1, num2 = 1, 1
    for base in bases:
        print(f"base: {base}")
        min_index = 0
        max_index1 = max_indexer(num1, base)
        max_index2 = max_indexer(num2, base)
        num1_index = random.randint(min_index, max_index1)
        num2_index = random.randint(min_index, max_index2)
        num1 *= (base ** num1_index)
        num2 *= (base ** num2_index)
    print(f"num1: {num1}")
    print(f"num2: {num2}")
    print(f"divisors: {divisors(num1, num2)}")
    print(f"lcms: {lcms(num1, num2)}")
    print("------------------")

"""

from random import choice

import sympy as sy


class LCMAndGCD:
    
    def __init__(self, **settings):
        self._problem_type_list = settings["problem_type_list"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        selected_problem_type = choice(self._problem_type_list)
        if selected_problem_type == "lcm":
            latex_answer, latex_problem = self._make_lcm_problem()
        elif selected_problem_type == "gcd":
            latex_answer, latex_problem = self._make_gcd_problem()
        return latex_answer, latex_problem
    