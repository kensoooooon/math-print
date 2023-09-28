from random import choice, randint

import sympy as sy

class AdditionAndSubtractionOfFraction:
    def __init__(self, **settings):
        sy.init_printing(order="grevlex")
        selected_calculation = choice(settings["used_calculation"])
        selected_integer_part = choice(settings["integer_part"])
        if selected_integer_part == "with_integer_part":
            with_integer_part = True
        elif selected_integer_part == "without_integer_part":
            with_integer_part = False
        if selected_calculation == "addition":
            self.latex_answer, self.latex_problem = self._make_addition_problem(with_integer_part)
        elif selected_calculation == "subtraction":
            self.latex_answer, self.latex_problem = self._make_subtraction_problem(with_integer_part)
        elif selected_calculation == "fill_in_the_square":
            self.latex_answer, self.latex_problem = self._make_fill_in_the_square_problem(with_integer_part)
        else:
            raise ValueError(f"'selected_calculation' is {selected_calculation}. It must be 'addition', 'subtraction' or 'fill_in_the_square'.")
    
    def _make_addition_problem(self, with_integer_part):
        latex_answer = "dummy answer in addition problem"
        latex_problem = "dummy problem in addition problem"
        return latex_answer, latex_problem
    
    def _make_subtraction_problem(self, with_integer_part):
        latex_answer = "dummy answer in subtraction problem"
        latex_problem = "dummy problem in subtraction problem"
        return latex_answer, latex_problem
    
    def _make_fill_in_the_square_problem(self, with_integer_part):
        latex_answer = "dummy answer in fill_in_the_square problem"
        latex_problem = "dummy problem in fill_in_the_square problem"
        return latex_answer, latex_problem
    