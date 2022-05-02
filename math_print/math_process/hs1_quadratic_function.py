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
        elif selected_given_information == "three_points":
            latex_answer, latex_problem = self._make_three_points_problem()
        elif selected_given_information == "the_axis_of_symmetry_and_two_points":
            latex_answer, latex_problem = self._make_axis_and_two_points_problem()
        elif selected_given_information == "before_parabora_and_line_or_parabora_containing_vertex_and_one_point":
            latex_answer, latex_problem = self._make_before_parabora_problem()
        return latex_answer, latex_problem
    
    def _make_vertex_and_one_point_problem(self):
        x = self._character["x"]
        
        x_coordinate_of_vertex = self._make_random_number(max_num=3)
        y_coordinate_of_vertex = self._make_random_number(max_num=3)
        coefficient_of_quadratic = self._make_random_number(max_num=3)
        
        quadratic_function = coefficient_of_quadratic * (x - x_coordinate_of_vertex) ** 2 + y_coordinate_of_vertex
        expanded_quadratic_function = sy.expand(quadratic_function)
        latex_answer = f"\( y = {sy.latex(expanded_quadratic_function)} \)"
        
        x_coordinate_for_substitution = self._make_random_number(max_num=4)
        if x_coordinate_for_substitution == x_coordinate_of_vertex:
            x_coordinate_for_substitution += randint(1, 3)
        y_coordinate_after_substitution = expanded_quadratic_function.subs(x, x_coordinate_for_substitution)
        
        x_vertex_latex = sy.latex(x_coordinate_of_vertex)
        y_vertex_latex = sy.latex(y_coordinate_of_vertex)
        x1 = sy.latex(x_coordinate_for_substitution)
        y1 = sy.latex(y_coordinate_after_substitution)
        
        latex_problem = f"頂点の座標が\( \left( {x_vertex_latex}, {y_vertex_latex} \\right) \)で、"\
        f"\( \left( {x1}, {y1} \\right) \)を通る。"

        return latex_answer, latex_problem
    
    def _make_three_points_problem(self):
        x = self._character["x"]
        a_num = self._make_random_number(integer_or_frac="integer")
        b_num = self._make_random_number(integer_or_frac="integer")
        c_num = self._make_random_number(integer_or_frac="integer")
        
        quadratic_function = a_num * x ** 2 + b_num * x + c_num
        latex_answer = f"\(y = {sy.latex(quadratic_function)}\)"
        
        x1 = self._make_random_number(integer_or_frac="integer", max_num=2)
        y1 = quadratic_function.subs(x, x1)
        x2 = self._make_random_number(integer_or_frac="integer", max_num=2)
        if x1 == x2:
            x2 += self._make_random_number(integer_or_frac="integer", max_num=2)
        y2 = quadratic_function.subs(x, x2)
        x3 = self._make_random_number(integer_or_frac="integer", max_num=2)
        if x2 == x3:
            x3 += self._make_random_number(integer_or_frac="integer", max_num=2)
        y3 = quadratic_function.subs(x, x3)
        
        x1_latex = sy.latex(x1)
        y1_latex = sy.latex(y1)
        x2_latex = sy.latex(x2)
        y2_latex = sy.latex(y2)
        x3_latex = sy.latex(x3)
        y3_latex = sy.latex(y3)
        
        latex_problem = f"3点\( \left( {x1_latex}, {y1_latex} \\right),  \left( {x2_latex},"\
        f"{y2_latex} \\right), \left( {x3_latex}, {y3_latex} \\right) \)を通る。"
        
        return latex_answer, latex_problem
    
    def _make_axis_and_two_points_problem(self):
        # a(x - axis) ** 2 + b
        x = self._character["x"]
        a_num = self._make_random_number(integer_or_frac="integer")
        axis = self._make_random_number(max_num=3)
        b_num = self._make_random_number()
        
        quadratic_function = sy.expand(a_num * (x - axis) ** 2 + b_num)
        latex_answer = f"\( y = {sy.latex(quadratic_function)} \)"
        
        x1 = self._make_random_number(integer_or_frac="integer", max_num=2)
        y1 = quadratic_function.subs(x, x1)
        x2 = self._make_random_number(integer_or_frac="integer", max_num=2)
        if x1 == x2:
            x2 += self._make_random_number(integer_or_frac="integer", max_num=2)
        y2 = quadratic_function.subs(x, x2)
        
        x1_latex = sy.latex(x1)
        y1_latex = sy.latex(y1)
        x2_latex = sy.latex(x2)
        y2_latex = sy.latex(y2)
        axis_latex = sy.latex(axis)
        
        latex_problem = f"軸が直線 \( x = {axis_latex} \)で、"\
        f"\( \left( {x1_latex}, {y1_latex} \\right),  \left( {x2_latex}, {y2_latex} \\right) \)を通る"
        
        return latex_answer, latex_problem
    
    def _make_before_parabora_problem(self):
        """
        parallel 
        vertex is on the parabora or line.
        one point
        """
        x = self._character["x"]
        a_num = self._make_random_number(max_num=4, min_num=4)
        # y = ax^2....
        # t -> t decide
        # x_vertex = self._make_random_number(max_num=4, integer_or_frac="integer")
        vertex_function_checker = choice(["linear", "parabora"])
        if vertex_function_checker == "linear":
            # y = ax + b
            linear_for_vertex = self._make_random_number(max_num=3, integer_or_frac="integer") * x + self._make_random_number(max_num=3, integer_or_frac="integer")
            x_vertex1 = self._make_random_number()
            y_vertex1 = linear_for_vertex.subs(x, x_vertex1)
            quadratic_function1 = sy.expand(a_num * (x - x_vertex1) ** 2 + y_vertex1)
            latex_answer = f"\( y = {sy.latex(quadratic_function1)} \)"
            x1 = self._make_random_number(integer_or_frac="integer", max_num=3)
            y1 = quadratic_function1.subs(x, x1)
            latex_problem = f"放物線\( y = {sy.latex(a_num)} x^2 \)を平行移動した曲線で、"\
            f"点\( \left( {sy.latex(x1)}, {sy.latex(y1)} \\right) \)を通り、\n"\
            f"頂点が直線\( y = {sy.latex(linear_for_vertex)} \)上にある。"
        elif vertex_function_checker == "parabora":
            # y = ax^2 + bx + c
            quadratic_function_for_vertex = self._make_random_number(max_num=2, integer_or_frac="integer") * x ** 2 + self._make_random_number(max_num=3, integer_or_frac="integer") * x + self._make_random_number(max_num=3, integer_or_frac="integer")
            x_vertex1 = self._make_random_number()
            y_vertex1 = quadratic_function_for_vertex.subs(x, x_vertex1)
            x_vertex2 = self._make_random_number()
            y_vertex2 = quadratic_function_for_vertex.subs(x, x_vertex2)
            quadratic_function1 = sy.expand(a_num * (x - x_vertex1) ** 2 + y_vertex1)
            print(f"quadratic_function1: {quadratic_function1}")
            quadratic_function2 = sy.expand(a_num * (x - x_vertex2) ** 2 + y_vertex2)
            print(f"quadratic_function2: {quadratic_function2}")
            latex_answer = f"\( y = {sy.latex(quadratic_function1)} \)\n"\
            f"\( y = {sy.latex(quadratic_function2)}\)"
            x1 = self._make_random_number(integer_or_frac="integer", max_num=3)
            y1 = quadratic_function1.subs(x, x1)
            # x2 = self._make_random_number(integer_or_frac="integer", max_num=3)
            y2 = quadratic_function2.subs(x, x1)
            if (y1 != y2):
                raise ValueError(f"y1: {y1}, y2: {y2}")
            latex_answer = f"放物線\( y = {sy.latex(a_num)} x^2 \)を平行移動した曲線で、"\
            f"点\( \left( {sy.latex(x1)}, {sy.latex(y1)} \\right) \)を通り、\n"\
            f"頂点が放物線\( y = {sy.latex(quadratic_function_for_vertex)} \)上にある。"

        return latex_answer, latex_problem
    
    def _make_random_number(self, integer_or_frac=None, positive_or_negative=None, max_num=None, min_num=None):
        if max_num is None:
            max_num = 6
        if min_num is None:
            min_num = 1
            
        if max_num == min_num:
            max_num += 1
        
        def _make_positive_integer():
            integer = sy.Integer(randint(min_num, max_num))          
            return integer

        def _make_positive_frac():
            while True:
                numerator = randint(min_num, max_num)
                denominator = randint(min_num, max_num)
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