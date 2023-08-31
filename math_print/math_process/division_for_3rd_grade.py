"""
8/30
側作成

8/31
余りが制御できていない問題
"""
from random import choice, randint, random
from typing import Dict, Tuple, Union

import sympy as sy


class DivisionFor3rdGrade:
    def __init__(self, **settings: Dict) -> None:
        sy.init_printing(order="grevlex")
        selected_remainder_type = choice(settings["remainder_types"])
        selected_digit_of_divided_number = int(choice(settings["digit_of_divided_numbers"]))
        self.latex_answer, self.latex_problem = self._make_problem(selected_remainder_type, selected_digit_of_divided_number)
    
    def _make_problem(self, selected_remainder_type: str, selected_digit_of_divided_number: int) -> Tuple[str, str]:
        """指定された余りの有無と、割られる数の桁数に応じた問題と解答を出力する
        
        Args:
            selected_remainder_type (str): 余りの有無
            selected_digit_of_divided_number (int): 割られる数の桁数
        
        Returns:
            latex_answer (str): latex形式で表記された割り算の答え
            latex_problem (str): latex形式で表示された割り算の問題の式
        """
        if selected_digit_of_divided_number == 1:
            divided_number = randint(0, 9)
        elif selected_digit_of_divided_number == 2:
            divided_number = randint(10, 99)
        dividing_number = randint(1, 9)
        quotient, remainder = divmod(divided_number, dividing_number)
        if selected_remainder_type == "without_remainder":
            divided_number = divided_number - remainder
            quotient, remainder = divmod(divided_number, dividing_number)
            latex_answer = f"\\( {sy.latex(quotient)} \\)"
        elif selected_remainder_type == "with_remainder":
            latex_answer = f"\\( {sy.latex(quotient)} \\) あまり \\( {sy.latex(remainder)} \\)"
        latex_problem = f"\\( {sy.latex(divided_number)} \\div {sy.latex(dividing_number)} \\)"
        return latex_answer, latex_problem
    