from random import choice, randint, random

import sympy as sy

class FractionCalculateProblem:
    
    def __init__(self, **settings):
        self._calculate_types_list = settings["calculate_types_list"]
        self._fraction_type_list = settings["fraction_type_list"]
        self._term_number = settings["term_number"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        
        
        return latex_answer, latex_problem

    def _make_positive_integer_number(max_num, min_num):
        
        integer = randint(min_num, max_num)
        
        return sy.Integer(integer)
    
    def _make_positive_frac_number(max_num, min_num)