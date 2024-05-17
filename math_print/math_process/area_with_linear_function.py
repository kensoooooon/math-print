from random import choice
from typing import Dict

import sympy as sy


class AreaWithLinearFunction:
    """中学2年生用の、直線で囲まれた面積の問題と解答を出力
    
    Attributes:
        latex_answer (str): LaTeX形式を前提とした解答
        latex_problem (str): LaTeX形式を前提とした問題
    """
    def __init__(self, **settings: Dict):
        
        sy.init_printing(order='grevlex')
        selected_problem_type = choice(settings["problem_types"])
        if selected_problem_type == "one_side_on_axis":
            self.latex_answer, self.latex_problem = self._make_one_side_on_axis_problem()
        elif selected_problem_type == "no_side_on_axis":
            self.latex_answer, self.latex_problem = self._make_no_side_on_axis_problem()
    
    def _make_one_side_on_axis_problem(self):
        latex_answer = "dummy answer"
        latex_problem = "dummy problem"
        return latex_answer, latex_problem
    
    def _make_no_side_on_axis_problem(self):
        latex_answer = "dummy answer"
        latex_problem = "dummy problem"
        return latex_answer, latex_problem
    