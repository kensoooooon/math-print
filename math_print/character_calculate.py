"""
latexまわり？正しく計算できていない系
足し算だけだと表示順除けば概ね

import sympy as sy

x = sy.Symbol("x")
frac = sy.Rational(1, 3)
print(f"frac: {frac}")
frac2 = sy.Rational(2, 10)
decimal = float(frac2)
print(f"decimal: {decimal}")
result = frac + decimal
print(f"result: {result}")
"""

from random import choice, randint, random
import sympy as sy


class CharacterMathProblem:

    def __init__(self, **settings):
        self._term_number = settings["term_number"]
        self._max_number_to_frac = settings["max_number_to_frac"]
        self._min_number_to_frac = settings["min_number_to_frac"]
        self._used_number_type_list = settings["used_number_type_list"]
        self._used_operator_type_list = settings["used_operator_type_list"]
        self._used_character_type_list = settings["used_character_type_list"]
        self._character_dict = {}
        for character in self._used_character_type_list:
            self._character_dict[character] = sy.Symbol(character)
        self.latex_answer, self.latex_problem = self._make_problem()

    def _make_problem(self):
        max_number = self._max_number_to_frac
        min_number = self._min_number_to_frac

        first_number_checker = choice(self._used_number_type_list)
        if first_number_checker == 'integer':
            first_number, first_latex = self._make_random_integer(max_number, min_number, "character")
        elif first_number_checker == 'frac':
            first_number, first_latex = self._make_random_frac(max_number, min_number, "character")
        elif first_number_checker == 'decimal':
            first_number, first_latex = self._make_random_decimal(max_number, min_number, 10, "character")
        else:
            raise ValueError("The first number choice may be wrong. Please check 'used_number_type_list'.")

        answer = first_number
        latex_problem = first_latex
        # 後ろを追加していく
        for _ in range(self._term_number-1):
            num_type_checker = choice(self._used_number_type_list)
            # plus, minus, times, divided
            operator_type_checker = choice(self._used_operator_type_list)
            
            # decide number type and character or number within if block
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
            else:
                raise ValueError("The second and subsequent number may be wrong. Please check 'used_number_type_list'.")

            # 足し算のとき
            if operator_type_checker == "plus":
                answer = answer + number
                latex_problem = latex_problem + " + " + latex_number
            # 引き算の時
            elif operator_type_checker == "minus":
                answer = answer - number
                latex_problem = latex_problem + " - " + latex_number
            # 掛け算の時
            elif operator_type_checker == "times":
                answer = answer * number
                latex_problem =  latex_problem + " \\times " + latex_number
            # 割り算の時
            elif operator_type_checker == "divided":
                answer = answer / number
                latex_problem = latex_problem + " \\div " + latex_number
            else:
                raise ValueError("operator_checker isn't in any condition.")              
        print(f"answer: {answer}")
        expanded_answer = sy.expand(answer)
        print(f"expanded_answer: {expanded_answer}")
        """
        simplified_answer = sy.simplify(expanded_answer)
        print(f"simplified_answer:{simplified_answer}")
        """
        collected_answer = sy.collect(expanded_answer, self._character_dict["x"])
        print(f"collected_answer: {collected_answer}")
        latex_answer = " = " + sy.latex(collected_answer)
        
        print(f"latex_answer: {latex_answer}")
        print(f"latex_problem: {latex_problem}")
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
            print(f"frac_with_character: {frac_with_character}, type: {type(frac_with_character)}")
            frac_with_character_latex = sy.latex(frac_with_character)
            print(f"frac_with_character_latex: {frac_with_character_latex}, type: {type(frac_with_character_latex)}")
            if frac < 0:
                frac_with_character_latex = f"\\left({frac_with_character_latex}\\right)"

            return frac_with_character, frac_with_character_latex

        elif number_or_character == "number":
            print(f"frac: {frac}, type:{type(frac)}")
            frac_with_number_latex = sy.latex(frac)
            print(f"frac_with_character_latex: {frac_with_number_latex}, type: {type(frac_with_number_latex)}")
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
        
        decimal = sy.Float(numerator/denominator)

        if number_or_character == "character":
            used_character = choice(self._used_character_type_list)
            decimal_with_character = decimal * self._character_dict[used_character]
            decimal_with_character_latex = sy.latex(decimal_with_character)
            if decimal < 0:
                decimal_with_character_latex = f"\\left({decimal_with_character_latex}\\right)"
            return decimal_with_character, decimal_with_character_latex

        elif number_or_character == "number":
            decimal_with_number_latex = sy.latex(decimal)
            if decimal < 0:
                decimal_with_number_latex = f"\\left({decimal_with_number_latex}\\right)"
            return decimal, decimal_with_number_latex
        else:
            raise ValueError("There is something wrong with 'add_number_or_character'.")
    
    def _make_random_integer(self, max_num, min_num, number_or_character):
        checker = random()
        if checker > 0.5:
            numerator = randint(1, max_num)
        else:
            numerator = randint(min_num, -1)
        
        integer = numerator
        
        if number_or_character == "character":
            used_character = choice(self._used_character_type_list)
            integer_with_character = integer * self._character_dict[used_character]
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

