from random import choice, randint, random
from typing import Dict, Tuple

import sympy as sy


class Series:
    """種々の数列の和を求める問題と解答を、指定された条件に応じて作成・格納
    
    Attributes:
        latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
        latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題 
    """
    def __init__(self, **settings: Dict) -> None:
        """初期設定
        
        Args:
            settings (dict): 問題の設定を格納
            - 出力すべき問題のタイプ(多項式の和、等比数列の和など)を格納
        
        Raises:
            ValueError: 想定されていないタイプの問題が指定されたときに挙上
        """
        sy.init_printing(order='grevlex')
        selected_series_type = choice(settings["series_types"])
        if selected_series_type == "sum_from_linear_to_cubic":
            self.latex_answer, self.latex_problem = self._make_sum_from_linear_to_cubic_problem()
        elif selected_series_type == "sum_of_geometric":
            self.latex_answer, self.latex_problem = self._make_sum_of_geometric_problem()
        elif selected_series_type == "sum_of_arithmetic_times_geometric":
            self.latex_answer, self.latex_problem = self._make_sum_of_arithmetic_times_geometric_problem()
        elif selected_series_type == "sum_of_sum":
            self.latex_answer, self.latex_problem = self._make_sum_of_sum_problem()
        else:
            raise ValueError(f"'selected_series_type is {selected_series_type}. This isn't expected value.")
    
    def _make_sum_from_linear_to_cubic_problem(self) -> Tuple[str, str]:
        """1~3次式の和の問題と解答を作成
        
        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題 
        """
        k = sy.Symbol("k")
        n = sy.Symbol("n")
        constant = sy.Integer(randint(-3, 3))
        linear_coeff = sy.Integer(randint(-3, 3))
        quadratic_coeff = sy.Integer(randint(-3, 3))
        cubic_coeff = sy.Integer(randint(-3, 3))
        function = cubic_coeff * k ** 3 + quadratic_coeff * k ** 2 + linear_coeff * k + constant
        if random() > 0.3:
            problem_mode = "character"
            start = 1
            end = choice([n, n-1])
        else:
            problem_mode = "number"
            start = 1
            end = sy.Integer(randint(2, 10))
        series = sy.Sum(function, (k, start, end))
        latex_problem = f"\\displaystyle {sy.latex(series)}"
        if problem_mode == "character":
            answer = sy.factor(series.doit())
        elif problem_mode == "number":
            answer = series.doit()
        latex_answer = f"= {sy.latex(answer)}"
        return latex_answer, latex_problem
    
    def _make_sum_of_geometric_problem(self):
        """等比数列の和
        
        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題 
        """
        latex_answer = "dummy answer in _make_sum_of_geometric_problem"
        latex_problem = "dummy problem in _make_sum_of_geometric_problem"
        return latex_answer, latex_problem

    def _make_sum_of_arithmetic_times_geometric_problem(self):
        """等差x等比数列の和
        
        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題 
        """
        latex_answer = "dummy answer in _make_sum_of_arithmetic_times_geometric_problem"
        latex_problem = "dummy problem in _make_sum_of_arithmetic_times_geometric_problem"
        return latex_answer, latex_problem
    
    def _make_sum_of_sum_problem(self):
        """数列の和が一般項となる数列の和
        
        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題 
        """
        latex_answer = "dummy answer in _make_sum_of_sum_problem"
        latex_problem = "dummy problem in _make_sum_of_sum_problem"
        return latex_answer, latex_problem