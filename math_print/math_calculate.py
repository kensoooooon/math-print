from fractions import Fraction
from random import choice, randint, random


class MathProblem:
    """
    とりあえず整数、分数、小数の3つを使った適当な演算を請け負うクラス
    属性として、latex用の問題文と回答を持っておく必要がある
    →tupleで持たせる
    """
    def __init__(self, term_number, max_number_to_frac, min_number_to_frac, used_number_type_list):
        self._term_number = term_number
        self._max_number_to_frac = max_number_to_frac
        self._min_number_to_frac = min_number_to_frac
        self._used_number_type_list = used_number_type_list
        self.latex_answer, self.latex_problem = self._make_problem()

    def _make_problem(self):
        max_number = self._max_number_to_frac
        min_number = self._min_number_to_frac
        """
        演算子(operator)を挟む？
        addition, subtraction, multiplication, division
        """
        first_number_checker = choice(self._used_number_type_list)
        if first_number_checker == 'integer':
            first_number, first_latex = self._make_random_integer(max_number, min_number)
        elif first_number_checker == 'frac':
            first_number, first_latex = self._make_random_frac(max_number, min_number)
        elif first_number_checker == 'decimal':
            first_number, first_latex = self._make_random_decimal(max_number, min_number, 10)
        else:
            raise ValueError("The first number choice may be wrong. Please check 'used_number_type_list'.")

        answer = first_number
        latex_problem = first_latex
        # 後ろを追加していく
        for _ in range(self._term_number-1):
            num_type_checker = choice(self._used_number_type_list)
            operator_type_checker = random()
            
            # 数字決定
            if num_type_checker == 'integer':
                number, latex_number = self._make_random_integer(max_number, min_number)
            elif num_type_checker == 'frac':
                number, latex_number = self._make_random_frac(max_number, min_number)
            elif num_type_checker == 'decimal':
                number, latex_number = self._make_random_decimal(max_number, min_number, 10)
            else:
                raise ValueError("The second and subsequent number may be wrong. Please check 'used_number_type_list'.")
            # 演算終了時
            """
            if i == (self._term_number-1):
                latex_problem = latex_problem + latex_number
                break
            """
            # 足し算のとき
            if (operator_type_checker >= 0) and (operator_type_checker < 0.25):
                answer = answer + number
                latex_problem = latex_problem + " + " + latex_number
            # 引き算の時
            elif (operator_type_checker >= 0.25) and (operator_type_checker < 0.5):
                answer = answer - number
                latex_problem = latex_problem + " - " + latex_number
            # 掛け算の時
            elif (operator_type_checker >= 0.5) and (operator_type_checker < 0.75):
                answer = answer * number
                latex_problem =  latex_problem + " \\times " + latex_number
            # 割り算の時
            elif (operator_type_checker >= 0.75) and (operator_type_checker < 1):
                answer = answer / number
                latex_problem = latex_problem + " \\div " + latex_number
            else:
                raise ValueError("operator_checker isn't in any condition.")              

        answer_numerator = answer.numerator
        answer_denominator = answer.denominator
        if answer_numerator == 0:
            latex_answer = "0"
        elif answer_denominator == 1:
            latex_answer = answer_numerator
        else:
            latex_answer = f" = \\frac{{{answer_numerator}}}{{{answer_denominator}}}"
        return latex_answer, latex_problem

    def _make_random_frac(self, max_num, min_num):
        checker = random()
        if checker > 0.5:
            numerator = randint(2, max_num)
            denominator = randint(2, max_num)
        else:
            numerator = randint(min_num, -2)
            denominator = randint(2, max_num)
        
        frac = Fraction(numerator, denominator)
        if frac.denominator == 1:
            latex_frac = str(frac.numerator)
        else:
            latex_frac = f"\\frac{{{frac.numerator}}}{{{frac.denominator}}}"

        if frac < 0:
            latex_frac = f"\\left({latex_frac}\\right)"
        return frac, latex_frac
    
    def _make_random_decimal(self, max_num, min_num, denominator):
        checker = random()
        if checker > 0.5:
            numerator = randint(1, max_num)
        else:
            numerator = randint(min_num, -1)
        
        decimal = Fraction(f"{numerator}/{denominator}")
        if decimal > 0:
            latex_decimal = f"{float(decimal)}"
        elif decimal <= 0:
            latex_decimal = f"\\left({float(decimal)}\\right)"
        return decimal, latex_decimal
    
    def _make_random_integer(self, max_num, min_num):
        checker = random()
        if checker > 0.5:
            numerator = randint(1, max_num)
        else:
            numerator = randint(min_num, -1)
        
        integer = Fraction(f"{numerator}/1")
        if integer > 0:
            latex_integer = f"{int(integer)}"
        elif integer <= 0:
            latex_integer = f"\\left({int(integer)}\\right)"
        return integer, latex_integer

