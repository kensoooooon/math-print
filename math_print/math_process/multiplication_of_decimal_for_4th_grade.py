from random import randint, choice
import re
from typing import Dict, Tuple, Union


import sympy as sy


class MultiplicationOfDecimalFor4thGrade:
    """小数を含むかけ算の問題と解答の作成・格納
    
    Attributes:
        latex_answer (str): latex形式で記述された解答
        latex_problem (str): latex形式で記述された問題
    """
    def __init__(self, **settings: Dict) -> None:
        """初期設定

        Args:
            settings (dict): 問題の設定を格納
        """
        sy.init_printing(order="grevlex")
        selected_multiplied_number_of_decimal_places = int(choice(settings["multiplied_numbers_of_decimal_places"]))
        selected_multiplying_number_of_decimal_places = int(choice(settings["multiplying_numbers_of_decimal_places"]))
        self.latex_answer, self.latex_problem = self._make_problem(selected_multiplied_number_of_decimal_places, selected_multiplying_number_of_decimal_places)

    def _make_problem(self, multiplied_number_of_decimal_places: int, multiplying_number_of_decimal_places: int) -> Tuple[str, str]:
        """問題と解答の作成

        Args:
            multiplied_number_of_decimal_places (int): かけられる数の小数点以下の桁数
            multiplying_number_of_decimal_places (int): かける数の小数点以下の桁数

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        multiplied_number = self._make_random_number(multiplied_number_of_decimal_places)
        multiplying_number = self._make_random_number(multiplying_number_of_decimal_places)
        answer = multiplied_number * multiplying_number
        answer_str = re.sub(".0+$", "", sy.latex(answer))
        latex_answer = f"= {answer_str}"
        latex_problem = f"{sy.latex(multiplied_number)} \\times {sy.latex(multiplying_number)}"
        return latex_answer, latex_problem

    def _make_random_number(self, number_of_decimal_places: int) -> Union[sy.Integer, sy.Float]:
        """指定された小数点以下の桁数に応じて出力

        Args:
            number_of_decimal_places (int): 小数点以下の桁数(0だと整数)
        
        Returns:
            number (Union[sy.Integer, sy.Float]): 数
        """
        if number_of_decimal_places == 0:
            number = sy.Integer(randint(1, 100))
        elif number_of_decimal_places == 1:
            number = sy.Float(1 * randint(0, 99) + 0.1 * randint(1, 9))
        elif number_of_decimal_places == 2:
            number = sy.Float(1 * randint(0, 9) + 0.1 * randint(0, 9) + 0.01 * randint(1, 9))
        elif number_of_decimal_places == 3:
            number = sy.Float(1 * randint(0, 9) + 0.1 * randint(0, 9) + 0.01 * randint(0, 9) + 0.001 * randint(1, 9))
        else:
            raise ValueError(f"'number_of_decimal_places' is {number_of_decimal_places}. It must be 0, 1, 2 or 3.")
        return number
