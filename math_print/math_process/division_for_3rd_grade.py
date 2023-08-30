"""
8/30
側作成
"""
from random import choice

import sympy as sy


class DivisionFor3rdGrade:
    def __init__(self, **settings):
        sy.init_printing(order="grevlex")
        selected_remainder_type = choice(settings["remainder_types"])
        selected_digit_of_divided_number = int(choice(settings["digit_of_divided_numbers"]))
        self.latex_answer, self.latex_problem = self._make_problem(selected_remainder_type, selected_digit_of_divided_number)
    
    def _make_problem(self, selected_remainder_type, selected_digit_of_divided_number):
        latex_answer = "dummy answer"
        latex_problem = "dummy problem"
        return latex_answer, latex_problem
    