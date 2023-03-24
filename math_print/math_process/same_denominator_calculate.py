from random import choice, randint, random


import sympy as sy


class SameDenominatorCalculate:
    """同じ分母の足し算・引き算の問題を出力
    
    Attributes:
        _calculate_type (list): 計算に使用される演算子が格納
    """
    def __init__(self, **settings):
        """初期設定
        
        Args:
            settings (dict): 問題の各種設定
        """
        sy.init_printing(order='grevlex')
        self._calculate_type = settings["calculate_type"]
        self._term_numbers = settings["term_number"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        """指定された計算の条件を満たす問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題 
        """
        
        return latex_answer, latex_problem