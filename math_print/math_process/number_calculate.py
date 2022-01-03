from fractions import Fraction
from random import choice, randint, random

import sympy as sy


class NumberMathProblem:
    """
    とりあえず整数、分数、小数の3つを使った適当な演算を請け負うクラス
    属性として、latex用の問題文と回答を持っておく必要がある
    →tupleで持たせる
    """
    def __init__(self, term_number, max_number_to_frac, min_number_to_frac, used_number_type_list, used_operator_type_list):
        sy.init_printing(order='grevlex')
        self._term_number = term_number
        self._max_number_to_frac = max_number_to_frac
        self._min_number_to_frac = min_number_to_frac
        self._used_number_type_list = used_number_type_list
        self._used_operator_type_list = used_operator_type_list
        self.latex_answer, self.latex_problem = self._make_problem()

    def _make_problem(self):
        first_number_checker = choice(self._used_number_type_list)
        if first_number_checker == 'one_digit_integer':
            first_number, first_latex = self._make_random_integer_number(9, -9)
        elif first_number_checker == 'two_digit_integer':
            first_number, first_latex = self._make_random_integer_number(99, -99)
        elif first_number_checker == 'frac':
            first_number, first_latex = self._make_random_frac_number(8, -8)
        elif first_number_checker == 'decimal':
            first_number, first_latex = self._make_random_decimal_number(100, -100, 10)
        else:
            raise ValueError("The first number choice may be wrong. Please check 'used_number_type_list'.")

        answer = first_number
        latex_problem = first_latex
        # 後ろを追加していく
        for _ in range(self._term_number-1):
            num_type_checker = choice(self._used_number_type_list)
            # plus, minus, times, divided
            
            # 数字決定
            if num_type_checker == 'one_digit_integer':
                number, latex_number = self._make_random_integer_number(9, -9)
            elif num_type_checker == 'two_digit_integer':
                number, latex_number = self._make_random_integer_number(99, -99)
            elif num_type_checker == 'frac':
                number, latex_number = self._make_random_frac_number(8, -8)
            elif num_type_checker == 'decimal':
                number, latex_number = self._make_random_decimal_number(100, -100, 10)
            else:
                raise ValueError("The second and subsequent number may be wrong. Please check 'used_number_type_list'.")
            
            operator_type_checker = choice(self._used_operator_type_list)
            if operator_type_checker == "plus":
                answer = answer + number
                latex_problem = latex_problem + " + " + latex_number
            elif operator_type_checker == "minus":
                answer = answer - number
                latex_problem = latex_problem + " - " + latex_number
            elif operator_type_checker == "times":
                answer = answer * number
                latex_problem =  latex_problem + " \\times " + latex_number
            elif operator_type_checker == "divided":
                answer = answer / number
                latex_problem = latex_problem + " \\div " + latex_number
            else:
                raise ValueError("operator_checker isn't in any condition.")
        
        used_number_type_set = set(self._used_number_type_list)
        used_operator_type_set = set(self._used_operator_type_list)
        
        """
        if used_number_type_set == {'decimal'}:
            if 'divided' not in used_operator_type_set:
                if self._is_finite_decimal(number):
                    latex_answer = f"= {sy.latex(float(answer))}"
                    return latex_answer, latex_problem
        """
        if ('decimal' in used_number_type_set)  and ('frac' not in used_number_type_set):
            if 'divided' not in used_operator_type_set:
                if not answer.is_Integer:
                    latex_answer = f"= {sy.latex(float(answer))}"
                    return latex_answer, latex_problem
            
        latex_answer = f"= {sy.latex(answer)}"
        
        return latex_answer, latex_problem

    def _make_random_frac_number(self, max_num, min_num):
        checker = random()
        if checker > 0.5:
            numerator = randint(2, max_num)
            denominator = randint(2, max_num)
        else:
            numerator = randint(min_num, -2)
            denominator = randint(2, max_num)
        
        frac = sy.Rational(numerator, denominator)
        
        frac_with_number_latex = sy.latex(frac)
        if frac < 0:
            frac_with_number_latex = f"\\left({frac_with_number_latex}\\right)"
        return frac, frac_with_number_latex
        
    
    def _make_random_decimal_number(self, max_num, min_num, denominator):
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

        decimal_with_number = frac_for_decimal
        decimal_with_number_latex = sy.latex(decimal)
        if decimal < 0:
            decimal_with_number_latex = f"\\left({decimal_with_number_latex}\\right)"
        return decimal_with_number, decimal_with_number_latex
    
    def _make_random_integer_number(self, max_num, min_num):
        checker = random()
        if checker > 0.5:
            numerator = randint(1, max_num)
        else:
            numerator = randint(min_num, -1)
        
        # integer = numerator
        integer = sy.Integer(numerator)

        integer_with_number_latex = sy.latex(integer)
        if integer < 0:
            integer_with_number_latex = f"\\left({integer_with_number_latex}\\right)"
        return integer, integer_with_number_latex
    
    def _is_finite_decimal(self, number):
        print("------------------")
        print(f"number is {number}")
        denominator_list = list(sy.factorint(number.denominator).keys())
        denominator_set = set(denominator_list)
        print(f"denominator_set:{denominator_set}")
        if denominator_set == set():
            return True
        elif denominator_set == {2}:
            return True
        elif denominator_set == {5}:
            return True
        elif denominator_set == {2, 5}:
            return True
        else:
            return False
