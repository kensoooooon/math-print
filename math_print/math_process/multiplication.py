from random import choice, randint
from typing import Dict, Tuple

import sympy as sy


class MultiplicationFor3rdGrade:
    """3年生用の掛け算の問題と解答を出力
    
    Attributes:
        _digits_of_multiplied_number (list): 掛けられる数の桁数の候補が格納
        _digits_of_multiplying_number (list): 掛ける数の桁数の候補が格納
        latex_answer (str): latex形式の解答
        latex_problem (str): latex形式の問題
    """
    def __init__(self, **settings: Dict) -> None:
        """初期設定
        
        Args:
            settings(dict): 問題の設定を格納
        """
        self._digits_of_multiplied_number = settings["digits_of_multiplied_number"]
        self._digits_of_multiplying_number = settings["digits_of_multiplying_number"]
        self.latex_answer, self.latex_problem = self._make_problem()

    def _make_problem(self) -> Tuple[str, str]:
        """問題と解答の作成を担当
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        selected_digit_of_multiplied_number = int(choice(self._digits_of_multiplied_number))
        min_multiplied_number = 10 ** (selected_digit_of_multiplied_number - 1)
        max_multiplied_number = 10 ** selected_digit_of_multiplied_number - 1
        multiplied_number = randint(min_multiplied_number, max_multiplied_number)
        selected_digit_of_multiplying_number = int(choice(self._digits_of_multiplying_number))
        min_multiplying_number = 10 ** (selected_digit_of_multiplying_number - 1)
        max_multiplying_number = 10 ** selected_digit_of_multiplying_number - 1
        multiplying_number = randint(min_multiplying_number, max_multiplying_number)
        answer = multiplied_number * multiplying_number
        latex_answer = f"= {sy.latex(answer)}"
        latex_problem = f"{sy.latex(multiplied_number)} \\times {sy.latex(multiplying_number)}"
        return latex_answer, latex_problem
