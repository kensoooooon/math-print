from random import choice, randint, random

import sympy as sy


class SimultaneousEquation:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._used_number_type_list = settings['used_number_type_list']
        self._answer_type = settings['simultaneous_equation_type']
        self._used_character_type_list = ["x"]
        self._character_dict = {}
        for character in self._used_character_type_list:
            self._character_dict[character] = sy.Symbol(character, real=True)
        if self._answer_type == "ax_plus_by_equal_c_only_integer":
            self.latex_answer, self.latex_problem = self._make_ax_plus_by_equal_c_only_integer()
        elif self._answer_type == "ax_plus_by_equal_c_all_number":
            self.latex_answer, self.latex_problem = self._make_ax_plus_by_equal_c_all_number()
        else:
            raise ValueError("linear_equation_type may be wrong.")

    def _make_ax_plus_by_equal_c_only_integer(self):
        x, x_latex = self._make_random_integer(8, -8)
        y, y_latex = self._make_random_integer(8, -8)
        
        two_problems_list = []
        
        for _ in range(2):
            a_type_checker = self._number_type_selector()
            
            if a_type_checker == "integer":
                a, a_latex = self._make_random_integer(8, -8)
            elif a_type_checker == "frac":
                a, a_latex = self._make_random_frac(8, -8)
            elif a_type_checker == "decimal":
                a, a_latex = self._make_random_decimal(8, -8)
            
            b_type_checker = self._number_type_selector()
            
            if b_type_checker == "integer":
                b, b_latex = self._make_random_integer(8, -8)
            elif b_type_checker == "frac":
                b, b_latex = self._make_random_frac(8, -8)
            elif b_type_checker == "decimal":
                b, b_latex = self._make_random_decimal(8, -8)

            c = a * x + b * y
            c_latex = sy.latex(c)
            
            left_latex = ""
            if a == 1:
                left_latex = left_latex + "x"
            elif a == -1:
                left_latex = left_latex + "-x"
            else:
                left_latex = left_latex + f"{a_latex}x"

            if b == 1:
                left_latex = left_latex + "+y"
            elif b == -1:
                left_latex = left_latex + "-y"
            elif b > 0:
                left_latex = left_latex + f"+ {b_latex}y"
            elif b < 0:
                left_latex = left_latex + f"{b_latex}y"
            
            if ("integer" not in self._used_number_type_list) and ("frac" not in self._used_number_type_list) and ("decimal" in self._used_number_type_list):
                right_latex = f"{sy.latex(float(c))}"
            else:
                right_latex = f"{c_latex}"
            
            two_problems_list.append(f"{left_latex}={right_latex}")
         
        latex_problem = f"{two_problems_list[0]} \\\\ {two_problems_list[1]}"
        latex_answer = f"x = {x_latex}, y = {y_latex}"
        
        return latex_answer, latex_problem
        
    def _make_ax_plus_by_equal_c_all_number(self):
        answer_type_checker = self._number_type_selector()
        
        if answer_type_checker == "integer":
            x, x_latex = self._make_random_integer(8, -8)
        if answer_type_checker == "frac":
            x, x_latex = self._make_random_frac(8, -8)
        if answer_type_checker == "decimal":
            x, x_latex = self._make_random_decimal(8, -8)

        answer_type_checker = self._number_type_selector()
        
        if answer_type_checker == "integer":
            y, y_latex = self._make_random_integer(8, -8)
        if answer_type_checker == "frac":
            y, y_latex = self._make_random_frac(8, -8)
        if answer_type_checker == "decimal":
            y, y_latex = self._make_random_decimal(8, -8)
        
        two_problems_list = []
        
        for _ in range(2):
            a_type_checker = self._number_type_selector()
            
            if a_type_checker == "integer":
                a, a_latex = self._make_random_integer(8, -8)
            elif a_type_checker == "frac":
                a, a_latex = self._make_random_frac(8, -8)
            elif a_type_checker == "decimal":
                a, a_latex = self._make_random_decimal(8, -8)
            
            b_type_checker = self._number_type_selector()
            
            if b_type_checker == "integer":
                b, b_latex = self._make_random_integer(8, -8)
            elif b_type_checker == "frac":
                b, b_latex = self._make_random_frac(8, -8)
            elif b_type_checker == "decimal":
                b, b_latex = self._make_random_decimal(8, -8)
            
            c = a * x + b * y
            c_latex = sy.latex(c)
            
            left_latex = ""
            if a == 1:
                left_latex = left_latex + "x"
            elif a == -1:
                left_latex = left_latex + "-x"
            else:
                left_latex = left_latex + f"{a_latex}x"

            if b == 1:
                left_latex = left_latex + "+y"
            elif b == -1:
                left_latex = left_latex + "-y"
            elif b > 0:
                left_latex = left_latex + f"+ {b_latex}y"
            elif b < 0:
                left_latex = left_latex + f"{b_latex}y"
            
            if ("integer" not in self._used_number_type_list) and ("frac" not in self._used_number_type_list) and ("decimal" in self._used_number_type_list):
                right_latex = f"{sy.latex(float(c))}"
            else:
                right_latex = f"{c_latex}"
            
            two_problems_list.append(f"{left_latex}={right_latex}")
         
        latex_problem = f"{two_problems_list[0]} \\\\ {two_problems_list[1]}"
        latex_answer = f"x = {x_latex}, y = {y_latex}"
        
        return latex_answer, latex_problem
    
    def _number_type_selector(self):
        if self._used_number_type_list:
            selected_number_type = choice(self._used_number_type_list)
        else:
            selected_number_type = choice(
                ["integer", "frac", "decimal"]
            )
        return selected_number_type

    def _make_random_frac(self, max_num, min_num):
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
        
    
    def _make_random_decimal(self, max_num, min_num):
        checker = random()
        if checker > 0.5:
            numerator = randint(1, max_num)
        else:
            numerator = randint(min_num, -1)
        
        frac_for_decimal = sy.Rational(numerator, 10)
        if frac_for_decimal == 1:
            decimal = 1
        else:
            decimal = float(frac_for_decimal)

        decimal_with_number = frac_for_decimal
        decimal_with_number_latex = sy.latex(decimal)
        return decimal_with_number, decimal_with_number_latex
    
    def _make_random_integer(self, max_num, min_num):
        checker = random()
        if checker > 0.5:
            numerator = randint(1, max_num)
        else:
            numerator = randint(min_num, -1)
        
        integer = sy.Integer(numerator)
        
        integer_with_number_latex = sy.latex(integer)
        return integer, integer_with_number_latex
