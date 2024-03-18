from random import randint
from typing import Tuple

import sympy as sy

class IntegrationCalculationOfHighSchool3:
    """高校3年生用の積分計算の問題と解答を出力
    
    Attributes:
        latex_answer (str): LaTeX形式を前提とした解答
        latex_problem (str): LaTeX形式を前提とした問題
    """
    def __init__(self, **settings):
        self.latex_answer, self.latex_problem = self._make_problem()
    def _make_problem(self) -> Tuple[str, str]:
        latex_answer = "dummy answer"
        latex_problem = "dummy problem"
        return latex_answer, latex_problem
