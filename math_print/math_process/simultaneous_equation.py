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
        x, x_latex = self._make_random_integer(10, -10, "number")
        y, y_latex = self._make_random_integer(10, -10, "number")
        
        two_problems_list = []
        
        for _ in range(2):
            a_type_checker = choice(self._used_number_type_list)
            print(f"a_type_checker: {a_type_checker}")
            
            if a_type_checker == "integer":
                a, a_latex = self._make_random_integer(10, -10, "number")
            elif a_type_checker == "frac":
                a, a_latex = self._make_random_frac(10, -10, "number")
            elif a_type_checker == "decimal":
                a, a_latex = self._make_random_decimal(10, -10, 10, "number")
            else:
                raise ValueError(f"a_type_checker is {a_type_checker}, it may be wrong.")
            
            b_type_checker = choice(self._used_number_type_list)
            
            if b_type_checker == "integer":
                b, b_latex = self._make_random_integer(10, -10, "number")
            elif a_type_checker == "frac":
                b, b_latex = self._make_random_frac(10, -10, "number")
            elif a_type_checker == "decimal":
                b, b_latex = self._make_random_decimal(10, -10, 10, "number")
            else:
                raise ValueError(f"a_type_checker is {a_type_checker}, it may be wrong.")

            c = a * x + b * y
            c_latex = sy.latex(c)
            
            left_latex = ""
            if a == 1:
                left_latex = left_latex + "x"
            elif a == -1:
                left_latex = left_latex + "-x"
            else:
                left_latex = left_latex + f"{a_latex}x"

            if b > 0:
                left_latex = left_latex + f"+ {b_latex}"
            elif b < 0:
                left_latex = left_latex + f"{b_latex}"
            
            right_latex = f"{c_latex}"
            
            two_problems_list.append(f"{left_latex}={right_latex}")
         
        latex_problem = f"{two_problems_list[0]} \\\\ {two_problems_list[1]}"
        latex_answer = f"x = {x_latex}, y = {y_latex}"
        
        return latex_answer, latex_problem
        
    def _make_ax_plus_by_equal_c_all_number(self):
        answer_type_checker =choice(self._used_number_type_list)
        
        if answer_type_checker == "integer":
            x, x_latex = self._make_random_integer(10, -10, "number")
            y, y_latex = self._make_random_integer(10, -10, "number")
        if answer_type_checker == "frac":
            x, x_latex = self._make_random_frac(10, -10, "number")
            y, y_latex = self._make_random_frac(10, -10, "number")
        if answer_type_checker == "decimal":
            x, x_latex = self._make_random_decimal(10, -10, "number")
            y, y_latex = self._make_random_decimal(10, -10, "number")
        
        two_problems_list = []
        
        for _ in range(2):
            a_type_checker = choice(self._used_number_type_list)
            
            if a_type_checker == "integer":
                a, a_latex = self._make_random_integer(10, -10, "number")
            elif a_type_checker == "frac":
                a, a_latex = self._make_random_frac(10, -10, "number")
            elif a_type_checker == "decimal":
                a, a_latex = self._make_random_decimal(10, -10, 10, "number")
            else:
                raise ValueError(f"a_type_checker is {a_type_checker}, it may be wrong.")
            
            b_type_checker = choice(self._used_number_type_list)
            
            if b_type_checker == "integer":
                b, b_latex = self._make_random_integer(10, -10, "number")
            elif a_type_checker == "frac":
                b, b_latex = self._make_random_frac(10, -10, "number")
            elif a_type_checker == "decimal":
                b, b_latex = self._make_random_decimal(10, -10, 10, "number")
            else:
                raise ValueError(f"a_type_checker is {a_type_checker}, it may be wrong.")

            c = a * x + b * y
            c_latex = sy.latex(c)
            
            left_latex1 = ""
            if a == 1:
                left_latex = left_latex + "x"
            elif a == -1:
                left_latex = left_latex + "-x"
            else:
                left_latex = left_latex + f"{a_latex}x"

            if b > 0:
                left_latex = left_latex + f"+ {b_latex}"
            elif b < 0:
                left_latex = left_latex + f"{b_latex}"
            
            right_latex = f"{c_latex}"
            
            two_problems_list.append(f"{left_latex}={right_latex}")
         
        latex_problem = f"{two_problems_list[0]} \\\\ {two_problems_list[1]}"
        latex_answer = f"x = {x_latex}, y = {y_latex}"
        
        return latex_answer, latex_problem
        

    def _make_random_frac(self, max_num, min_num, number_or_character):
        checker = random()
        if checker > 0.5:
            numerator = randint(2, max_num)
            denominator = randint(2, max_num)
        else:
            numerator = randint(min_num, -2)
            denominator = randint(2, max_num)
        
        frac = sy.Rational(numerator, denominator)
        
        if number_or_character == "character":
            used_character = choice(self._used_character_type_list)
            frac_with_character = frac * self._character_dict[used_character]
            frac_with_character_latex = sy.latex(frac_with_character)
            return frac_with_character, frac_with_character_latex

        elif number_or_character == "number":
            frac_with_number_latex = sy.latex(frac)
            return frac, frac_with_number_latex
        else:
            raise ValueError("There is something wrong with 'add_number_or_character'.")
        
    
    def _make_random_decimal(self, max_num, min_num, denominator, number_or_character):
        checker = random()
        if checker > 0.5:
            numerator = randint(1, max_num)
        else:
            numerator = randint(min_num, -1)
        
        frac_for_decimal = sy.Rational(numerator, denominator)
        if frac_for_decimal == 1:
            decimal = 1
        else:
            decimal = float(frac_for_decimal)

        if number_or_character == "character":
            used_character = choice(self._used_character_type_list)
            character = self._character_dict[used_character]
            decimal_with_character = frac_for_decimal * character
            decimal_with_character_latex = sy.latex(decimal * character)
            return decimal_with_character, decimal_with_character_latex

        elif number_or_character == "number":
            decimal_with_number = frac_for_decimal
            decimal_with_number_latex = sy.latex(decimal)
            return decimal_with_number, decimal_with_number_latex
        else:
            raise ValueError("There is something wrong with 'add_number_or_character'.")
    
    def _make_random_integer(self, max_num, min_num, number_or_character):
        checker = random()
        if checker > 0.5:
            numerator = randint(1, max_num)
        else:
            numerator = randint(min_num, -1)
        
        integer = sy.Integer(numerator)
        
        if number_or_character == "character":
            used_character = choice(self._used_character_type_list)
            integer_with_character = self._character_dict[used_character] * integer
            integer_with_character_latex = sy.latex(integer_with_character)
            return integer_with_character, integer_with_character_latex

        elif number_or_character == "number":
            integer_with_number_latex = sy.latex(integer)
            return integer, integer_with_number_latex
        else:
            raise ValueError("There is something wrong with 'add_number_or_character'.")