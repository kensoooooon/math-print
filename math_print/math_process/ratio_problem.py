from random import choice, random, randint
from typing import Dict, Optional, Tuple, Union

import sympy as sy


class RatioProblem:
    """指定された割合関連の値を求める問題とその解答を出力
    
    Attributes:
        _used_numbers_for_ratio (list): 割合に利用する数のタイプ(分数, 小数)が格納されている
        latex_answer (str): latex形式と通常の文字が混在した解答
        latex_problem (str): latex形式と通常の文字が混在した問題
    """
    def __init__(self, **settings: Dict) -> None:
        """初期設定
        
        Args:
            settings (dict): 問題の各種設定を格納
        
        Raises:
            ValueError: 想定されていない問題のタイプが混入したときに挙上
        """
        self._used_numbers_for_ratio = settings["used_numbers_for_ratio"]
        selected_problem_type = choice(settings["problem_types"])
        if selected_problem_type == "amount_to_compare":
            self.latex_answer, self.latex_problem = self._make_amount_to_compare_problem()
        elif selected_problem_type == "standard_amount":
            self.latex_answer, self.latex_problem = self._make_standard_amount_problem()
        elif selected_problem_type == "ratio":
            self.latex_answer, self.latex_problem = self._make_ratio_problem()
        else:
            raise ValueError(f"'selected_problem_type' is {selected_problem_type}. This isn't expected value.")
    
    def _make_amount_to_compare_problem(self) -> Tuple[str, str]:
        """比べる量を求める問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式と通常の文字が混在した解答
            latex_problem (str): latex形式と通常の文字が混在した問題
        
        Develop:
            重さ、長さ、体積、人数や個数など
        """
        selected_theme = choice(["weight", "length", "volume", "quantity"])
        if selected_theme == "weight":
            pass
        elif selected_theme == "length":
            pass
        elif selected_theme == "volume":
            pass
        elif selected_theme == "quantity":
            pass
        latex_answer = "dummy answer in amount to compare problem."
        latex_problem = "dummy problem in amount to compare problem."
        return latex_answer, latex_problem

    def _make_standard_amount_problem(self) -> Tuple[str, str]:
        """元の量を求める問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式と通常の文字が混在した解答
            latex_problem (str): latex形式と通常の文字が混在した問題
        """
        latex_answer = "dummy answer in standard amount problem."
        latex_problem = "dummy problem in standard amount problem."
        return latex_answer, latex_problem

    def _make_ratio_problem(self) -> Tuple[str, str]:
        """割合を求める問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式と通常の文字が混在した解答
            latex_problem (str): latex形式と通常の文字が混在した問題
        """
        latex_answer = "dummy answer in ratio problem."
        latex_problem = "dummy problem in ratio problem."
        return latex_answer, latex_problem
    
    def _make_random_number(self, ):
        """
        Developing:
            整数, 分数, 小数
        """
