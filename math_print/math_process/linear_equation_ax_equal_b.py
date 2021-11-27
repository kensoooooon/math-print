from random import choice, randint, random

import sympy as sy


class LinearEquationAxEqualB:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._used_number_type_list = settings['used_number_type_list']
        self._answer_type = settings['linear_equation_type']
        self._used_character_type_list = ["x"]
        self._character_dict = {}
        for character in self._used_character_type_list:
            self._character_dict[character] = sy.Symbol(character, real=True)
        if self._answer_type == "ax_equal_b_only_integer":
            self.latex_answer, self.latex_problem = self._make_integer_answer_problem()
        elif self._answer_type == "ax_equal_b_all_number":
            self.latex_answer, self.latex_problem = self._make_all_answer_problem()
        else:
            raise ValueError("linear_equation_type may be wrong.")

    def _make_integer_answer_problem(self):
        print(f"number_type_checker: {self._used_number_type_list}")
        number_type_checker = choice(self._used_number_type_list)
        print(f"checked_number_type: {number_type_checker}")
        
        if number_type_checker == "integer":
            linear_coefficient, linear_coefficient_latex = self._make_random_integer(10, -10, "number")
            answer, answer_latex = self._make_random_integer(10, -10, "number")
        elif number_type_checker == "frac":
            linear_coefficient, linear_coefficient_latex = self._make_random_frac(10, -10, "number")
            answer, answer_latex = self._make_random_integer(10, -10, "number")
        elif number_type_checker == "decimal":
            linear_coefficient, linear_coefficient_latex = self._make_random_decimal(10, -10, 10, "number")
            answer, answer_latex = self._make_random_integer(10, -10, "number")
        else:
            raise ValueError(f"number_type_checker may be wrong. value is {number_type_checker}")
        intercept = linear_coefficient * answer
        
        print(f"linear_coefficient: {linear_coefficient}")
        print(f"answer: {answer}")
        print(f"intercept: {intercept}")

        left = linear_coefficient * self._character_dict["x"]
        left_latex = sy.latex(left)
        right = intercept
        right_latex = sy.latex(right)
        
        latex_answer = f"x = {sy.latex(answer)}"
        latex_problem = f"{left_latex} = {right_latex}"
        
        return latex_answer, latex_problem
    
    def _make_all_answer_problem(self):
        print(f"number_type_checker: {self._used_number_type_list}")
        number_type_checker = choice(self._used_number_type_list)
        print(f"checked_number_type: {number_type_checker}")

        if number_type_checker == "integer":
            left, left_latex = self._make_random_integer(10, -10, "character")
        elif number_type_checker == "frac":
            left, left_latex = self._make_random_frac(10, -10, "character")
        elif number_type_checker == "decimal":
            right, right_latex = self._make_random_decimal(10, -10, 10, "character")

        number_type_checker = choice(self._used_number_type_list)

        if number_type_checker == "integer":
            right, right_latex = self._make_random_integer(10, -10, "number")
        elif number_type_checker == "frac":
            right, right_latex = self._make_random_frac(10, -10, "number")
        elif number_type_checker == "decimal":
            right, right_latex = self._make_random_decimal(10, -10, 10, "number")
        
        latex_problem = f"{left_latex} = {right_latex}"
        diff = left - right
        solve_result = sy.solve(diff, self._character_dict["x"])
        equation_answer = solve_result[0]
        answer = sy.collect(equation_answer, self._character_dict["x"])
        latex_answer = f"x = {sy.latex(answer)}"
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
            """
            if frac < 0:
                frac_with_character_latex = f"\\left({frac_with_character_latex}\\right)"
            """

            return frac_with_character, frac_with_character_latex

        elif number_or_character == "number":
            frac_with_number_latex = sy.latex(frac)
            """
            if frac < 0:
                frac_with_number_latex = f"\\left({frac_with_number_latex}\\right)"
            """
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
            """
            if decimal < 0:
                decimal_with_character_latex = f"\\left({decimal_with_character_latex}\\right)"
            """
            return decimal_with_character, decimal_with_character_latex

        elif number_or_character == "number":
            decimal_with_number = frac_for_decimal
            decimal_with_number_latex = sy.latex(decimal)
            """
            if decimal < 0:
                decimal_with_number_latex = f"\\left({decimal_with_number_latex}\\right)"
            """
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
            """
            if integer < 0:
                integer_with_character_latex = f"\\left({integer_with_character_latex}\\right)"
            """
            return integer_with_character, integer_with_character_latex

        elif number_or_character == "number":
            integer_with_number_latex = sy.latex(integer)
            """
            if integer < 0:
                integer_with_number_latex = f"\\left({integer_with_number_latex}\\right)"
            """
            return integer, integer_with_number_latex
        else:
            raise ValueError("There is something wrong with 'add_number_or_character'.")