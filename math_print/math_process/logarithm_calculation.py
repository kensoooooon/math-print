from random import choice, randint, random, shuffle

import sympy as sy

"""
import sympy as sy

class Log:
    
    def __init__(self, base_numerator, antilog_numerator, base_denominator=1, antilog_denominator=1):
        base = sy.Rational(base_numerator, base_denominator)
        antilog = sy.Rational(antilog_numerator, antilog_denominator)
        if (base <= 0) or (antilog <= 0):
            raise ValueError(f"base must be more than 0, and antilog must also be more than 0.")
            
        self.base = base
        self.antilog = antilog
        self.coefficient = 1
    
    def __str__(self):
        return f"\log_{{{self.base}}} {self.antilog}"
    
    def __add__(self, other_num):
        print("Log's add")
        if isinstance(other_num, Log):
            if self.base == other_num.base:
                new_antilog = self.antilog * other_num.antilog
                return Log(self.base, new_antilog)
            else:
                return AddedLog(self, other_num)

            
class AddedLog:
    
    def __init__(self, one_num, other_num):
        # one_num and other_num should be log

        # defaultdict{2
        
        # change to dictionary?
        self.added_log_list = []
        self.added_log_list.append(one_num)
        self.added_log_list.append(other_num)
    
    def __str__(self):
        returned_str = ""
        for index, num in enumerate(self.added_log_list):
            if index == 0:
                returned_str += str(num)
            else:
                returned_str += f"+ {str(num)}"
        return returned_str
    
    def __add__(self, other_num):
        print("AddedLog's add!")
        if isinstance(other_num, Log):
            self.added_log_list.append(other_num)
        elif isinstance(other_num, AddedLog):
            self.added_log_list += other_num.added_log_list
        return self



num1 = Log(2, 3)
num2 = Log(3, 5)
add1 = num1 + num2
num3 = Log(7, 11)
num4 = Log(11, 17)
add2 = num3 + num4
print(add1 + add2)
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
        elif selected_problem_type == "add_and_subtraction_with_change_of_base_formula":
            latex_answer, latex_problem = self._make_add_and_subtraction_with_change_of_base_formula()
        
        return latex_answer, latex_problem
    
    def _make_change_of_base_problem(self):
        common_base = choice([2, 3, 5, 7])
        logarithm_base = common_base ** randint(2, 10 - common_base)
        logarithm_antilog = common_base ** randint(2, 10 - common_base)
        latex_problem = f"\log_{{{logarithm_base}}} {logarithm_antilog}"
        
        denominator = int(sy.log(logarithm_base, common_base))
        numerator = int(sy.log(logarithm_antilog, common_base))
        answer = sy.Rational(numerator, denominator)
        latex_answer = f" = {sy.latex(answer)}"
        
        return latex_answer, latex_problem
    
    def _make_add_and_subtraction_without_change_of_base_formula(self):

        def random_pop_from_two_list(list1, list2):
            while True:
                if not(list1):
                    selected_list = list2
                    selected_type = "minus"
                elif not(list2):
                    selected_list = list1
                    selected_type = "plus"
                else:
                    if random() > 0.5:
                        selected_list = list1
                        selected_type = "plus"
                    else:
                        selected_list = list2
                        selected_type = "minus"
                popped_value = selected_list.pop()
                yield (popped_value, selected_type)
                
                if not(list1) and not(list2):
                    break

        base_and_antilog_list = [2, 3, 5, 7, 11]
        common_base = choice(base_and_antilog_list)

        numerator_list = []
        denominator_list = []

        for _ in range(4):
            if random() > 0.6:
                antilog_base = common_base
                if random() > 0.5:
                    numerator_list.append(antilog_base)
                else:
                    denominator_list.append(antilog_base)
            else:
                antilog_base = choice(base_and_antilog_list)
                numerator_list.append(antilog_base)
                denominator_list.append(antilog_base)
                
        multiplied_logarithm_antilog_list = []
        first_num = numerator_list.pop()
        multiplied_logarithm_antilog_list.append(first_num)

        for num in numerator_list:
            if random() > 0.5:
                multiplied_logarithm_antilog_list.append(num)
            else:
                multiplied_logarithm_antilog_list[-1] = num * multiplied_logarithm_antilog_list[-1]


        divided_logarithm_antilog_list = []
        first_num = denominator_list.pop()
        divided_logarithm_antilog_list.append(first_num)

        for num in denominator_list:
            if random() > 0.3:
                divided_logarithm_antilog_list.append(num)
            else:
                divided_logarithm_antilog_list[-1] = num * divided_logarithm_antilog_list[-1]

        shuffle(multiplied_logarithm_antilog_list)
        shuffle(divided_logarithm_antilog_list)

        antilog_numerator = 1
        for antilog in multiplied_logarithm_antilog_list:
            antilog_numerator = antilog_numerator * antilog

        antilog_denominator = 1
        for antilog in divided_logarithm_antilog_list:
            antilog_denominator = antilog_denominator * antilog

        frac = sy.Rational(antilog_numerator, antilog_denominator)

        log = sy.log(frac, common_base)

        problem = ""
        first_antilog = multiplied_logarithm_antilog_list.pop()
        problem += f"\log_{{{common_base}}} {first_antilog}"

        for antilog, selected_type in random_pop_from_two_list(multiplied_logarithm_antilog_list, divided_logarithm_antilog_list):
            if selected_type == "plus":
                problem += f"+ \log_{{{common_base}}} {antilog}"
            elif selected_type == "minus":
                problem += f"- \log_{{{common_base}}} {antilog}"
        
        latex_answer = f"= {sy.latex(log)}"
        latex_problem = problem
        
        return latex_answer, latex_problem
    
    def _make_add_and_subtraction_with_change_of_base_formula(self):
        latex_answer = "=3"
        latex_problem = "1+2"
        
        return latex_answer, latex_problem
    