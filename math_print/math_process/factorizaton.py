from random import choice, randint, random

import sympy as sy


class FactorizationProblem:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._factorization_type_list = settings["factorization_type_list"]
        self._used_coefficient = settings["used_coefficient"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        selected_factorization_type = choice(self._factorization_type_list)
        
        if selected_factorization_type == "ax+ab=a(x+b)":
            latex_answer, latex_problem = self._make_ax_plus_ab_problem()
        elif selected_factorization_type == "x^2+2ax+a^2=(x+a)^2":
            latex_answer, latex_problem = self._make_square_plus_problem()
        elif selected_factorization_type == "x^2-2ax+a^2=(x-a)^2":
            latex_answer, latex_problem = self._make_square_minus_problem()
        elif selected_factorization_type == "x^2+(a+b)x+ab=(x+a)(x+b)":
            latex_answer, latex_problem = self._make_cross_multiplication_problem()
        
        return latex_answer, latex_problem

    def _make_ax_plus_ab_problem(self):
        a_checker = choice(self._used_coefficient)
        
        if a_checker == "only_integer":
            a = randint(1, 8)
        elif a_checker == "integer_and_frac":
            if random() > 0.5:
                a = randint(1, 8)
            else:
                numerator = randint()

    # 数字だけ改修予定
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
    