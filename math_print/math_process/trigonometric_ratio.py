"""
# by degree

from random import choice
import sympy as sy

# 0 ~ 180
# step by 30
list_30 = [i * 30 for i in range(6 + 1)]
list_45 = [i * 45 for i in range(4 + 1)]
candidates = sorted(list(set(list_30 + list_45)))
print(candidates)
selected_degree = choice(candidates)
print(selected_degree)
selected_radian = selected_degree * sy.pi / 180
sin_value = sy.sin(selected_radian)
print(sin_value)
cos_value = sy.cos(selected_radian)
print(cos_value)
"""

from random import choice

import sympy as sy


class TrigonometricRatioProblem:
    """三角比の値と角度に関連する問題を出力
    
    Attributes:
        _problem_types (list): 問題の候補を格納
        _used_trigonometric_ratios (list): 使用される三角比の候補を格納
        latex_answer (str): latex形式で記述された解答
        latex_answer (str): latex形式で記述された問題
    """
    def __init__(self, **settings):
        """初期処理
        
        settings (dict): 問題設定を格納
        """
        self._problem_types = settings["problem_types"]
        self._used_trigonometric_ratios = settings["used_trigonometric_ratios"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        """問題作成のコントローラー

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        selected_problem_type = choice(self._problem_types)
        if selected_problem_type == "value_to_degree":
            latex_answer, latex_problem = self._make_value_to_degree_problem()
        elif selected_problem_type == "degree_to_value":
            latex_answer, latex_problem = self._make_degree_to_value_problem()
        return latex_answer, latex_problem
    
    def _make_value_to_degree_problem(self):
        """値から角度を求める問題と解答の出力
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        list_30 = [i * 30 for i in range(7)]
        list_45 = [i * 45 for i in range(5)]
        degree_candidates = list(set(list_30 + list_45))
        selected_degree = choice(degree_candidates)
        latex_answer = f"{selected_degree}^{{\\circ}}"
        selected_radian = selected_degree * sy.pi / 180
        
        return latex_answer, latex_problem
    
    def _make_degree_to_value_problem(self):
        """角度から値を求める問題と解答の出力

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        latex_answer = "hogee"
        latex_problem = "fugaaa"
        return latex_answer, latex_problem
