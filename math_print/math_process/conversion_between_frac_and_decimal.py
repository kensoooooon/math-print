from random import choice, randint, random

import sympy as sy

class ConversionBetweenFracAndDecimalProblem:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._conversion_type_list = settings["conversion_type_list"]
        self._below_the_decimal_point_list = settings["below_the_decimal_point_list"]
        self.latex_answer, self.latex_problem = self._make_conversion_problem()
    
    def _make_conversion_problem(self):
        if self._conversion_type_list:
            selected_conversion_type = choice(self._conversion_type_list)
        else:
            selected_conversion_type = choice(
                ["frac_to_decimal", "decimal_to_frac"]
            )
        
        if selected_conversion_type == "frac_to_decimal":
            latex_answer, latex_problem = self._make_frac_to_decimal_problem()
        elif selected_conversion_type == "decimal_to_frac":
            latex_answer, latex_problem = self._make_decimal_to_frac_problem()
        
        return latex_answer, latex_problem
    
    def _make_frac_to_decimal_problem(self):
        if self._below_the_decimal_point_list:
            selected_below_the_decimal_point = choice(self._below_the_decimal_point_list)
        else:
            selected_below_the_decimal_point = choice([1, 2])
        frac, decimal = self._make_random_decimal_and_frac_by_frac(selected_below_the_decimal_point)
        
        latex_answer = f"= {sy.latex(decimal)}"
        latex_problem = f"{sy.latex(frac)}"
        
        return latex_answer, latex_problem
    
    def _make_decimal_to_frac_problem(self):
        if self._below_the_decimal_point_list:
            selected_below_the_decimal_point = choice(self._below_the_decimal_point_list)
        else:
            selected_below_the_decimal_point = choice([1, 2])
        frac, decimal = self._make_random_decimal_and_frac_by_frac(selected_below_the_decimal_point)
        
        latex_answer = f"= {sy.latex(frac)}"
        latex_problem = f"{sy.latex(decimal)}"

        return latex_answer, latex_problem

    def _make_random_decimal_and_frac_by_frac(self, selected_below_the_decimal_point):
        if selected_below_the_decimal_point == 1:
            DENOMINATOR = 10
            while True:
                numerator = self._make_random_integer_positive_number(100, 2)
                frac = sy.Rational(numerator, DENOMINATOR)
                
                if frac.denominator != 1:
                    break

        elif selected_below_the_decimal_point == 2:
            DENOMINATOR = 100
            while True:
                numerator = self._make_random_integer_positive_number(100, 2)
                frac = sy.Rational(numerator, DENOMINATOR)
                
                if frac.denominator != 1:
                    break
        
        decimal = float(frac)
        return frac, decimal

    def _make_random_integer_positive_number(self, max_num ,min_num):
        number = randint(min_num, max_num)
        
        integer = sy.Integer(number)
        
        return integer
