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
        problem_types = settings["used_problems"]
        selected_solid_body = choice(settings["used_solid_bodies"])
        if selected_solid_body == "quadrangular_prism":
            self.solid_body = "quadrangular_prism"
            self.latex_answer, self.latex_problem = self._make_quadrangular_prism_problem(problem_types)
        elif selected_solid_body == "triangular_prism":
            self.solid_body = "triangular_prism"
            self.latex_answer, self.latex_problem = self._make_triangular_prism_problem(problem_types)
        else:
            raise ValueError(f"'selected_solid_body' is {selected_solid_body}. This must be 'quadrangular_prism' or 'triangular_prism.")
    
    def _make_quadrangular_prism_problem(self, problem_types):
        """直方体を用いた直線と平面の位置関係の問題を作成

        Args:
            problem_types (list): 使用される問題(直線と直線, 直線と平面, 平面と平面)が格納されている

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Developing:
            上面左手前から反時計回りでABCD, EFGHの直方体
            答えさせる問題のタイプ
            -> ある辺に平行な直線は？
            -> ある辺と垂直な直線は？
            -->> 直線同士の位置関係
            -->> 平面同士の位置関係
            -->> 直線と平面の位置関係
        """
        latex_answer = ""
        latex_problem = ""
        for _ in range(3):
            selected_problem_type = choice(problem_types)
            if selected_problem_type == "line_and_line":
                """
                二直線の位置関係
                -> 平行, ねじれ, 垂直に交わる, (垂直以外に交わる)
                """
            elif selected_problem_type == "line_and_flat":
            elif selected_problem_type == "flat_and_flat":
            else:
                raise ValueError(f"'selected_problem_type' is {selected_problem_type}."\
                                 "This must be 'line_and_line', 'line_and_flat' or 'flat_and_flat'.")
        parallel_lines = (
            ("直線AB", "直線CD", "直線EF", "直線GH",),
            ("直線AD", "直線BC", "直線EH", "直線FG",),
            ("直線AE", "直線BF", "直線CG", "直線DH",),
            )
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
    