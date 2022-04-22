from random import choice, randint, random

import sympy as sy


class CompletingTheSquareProblem:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._used_number_type_list = settings["used_number_type_list"]
        self._character_dict = {}
        self._character_dict["x"] = sy.Symbol("x", real=True)
        if settings["number_including_in_bracket"] == "not_including_fraction":
            self.latex_answer, self.latex_problem = self._make_only_integer_completing_the_square()
        elif settings["number_including_in_bracket"] == "including_fraction":
            self.latex_answer, self.latex_problem = self._make_completing_the_square()
    
    def _make_only_integer_completing_the_square(self):
        integer_in_bracket, integer_in_bracket_latex = self._make_random_integer(4, -4)
        
        a_checker = self._number_type_selector()
        
        if a_checker == "integer":
            a, a_latex = self._make_random_integer(4, -4)
        elif a_checker == "frac":
            a, a_latex = self._make_random_frac(8, -8)
        
        b = 2 * a * integer_in_bracket
        b_latex = sy.latex(b)
        
        c_checker = self._number_type_selector()
        
        if c_checker == "integer":
            c, c_latex = self._make_random_integer(10, -10)
        elif c_checker == "frac":
            c, c_latex =  self._make_random_frac(8, -8)
        
        x = self._character_dict["x"]
        
        left = a * x * x + b * x + c
        left_latex = sy.latex(left)
        latex_problem = left_latex
        
        number_in_bracket  = b / 2 * a
        number_in_bracket_latex = sy.latex(number_in_bracket)
        answer_constant = - (b * b / (4 * a)) + c
        answer_constant_latex = sy.latex(answer_constant)
        
        right_latex = "="

        if a != 1:
            if a == -1:
                right_latex += "-"
            else:
                right_latex += f"{a_latex}"

        if  integer_in_bracket > 0:
            right_latex += f"\\left( x + {integer_in_bracket_latex}\\right)^2"
        elif integer_in_bracket < 0:
            right_latex += f"\\left( x {integer_in_bracket_latex}\\right)^2"
        
        if answer_constant > 0:
            right_latex += f"+ {answer_constant_latex}"
        elif answer_constant < 0:
            right_latex += f"{answer_constant_latex}"
        
        latex_answer = right_latex
        
        return latex_answer, latex_problem
    
    def _make_completing_the_square(self):
        a_checker = self._number_type_selector()
        
        if a_checker == "integer":
            a, a_latex = self._make_random_integer(4, -4)
        elif a_checker == "frac":
            a, a_latex = self._make_random_frac(8, -8)
        
        b_checker = self._number_type_selector()
        
        if b_checker == "integer":
            b, b_latex = self._make_random_integer(4, -4)
        elif b_checker == "frac":
            b, b_latex = self._make_random_frac(8, -8)

        c_checker = self._number_type_selector()
        
        if c_checker == "integer":
            c, c_latex = self._make_random_integer(4, -4)
        elif c_checker == "frac":
            c, c_latex = self._make_random_frac(8, -8)
        
        x = self._character_dict["x"]
        
        before_completing = a * x * x + b * x + c
        latex_problem = sy.latex(before_completing)
        
        h, k = sy.symbols("h k")
        after_completing = a * (x + h) * (x + h) + k
        
        answer = sy.solve(before_completing - after_completing, [h, k])
        num_in_bracket = answer[0][0]
        num_in_bracket_latex = sy.latex(num_in_bracket)
        num_out_of_bracket = answer[0][1]
        num_out_of_bracket_latex = sy.latex(num_out_of_bracket)
        
        right_latex = "="
        if a != 1:
            if a == -1:
                right_latex += "-"
            else:
                right_latex += f"{a_latex}"
        
        if num_in_bracket > 0:
            right_latex += f"\\left( x + {num_in_bracket_latex} \\right)^2"
        elif num_in_bracket < 0:
            right_latex += f"\\left(x {num_in_bracket_latex} \\right)^2"
        
        if num_out_of_bracket > 0:
            right_latex += f"+ {num_out_of_bracket_latex}"
        elif num_out_of_bracket < 0:
            right_latex += f"{num_out_of_bracket_latex}"
        
        latex_answer = right_latex
        
        return latex_answer, latex_problem
    
    def _number_type_selector(self):
        if self._used_number_type_list:
            selected_number_type = choice(self._used_number_type_list)
        else:
            selected_number_type = choice(["integer", "frac"])
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


    
    def _make_random_integer(self, max_num, min_num):
        checker = random()
        if checker > 0.5:
            numerator = randint(1, max_num)
        else:
            numerator = randint(min_num, -1)
        
        integer = sy.Integer(numerator)
        integer_with_number_latex = sy.latex(integer)
        return integer, integer_with_number_latex
