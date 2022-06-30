from random import choice, randint, random

import sympy as sy

"""
# inheritance?
import sympy as sy

class Log:
    
    def __init__(self, base_numerator, antilog_numerator, base_denominator=1, antilog_denominator=1):
        base = sy.Rational(base_numerator, base_denominator)
        antilog = sy.Rational(antilog_numerator, antilog_denominator)
        if (base <= 0) or (antilog < 0):
            raise ValueError(f"base must be more than 0, and antilog must be 0 or more than 0.")
            
        self.base = base
        self.antilog = antilog
        self.other_log_part = 0  # = 0
    
    def __str__(self):
        return f"\log_{{{self.base}}} {self.antilog}"
    
    def __add__(self, other_num):
        if isinstance(other_num, Log):
            if self.base == other_num.base:
                return Log(self.base, self.antilog * other_num.antilog)
        else:
            new_antilog = self.base ** other_num
            return Log(self.base, self.antilog * new_antilog)
    
    def __radd__(self, other_num):
        new_antilog = self.base ** other_num
        return Log(self.base, new_antilog * self.antilog)
    
    def __sub__(self, other_num):
        if isinstance(other_num, Log):
            if self.base == other_num.base:
                return Log(self.base, self.antilog / other_num.antilog)
        else:
            new_antilog = self.base ** other_num
            return Log(self.base, self.antilog / new_antilog)
    
    def __rsub__(self, other_num):
        new_antilog = self.base ** other_num
        return Log(self.base, new_antilog / self.antilog)
    
    def __mul__(self, other_num):
        if not(isinstance(other_num, Log)):
            new_antilog = self.antilog ** other_num
            return Log(self.base, new_antilog)
    
    def __rmul__(self, other_num):
        new_antilog = self.antilog ** other_num
        return Log(self.base, new_antilog)
        

            
num1 = Log(2, 3)
num2 = Log(2, 5)
print(num1 + num2)
print(num1 - num2)
print(num1 + 2)
print(2 + num1)
print(num1 - 2)
print(2 - num1)
print(2 * num1)
print(num1 * 2)
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
        """
        # not use pop
        from random import choice, randint, random

        base_and_antilog_list = [2, 3, 5, 7, 11, 13]
        common_base = choice(base_and_antilog_list)
        print(common_base)

        numerator_list = []
        denominator_list = []

        for _ in range(5):
            if random() > 0.7:
                antilog_base = common_base
                if random() > 0.5:
                    numerator_list.append(antilog_base)
                else:
                    denominator_list.append(antilog_base)
            else:
                antilog_base = choice(base_and_antilog_list)
                numerator_list.append(antilog_base)
                denominator_list.append(antilog_base)

        print(f"numerator_list: {numerator_list}")
        print(f"denominator_list: {denominator_list}")

        multiplied_logarithm_antilog_list = []
        first_num = numerator_list.pop()
        multiplied_logarithm_antilog_list.append(first_num)

        for num in numerator_list:
            if random() > 0.5:
                multiplied_logarithm_antilog_list.append(num)
            else:
                multiplied_logarithm_antilog_list[-1] = num * multiplied_logarithm_antilog_list[-1]

        print(f"multiplied_logarithm_antilog_list: {multiplied_logarithm_antilog_list}")

        divided_logarithm_antilog_list = []
        first_num = denominator_list.pop()
        divided_logarithm_antilog_list.append(first_num)

        for num in denominator_list:
            if random() > 0.3:
                divided_logarithm_antilog_list.append(num)
            else:
                divided_logarithm_antilog_list[-1] = num * divided_logarithm_antilog_list[-1]

        print(f"divided_logarithm_antilog_list: {divided_logarithm_antilog_list}")
        """
            
            
        
        return latex_answer, latex_problem
    