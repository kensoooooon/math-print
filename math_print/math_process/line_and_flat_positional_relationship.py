from random import choice, random, randint

import sympy as sy


class LineAndFlatPositionalRelationship:
    """直線と平面の位置関係の問題と解答を出力
    
    Attributes:
        latex_answer (str): latex形式で記述された解答
        latex_problem (str): latex形式で記述された問題
        solid_body (str): 問題に使用される立体
    """
    def __init__(self, **settings):
        """初期設定
        
        Args:
            settings (dict): 問題に使用する各種設定を格納
        """
        selected_solid_body = choice(settings["used_solid_bodies"])
        if selected_solid_body == "quadrangular_prism":
            self.solid_body = "quadrangular_prism"
            self.latex_answer, self.latex_problem = self._make_quadrangular_prism_problem()
        elif selected_solid_body == "triangular_prism":
            self.solid_body = "triangular_prism"
            self.latex_answer, self.latex_problem = self._make_triangular_prism_problem()
        else:
            raise ValueError(f"'selected_solid_body' is {selected_solid_body}. This must be 'quadrangular_prism' or 'triangular_prism.")
    
    def _make_quadrangular_prism_problem(self):
        """直方体を用いた直線と平面の位置関係の問題を作成

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Developing:
            上面から反時計回りでABCD, EFGHの直方体
        """
        
        latex_answer = "dummy answer in quadrangular problem."
        latex_problem = "dummy problem in quadrangular problem."
        return latex_answer, latex_problem
    
    def _make_triangular_prism_problem(self):
        """三角柱を用いた直線と平面の位置関係の問題を作成

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        latex_answer = "dummy answer in triangular problem."
        latex_problem = "dummy problem in triangular problem."
        return latex_answer, latex_problem
    