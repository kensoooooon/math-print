from random import choice, randint
from typing import Tuple

import sympy as sy

class IntegralCalculationOfHighSchool3:
    """高校3年生用の積分計算の問題と解答を出力
    
    Attributes:
        latex_answer (str): LaTeX形式を前提とした解答
        latex_problem (str): LaTeX形式を前提とした問題
    """
    def __init__(self, **settings):
        selected_integral_type = choice(settings["integral_types"])
        selected_calculation_type = choice(settings["calculation_types"])
        if selected_integral_type == "substitution_of_linear_expression":
            self.latex_answer, self.latex_problem = self._make_substitution_of_linear_expression_problem(selected_integral_type)

    def _make_substitution_of_linear_expression_problem(self, integral_type: str) -> Tuple[str, str]:
        """1次式の置換を用いるタイプの積分計算問題を作成

        Args:
            integral_type (str): 不定積分か定積分かの指定

        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題
        
        Developing:
            
        """
        latex_answer = "dummy answer"
        latex_problem = "dummy problem"
        return latex_answer, latex_problem
