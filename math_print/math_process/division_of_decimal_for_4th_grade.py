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
        divided_number = self._random_number(divided_number_of_decimal_places)
        dividing_number = self._random_number(divi)
        return latex_answer, latex_problem

    def _random_number(self, number_of_decimal_places: int) -> Union[sy.Integer, sy.Float]:
        """指定された小数点以下の桁数が保証された小数(整数含む)を出力

        Args:
            number_of_decimal_places (int): 小数点以下の桁数。0のときは整数

        Returns:
            Union[sy.Integer, sy.Float]: 整数のときはsy.Integer, 小数のときはsy.Floatをそれぞれ返す
        """
        if number_of_decimal_places == 0:
            integer_number = sy.Integer(randint(1, 9))
            return integer_number
        else:
            numerator = randint(10 ** (number_of_decimal_places - 1), 10 ** number_of_decimal_places - 1)
            denominator = 10 ** number_of_decimal_places
            rational = sy.Rational(numerator, denominator)
            float_number = sy.Float(rational)
            return float_number
