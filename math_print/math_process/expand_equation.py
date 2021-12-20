from random import choice, randint, random

import sympy as sy


class ExpandEquationProblem:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._used_number_type_list = settings["used_number_type_list"]
        self._expand_equation_type = settings["expand_equation_type"]
        self._character_dict = {}
        for character in ["x", "y"]:
            self._character_dict[character] = sy.Symbol(character, real=True)
        if self._expand_equation_type == 'ax_times_bx_plus_c':
            self.latex_answer, self.latex_problem = self._make_ax_times_bx_plus_c()
        elif self._expand_equation_type == 'double_ax_times_bx_plus_c':
            self.latex_answer, self.latex_problem = self._make_double_ax_times_bx_plus_c()
    
    def _make_ax_times_bx_plus_c(self):
        a_checker = choice(self._used_number_type_list)
        
        if a_checker == "integer":
            a, a_latex = self._make_random_integer(8, -8, "number")
        elif a_checker == "frac":
            a, a_latex = self._make_random_frac(8, -8, "number")
        
        b_checker = choice(self._used_number_type_list)
        
        if b_checker == "integer":
            b, b_latex = self._make_random_integer(8, -8, "number")
        elif a_checker == "frac":
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