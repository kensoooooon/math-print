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
        if self._problem_type_list:
            selected_problem_type = choice(self._problem_type_list)
        else:
            selected_problem_type = choice(
                ["one_point_to_quadratic", "two_x_values_and_change_rate_to_quadratic",
                 "two_x_values_and_quadratic_to_change_rate", "x_range_and_quadratic_to_max_and_min"
                ]
            )
        
        if selected_problem_type == "one_point_to_quadratic":
            latex_answer, latex_problem = self._make_one_point_to_quadratic_problem()
        elif selected_problem_type == "two_x_values_and_change_rate_to_quadratic":
            latex_answer, latex_problem = self._make_two_x_values_and_change_rate_to_quadratic_problem()
        elif selected_problem_type == "two_x_values_and_quadratic_to_change_rate":
            latex_answer, latex_problem = self._make_two_x_values_and_quadratic_to_change_rate_problem()
        elif selected_problem_type == "x_range_and_quadratic_to_max_and_min":
            latex_answer, latex_problem = self._make_x_range_and_quadratic_to_max_and_min_problem()
        
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
        latex_problem = f"???\( ({x_latex}, {y_latex}) \)?????????2????????????????????????"
        
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
        
        latex_problem = f"\( x \)???\( {small_x_latex}\)??????\( {large_x_latex} \)???????????????????????????\n"\
            f"??????????????????\( {change_rate_latex} \)?????????2????????????????????????"

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
        
        latex_answer = f"???????????????: \( {change_rate_latex} \)"
        if a == 1:
            latex_problem = f"\( x \)???\( {small_x_latex}\)??????\( {large_x_latex} \)???????????????????????????\n"\
                "2?????????\( y = x ^ {{2}} \)?????????????????????????????????"
        elif a == -1:
            latex_problem = f"\( x \)???\( {small_x_latex}\)??????\( {large_x_latex} \)???????????????????????????\n"\
                "2?????????\( y = -x ^ {{2}} \)?????????????????????????????????"
        else:
            latex_problem = f"\( x \)???\( {small_x_latex}\)??????\( {large_x_latex} \)???????????????????????????\n"\
                f"2?????????\( y = {a_latex }x ^ {{2}} \)?????????????????????????????????"

        return latex_answer, latex_problem

    def _make_x_range_and_quadratic_to_max_and_min_problem(self):
        
        def check_which_far_from_zero(left_x, right_x):
            distance_of_left_x_from_zero = abs(left_x - 0)
            distance_of_right_x_from_zero = abs(right_x - 0)

            if distance_of_left_x_from_zero > distance_of_right_x_from_zero:
                return "left"
            elif distance_of_left_x_from_zero < distance_of_right_x_from_zero:
                return "right"
            else:
                return "both"
        
        right_x, left_x = self._make_large_and_small_x_values(6, -6)
        right_x_latex = sy.latex(right_x)
        left_x_latex = sy.latex(left_x)
        a = self._make_coefficient_value(5, -5)
        a_latex = sy.latex(a)
        if a == 1:
            latex_problem = f"\( y = x ^ {{2}} \)??????????????????"
        elif a == -1:
            latex_problem = f"\( y = -x ^ {{2}} \)??????????????????"
        else:
            latex_problem = f"\( y = {a_latex} x ^ {{2}} \)??????????????????"
            
            
        latex_problem += f"\( x \)???\( {left_x_latex} \)??????\( {right_x_latex} \)??????????????????\n"\
                "????????????????????????????????????????????????x?????????????????????"
        
        which_far_from_zero = check_which_far_from_zero(left_x, right_x)        
        
        if a > 0:
            if which_far_from_zero == "left":
                y_max = a * (left_x ** 2)
                x_with_y_max = left_x
            elif which_far_from_zero == "right":
                y_max = a * (right_x ** 2)
                x_with_y_max = right_x
            elif which_far_from_zero == "both":
                y_max = a * (right_x ** 2)
                x_with_y_max = "both_x"

            if (left_x <= 0) and (right_x >= 0):
                y_min = 0
                x_with_y_min = 0
            else:
                if which_far_from_zero == "left":
                    y_min = a * (right_x ** 2)
                    x_with_y_min = right_x
                elif which_far_from_zero == "right":
                    y_min = a * (left_x ** 2)
                    x_with_y_min = left_x
                elif which_far_from_zero == "both":
                    y_min = a * (right_x ** 2)
                    x_with_y_min = "both_x"
        
        elif a < 0:
            if which_far_from_zero == "left":
                y_min = a * (left_x ** 2)
                x_with_y_min = left_x
            elif which_far_from_zero == "right":
                y_min = a * (right_x ** 2)
                x_with_y_min = right_x
            elif which_far_from_zero == "both":
                y_min = a * (right_x ** 2)
                x_with_y_min = "both_x"

            if (left_x <= 0) and (right_x >= 0):
                y_max = 0
                x_with_y_max = 0
            else:
                if which_far_from_zero == "left":
                    y_max = a * (right_x ** 2)
                    x_with_y_max = right_x
                elif which_far_from_zero == "right":
                    y_max = a * (left_x ** 2)
                    x_with_y_max = left_x
                elif which_far_from_zero == "both":
                    y_max = a * (right_x ** 2)
                    x_with_y_max = "both_x"
        
        y_max_latex = sy.latex(y_max)
        x_with_y_max_latex = sy.latex(x_with_y_max)
        
        latex_answer = ""
        if x_with_y_max == "both_x":
            latex_answer += f"\( x = {left_x_latex}, {right_x_latex} \)????????????"
        else:
            latex_answer += f"\( x = {x_with_y_max_latex} \)????????????"
        latex_answer += f"?????????\( {y_max_latex} \)???\n"

        y_min_latex = sy.latex(y_min)
        x_with_y_min_latex = sy.latex(x_with_y_min)
        
        if x_with_y_min == "both_x":
            latex_answer += f"\( x = {left_x_latex}, {right_x_latex} \)????????????"
        else:
            latex_answer += f"\( x = {x_with_y_min_latex} \)????????????"
        latex_answer += f"?????????\( {y_min_latex} \)???"
        
        return latex_answer, latex_problem
                    
    def _make_large_and_small_x_values(self, max_num, min_num):
        if self._used_coefficient_number_type_list:
            num_type_checker1 = choice(self._used_point_number_type_list)
        else:
            num_type_checker1 = choice(["integer", "frac"])
            
        if num_type_checker1 == "integer":
            x1 = self._make_random_integer_number(max_num, min_num)
        elif num_type_checker1 == "frac":
            x1 = self._make_random_frac_number(max_num, min_num)

        if self._used_coefficient_number_type_list:
            num_type_checker2 = choice(self._used_point_number_type_list)
        else:
            num_type_checker2 = choice(["integer", "frac"])

        if num_type_checker2 == "integer":
            x2 = self._make_random_integer_number(max_num, min_num)
        elif num_type_checker2 == "frac":
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
        if self._used_coefficient_number_type_list:
            num_type_checker = choice(self._used_coefficient_number_type_list)
        else:
            num_type_checker = choice(["integer", "frac"])
        
        if num_type_checker == "integer":
            a = self._make_random_integer_number(max_num, min_num)
        elif num_type_checker == "frac":
            a = self._make_random_frac_number(max_num, min_num)
        
        return a

    def _make_single_x_value(self, max_num, min_num):
        if self._used_coefficient_number_type_list:
            num_type_checker = choice(self._used_coefficient_number_type_list)
        else:
            num_type_checker = choice(["integer", "frac"])
        
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
