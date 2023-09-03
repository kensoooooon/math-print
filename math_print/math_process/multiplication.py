from random import choice, randint
from typing import Dict, Tuple, Union

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
        latex_answer = "dummy answer in multiplication."
        latex_problem = "dummy problem in multiplication."
        return latex_answer, latex_problem