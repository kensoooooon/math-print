from random import choice, randint, random

import sympy as sy

class HS1QuadraticFunctionProblem:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._given_information_list = settings["given_information_list"]
        self._character = {}
        self._character["x"] = sy.Symbol("x", real=True)
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        selected_given_information = choice(self._given_information_list)
        
        if selected_given_information == "vertex_and_one_point":
            latex_answer, latex_problem = self._make_vertex_and_one_point_problem()
        """
        elif selected_given_information == "three_points":
            latex_answer, latex_problem = self._make_three_points_problem()
        elif selected_given_information == "the_axis_of_symmetry_and_two_points":
            latex_answer, latex_problem = self._make_axis_and_two_points_problem()
        elif selected_given_information == "before_parabora_and_line_or_parabora_containing_vertex_and_one_point":
            latex_answer, latex_problem = self._make_before_parabora_problem()
        """    
        return latex_answer, latex_problem
    
    def _make_vertex_and_one_point_problem(self):
        x = self._character["x"]
        
        x_coordinate_of_vertex = self._make_random_number()
        y_coordinate_of_vertex = self._make_random_number()
        coefficient_of_quadratic = self._make_random_number()
        
        quadratic_function = coefficient_of_quadratic * (x - x_coordinate_of_vertex) ** 2 + y_coordinate_of_vertex
        expanded_quadratic_function = sy.expand(quadratic_function)
        latex_answer = f"\( y = {sy.latex(expanded_quadratic_function)} \)"
        
        x_coordinate_for_substitution = self._make_random_number()
        if x_coordinate_for_substitution == x_coordinate_of_vertex:
            x_coordinate_for_substitution += randint(1, 3)
        y_coordinate_after_substitution = expanded_quadratic_function.subs(x, x_coordinate_for_substitution)
        
        latex_problem = f"""
        頂点の座標が\( \left( {sy.latex(x_coordinate_of_vertex)}, {sy.latex(y_coordinate_of_vertex)} \\right) \)で、
        点\( \left( {sy.latex(x_coordinate_for_substitution)}, {sy.latex(y_coordinate_after_substitution)} \\right) \)
        を通る。
        """
        
        return latex_answer, latex_problem
    
    def _make_random_number(self, integer_or_frac=None, positive_or_negative=None):
        
        def _make_positive_integer():
            integer = sy.Integer(randint(1, 6))          
            return integer

        def _make_positive_frac():
            while True:
                numerator = randint(2, 7)
                denominator = randint(2, 7)
                frac = sy.Rational(numerator, denominator)
                if frac.denominator != 1:
                    break
            return frac
        
        if integer_or_frac == "integer":
            number = _make_positive_integer()
        elif integer_or_frac == "frac":
            number = _make_positive_frac()
        elif integer_or_frac is None:
            if random() > 0.5:
                number = _make_positive_integer()
            else:
                number = _make_positive_frac()
        
        if positive_or_negative == "negative":
            number = -1 * number
        
        return number