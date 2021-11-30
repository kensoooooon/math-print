from random import choice, randint, random

import sympy as sy


class SpecificLinearEquation:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._used_number_type_list = settings['used_number_type_list']
        self._answer_type = settings['linear_equation_type']
        self._used_character_type_list = ["x"]
        self._character_dict = {}
        for character in self._used_character_type_list:
            self._character_dict[character] = sy.Symbol(character, real=True)
        if self._answer_type == "ax_equal_b_only_integer":
            self.latex_answer, self.latex_problem = self._make_ax_equal_b_only_integer()
        elif self._answer_type == "ax_equal_b_all_number":
            self.latex_answer, self.latex_problem = self._make_ax_equal_b_all_number()
        elif self._answer_type == 'ax_plus_b_equal_c_only_integer':
            self.latex_answer, self.latex_problem = self._make_ax_plus_b_equal_c_only_integer()
        elif self._answer_type == 'ax_plus_b_equal_c_all_number':
            self.latex_answer, self.latex_problem = self._make_ax_plus_b_equal_c_all_number()
        else:
            raise ValueError("linear_equation_type may be wrong.")

    def _make_ax_equal_b_only_integer(self):
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

        # left = linear_coefficient * self._character_dict["x"]
        if linear_coefficient_latex == "1":
            left_latex = "x"
        elif linear_coefficient_latex == "-1":
            left_latex = "-x"
        else:
            left_latex = f"{linear_coefficient_latex} x"
        print(f"left_latex: {left_latex}")
        
        right = intercept
        if number_type_checker == "decimal":
            right_latex = sy.latex(float(right))
        else:
            right_latex = sy.latex(right)
        
        print(f"left_latex: {left_latex}")
        print(f"right_latex: {right_latex}")
        latex_answer = f"x = {answer_latex}"
        latex_problem = f"{left_latex} = {right_latex}"
        
        return latex_answer, latex_problem
    
    def _make_ax_equal_b_all_number(self):
        print(f"number_type_checker: {self._used_number_type_list}")
        number_type_checker = choice(self._used_number_type_list)
        print(f"checked_number_type: {number_type_checker}")

        if number_type_checker == "integer":
            left, left_latex = self._make_random_integer(10, -10, "character")
            if left == 1:
                left_latex = "x"
            elif left == -1:
                left_latex = "-x"
        elif number_type_checker == "frac":
            left, left_latex = self._make_random_frac(10, -10, "character")
        elif number_type_checker == "decimal":
            left, left_latex = self._make_random_decimal(10, -10, 10, "character")

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

    def _make_ax_plus_b_equal_c_only_integer(self):
        a_type_checker = choice(self._used_number_type_list)
        
        if a_type_checker == 'integer':
            a, a_latex = self._make_random_integer(10, -10, "number")
        elif a_type_checker == 'frac':
            a, a_latex = self._make_random_frac(10, -10, "number")
        elif a_type_checker == 'decimal':
            a, a_latex = self._make_random_decimal(10, -10, 10, "number")
        else:
            raise ValueError(f"a_type_checker is {a_type_checker}, it may be wrong.")
        
        c_type_checker = choice(self._used_number_type_list)
        
        if c_type_checker == 'integer':
            c, c_latex = self._make_random_integer(10, -10, "number")
        elif c_type_checker == 'frac':
            c, c_latex = self._make_random_frac(10, -10, "number")
        elif c_type_checker == 'decimal':
            c, c_latex = self._make_random_decimal(10, -10, 10, "number")
        else:
            raise ValueError(f"c_type_checker is {c_type_checker}, it may be wrong.")
        
        answer, answer_latex = self._make_random_integer(10, -10, "number")
        b = c - a * answer
        b_latex = sy.latex(b)
        
        left = a * self._character_dict["x"] + b
        left_latex = ""
        if a == 1:
            left_latex = left_latex + "x"
        elif a == -1:
            left_latex = left_latex + "-x"
        else:
            left_latex = left_latex + f"{a_latex}x"
        
        if ('decimal' in self._used_number_type_list) and ('frac' not in self._used_number_type_list):
            b_latex = sy.latex(float(b))
            answer_latex = sy.latex(float(answer))

        if b > 0:
            left_latex = left_latex + f"+ {b_latex}"
        elif b < 0:
            left_latex = left_latex + f"{b_latex}"

        right_latex = ""
        if c_type_checker == 'decimal':
            right_latex = right_latex + f"{sy.latex(float(c))}"
        else:
            right_latex = right_latex + f"{c_latex}"
        latex_problem = f"{left_latex} = {right_latex}"
        latex_answer = f"x = {answer_latex}"     
        return latex_answer, latex_problem

    def _make_ax_plus_b_equal_c_all_number(self):
        a_type_checker = choice(self._used_number_type_list)
        
        if a_type_checker == 'integer':
            a, a_latex = self._make_random_integer(10, -10, "number")
        elif a_type_checker == 'frac':
            a, a_latex = self._make_random_frac(5, -5, "number")
        elif a_type_checker == 'decimal':
            a, a_latex = self._make_random_decimal(10, -10, 10, "number")
        else:
            raise ValueError(f"a_type_checker is {a_type_checker}, it may be wrong.")
        
        c_type_checker = choice(self._used_number_type_list)
        
        if c_type_checker == 'integer':
            c, c_latex = self._make_random_integer(10, -10, "number")
        elif c_type_checker == 'frac':
            c, c_latex = self._make_random_frac(5, -5, "number")
        elif c_type_checker == 'decimal':
            c, c_latex = self._make_random_decimal(10, -10, 10, "number")
        else:
            raise ValueError(f"c_type_checker is {c_type_checker}, it may be wrong.")
        
        answer_type_checker = choice(self._used_number_type_list)
        if answer_type_checker == 'integer':
            answer, answer_latex = self._make_random_integer(10, -10, "number")
        elif answer_type_checker == 'frac':
            answer, answer_latex = self._make_random_frac(5, -5, "number")
        elif answer_type_checker == 'decimal':
            answer, answer_latex = self._make_random_decimal(10, -10, 10, "number")
        else:
            raise ValueError(f"c_type_checker is {c_type_checker}, it may be wrong.")       

        b = c - a * answer
        b_latex = sy.latex(b)
        
        left = a * self._character_dict["x"] + b
        left_latex = ""
        if a == 1:
            left_latex = left_latex + "x"
        elif a == -1:
            left_latex = left_latex + "-x"
        else:
            left_latex = left_latex + f"{a_latex}x"
        
        if ('decimal' in self._used_number_type_list) and ('frac' not in self._used_number_type_list):
            b_latex = sy.latex(float(b))
            answer_latex = sy.latex(float(answer))

        if b > 0:
            left_latex = left_latex + f"+ {b_latex}"
        elif b < 0:
            left_latex = left_latex + f"{b_latex}"

        right_latex = ""
        if c_type_checker == 'decimal':
            right_latex = right_latex + f"{sy.latex(float(c))}"
        else:
            right_latex = right_latex + f"{c_latex}"
        latex_problem = f"{left_latex} = {right_latex}"
        latex_answer = f"x = {answer_latex}"        
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