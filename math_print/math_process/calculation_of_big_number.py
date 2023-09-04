from random import choice, randint
from typing import Dict, Tuple

import sympy as sy


class CalculationOfBigNumber:
    """1億を超える数を用いた計算の問題と解答を出力
    
    Attributes:
        latex_answer (str): latex形式と通常の文字列が混在した解答
        latex_problem (str): latex形式と通常の文字列が混在した解答
    """
    def __init__(self, **settings: Dict) -> None:
        """初期設定
        
        Args:
            settings (dict): 問題の設定
        """
        self._units_of_used_number = settings["units_of_used_number"]
        selected_problem_type = choice(settings["problem_types"])
        if selected_problem_type == "from_chinese_numerical_to_alphanumeric":
            self.latex_answer, self.latex_problem = self._make_from_chinese_numerical_to_alphanumeric_problem()
        elif selected_problem_type == "from_alphanumeric_to_chinese_numerical":
            self.latex_answer, self.latex_problem = self._make_from_alphanumeric_to_chinese_numerical_problem()
    
    def _make_from_chinese_numerical_to_alphanumeric_problem(self):
        latex_answer = "dummy answer in _make_from_chinese_numerical_to_alphanumeric_problem"
        latex_problem = "dummy problem in _make_from_chinese_numerical_to_alphanumeric_problem"
        return latex_answer, latex_problem
    
    def _make_from_alphanumeric_to_chinese_numerical_problem(self):
        latex_answer = "dummy answer in from_alphanumeric_to_chinese_numerical_problem"
        latex_problem = "dummy problem in from_alphanumeric_to_chinese_numerical_problem"
        return latex_answer, latex_problem
    