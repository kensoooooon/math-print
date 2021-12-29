from random import choice, randint, random

import sympy as sy
from sympy.parsing.sympy_parser import _add_factorial_tokens

class LinearFunctionProblem:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._used_number_type_list = settings["number_to_use"]
        self._given_information = settings["given_information"]
        if self._given_information == "slope_and_one_point":
            self.latex_answer, self.latex_problem = self._make_slope_and_one_point_problem()
        elif self._given_information == "two_points":
            self.latex_answer, self.latex_problem = self._make_two_points_problem()
        elif self._given_information == "one_point_and_parallel_line":
            self.latex_answer, self.latex_problem = self._make_one_point_and_parallel_line_problem()
        elif self._given_information == "mixed":
            self.latex_answer, self.latex_problem = self._choice_random_problem()
    
    def _make_slope_and_one_point_problem(self):
        a_checker = choice(self._used_number_type_list)
        
        if a_checker == "integer":
            a, a_latex = self._make_random_integer_number(8, -8)
        elif a_checker == "frac":
            a, a_latex = self._make_random_frac_number(8, -8)
        
        b_checker = choice(self._used_number_type_list)
        
        if b_checker == "integer":
            b, b_latex = self._make_random_integer_number(8, -8)
        elif b_checker == "frac":
            b, b_latex = self._make_random_frac_number(8, -8)
        
        # print(f"b: {b}")
        
        # y = ax +b 
        x1_checker = choice(self._used_number_type_list)
        if x1_checker == "integer":
            x1, x1_latex = self._make_random_integer_number(8, -8)
        elif x1_checker == "frac":
            x1, x1_latex = self._make_random_frac_number(8, -8)
        y1 = a * x1 + b 
        y1_latex = sy.latex(y1)
        
        latex_answer = "y ="
        if a == 1:
            latex_answer += "x"
        elif a == -1:
            latex_answer += "-x"
        else:
            latex_answer += f"{a_latex}x"
        
        if b > 0:
            latex_answer += f"+{b_latex}"
        elif b < 0:
            latex_answer += f"{b_latex}"
        
        latex_answer = f"\( {latex_answer} \)"
        
        latex_problem = f"傾きが\({a_latex}\)で、\( \\left({x1_latex}, {y1_latex}\\right) \)を通る"
        
        return latex_answer, latex_problem

    def _make_two_points_problem(self):
        a_checker = choice(self._used_number_type_list)
        
        if a_checker == "integer":
            a, a_latex = self._make_random_integer_number(6, -6)
        elif a_checker == "frac":
            a, a_latex = self._make_random_frac_number(6, -6)
        
        b_checker = choice(self._used_number_type_list)
        
        if b_checker == "integer":
            b, b_latex = self._make_random_integer_number(8, -8)
        elif b_checker == "frac":
            b, b_latex = self._make_random_frac_number(8, -8)
        
        latex_answer = "y ="
        if a == 1:
            latex_answer += "x"
        elif a == -1:
            latex_answer += "-x"
        else:
            latex_answer += f"{a_latex}x"
        
        if b > 0:
            latex_answer += f"+{b_latex}"
        elif b < 0:
            latex_answer += f"{b_latex}"
        
        latex_answer = f"\( {latex_answer} \)"
        
        x1_checker = choice(self._used_number_type_list)
        
        if x1_checker == "integer":
            x1, x1_latex = self._make_random_integer_number(8, -8)
        elif x1_checker == "frac":
            x1, x1_latex = self._make_random_frac_number(8, -8)
        
        delta_checker = choice(self._used_number_type_list)

        if delta_checker == "integer":
            delta, _ = self._make_random_integer_number(8, -8)
        elif delta_checker == "frac":
            delta, _ = self._make_random_frac_number(8, -8) 
        
        x2 = x1 + delta
        x2_latex = sy.latex(x2)
        
        y1 = a * x1 + b
        y1_latex = sy.latex(y1)
        y2 = a * x2 + b
        y2_latex = sy.latex(y2)
        
        latex_problem = f"\( \\left({x1_latex}, {y1_latex}\\right) \)と\( \left({x2_latex}, {y2_latex}\\right) \)を通る"
        
        return latex_answer, latex_problem
        
    def _make_one_point_and_parallel_line_problem(self):
        a_checker = choice(self._used_number_type_list)
        
        if a_checker == "integer":
            a, a_latex = self._make_random_integer_number(6, -6)
        elif a_checker == "frac":
            a, a_latex = self._make_random_frac_number(6, -6)
        
        b_checker = choice(self._used_number_type_list)
        
        if b_checker == "integer":
            b, b_latex = self._make_random_integer_number(8, -8)
        elif b_checker == "frac":
            b, b_latex = self._make_random_frac_number(8, -8)
        
        latex_answer = "y ="
        if a == 1:
            latex_answer += "x"
        elif a == -1:
            latex_answer += "-x"
        else:
            latex_answer += f"{a_latex}x"
        
        if b > 0:
            latex_answer += f"+{b_latex}"
        elif b < 0:
            latex_answer += f"{b_latex}"
        
        latex_answer = f"\( {latex_answer} \)"
        
        a_for_parallel_line = a
        a_for_parallel_line_latex = sy.latex(a_for_parallel_line)
        
        b_for_parallel_line_checker = choice(self._used_number_type_list)
        
        if b_for_parallel_line_checker == "integer":
            b_for_parallel_line, b_for_parallel_line_latex = self._make_random_integer_number(10, -10)
        elif b_for_parallel_line_checker == "frac":
            b_for_parallel_line, b_for_parallel_line_latex = self._make_random_frac_number(10, -10)
        
        parallel_line_latex = "y="
        if a == 1:
            parallel_line_latex += "x"
        elif a == -1:
            parallel_line_latex += "-x"
        else:
            parallel_line_latex += f"{a_for_parallel_line_latex}x"
        
        if b_for_parallel_line > 0:
            parallel_line_latex += f"+{b_for_parallel_line_latex}"
        elif b_for_parallel_line < 0:
            parallel_line_latex += f"{b_for_parallel_line_latex}"
        
        x1_checker = choice(self._used_number_type_list)
        
        if x1_checker ==  "integer":
            x1, x1_latex = self._make_random_integer_number(7, -7)
        elif x1_checker == "frac":
            x1,  x1_latex = self._make_random_frac_number(7, -7)
        
        y1 = a * x1 + b
        y1_latex = sy.latex(y1)
        
        latex_problem = f"点\( \\left({x1_latex}, {y1_latex}\\right) \)を通り、直線\({parallel_line_latex}\)に平行"
        
        return latex_answer, latex_problem

    def _choice_random_problem(self):
        chosen_problem_type = choice(["two_points", "one_point_and_parallel_line", "slope_and_one_point"])
        
        if chosen_problem_type == "two_points":
            return self._make_two_points_problem()
        elif chosen_problem_type == "one_point_and_parallel_line":
            return self._make_one_point_and_parallel_line_problem()
        elif chosen_problem_type == "slope_and_one_point":
            return self._make_slope_and_one_point_problem()
        
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
        