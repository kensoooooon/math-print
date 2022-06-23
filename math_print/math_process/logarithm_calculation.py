from random import choice, randint

import sympy as sy

"""
one idea: log making

# self definition of logarithm
# self definition of logarithm
import sympy as sy

class Log:
    
    def __init__(self, base_numerator, antilog_numerator, base_denominator=1, antilog_denominator=1, coefficient=1, other_part=0):
        base = sy.Rational(base_numerator, base_denominator)
        antilog = sy.Rational(antilog_numerator, antilog_denominator)
        if (base <= 0) or (antilog < 0):
            raise ValueError(f"base must be more than 0, and antilog must be 0 or more than 0.")
            
        self.base = base
        self.antilog = antilog
        self.coefficient = coefficient
        self.other_part = other_part
    
    def __str__(self):
        log_str = ""
        if self.coefficient != 0:
            if self.coefficient == 1:
                log_str += f"log_{self.base}({self.antilog})"
            else:
                log_str += f"{self.coefficient} * log_{self.base} {self.antilog}"
        if self.other_part != 0:
            if self.other_part > 0:
                log_str += f"+{self.other_part}"
            else:
                log_str += f"{self.other_part}"
        
        return log_str
    
    def __add__(self, other_num):
        # same base
        if isinstance(other_num, Log):
            if self.base == other_num.base:
                return Log(self.base, self.antilog * other_num.antilog)
        else:
            new_other_part = self.other_part + other_num
            return Log(self.base, self.antilog, other_part=new_other_part)
    
    def __sub__(self, other_num):
        # same base
        if isinstance(other_num, Log):
            if self.base == other_num.base:
                return Log(self.base, self.antilog / other_num.antilog)
        else:
            new_other_part = self.other_part - other_num
            return Log(self.base, self.antilog, other_part=new_other_part)
            
    
    def __mul__(self, other_num):
        new_coefficient = self.coefficient * other_num
        return Log(self.base, self.antilog, coefficient=new_coefficient)
    
    # def change_of_base_formula(self, new_base):
        

num1 = Log(2, 5)
print(f"type: {type(num1)}")
print(num1)
print(num1 + 2)
print(num1 - 3)
num2 = Log(2, 11)
print(num1 + num2)
num3 = Log(2, 2)
print(num1 + num2 + num3)
print(3 * num1)
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
    