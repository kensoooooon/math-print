from random import randint, choice
from typing import Dict, Tuple


import sympy as sy


class AdditionAndSubtractionOfDecimalFor4thGrade:
    """小学4年生用の小数の足し算・引き算の問題の問題と解答を作成、保持
    
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
        numbers_of_decimal_places = settings["numbers_of_decimal_places"]
        selected_calculation_type = choice(settings["calculation_types"])
        if selected_calculation_type == "addition":
            self.latex_answer, self.latex_problem = self._make_addition_problem(numbers_of_decimal_places)
        elif selected_calculation_type == "subtraction":
            self.latex_answer, self.latex_problem = self._make_subtraction_problem(numbers_of_decimal_places)
    
    def _make_addition_problem(self, numbers_of_decimal_places: list) -> Tuple[str, str]:
        """与えられた小数点以下の桁数の条件に応じて、小数の足し算の問題と解答を出力

        Args:
            numbers_of_decimal_places (list): 使用する小数点以下の桁数

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        number_of_decimal_places1 = int(choice(numbers_of_decimal_places))
        number1 = self._random_decimal_maker(number_of_decimal_places1)
        number_of_decimal_places2 = int(choice(numbers_of_decimal_places))
        number2 = self._random_decimal_maker(number_of_decimal_places2)
        answer = (number1 + number2).round(6)
        latex_answer = f"= {sy.latex(answer)}"
        latex_problem = f"{sy.latex(number1)} + {sy.latex(number2)}"
        return latex_answer, latex_problem
    
    def _make_subtraction_problem(self, numbers_of_decimal_places: list) -> Tuple[str, str]:
        """与えられた小数点以下の桁数の条件に応じて、小数の引き算の問題と解答を出力

        Args:
            number_of_decimal_places (list): 使用する小数点以下の桁数

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        number_of_decimal_places1 = int(choice(numbers_of_decimal_places))
        number1 = self._random_decimal_maker(number_of_decimal_places1)
        number_of_decimal_places2 = int(choice(numbers_of_decimal_places))
        number2 = self._random_decimal_maker(number_of_decimal_places2)
        if number1 >= number2:
            bigger_number, smaller_number = number1, number2
        else:
            bigger_number, smaller_number = number2, number1
        answer = (bigger_number - smaller_number).round(6)
        latex_answer = f"= {sy.latex(answer)}"
        latex_problem = f"{sy.latex(bigger_number)} - {sy.latex(smaller_number)}"
        return latex_answer, latex_problem
    
    def _random_decimal_maker(self, number_of_decimal_places: int) -> sy.Float:
        """指定された小数点以下の桁数が保証された小数を出力

        Args:
            number_of_decimal_places (int): 出力したい小数点以下の桁数 eg. 1 -> 0.1 ~ 0.9

        Returns:
            decimal_number (sy.Float): 指定された小数点以下の桁数を満たす小数
        
        Raises:
            ValueError: 1,2,3以外の実装されていない桁数が指定されたときに挙上
        """
        if number_of_decimal_places == 1:
            decimal_number = sy.Float(randint(1, 9) * 0.1)
        elif number_of_decimal_places == 2:
            decimal_number = sy.Float(randint(0, 9) * 0.1 + randint(1, 9) * 0.01)
        elif number_of_decimal_places == 3:
            decimal_number = sy.Float(randint(0, 9) * 0.1 + randint(0, 9) * 0.01 + randint(1, 9) * 0.001)
        else:
            raise ValueError(f"'number_of_decimal_places' is {number_of_decimal_places}. It must be 1, 2 or 3.")
        return decimal_number
