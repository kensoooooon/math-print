from random import randint, choice
from typing import Dict, Tuple


import sympy as sy


class DivisionOfDecimalFor4thGrade:
    def __init__(self, **settings):
        sy.init_printing(order="grevlex")
        selected_divided_number_of_decimal_places = choice(settings["divided_numbers_of_decimal_places"])
        selected_dividing_number_of_decimal_places = choice(settings["dividing_numbers_of_decimal_places"])
        self.latex_answer, self.latex_problem = self._make_problem(selected_divided_number_of_decimal_places, selected_dividing_number_of_decimal_places)
    
    def _make_problem(self, divided_number_of_decimal_places, dividing_number_of_decimal_places):
        latex_answer = "dummy answer"
        latex_problem = "dummy problem"
        return latex_answer, latex_problem
