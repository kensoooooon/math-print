from random import choice, randint, random

import sympy as sy

class LinearFunctionProblem:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._used_number_type_list = settings["number_to_use"]
        self._given_information = settings["given_information"]
        if self._given_information == "slope_and_one_point":
            self.latex_answer, self.latex_problem = self._make_slope_and_one_point_problem()
        elif self._given_information == "two_points":
            self.latex_answer, self.latex_problem = self._make_two_points_problem()
    
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
        
        print(f"b: {b}")
        
        # y = ax +b 
        x1, x1_latex = self._make_random_integer_number(8, -8)
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
        
        latex_problem = f"傾きが\({a_latex}\)で、\(({x1_latex}, {y1_latex})\)を通る"
        
        return latex_answer, latex_problem

    def _make_two_points_problem(self):
        x1_checker = choice(self._used_number_type_list)
        
        if x1_checker == "integer":
            x1, x1_latex = self._make_random_integer_number(8, -8)
        elif x1_checker == "frac":
            x1, x1_latex = self._make_random_frac_number(8, -8)
        
        y1_checker = choice(self._used_number_type_list)
        
        if y1_checker == "integer":
            y1, y1_latex = self._make_random_integer_number(8, -8)
        elif y1_checker == "frac":
            y1, y1_latex = self._make_random_frac_number(8, -8)
        
        x2_checker = choice(self._used_number_type_list)
        
        if x2_checker == "integer":
            x2, x2_latex = self._make_random_integer_number(8, -8)
        elif x2_checker == "frac":
            x2, x2_latex = self._make_random_frac_number(8, -8)
        
        y2_checker = choice(self._used_number_type_list)
        
        if y2_checker == "integer":
            y2, y2_latex = self._make_random_integer_number(8, -8)
        elif y2_checker == "frac":
            y2, y2_latex = self._make_random_frac_number(8, -8)
        
        # y = ax + b
        a = (y2 - y1) / (x2 - x1)
        a_latex = sy.latex(a)
        b = y1 - a * x1
        b_latex = sy.latex(b)
        
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
        
        latex_problem = f"\(({x1_latex}, {y1_latex})\)と\(({x2_latex}, {y2_latex}\))を通る"
        
        return latex_answer, latex_problem
        
            
        
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
        