from random import choice

import sympy as sy


class TrigonometricRatioProblem:
    """三角比の値と角度に関連する問題を出力
    
    Attributes:
        _problem_types (list): 問題の候補を格納
        _used_trigonometric_ratios (list): 使用される三角比の候補を格納
        _degree_range (str): 使用される角度の範囲
        latex_answer (str): latex形式で記述された解答
        latex_answer (str): latex形式で記述された問題
    """
    def __init__(self, **settings):
        """初期処理
        
        settings (dict): 問題設定を格納
        """
        self._problem_types = settings["problem_types"]
        self._used_trigonometric_ratios = settings["used_trigonometric_ratios"]
        self._degree_range = settings["degree_range"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        """問題作成のコントローラー

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Raises:
            ValueError: 問題のタイプが存在しないときに挙上
        """
        selected_problem_type = choice(self._problem_types)
        selected_used_trigonometric_ratio = choice(self._used_trigonometric_ratios)
        if selected_problem_type == "value_to_degree":
            latex_answer, latex_problem = self._make_value_to_degree_problem(selected_used_trigonometric_ratio)
        elif selected_problem_type == "degree_to_value":
            latex_answer, latex_problem = self._make_degree_to_value_problem(selected_used_trigonometric_ratio)
        elif selected_problem_type == "mutual_relationships":
            latex_answer, latex_problem = self._make_mutual_relationships_problem()
        else:
            raise ValueError(f"selected_problem_type is {selected_problem_type}. This must be wrong.")
        return latex_answer, latex_problem
    
    def _make_value_to_degree_problem(self, trigonometric_ratio):
        """値から角度を求める問題と解答の出力
        
        Args:
            trigonometric_ratio (str): 問題に使用される三角比
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        if self._degree_range == "up_to_90":
            list_30 = [i * 30 for i in range(4)]
            list_45 = [i * 45 for i in range(3)]
        elif self._degree_range == "up_to_180":
            list_30 = [i * 30 for i in range(7)]
            list_45 = [i * 45 for i in range(5)]
        degree_candidates = list(set(list_30 + list_45))
        if trigonometric_ratio == "tan":
            degree_candidates.remove(90)
        selected_degree = choice(degree_candidates)
        latex_answer = f"\\theta = {selected_degree}^{{\\circ}}"
        selected_radian = selected_degree * sy.pi / 180
        if trigonometric_ratio == "sin":
            sin_value = sy.sin(selected_radian)
            latex_problem = f"\\sin \\theta = {sy.latex(sin_value)}"
        elif trigonometric_ratio == "cos":
            cos_value = sy.cos(selected_radian)
            latex_problem = f"\\cos \\theta = {sy.latex(cos_value)}"
        elif trigonometric_ratio == "tan":
            tan_value = sy.tan(selected_radian)
            latex_problem = f"\\tan \\theta = {sy.latex(tan_value)}"        
        return latex_answer, latex_problem
    
    def _make_degree_to_value_problem(self, trigonometric_ratio):
        """角度から値を求める問題と解答の出力
        
        Args:
            trigonometric_ratio (str): 問題に使用される三角比

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        if self._degree_range == "up_to_90":
            list_30 = [i * 30 for i in range(4)]
            list_45 = [i * 45 for i in range(3)]
        elif self._degree_range == "up_to_180":
            list_30 = [i * 30 for i in range(7)]
            list_45 = [i * 45 for i in range(5)]
        degree_candidates = list(set(list_30 + list_45))
        if trigonometric_ratio == "tan":
            degree_candidates.remove(90)
        selected_degree = choice(degree_candidates)
        latex_problem = f"\\{trigonometric_ratio} {selected_degree}^{{\\circ}}"
        selected_radian = selected_degree * sy.pi / 180
        if trigonometric_ratio == "sin":
            sin_value = sy.sin(selected_radian)
            latex_answer = f" = {sy.latex(sin_value)}"
        elif trigonometric_ratio == "cos":
            cos_value = sy.cos(selected_radian)
            latex_answer = f" = {sy.latex(cos_value)}"
        elif trigonometric_ratio == "tan":
            tan_value = sy.tan(selected_radian)
            latex_answer = f" = {sy.latex(tan_value)}"        
        return latex_answer, latex_problem
