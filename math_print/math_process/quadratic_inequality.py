from random import choice, randint, random


import sympy as sy


class QuadraticInequality:
    """2次不等式の問題と解答を出力
    
    Attributes:
        _used_quadratic_function (list): 登場する2次方程式のタイプを格納
        latex_answer (str): latex形式で記述された解答
        latex_problem (str): latex形式で記述された問題
    """
    def __init__(self, **settings):
        """初期設定
        
        Args:
            settings (dict): 問題の各種設定
        """
        sy.init_printing(order='grevlex')
        used_quadratic_functions = settings["used_quadratic_function"]
        self.latex_answer, self.latex_problem = self._make_problem(used_quadratic_functions)
    
    def _make_problem(self, used_quadratic_functions):
        """問題と解答の出力を制御するコントローラ
        
        Args:
            used_quadratic_functions (list): 使用する2次関数の候補を格納
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        selected_quadratic_function = choice(used_quadratic_functions)
        if selected_quadratic_function == "two_different_answer":
            latex_answer, latex_problem = self._make_two_different_answer_problem()
        elif selected_quadratic_function == "same_answer":
            latex_answer, latex_problem = self._make_same_answer_problem()
        elif selected_quadratic_function == "no_answer":
            latex_answer, latex_problem = self._make_no_answer_problem()
        else:
            raise ValueError(f"'selected_quadratic_function' is {selected_quadratic_function}. This isn't expected.")
        return latex_answer, latex_problem
    
    def _make_two_different_answer_problem(self):
        """異なる2つの解を持つ2次方程式を使った2次不等式の問題を作成
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        latex_answer = "dummy answer in two_different_answer_problem"
        latex_problem = "dummy problem in two_different_answer_problem"
        return latex_answer, latex_problem

    def _make_same_answer_problem(self):
        """重解を持つ2次方程式を使った2次不等式の問題を作成
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        latex_answer = "dummy answer in same_answer_problem"
        latex_problem = "dummy problem in same_answer_problem"
        return latex_answer, latex_problem

    def _make_no_answer_problem(self):
        """実数解を持たない2次方程式を使った2次不等式の問題を作成
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        latex_answer = "dummy answer in no_answer_problem"
        latex_problem = "dummy problem in no_answer_problem"
        return latex_answer, latex_problem
