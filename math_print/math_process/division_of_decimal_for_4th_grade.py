"""
from random import randint
import sympy as sy

def truncate_decimal(number, decimal_places):
    return sy.floor(number * 10 ** decimal_places) / 10 ** decimal_places

number = truncate_decimal(0.12345, 2)
print(number)
print(f"float_number: {sy.Float(number)}")
print(f"latex_number: {sy.latex(sy.Float(number))}")

from random import randint
import sympy as sy


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

for _ in range(10):
    number_of_decimal_places = randint(0, 3)
    print(f"number_of_decimal_places: {number_of_decimal_places}")
    random_number = random_decimal(number_of_decimal_places)
    print(f"random_number: {random_number}")
    print(f"latex_number: {sy.latex(random_number)}")
    print("----------------------------------")
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
        # 6.8, 
        divided_number, divided_number_latex = self._random_number(divided_number_of_decimal_places)
        dividing_number, dividing_number_latex = self._random_number(dividing_number_of_decimal_places)
        latex_problem = f"\\( {divided_number_latex} \\div {dividing_number_latex} \\)"
        answer = divided_number / dividing_number
        truncated_answer, truncated_answer_latex = self._truncate_decimal(answer, 2)
        remainder = 
        return latex_answer, latex_problem

    def _random_number(self, number_of_decimal_places: int) -> Union[sy.Integer, sy.Float]:
        """指定された小数点以下の桁数が保証された小数(整数含む)を出力

        Args:
            number_of_decimal_places (int): 小数点以下の桁数。0のときは整数

        Returns:
            Union[sy.Integer, sy.Float]: 整数のときはsy.Integer, 小数のときはsy.Floatをそれぞれ返す
        """
        if number_of_decimal_places == 0:
            number = sy.Rational(randint(1, 9), 1)
            number_latex = sy.latex(sy.Float(number))
        else:
            numerator = randint(10 ** (number_of_decimal_places - 1), 10 ** number_of_decimal_places - 1)
            denominator = 10 ** number_of_decimal_places
            number = sy.Rational(numerator, denominator)
            number_latex = sy.latex(sy.Float(number))
        return number, number_latex

    def _truncate_decimal(self, number: sy.Rational, number_of_decimal_places: int) -> str:
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
