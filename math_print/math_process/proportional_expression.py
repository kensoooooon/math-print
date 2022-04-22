from random import choice, randint, random

import sympy as sy

class ProportionalExpressionProblem:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._used_number_type_list = settings["used_number_type_list"]
        self._proportional_expression_type = settings["proportional_expression_type"]
        if self._proportional_expression_type == 'x_and_y':
            self.latex_answer, self.latex_problem = self._make_x_and_y()
        
    def _make_x_and_y(self):
        x_checker = self._number_type_selector()
        
        if x_checker == "integer":
            x, x_latex = self._make_random_integer_number(8, -8)
        elif x_checker == "frac":
            x, x_latex = self._make_random_frac_number(8, -8)
        
        a_checker = self._number_type_selector()
        
        if a_checker == "integer":
            a, a_latex = self._make_random_integer_number(8, -8)
        elif a_checker == "frac":
            a, a_latex = self._make_random_frac_number(8, -8)
        
        y = a * x
        y_latex = sy.latex(y)
        
        latex_answer = f"a = {a_latex}"
        
        latex_problem = f"x = {x_latex}, y = {y_latex}"
        
        return latex_answer, latex_problem

    def _number_type_selector(self):
        if self._used_number_type_list:
            selected_number_type = choice(self._used_number_type_list)
        else:
            selected_number_type = choice(["integer", "frac"])
        return selected_number_type

    def _make_random_frac_number(self, max_num, min_num):
        checker = random()
        if checker > 0.5:
            numerator = randint(2, max_num)
            denominator = randint(2, max_num)
        else:
            numerator = randint(min_num, -2)
            denominator = randint(2, max_num)
        
        frac = sy.Rational(numerator, denominator)

        frac_with_number_latex = sy.latex(frac)
        return frac, frac_with_number_latex

    
    def _make_random_integer_number(self, max_num, min_num):
        checker = random()
        if checker > 0.5:
            numerator = randint(1, max_num)
        else:
            numerator = randint(min_num, -1)
        
        integer = sy.Integer(numerator)

        integer_with_number_latex = sy.latex(integer)
        return integer, integer_with_number_latex
