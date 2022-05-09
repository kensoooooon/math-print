from random import choice, randint, random
from typing import NamedTuple

import sympy as sy

class HS1QuadraticFunctionMaxMinProblem:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._moving_part_list = settings["moving_part_list"]
        self._max_min_list = settings["max_min_list"]
        self._character = {}
        self._character["x"] = sy.Symbol("x", real=True)
        self._character["y"] = sy.Symbol("y", real=True)
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        selected_moving_part = choice(self._moving_part_list)
        selected_max_min = choice(self._max_min_list)
        
        if selected_moving_part == "the_axis_of_symmetry":
            latex_answer, latex_problem = self._make_the_axis_of_symmetry_problem(max_or_min=selected_max_min)
        elif selected_moving_part == "domain":
            latex_answer, latex_problem = self._make_domain_problem(max_or_min=selected_max_min)

        return latex_answer, latex_problem

    def _make_the_axis_of_symmetry_problem(self, max_or_min):
        """
        domain: fixed
        moving: the axis of symmetry
        """
        x = self._character["x"]
        y = self._character["y"]
        domain_left = self._make_random_number(integer_or_frac="integer")
        domain_right = domain_left + self._make_random_number(integer_or_frac="integer", positive_or_negative="positive")
        print(f"domain_left: {domain_left} domain_right: {domain_right}")
        coefficient_of_x_squared = self._make_random_number(integer_or_frac="integer")
        x_vertex = self._make_random_number(integer_or_frac="integer", max_num=2) * y
        y_vertex = self._make_random_number(integer_or_frac="integer", max_num=3) * y
        quadratic_function_before_collecting = coefficient_of_x_squared * (x - x_vertex) ** 2 + y_vertex
        quadratic_function = sy.collect(sy.expand(quadratic_function_before_collecting), x)
        print(f"quadratic_function: {quadratic_function}")
        if max_or_min == "max":
            problem_mode = "最大値"
        elif max_or_min == "min":
            problem_mode = "最小値" 
        latex_problem = f"\( y = {sy.latex(quadratic_function)} \\quad \)"\
            f"\( \left( {sy.latex(domain_left)} \leqq x \leqq {sy.latex(domain_right)} \\right) \) \n"\
            f"の{problem_mode}を求めよ。"
        patterns_and_values = self._calculate_patterns_with_moving_axis(max_or_min, domain_left, domain_right, quadratic_function)
        
        latex_answer = f"""
        {patterns_and_values.pattern1_latex}のとき、{patterns_and_values.value1_latex}
        {patterns_and_values.pattern2_latex}のとき、{patterns_and_values.value2_latex}
        {patterns_and_values.pattern3_latex}のとき、{patterns_and_values.value3_latex}
        """
        
        return latex_answer, latex_problem
    
    def _make_domain_problem(self, max_or_min):
        print("----------------domain!!!!!!-------------")
        x = self._character["x"]
        y = self._character["y"]
        domain_left = self._make_random_number(integer_or_frac="integer", positive_or_negative="positive") * y
        domain_right = domain_left + self._make_random_number(integer_or_frac="integer", positive_or_negative="positive")
        print(f"domain_left: {domain_left} domain_right: {domain_right}")
        coefficient_of_x_squared = self._make_random_number(integer_or_frac="integer")
        x_vertex = self._make_random_number(integer_or_frac="integer", max_num=2)
        y_vertex = self._make_random_number(integer_or_frac="integer", max_num=3)
        quadratic_function_before_collecting = coefficient_of_x_squared * (x - x_vertex) ** 2 + y_vertex
        quadratic_function = sy.collect(sy.expand(quadratic_function_before_collecting), x)
        print(f"quadratic_function: {quadratic_function}")
        if max_or_min == "max":
            problem_mode = "最大値"
        elif max_or_min == "min":
            problem_mode = "最小値" 
        latex_problem = f"\( y = {sy.latex(quadratic_function)} \\quad \)"\
            f"\( \left( {sy.latex(domain_left)} \leqq x \leqq {sy.latex(domain_right)} \\right) \) \n"\
            f"の{problem_mode}を求めよ。"
        patterns_and_values = self._calculate_patterns_with_moving_domain(max_or_min, domain_left, domain_right, quadratic_function)
        
        latex_answer = f"""
        {patterns_and_values.pattern1_latex}のとき、{patterns_and_values.value1_latex}
        {patterns_and_values.pattern2_latex}のとき、{patterns_and_values.value2_latex}
        {patterns_and_values.pattern3_latex}のとき、{patterns_and_values.value3_latex}
        """
        
        return latex_answer, latex_problem
    
    def _calculate_patterns_with_moving_domain(self, max_or_min, domain_left, domain_right, quadratic_function):
        
        class PatternsAndValues(NamedTuple):
            """
            解答に表示する場合分けと値の組み合わせ
            """
            pattern1_latex : str
            value1_latex : str
            pattern2_latex : str
            value2_latex : str
            pattern3_latex : str
            value3_latex : str

        y = self._character["y"]
        x = self._character["x"]
        quadratic_coefficient = quadratic_function.coeff(x, 2)
        linear_coefficient = quadratic_function.coeff(x, 1)
        the_axis_of_symmetry = (-1 * linear_coefficient) / (2 * quadratic_coefficient)
        
        # far from axis
        if ((quadratic_coefficient > 0) and (max_or_min == "max")) or ((quadratic_coefficient < 0) and (max_or_min == "min")):
            print(f"quadratic_function: {quadratic_function}")
            print(f"the_axis_of_symmetry: {the_axis_of_symmetry}")
            middle_domain = (domain_left + domain_right) / 2
            print(f"middle_domain: {middle_domain}")
            middle_y_point = sy.solve(the_axis_of_symmetry-middle_domain, y)[0]
            print(f"middle_y_point: {middle_y_point}")
            left_value = sy.expand(quadratic_function.subs(x, domain_left))
            right_value = sy.expand(quadratic_function.subs(x, domain_right))
            middle_value = sy.expand(quadratic_function.subs(y, middle_y_point).subs(x, domain_left))
            
            pattern1_latex = f"\( y < {sy.latex(middle_y_point)} \)"
            value1_latex = f"\( {sy.latex(right_value)} \)"
            pattern2_latex = f"\( y = {sy.latex(middle_y_point)} \)"
            value2_latex = f"\( {sy.latex(middle_value)} \)"
            pattern3_latex = f"\( y > {sy.latex(middle_y_point)} \)"
            value3_latex = f"\( {sy.latex(left_value)} \)"
        # near by axis
        elif ((quadratic_coefficient > 0) and (max_or_min == "min")) or ((quadratic_coefficient < 0) and (max_or_min == "max")):
            left_y_point = sy.solve(the_axis_of_symmetry - domain_left)[0]
            left_value = sy.expand(quadratic_function.subs(x, domain_left))
            right_y_point = sy.solve(the_axis_of_symmetry - domain_right)[0]
            right_value = sy.expand(quadratic_function.subs(x, domain_right))
            axis_value = sy.expand(quadratic_function.subs(x, the_axis_of_symmetry))
            
            pattern1_latex = f"\( y < {sy.latex(right_y_point)} \)"
            value1_latex = f"\( {sy.latex(right_value)} \)"
            pattern2_latex = f"\( {sy.latex(right_y_point)} \leqq y \leqq {sy.latex(left_y_point)} \)"
            value2_latex = f"\( {sy.latex(axis_value)} \)"
            pattern3_latex = f"\( y > {sy.latex(left_y_point)} \)"
            value3_latex = f"\( {sy.latex(left_value)} \)"
        
        patterns_and_values = PatternsAndValues(pattern1_latex, value1_latex, pattern2_latex, value2_latex, pattern3_latex, value3_latex)
        return patterns_and_values

    def _calculate_patterns_with_moving_axis(self, max_or_min, domain_left, domain_right, quadratic_function):
        # 中で判別して、left_a, right_aにして、そこと値を紐づける感じ？
        class PatternsAndValues(NamedTuple):
            pattern1_latex : str
            value1_latex: str
            pattern2_latex : str
            value2_latex: str
            pattern3_latex : str
            value3_latex: str

        y = self._character["y"]
        x = self._character["x"]
        quadratic_coefficient = quadratic_function.coeff(x, 2)
        print(f"quadratic_coefficient: {quadratic_coefficient}")
        linear_coefficient = quadratic_function.coeff(x, 1)
        print(f"linear_coefficient: {linear_coefficient}")
        the_axis_of_symmetry = (-1 * linear_coefficient) / (2 * quadratic_coefficient)
        print(f"the_axis_of_symmetry: {the_axis_of_symmetry}")
        
        # far from axis
        if ((quadratic_coefficient > 0) and (max_or_min == "max")) or ((quadratic_coefficient < 0) and (max_or_min == "min")):
            middle_domain = (domain_left + domain_right) / 2
            print(f"middle_domain: {middle_domain}")
            middle_y_point = sy.solve(the_axis_of_symmetry-middle_domain, y)[0]
            print(f"middle_y_point: {middle_y_point}")
            axis_coefficient = the_axis_of_symmetry.coeff(y, 1)
            # when axis on left->value is right
            right_value = quadratic_function.subs(x, domain_right)
            print(f"right_value: {right_value}")
            left_value = quadratic_function.subs(x, domain_left)
            middle_value = quadratic_function.subs(y, middle_y_point).subs(x, domain_left)
            if axis_coefficient > 0:
                pattern1_latex = f"\( y < {sy.latex(middle_y_point)} \)"
                value1_latex = f"\( {sy.latex(right_value)} \)"
                pattern2_latex = f"\( y = {sy.latex(middle_y_point)} \)"
                value2_latex = f"\( {sy.latex(middle_value)} \)"
                pattern3_latex = f"\( y > {sy.latex(middle_y_point)} \)"
                value3_latex = f"\( {sy.latex(left_value)} \)"
            elif axis_coefficient < 0:
                pattern1_latex = f"\( y < {sy.latex(middle_y_point)} \)"
                value1_latex = f"\( {sy.latex(left_value)} \)"
                pattern2_latex = f"\( y = {sy.latex(middle_y_point)} \)"
                value2_latex = f"\( {sy.latex(middle_value)} \)"
                pattern3_latex = f"\( y > {sy.latex(middle_y_point)} \)"
                value3_latex = f"\( {sy.latex(right_value)} \)"
            else:
                raise ValueError(f"axis_coefficient: {axis_coefficient}, middle_y_point: {middle_y_point} may be wrong.")
        
        # near by axis
        elif ((quadratic_coefficient > 0) and (max_or_min == "min")) or ((quadratic_coefficient < 0) and (max_or_min == "max")):
            left_y_point = sy.solve(the_axis_of_symmetry-domain_left, y)[0]
            print("check!!")
            print(f"the_axis_of_symmetry: {the_axis_of_symmetry}")
            print(f"domain_left: {domain_left}")
            print(f"left_a_point: {left_y_point}")
            right_y_point = sy.solve(the_axis_of_symmetry-domain_right, y)[0]

            left_value = quadratic_function.subs(x, domain_left)
            right_value = quadratic_function.subs(x, domain_right)
            
            axis_coefficient = the_axis_of_symmetry.coeff(y, 1)

            if axis_coefficient > 0:
                print("positive")
                pattern1_latex = f"\( y < {sy.latex(left_y_point)} \)"
                value1_latex = f"\( {sy.latex(left_value)} \)"
                pattern2_latex = f"\( {sy.latex(left_y_point)} \leqq y \leqq {sy.latex(right_y_point)} \)"
                value2_latex = f"\( {sy.latex(quadratic_function.subs(x, the_axis_of_symmetry))} \)"
                pattern3_latex = f"\( y > {sy.latex(right_y_point)} \)"
                value3_latex = f"\( {sy.latex(right_value)} \)"
            elif axis_coefficient < 0:
                print("negative")
                pattern1_latex = f"\( y < {sy.latex(right_y_point)} \)"
                value1_latex = f"\( {sy.latex(right_value)} \)"
                pattern2_latex = f"\( {sy.latex(right_y_point)} \leqq y \leqq {sy.latex(left_y_point)} \)"
                value2_latex = f"\( {sy.latex(quadratic_function.subs(x, the_axis_of_symmetry))} \)"
                pattern3_latex = f"\( y > {sy.latex(left_y_point)} \)"
                value3_latex = f"\( {sy.latex(left_value)} \)" 
            else:
                raise ValueError(f"axis_coefficient: {axis_coefficient}, the_axis_of_symmetry: {the_axis_of_symmetry} may be wrong.")
        
        patterns_and_values = PatternsAndValues(pattern1_latex, value1_latex, pattern2_latex, value2_latex, pattern3_latex, value3_latex)
        print(patterns_and_values)

        return patterns_and_values

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
        elif positive_or_negative == "positive":
            pass
        else:
            if random() > 0.5:
                number = -1 * number
        
        return number

