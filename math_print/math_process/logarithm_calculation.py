from random import choice, randint

import sympy as sy

"""
one idea: log making

# self definition of logarithm
import sympy as sy

class Log:
    
    def __init__(self, base_numerator, antilog_numerator, base_denominator=1, antilog_denominator=1):
        base = sy.Rational(base_numerator, base_denominator)
        antilog = sy.Rational(antilog_numerator, antilog_denominator)
        if (base <= 0) or (antilog < 0):
            raise ValueError(f"base must be more than 0, and antilog must be 0 or more than 0.")
            
        self.base = base
        self.antilog = antilog
    
    def __str__(self):
        return f"log_{self.base} {self.antilog}"
    
    def __add__(self, other_log):
        # same base
        if self.base == other_log.base:
            return Log(self.base, self.antilog * other_log.antilog)
        # different base but can be same base
    
    def __sub__(self, other_log):
        # same base
        if self.base == other_log.base:
            return Log(self.base, sy.Rational(self.antilog / other_log.antilog))

num = Log(2, 5)
print(num)
num2 = Log(2, 3)
print(num + num2)
print(num - num2)
print(num ** 3)
"""

class LogarithmCalculationProblem:
    
    def __init__(self, **settings):
        self._problem_type_list = settings["problem_type_list"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        selected_problem_type = choice(self._problem_type_list)
        
        if selected_problem_type == "change_of_base_formula":
            latex_answer, latex_problem = self._make_change_of_base_problem()
        elif selected_problem_type == "add_and_subtraction_without_change_of_base_formula":
            latex_answer, latex_problem = self._make_add_and_subtraction_without_change_of_base_formula()
        
        return latex_answer, latex_problem
    
    def _make_change_of_base_problem(self):
        common_base = choice([2, 3, 5, 7])
        logarithm_base = common_base ** randint(2, 10 - common_base)
        logarithm_antilog = common_base ** randint(2, 10 - common_base)
        latex_problem = f"\log_{{{logarithm_base}}} {logarithm_antilog}"
        print(f"latex_problem: {latex_problem}")
        
        denominator = int(sy.log(logarithm_base, common_base))
        numerator = int(sy.log(logarithm_antilog, common_base))
        answer = sy.Rational(numerator, denominator)
        latex_answer = f" = {sy.latex(answer)}"
        print(f"latex_answer: {latex_answer}") 
        
        return latex_answer, latex_problem
    
    def _make_add_and_subtraction_without_change_of_base_formula(self):
        common_base = choice([2, 3, 5, 7, 11, 13])
        latex_answer = "14332"
        latex_problem = "202948"
        
        return latex_answer, latex_problem
    