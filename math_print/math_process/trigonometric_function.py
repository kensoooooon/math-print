from random import choice, randint, random

import sympy as sy


class TrigonometricFunctionProblem:
    """三角関数の値と角度に関連する問題を出力
    
    Attributes:
        _problem_types (list): 問題の候補を格納
        _used_trigonometric_functions (list): 値と角度の相互変換に使用される三角関数
        _radian_range (str): 値と角度の相互変換に使用される角度の範囲
        latex_answer (str): latex形式で記述された解答
        latex_problem (str): latex形式で記述された問題
    """
    def __init__(self, **settings):
        """初期処理
        
        settings (dict): 問題設定を格納
        """
        self._problem_types = settings["problem_types"]
        self._radian_range = settings["radian_range"]
        self._used_trigonometric_functions = settings["used_trigonometric_functions"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        """問題作成のコントローラー

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Raises:
            ValueError: 問題のタイプが存在しない時に挙上
        """
        selected_problem_type = choice(self._problem_types)
        selected_trigonometric_function = choice(self._used_trigonometric_functions)
        if selected_problem_type == "value_to_radian":
            latex_answer, latex_problem = self._make_value_to_radian_problem(selected_trigonometric_function)
        elif selected_problem_type == "radian_to_value":
            latex_answer, latex_problem = self._make_radian_to_value_problem(selected_trigonometric_function)
        elif selected_problem_type == "mutual_relationships":
            latex_answer, latex_problem = self._make_mutual_relationships_problem()
        else:
            raise ValueError(f"'selected_problem_type' is {selected_problem_type}. This may be wrong.")
        return latex_answer, latex_problem
    
    def _make_value_to_radian_problem(self, trigonometric_ratio):
        latex_answer = "fuga"
        latex_problem = "hoge"
        return latex_answer, latex_problem
    
    def _make_radian_to_value_problem(self, trigonometric_ratio):
        latex_answer = "fuga"
        latex_problem = "hoge"
        return latex_answer, latex_problem
    
    def _make_mutual_relationships_problem(self):
        latex_answer = "fuga"
        latex_problem = "hoge"
        return latex_answer, latex_problem
        