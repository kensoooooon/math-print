"""
from random import randint
import sympy as sy

def truncate_decimal(number, decimal_places):
    return sy.floor(number * 10 ** decimal_places) / 10 ** decimal_places

def random_decimal(number_of_decimal_places):
    integer_part = randint(1, 50)
    if number_of_decimal_places == 0:
        number = sy.Integer(integer_part)
    elif number_of_decimal_places == 1:
        decimal_part = randint(1, 9) * sy.Float(0.1)
        number = integer_part + decimal_part
    elif number_of_decimal_places == 2:
        decimal_part = randint(0, 9) * sy.Float(0.1) + randint(1, 9) * sy.Float(0.01)
        number = integer_part + decimal_part
    elif number_of_decimal_places == 3:
        decimal_part = randint(0, 9) * sy.Float(0.1) + randint(0, 9) * sy.Float(0.01) + randint(1, 9) * sy.Float(0.001)
        number = integer_part + decimal_part
    return number

for _ in range(3):
    dividing_number_of_decimal_places = randint(0, 3)
    print(f"dividing_number_of_decimal_places: {dividing_number_of_decimal_places}")
    dividing_number = random_decimal(dividing_number_of_decimal_places)
    print(f"dividing_number: {dividing_number}")
    print(f"dividing_latex_number: {sy.latex(dividing_number)}")
    print("-----------")
    divided_number_of_decimal_places = randint(0, 3)
    print(f"divided_number_of_decimal_places: {divided_number_of_decimal_places}")
    divided_number = random_decimal(divided_number_of_decimal_places)
    print(f"divided_number: {divided_number}")
    print(f"divided_latex_number: {sy.latex(divided_number)}")
    print("-----------")
    answer = divided_number / dividing_number
    print(f"answer: {answer}")
    truncated_answer = truncate_decimal(answer, 2)
    print(f"truncated_answer: {truncated_answer}")
    floated_truncated_answer = sy.Float(truncated_answer)
    print(f"floated_truncated_answer: {floated_truncated_answer}")
    floated_truncated_latex_answer = sy.latex(floated_truncated_answer)
    print(f"floated_truncated_latex_answer: {floated_truncated_latex_answer}")
    print("-----------")
    # a ÷ b = q ... r
    # a = bq + r
    # r = a - bq
    remainder = divided_number - dividing_number * floated_truncated_answer
    print(f"remainder: {remainder}")
    print(f"latex_remainder: {sy.latex(remainder)}")
    print("----------------------------------")
    

# conversion
from random import randint, uniform
import sympy as sy


def truncate_decimal(number, decimal_places):
    return sy.floor(number * 10 ** decimal_places) / 10 ** decimal_places

def random_decimal(number_of_decimal_places):
    integer_part = randint(1, 50)
    if number_of_decimal_places == 0:
        number = sy.Integer(integer_part)
    elif number_of_decimal_places == 1:
        decimal_part = randint(1, 9) * sy.Float(0.1)
        number = integer_part + decimal_part
    elif number_of_decimal_places == 2:
        decimal_part = randint(0, 9) * sy.Float(0.1) + randint(1, 9) * sy.Float(0.01)
        number = integer_part + decimal_part
    elif number_of_decimal_places == 3:
        decimal_part = randint(0, 9) * sy.Float(0.1) + randint(0, 9) * sy.Float(0.01) + randint(1, 9) * sy.Float(0.001)
        number = integer_part + decimal_part
    return number


# a = bq + r <=> a ÷ b = q ... r
b = random_decimal(0)
print(f"b: {b}")
q = random_decimal(1)
print(f"q: {q}")
r = uniform(0, 0.1 * q)
print(f"r: {r}")
truncated_r = truncate_decimal(r, 1)
print(f"truncated_r: {truncated_r}")



import sympy as sy

# divided_number = sy.N(sy.Float(9.3), 2)
divided_number = sy.Float(9.3)
print(f"divided_number: {divided_number}")
dividing_number = sy.Integer(38)
print(f"dividing_number: {dividing_number}")
answer = (divided_number / dividing_number).round(2)
print(f"answer: {answer}")
remainder = divided_number - dividing_number * answer
print(f"remainder: {remainder}")
print("------------------------")

divided_number = sy.Float(9.3)
print(f"divided_number: {divided_number}")
dividing_number = sy.Integer(38)
print(f"dividing_number: {dividing_number}")
answer = divided_number / dividing_number
print(f"answer: {answer}")
rounded1_answer = answer.round(1)
print(f"rounded1_answer: {rounded1_answer}")
rounded2_answer = answer.round(2)
print(f"rounded2_answer: {rounded2_answer}")
rounded3_answer = answer.round(3)
print(f"rounded3_answer: {rounded3_answer}")
rounded4_answer = answer.round(4)
print(f"rounded4_answer: {rounded4_answer}")
remainder_with_answer = divided_number - dividing_number * answer
print(f"remainder_with_answer: {remainder_with_answer}")
remainder_with_rounded1_answer = divided_number - dividing_number * rounded1_answer
print(f"remainder_with_rounded1_answer: {remainder_with_rounded1_answer}")
remainder_with_rounded2_answer = divided_number - dividing_number * rounded2_answer
print(f"remainder_with_rounded2_answer: {remainder_with_rounded2_answer}")
remainder_with_rounded3_answer = divided_number - dividing_number * rounded3_answer
print(f"remainder_with_rounded3_answer: {remainder_with_rounded3_answer}")
remainder_with_rounded4_answer = divided_number - dividing_number * rounded4_answer
print(f"remainder_with_rounded4_answer: {remainder_with_rounded4_answer}")
print("------------------------")
"""
from random import randint, choice
from typing import Dict, Tuple, Union


import sympy as sy


class DivisionOfDecimalFor4thGrade:
    """小学4年生用の小数の割り算の問題と解答を出力
    
    Attributes:
        latex_answer (str): latex形式と通常の文字列が混在した解答
        latex_problem (str): latex形式と通常の文字列が混在した問題
    """
    def __init__(self, **settings: Dict) -> None:
        """初期設定
        
        Args:
            settings (dict): 初期設定が格納された辞書
        """
        sy.init_printing(order="grevlex")
        selected_divided_number_of_decimal_places = int(choice(settings["divided_numbers_of_decimal_places"]))
        selected_dividing_number_of_decimal_places = int(choice(settings["dividing_numbers_of_decimal_places"]))
        selected_remainder = choice(settings["remainder_types"])
        if selected_remainder == "with_remainder":
            with_remainder = True
        elif selected_remainder == "without_remainder":
            with_remainder = False
        self.latex_answer, self.latex_problem = self._make_problem(
            with_remainder,
            selected_divided_number_of_decimal_places,
            selected_dividing_number_of_decimal_places)
    
    def _make_problem(self, with_remainder: bool, divided_number_of_decimal_places: int, dividing_number_of_decimal_places: int) -> Tuple[str, str]:
        """問題の作成

        Args:
            with_remainder (bool): 余りの有無
            divided_number_of_decimal_places (int): 割られる数の桁数
            dividing_number_of_decimal_places (int): 割る数の桁数

        Returns:
            tuple: 解答と問題(latex_answer, latex_problem)
        """ 
        divided_number, divided_number_latex = self._random_number(divided_number_of_decimal_places)
        dividing_number, dividing_number_latex = self._random_number(dividing_number_of_decimal_places)
        latex_problem = f"\\( {divided_number_latex} \\div {dividing_number_latex} \\)"
        answer = divided_number / dividing_number
        # truncated_answer, truncated_answer_latex = self._truncate_decimal(answer, 2)
        rounded_answer = sy.N(answer, 3)
        print(f"rounded_answer: {rounded_answer}, type: {type(rounded_answer)}")
        rounded_answer_latex = sy.latex(rounded_answer)
        remainder = divided_number - rounded_answer * dividing_number
        # truncated_remainder, truncated_remainder_latex = self._truncate_decimal(remainder, 3)
        rounded_remainder = sy.N(remainder, 3)
        print(f"rounded_remainder: {rounded_remainder}, type: {type(rounded_remainder)}")
        print("----------------------------")
        rounded_remainder_latex = sy.latex(rounded_remainder)
        latex_answer = f"\\( {rounded_answer_latex} \\) あまり \\( {rounded_remainder_latex} \\)"
        return latex_answer, latex_problem

    def _random_number(self, number_of_decimal_places: int) -> Tuple[Union[sy.Integer, sy.Float], str]:
        """指定された小数点以下の桁数が保証された小数(整数含む)を出力

        Args:
            number_of_decimal_places (int): 小数点以下の桁数。0のときは整数

        Returns:
            Union[sy.Integer, sy.Float]: 整数のときはsy.Integer, 小数のときはsy.Floatをそれぞれ返す
        """
        if number_of_decimal_places == 0:
            number = sy.Integer(randint(1, 20))
            number_latex = sy.latex(number)
        else:
            numerator = randint(10 ** (number_of_decimal_places - 1), 10 ** number_of_decimal_places - 1)
            denominator = 10 ** number_of_decimal_places
            number = sy.Rational(numerator, denominator)
            number_latex = sy.latex(sy.Float(number))
        return number, number_latex

    def _truncate_decimal(self, number: sy.Rational, number_of_decimal_places: int) -> Tuple[sy.Rational, str]:
        """指定された桁数より下を切り捨てた小数の文字列を出力

        Args:
            number (sy.Rational): _description_
            number_of_decimal_places (int): _description_

        Returns:
            tuple: 計算用の数と文字列(floored_number, str_number)
        """
        float_number = sy.Float(number)
        floored_number = sy.floor(float_number * 10 ** number_of_decimal_places) / 10 ** number_of_decimal_places
        str_number = sy.latex(sy.Float(floored_number))
        return floored_number, str_number
    
    def _round_decimal(self, number, number_of_decimal_places):
        pass
