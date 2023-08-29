"""
Note 4.27
全部のせの設定で、0.13333333....が発生。frac,decimal,floatあたりの設定が原因と考えられるが、いったん保留
"""

from collections import defaultdict
from random import choice, randint, random

import sympy as sy


class CharacterMathProblem:

    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._term_number = settings["term_number"]
        self._max_number_to_frac = settings["max_number_to_frac"]
        self._min_number_to_frac = settings["min_number_to_frac"]
        self._used_number_type_list = settings["used_number_type_list"]
        self._used_operator_type_list = settings["used_operator_type_list"]
        self._used_character_type_list = settings["used_character_type_list"]
        self._character_dict = {}
        for character in ["x", "y"]:
            self._character_dict[character] = sy.Symbol(character, real=True)
        self.latex_answer, self.latex_problem = self._make_problem()

    def _make_problem(self):
        """
        基本方針
        
        x = sy.Symbol("x", real=True)
        string_for_eval = "1 + 3 * x * 4 / 5"
        answer = eval(string_for_eval)
        latex_problem = ...
        の同時並行作成 
        
        4.29
        fixing
        latex_string_for_eval: sy.Rational(5, 2) * x- -1/ 4- (sy.Rational(-1, 2) * x)/ (sy.Rational(-9, 10) * x)+ (sy.Rational(-9, 10) * x)
        answer: 8*x/5 - 0.305555555555556
        expanded_answer: 8*x/5 - 0.305555555555556
        """
        max_number = self._max_number_to_frac
        min_number = self._min_number_to_frac
        
        x = self._character_dict["x"]
        y = self._character_dict["y"]
        
        latex_problem = ""
        latex_string_for_eval = ""
        first_num_type_checker = self._number_type_selector()
        if first_num_type_checker == "integer":
            number = self._make_random_integer_number(max_number, min_number)
        elif first_num_type_checker == "frac":
            number = self._make_random_frac_number(max_number, min_number)
        elif first_num_type_checker == "decimal":
            number = self._make_random_decimal_number(max_number, min_number, 10)
        
        first_term = number * x
        first_term_latex = sy.latex(first_term)
        if first_num_type_checker == "decimal":
            latex_problem += f"{float(number)}x"
        else:
            latex_problem += f"{first_term_latex}"

        if (first_num_type_checker == "frac") or (first_num_type_checker == "decimal"):
            latex_string_for_eval += f"sy.Rational({number.numerator}, {number.denominator}) * x"
        else:    
            latex_string_for_eval += f"{number} * x"
        
        for _ in range(self._term_number-1):
            num_type_checker = self._number_type_selector()
            if num_type_checker == "integer":
                number = self._make_random_integer_number(max_number, min_number)
            elif num_type_checker == "frac":
                number = self._make_random_frac_number(max_number, min_number)
            elif num_type_checker == "decimal":
                number = self._make_random_decimal_number(max_number, min_number, 10)
        
            operator_type_checker = self._operator_type_selector()
            if operator_type_checker == "plus":
                operator_for_latex = "+"
                operator_for_eval = "+"
            elif operator_type_checker == "minus":
                operator_for_latex = "-"
                operator_for_eval = "-"
            elif operator_type_checker == "times":
                operator_for_latex = "\\times"
                operator_for_eval = "*"
            elif operator_type_checker == "divided":
                operator_for_latex = "\\div"
                operator_for_eval = "/"
            
            character = choice(self._used_character_type_list)
            
            if random() > 0.3:
                term = number * self._character_dict[character]
                term_latex = sy.latex(term)

                if (num_type_checker == "frac") or (num_type_checker == "decimal"):
                    latex_string_for_eval += f"{operator_for_eval} (sy.Rational({number.numerator}, {number.denominator}) * {character})"
                else:
                    # add sy.integer(int()) not to display infinite decimal
                    latex_string_for_eval += f"{operator_for_eval} (sy.Integer({int(number)}) * {character})"
                
                if ("frac" not in self._used_number_type_list) and ("integer" not in self._used_number_type_list) and ("divided" not in self._used_operator_type_list):
                    number = float(number)
                if number < 0:
                    latex_problem += f"{operator_for_latex} \\left( {term_latex} \\right)"
                else:
                    latex_problem += f"{operator_for_latex} {term_latex}"
            else:
                term = number
                term_latex = sy.latex(term)
                
                if (num_type_checker == "frac") or (num_type_checker == "decimal"):
                    latex_string_for_eval += f"{operator_for_eval} (sy.Rational({number.numerator}, {number.denominator}))"
                else:
                    # add sy.integer(int()) not to display infinite decimal
                    latex_string_for_eval += f"{operator_for_eval} sy.Integer({int(number)})"
                
                if ("frac" not in self._used_number_type_list) and ("integer" not in self._used_number_type_list) and ("divided" not in self._used_operator_type_list):
                    number = float(number)
                if number < 0:
                    latex_problem += f"{operator_for_latex} \\left( {term_latex} \\right)"
                else:
                    latex_problem += f"{operator_for_latex} {term_latex}"
        
        answer = eval(latex_string_for_eval)
        expanded_answer = sy.expand(answer)
        collected_answer = sy.collect(expanded_answer, (self._character_dict["x"], self._character_dict["y"], sy.Integer(0)))
        latex_answer = f" = {sy.latex(expanded_answer)}"
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
                ["plus", "minus", "times", "divided"]
            )
        return selected_operator_type

    def _make_random_frac_number(self, max_num, min_num):
        while True:
            checker = random()
            if checker > 0.5:
                numerator = randint(2, max_num)
                denominator = randint(2, max_num)
            else:
                numerator = randint(min_num, -2)
                denominator = randint(2, max_num)
                
            if numerator != denominator:
                break
        
        frac = sy.Rational(numerator, denominator)

        return frac
    
    def _make_random_decimal_number(self, max_num, min_num, denominator):
        while True:
            checker = random()
            if checker > 0.5:
                numerator = randint(1, max_num)
            else:
                numerator = randint(min_num, -1)
            
            frac_for_decimal = sy.Rational(numerator, denominator)
            if frac_for_decimal != 1:
                break

        decimal_with_number = frac_for_decimal
        return decimal_with_number

    
    def _make_random_integer_number(self, max_num, min_num):
        checker = random()
        if checker > 0.5:
            numerator = randint(1, max_num)
        else:
            numerator = randint(min_num, -1)

        integer = sy.Integer(numerator)

        return integer

