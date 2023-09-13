from random import choice, randint, random
from typing import Dict, Tuple, Union


import sympy as sy


class DivisionFor4thGrade:
    """指定された桁数や余りの有無などの条件に応じて、問題と解答を作成
    
    Attributes:
        latex_answer (str): latex形式と文字列が混在した形で記述された解答
        latex_problem (str): latex形式で記述された問題
    """
    def __init__(self, **settings):
        """初期設定
        
        Args:
            settings (dict): 問題の設定を格納
        """
        sy.init_printing(order='grevlex')
        selected_remainder_type = choice(settings["remainder_types"])
        if selected_remainder_type == "with_remainder":
            with_remainder = True
        elif selected_remainder_type == "without_remainder":
            with_remainder = False
        selected_digit_of_divided_number = int(choice(settings["digits_of_divided_number"]))
        selected_digit_of_dividing_number = int(choice(settings["digits_of_dividing_number"]))
        self.latex_answer, self.latex_problem = self._make_problem(with_remainder, selected_digit_of_divided_number, selected_digit_of_dividing_number)
    
    def _make_problem(self, selected_digit_of_divided_number, selected_digit_of_dividing_number):
        latex_answer = "dummy answer in division."
        latex_problem = "dummy problem in division."
        return latex_answer, latex_problem
