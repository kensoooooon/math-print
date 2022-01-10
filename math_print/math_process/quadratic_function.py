from random import choice, randint, random

import sympy as sy

class QuadraticFunctionProblem:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._problem_type_list = settings["problem_type_list"]
        self._used_point_number_type_list = settings["used_point_number_type_list"]
        self._used_coefficient_number_type_list = settings["used_coefficient_number_type_list"]
        self._character_dict = {}
        self._character_dict["x"] = sy.Symbol("x", real=True)
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        selected_problem_type = choice(self._problem_type_list)
        
        if selected_problem_type == "one_point_to_quadratic":
            latex_answer, latex_problem = self._make_one_point_to_quadratic_problem()
        elif selected_problem_type == "two_x_values_and_change_rate_to_quadratic":
            latex_answer, latex_problem = self._make_two_x_values_and_change_rate_to_quadratic_problem()
        elif selected_problem_type == "two_x_values_and_quadratic_to_change_rate":
            latex_answer, latex_problem = self._make_two_x_values_and_quadratic_to_change_rate_problem()
        elif selected_problem_type == "change_rate_and_quadratic_to_delta_x":
            latex_answer, latex_problem = self._make_change_rate_and_quadratic_to_delta_x_problem()
        
        return latex_answer, latex_problem

    def _make_one_point_to_quadratic_problem(self):
        a = self._make_coefficient_value(5, -5)
        a_latex = sy.latex(a)
        if a == 1:
            latex_answer = "\( y = x ^ {{2}} \)"
        elif a == -1:
            latex_answer = "\( y = -x ^ {{2}} \)"
        else:
            latex_answer = f"\( y = {a_latex} x ^ {{2}} \)"
        
        x = self._make_single_x_value(4, -4)
        x_latex = sy.latex(x)

        y = a * (x ** 2)
        y_latex = sy.latex(y)
        latex_problem = f"点\( ({x_latex}, {y_latex}) \)を通る2次関数を求めよ。"
        
        return latex_answer, latex_problem
    
    def _make_two_x_values_and_change_rate_to_quadratic_problem(self):
        a = self._make_coefficient_value(4, -4)
        a_latex = sy.latex(a)
        
        if a == 1:
            latex_answer = "\( y = x ^ {{2}} \)"
        elif a == -1:
            latex_answer = "\( y = - x ^ {{2}} \)"
        else:
            latex_answer = f"\( y = {a_latex} x ^ {{2}} \)"
        
        while True:
            large_x, small_x = self._make_large_and_small_x_values(4, -4)

            y_with_large_x = a * (large_x ** 2)
            y_with_small_x = a * (small_x ** 2)
            
            if (y_with_large_x - y_with_small_x) != 0:
                break
        
        change_rate = (y_with_large_x - y_with_small_x) / (large_x - small_x)
        change_rate_latex = sy.latex(change_rate)
        
        large_x_latex = sy.latex(large_x)
        small_x_latex = sy.latex(small_x)
        
        latex_problem = f"\( x \)が\( {small_x_latex}\)から\( {large_x_latex} \)まで増加したとき、"\
            f"変化の割合が\( {change_rate_latex} \)となる2次関数を求めよ。"

        return latex_answer, latex_problem
    
    def _make_two_x_values_and_quadratic_to_change_rate_problem(self):
        a = self._make_coefficient_value(4, -4)
        a_latex = sy.latex(a)
        
        large_x, small_x = self._make_large_and_small_x_values(4, -4)
        large_x_latex = sy.latex(large_x)
        small_x_latex = sy.latex(small_x)
        
        y_with_large_x = a * (large_x ** 2)
        y_with_small_x = a * (small_x ** 2)
        change_rate = (y_with_large_x - y_with_small_x) / (large_x - small_x)
        change_rate_latex = sy.latex(change_rate)
        
        latex_answer = f"変化の割合: \( {change_rate_latex} \)"
        if a == 1:
            latex_problem = f"\( x \)が\( {small_x_latex}\)から\( {large_x_latex} \)まで増加したとき、"\
                "2次関数\( y = x ^ {{2}} \)の変化の割合を求めよ。"
        elif a == -1:
            latex_problem = f"\( x \)が\( {small_x_latex}\)から\( {large_x_latex} \)まで増加したとき、"\
                "2次関数\( y = -x ^ {{2}} \)の変化の割合を求めよ。"
        else:
            latex_problem = f"\( x \)が\( {small_x_latex}\)から\( {large_x_latex} \)まで増加したとき、"\
                f"2次関数\( y = {a_latex }x ^ {{2}} \)の変化の割合を求めよ。"

        return latex_answer, latex_problem
    
    def _make_change_rate_and_quadratic_to_delta_x_problem(self):
        a = self._make_coefficient_value(6, -6)
        a_latex = sy.latex(a)
        
        large_x, small_x = self._make_large_and_small_x_values(8, -8)
        large_x_latex = sy.latex(large_x)
        small_x_latex = sy.latex(small_x)
        
        y_with_large_x = a * (large_x ** 2)
        y_with_small_x = a * (small_x ** 2)
        change_rate = (y_with_large_x - y_with_small_x) / (large_x - small_x)
        change_rate_latex = sy.latex(change_rate)

        delta_x = large_x - small_x
        delta_x_latex = sy.latex(delta_x)
        latex_answer = f"\( x \)の変化量は\( {delta_x_latex} \)"
        
        latex_problem = f"変化の割合が\( {change_rate_latex} \)になるような2次関数\( y = {a_latex} x ^ {{2}} \)"\
            f"のxの変化量を求めよ。"

        return latex_answer, latex_problem

    def _make_large_and_small_x_values(self, max_num, min_num):
        num_type_checker1 = choice(self._used_point_number_type_list)
        if num_type_checker1 == "integer":
            x1 = self._make_random_integer_number(max_num, min_num)
        else:
            x1 = self._make_random_frac_number(max_num, min_num)
        
        num_type_checker2 = choice(self._used_point_number_type_list)
        if num_type_checker2 == "integer":
            x2 = self._make_random_integer_number(max_num, min_num)
        else:
            x2 = self._make_random_frac_number(max_num, min_num)    
        
        if x1 == x2:
            large_x = x1 + sy.Integer(randint(1, 3))
            small_x = x1
        elif x1 > x2:
            large_x = x1
            small_x = x2
        else:
            large_x = x2
            small_x = x1
        
        return large_x, small_x

    def _make_coefficient_value(self, max_num, min_num):
        num_type_checker = choice(self._used_coefficient_number_type_list)
        
        if num_type_checker == "integer":
            a = self._make_random_integer_number(max_num, min_num)
        else:
            a = self._make_random_frac_number(max_num, min_num)
        
        return a

    def _make_single_x_value(self, max_num, min_num):
        num_type_checker = choice(self._used_point_number_type_list)
        
        if num_type_checker == "integer":
            x = self._make_random_integer_number(max_num, min_num)
        else:
            x = self._make_random_frac_number(max_num, min_num)
        
        return x


    def _make_random_integer_number(self, max_num, min_num):
        if random() > 0.5:
            random_number = randint(1, max_num)
        else:
            random_number = randint(min_num, -1)
        
        integer = sy.Integer(random_number)
        
        return integer
    
    def _make_random_frac_number(self, max_num, min_num):
        while True:
            checker = random()
            if checker > 0.5:
                numerator = randint(2, max_num)
                denominator = randint(2, max_num)
            else:
                numerator = randint(min_num, -2)
                denominator = randint(2, max_num)
            
            frac = sy.Rational(numerator, denominator)
            
            if frac.denominator != 1:
                break
        
        return frac
