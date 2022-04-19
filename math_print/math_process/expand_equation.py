from random import choice, randint, random

import sympy as sy


class ExpandEquationProblem:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._used_number_type_list = settings["used_number_type_list"]
        self._expand_equation_type_list = settings["expand_equation_type_list"]
        self._used_character_list = ["x", "y"]
        self._character_dict = {}
        for character in self._used_character_list:
            self._character_dict[character] = sy.Symbol(character, real=True)
        
        self.latex_answer, self.latex_problem = self._make_problem()

    def _make_problem(self):

        selected_equation_type = choice(self._expand_equation_type_list)
        
        if selected_equation_type == 'ax_times_bx_plus_c':
            latex_answer, latex_problem = self._make_ax_times_bx_plus_c()
        elif selected_equation_type == 'double_ax_times_bx_plus_c':
            latex_answer, latex_problem = self._make_double_ax_times_bx_plus_c()
        elif selected_equation_type == 'double_ax_plus_b':
            latex_answer, latex_problem = self._make_double_ax_plus_b()
        elif selected_equation_type == 'double_ax_plus_by':
            latex_answer, latex_problem = self._make_double_ax_plus_by()
        elif selected_equation_type == 'square_x_plus_a':
            latex_answer, latex_problem = self._make_square_x_plus_a()
        elif selected_equation_type == 'square_x_minus_a':
            latex_answer, latex_problem = self._make_square_x_minus_a()
        elif selected_equation_type == "x_plus_a_x_minus_a":
            latex_answer, latex_problem = self._make_plus_minus_problem()
                
        return latex_answer, latex_problem
    
    def _make_ax_times_bx_plus_c(self):
        a_checker = choice(self._used_number_type_list)
        
        if a_checker == "integer":
            a, a_latex = self._make_random_integer(8, -8, "number")
        elif a_checker == "frac":
            a, a_latex = self._make_random_frac(8, -8, "number")
        
        b_checker = choice(self._used_number_type_list)
        
        if b_checker == "integer":
            b, b_latex = self._make_random_integer(8, -8, "number")
        elif b_checker == "frac":
            b, b_latex = self._make_random_frac(8, -8, "number")

        c_checker = choice(self._used_number_type_list)
        
        if c_checker == "integer":
            c, c_latex = self._make_random_integer(8, -8, "number")
        elif c_checker == "frac":
            c, c_latex = self._make_random_frac(8, -8, "number")

        x = self._character_dict["x"]
        left = a * x * (b * x + c)
        right = sy.expand(left)
        
        left_latex = ""
        if a == 1:
            left_latex += "x"
        elif a == -1:
            left_latex += "-x"
        else:
            left_latex += f"{a_latex}x"
        
        if b == 1:
            left_latex += "\\left( x"
        elif b == -1:
            left_latex += "\\left( -x"
        else:
            left_latex += f"\\left( {b_latex}x"
        
        if c > 0:
            left_latex += f"+ {c_latex} \\right)"
        elif c < 0:
            left_latex += f"{c_latex} \\right)"
        
        latex_problem = left_latex
        latex_answer = f"= {sy.latex(right)}"
        
        return latex_answer, latex_problem
    
    def _make_double_ax_times_bx_plus_c(self):
        a_checker = choice(self._used_number_type_list)
        
        if a_checker == "integer":
            a, a_latex = self._make_random_integer(8, -8, "number")
        elif a_checker == "frac":
            a, a_latex = self._make_random_frac(8, -8, "number")
        
        b_checker = choice(self._used_number_type_list)
        
        if b_checker == "integer":
            b, b_latex = self._make_random_integer(8, -8, "number")
        elif b_checker == "frac":
            b, b_latex = self._make_random_frac(8, -8, "number")

        c_checker = choice(self._used_number_type_list)
        
        if c_checker == "integer":
            c, c_latex = self._make_random_integer(8, -8, "number")
        elif c_checker == "frac":
            c, c_latex = self._make_random_frac(8, -8, "number")

        d_checker = choice(self._used_number_type_list)
        
        if d_checker == "integer":
            d, d_latex = self._make_random_integer(8, -8, "number")
        elif d_checker == "frac":
            d, d_latex = self._make_random_frac(8, -8, "number")
        
        e_checker = choice(self._used_number_type_list)
        
        if e_checker == "integer":
            e, e_latex = self._make_random_integer(8, -8, "number")
        elif e_checker == "frac":
            e, e_latex = self._make_random_frac(8, -8, "number")

        f_checker = choice(self._used_number_type_list)
        
        if f_checker == "integer":
            f, f_latex = self._make_random_integer(8, -8, "number")
        elif f_checker == "frac":
            f, f_latex = self._make_random_frac(8, -8, "number")

        x = self._character_dict["x"]
        left = a * x * (b * x + c) + d * x * (e * x + f)
        right = sy.expand(left)
        
        left_latex = ""
        
        if a == 1:
            left_latex += "x"
        elif a == -1:
            left_latex += "-x"
        else:
            left_latex += f"{a_latex}x"
        
        if b == 1:
            left_latex += "\\left(x"
        elif b == -1:
            left_latex += "\\left(-x"
        else:
            left_latex += f"\\left( {b_latex}x"
        
        if c > 0:
            left_latex += f"+{c_latex} \\right)"
        elif c < 0:
            left_latex += f"{c_latex} \\right)"
        
        if d == 1:
            left_latex += "+ x"
        elif d == -1:
            left_latex += "- x"
        else:
            if d > 0:
                left_latex += f"+ {d_latex} x"
            if d < 0:
                left_latex += f"{d_latex} x"
        
        if e == 1:
            left_latex += "\\left(x"
        elif e == -1:
            left_latex += "\\left(-x"
        else:
            left_latex += f"\\left( {e_latex}x"
        
        if f > 0:
            left_latex += f"+{f_latex} \\right)"
        elif f < 0:
            left_latex += f"{f_latex} \\right)"
        
        latex_problem = left_latex
        latex_answer = f"= {sy.latex(right)}"
        
        return latex_answer, latex_problem
    
    def _make_double_ax_plus_b(self):
        a_checker = choice(self._used_number_type_list)
        
        if a_checker == "integer":
            a, a_latex = self._make_random_integer(8, -8, "number")
        elif a_checker == "frac":
            a, a_latex = self._make_random_frac(8, -8, "number")
        
        b_checker = choice(self._used_number_type_list)
        
        if b_checker == "integer":
            b, b_latex = self._make_random_integer(8, -8, "number")
        elif b_checker == "frac":
            b, b_latex = self._make_random_frac(8, -8, "number")

        c_checker = choice(self._used_number_type_list)
        
        if c_checker == "integer":
            c, c_latex = self._make_random_integer(8, -8, "number")
        elif c_checker == "frac":
            c, c_latex = self._make_random_frac(8, -8, "number")

        d_checker = choice(self._used_number_type_list)
        
        if d_checker == "integer":
            d, d_latex = self._make_random_integer(8, -8, "number")
        elif d_checker == "frac":
            d, d_latex = self._make_random_frac(8, -8, "number")
        
        x = self._character_dict["x"]
        left = (a * x + b) * (c * x + d)
        left_latex = sy.latex(left)
        latex_problem = left_latex
        answer = sy.expand(left)
        latex_answer = f"= {sy.latex(answer)}"
        
        return latex_answer, latex_problem

    def _make_double_ax_plus_by(self):
        a_checker = choice(self._used_number_type_list)
        
        if a_checker == "integer":
            a, a_latex = self._make_random_integer(8, -8, "number")
        elif a_checker == "frac":
            a, a_latex = self._make_random_frac(8, -8, "number")
        
        b_checker = choice(self._used_number_type_list)
        
        if b_checker == "integer":
            b, b_latex = self._make_random_integer(8, -8, "number")
        elif b_checker == "frac":
            b, b_latex = self._make_random_frac(8, -8, "number")

        c_checker = choice(self._used_number_type_list)
        
        if c_checker == "integer":
            c, c_latex = self._make_random_integer(8, -8, "number")
        elif c_checker == "frac":
            c, c_latex = self._make_random_frac(8, -8, "number")

        d_checker = choice(self._used_number_type_list)
        
        if d_checker == "integer":
            d, d_latex = self._make_random_integer(8, -8, "number")
        elif d_checker == "frac":
            d, d_latex = self._make_random_frac(8, -8, "number")
        
        x = self._character_dict["x"]
        y = self._character_dict["y"]
        left = (a * x + b * y) * (c * x + d * y)
        left_latex = sy.latex(left)
        latex_problem = left_latex
        answer = sy.expand(left)
        latex_answer = f"= {sy.latex(answer)}"
        
        return latex_answer, latex_problem

    def _make_square_x_plus_a(self):

        a_checker = choice(self._used_number_type_list)
        
        if a_checker == "integer":
            a, a_latex = self._make_random_positive_or_negative_integer(8, 1, "number", "positive")
        elif a_checker == "frac":
            a, a_latex = self._make_random_positive_or_negative_frac(8, 1, "number", "positive")
        
        x = self._character_dict["x"]
        left = (x + a) ** 2
        left_latex = sy.latex(left)
        
        right = sy.expand(left)
        right_latex = sy.latex(right)
        
        latex_problem = left_latex
        latex_answer = f"= {right_latex}"
        
        return latex_answer, latex_problem
    
    def _make_square_x_minus_a(self):
        a_checker = choice(self._used_number_type_list)
        
        if a_checker == "integer":
            a, a_latex = self._make_random_positive_or_negative_integer(-1, -8, "number", "negative")
        elif a_checker == "frac":
            a, a_latex = self._make_random_positive_or_negative_frac(-1, -8, "number", "negative")
        
        x = self._character_dict["x"]
        left = (x + a) ** 2
        left_latex = sy.latex(left)
        
        right = sy.expand(left)
        right_latex = sy.latex(right)
        
        latex_problem = left_latex
        latex_answer = f"= {right_latex}"
        
        return latex_answer, latex_problem
    
    def _make_plus_minus_problem(self):
        a_checker = choice(self._used_number_type_list)
        
        if a_checker == "integer":
            a, a_latex = self._make_random_integer(6, -6, "number")
        elif a_checker == "frac":
            a, a_latex = self._make_random_frac(6, -6, "number")
            
        x = self._character_dict["x"]
        left = (x + a) * (x - a)
        left_latex = sy.latex(left)
        
        right = sy.expand(left)
        right_latex = sy.latex(right)
        
        latex_problem = left_latex
        latex_answer = f"= {right_latex}"
        
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
    
    def _make_random_positive_or_negative_integer(self, max_num, min_num, number_or_character, positive_or_negative):
        numerator = randint(min_num, max_num)
        
        integer = sy.Integer(numerator)
        
        if positive_or_negative == "positive":
            integer = abs(integer)
        elif positive_or_negative == "negative":
            integer = -1 * abs(integer)
        
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

    def _make_random_positive_or_negative_frac(self, max_num, min_num, number_or_character, positive_or_negative):
        numerator = randint(min_num, max_num)
        denominator = randint(min_num, max_num)
    
        frac = sy.Rational(numerator, denominator)
        
        if positive_or_negative == "positive":
            frac = abs(frac)
        elif positive_or_negative == "negative":
            frac = -1 * abs(frac)
        
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

