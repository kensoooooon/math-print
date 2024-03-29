from collections import defaultdict
from random import choice, randint, random

import sympy as sy


class LinearEquationProblem:

    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._term_number = settings["term_number"]
        self._max_number_to_frac = settings["max_number_to_frac"]
        self._min_number_to_frac = settings["min_number_to_frac"]
        self._used_number_type_list = settings["used_number_type_list"]
        self._used_operator_type_list = settings["used_operator_type_list"]
        self._used_character_type_list = ["x"]
        self._character_dict = {}
        for character in self._used_character_type_list:
            self._character_dict[character] = sy.Symbol(character, real=True)
        self.latex_answer, self.latex_problem = self._make_problem()

    def _make_problem(self):
        max_number = self._max_number_to_frac
        min_number = self._min_number_to_frac
        
        left = 0
        left_latex = ""
        right = 0
        right_latex = ""

        first_number_checker = self._number_type_selector()
        if first_number_checker == 'integer':
            first_number, first_latex = self._make_random_integer(max_number, min_number, "character")
        elif first_number_checker == 'frac':
            first_number, first_latex = self._make_random_frac(max_number, min_number, "character")
        elif first_number_checker == 'decimal':
            first_number, first_latex = self._make_random_decimal(max_number, min_number, 10, "character")

        left += first_number
        left_latex += first_latex

        second_number_checker = self._number_type_selector()
        if second_number_checker == 'integer':
            second_number, second_latex = self._make_random_integer(max_number, min_number, "number")
        elif second_number_checker == 'frac':
            second_number, second_latex = self._make_random_frac(max_number, min_number, "number")
        elif second_number_checker == 'decimal':
            second_number, second_latex = self._make_random_decimal(max_number, min_number, 10, "number")

        right += second_number
        right_latex += second_latex

        for i in range(self._term_number - 2):
            num_type_checker = self._number_type_selector()
            
            if num_type_checker == 'integer':
                if random() > 0.3:
                    number, latex_number = self._make_random_integer(max_number, min_number, "character")
                else:
                    number, latex_number = self._make_random_integer(max_number, min_number, "number")
            elif num_type_checker == 'frac':
                if random() > 0.3:
                    number, latex_number = self._make_random_frac(max_number, min_number, "character")
                else:
                    number, latex_number = self._make_random_frac(max_number, min_number, "number")
            elif num_type_checker == 'decimal':
                if random() > 0.3:
                    number, latex_number = self._make_random_decimal(max_number, min_number, 10, "character")
                else:
                    number, latex_number = self._make_random_decimal(max_number, min_number, 10, "number")

            operator_type_checker = self._operator_type_selector()
            if operator_type_checker == "plus":
                if random() > 0.5:
                    left = left + number
                    left_latex = left_latex + " + " + latex_number
                else:
                    right = right + number
                    right_latex = right_latex + " + " + latex_number
                    
            # 引き算の時
            elif operator_type_checker == "minus":
                if random() > 0.5:
                    left = left - number
                    left_latex = left_latex + " - " + latex_number
                else:
                    right = right - number
                    right_latex = right_latex + " - " + latex_number
            else:
                raise ValueError("operator_checker isn't in any condition.")


        latex_problem = f"{left_latex} = {right_latex}"
        diff = (left) - (right)
        diff_latex = sy.latex(diff)
        if "x" not in diff_latex:
            if diff_latex == "0":
                return "常に成り立つ", latex_problem
            else:
                return "常に成り立たない", latex_problem
        solve_result = sy.solve(diff, self._character_dict["x"])
        equation_answer = solve_result[0]
        answer = sy.collect(equation_answer, self._character_dict["x"])
        latex_answer = f"x = {sy.latex(answer)}"
        return latex_answer, latex_problem
    
    def _number_type_selector(self):
        if self._used_number_type_list:
            selected_number_type = choice(self._used_number_type_list)
        else:
            selected_number_type = choice(
                ["integer", "frac", "decimal"]
            )
        return selected_number_type
    
    def _operator_type_selector(self):
        if self._used_operator_type_list:
            selected_operator_type = choice(self._used_operator_type_list)
        else:
            selected_operator_type = choice(
                ["plus", "minus"]
            )
        return selected_operator_type

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
            if frac < 0:
                frac_with_character_latex = f"\\left({frac_with_character_latex}\\right)"

            return frac_with_character, frac_with_character_latex

        elif number_or_character == "number":
            frac_with_number_latex = sy.latex(frac)
            if frac < 0:
                frac_with_number_latex = f"\\left({frac_with_number_latex}\\right)"
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
            if decimal < 0:
                decimal_with_character_latex = f"\\left({decimal_with_character_latex}\\right)"
            return decimal_with_character, decimal_with_character_latex

        elif number_or_character == "number":
            decimal_with_number = frac_for_decimal
            decimal_with_number_latex = sy.latex(decimal)
            if decimal < 0:
                decimal_with_number_latex = f"\\left({decimal_with_number_latex}\\right)"
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
            if integer < 0:
                integer_with_character_latex = f"\\left({integer_with_character_latex}\\right)"
            return integer_with_character, integer_with_character_latex

        elif number_or_character == "number":
            integer_with_number_latex = sy.latex(integer)
            if integer < 0:
                integer_with_number_latex = f"\\left({integer_with_number_latex}\\right)"
            return integer, integer_with_number_latex
        else:
            raise ValueError("There is something wrong with 'add_number_or_character'.")
