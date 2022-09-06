from random import choice

import sympy as sy

class FillInTheSquareProblem:
    """穴埋め算の問題を出力する
    
    Attributes:
        _calculation_type_list (list): 選択される演算の候補が格納されている
        latex_answer (str): latex形式で記述された解答
        latex_problem (str): latex形式で記述された問題
    """
    def __init__(self, **settings):
        """初期化
        
        Args:
            settings (dict): 問題の設定が格納されている
        """
        sy.init_printing(order='grevlex')
        self._calculation_type_list = settings["calculation_type_list"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        """選択された演算の形式に応じて、問題と解答を出力する
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        Raises:
            ValueError: 選択された問題形式が正しくないときに挙上される
        """
        selected_calculation_type = choice(self._calculation_type_list)
        if selected_calculation_type == "addition_only":
            latex_answer, latex_problem = self._make_addition_only_problem()
        elif selected_calculation_type == "subtraction_only":
            latex_answer, latex_problem = self._make_subtraction_only_problem()
        elif selected_calculation_type == "multiplication_only":
            latex_answer, latex_problem = self._make_multiplication_only_problem()
        elif selected_calculation_type == "division_only":
            latex_answer, latex_problem = self._make_division_only_problem()
        elif selected_calculation_type == "addition_and_subtraction":
            latex_answer, latex_problem = self._make_addition_and_subtraction_problem()
        elif selected_calculation_type == "multiplication_and_division":
            latex_answer, latex_problem = self._make_multiplication_and_division_problem()
        elif selected_calculation_type == "all_calculations":
            latex_answer, latex_problem = self._make_all_calculations_problem()
        else:
            raise ValueError(f"selected_calculation_type is {selected_calculation_type}. This may be wrong type.")
        return latex_answer, latex_problem
    
    def _make_addition_only_problem(self):
        """足し算のみが用いられた穴埋め算の問題を出力

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Developing:
            要するにx+a=c, a+x=c型の方程式と考え方は同じ
            a=c-xでここは正負を問わない。正でなければならないのはxになる
        """
        return latex_answer, latex_problem

    def _make_subtraction_only_problem(self):
        """引き算のみが用いられた穴埋め算の問題を出力

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        return latex_answer, latex_problem

    def _make_multiplication_only_problem(self):
        """かけ算のみが用いられた穴埋め算の問題を出力

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        return latex_answer, latex_problem

    def _make_division_only_problem(self):
        """割り算のみが用いられた穴埋め算の問題を出力

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        return latex_answer, latex_problem

    def _make_addition_and_subtraction_problem(self):
        """足し算と引き算が用いられた穴埋め算の問題を出力

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        return latex_answer, latex_problem

    def _make_multiplication_and_division_problem(self):
        """かけ算と割り算が用いられた穴埋め算の問題を出力

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        return latex_answer, latex_problem
    
    def _make_all_calculations_problem(self):
        """四則演算全てが用いられた穴埋め算の問題を出力

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        return latex_answer, latex_problem
    
    def _make_random_integer(self, max_num=10, min_num=-10):
        """_summary_

        Args:
            max_num (int, optional): _description_. Defaults to 10.
            min_num (int, optional): _description_. Defaults to -10.
        """