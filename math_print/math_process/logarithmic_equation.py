from random import choice, random, randint
from typing import Dict, Tuple


import sympy as sy


class LogarithmicEquation:
    """指定されたタイプの対数方程式の問題とその解答を出力
    
    Attributes:
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
        sy.init_printing(order='grevlex')
        problem_type = choice(settings["problem_types"])
        if problem_type == "without_calculation_and_change_base_of_formula":
            self.latex_answer, self.latex_problem = self._make_without_calculation_and_change_base_of_formula_problem()
        elif problem_type == "only_with_calculation":
            self.latex_answer, self.latex_problem = self._make_only_with_calculation_problem()
        elif problem_type == "with_calculation_and_change_base_of_formula":
            self.latex_answer, self.latex_problem = self._make_with_calculation_and_change_base_of_formula_problem()
        else:
            raise ValueError(f"problem_type is {problem_type}. This isn't expected value.")
    
    def _make_without_calculation_and_change_base_of_formula_problem(self) -> Tuple[str, str]:
        """対数の計算も底の変換も使わない対数方程式の問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式と通常の文字が混在した解答
            latex_problem (str): latex形式と通常の文字が混在した問題
        """
        latex_answer = "dummy answer in _make_without_calculation_and_change_base_of_formula_problem"
        latex_problem = "dummy problem in _make_without_calculation_and_change_base_of_formula_problem"
        return latex_answer, latex_problem
    
    def _make_only_with_calculation_problem(self) -> Tuple[str, str]:
        """対数の計算のみを行う対数方程式の問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式と通常の文字が混在した解答
            latex_problem (str): latex形式と通常の文字が混在した問題
        """
        latex_answer = "dummy answer in _make_only_with_calculation_problem"
        latex_problem = "dummy problem in _make_only_with_calculation_problem"
        return latex_answer, latex_problem
    
    def _make_with_calculation_and_change_base_of_formula_problem(self):
        """対数の計算と底の変換を行う対数方程式の問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式と通常の文字が混在した解答
            latex_problem (str): latex形式と通常の文字が混在した問題
        """
        latex_answer = "dummy answer in _make_with_calculation_and_change_base_of_formula_problem"
        latex_problem = "dummy problem in _make_with_calculation_and_change_base_of_formula_problem"
        return latex_answer, latex_problem
    