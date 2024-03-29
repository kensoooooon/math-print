from random import choice, randint
from typing import Dict, Tuple


import sympy as sy


class DivisionFor4thGrade:
    """指定された桁数や余りの有無などの条件に応じて、問題と解答を作成
    
    Attributes:
        latex_answer (str): latex形式と文字列が混在した形で記述された解答
        latex_problem (str): latex形式で記述された問題
    """
    def __init__(self, **settings: Dict) -> None:
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
        if selected_digit_of_divided_number < selected_digit_of_dividing_number:
            selected_digit_of_dividing_number = randint(1, selected_digit_of_divided_number)
        self.latex_answer, self.latex_problem = self._make_problem(with_remainder, selected_digit_of_divided_number, selected_digit_of_dividing_number)
    
    def _make_problem(self, with_remainder: bool, selected_digit_of_divided_number: int, selected_digit_of_dividing_number: int) -> Tuple[str, str]:
        """指定された余りと数の桁数に応じて、割り算の問題と解答を出力

        Args:
            with_remainder (bool): 余りがあるか否か
            selected_digit_of_divided_number (int): 割られる数の桁数
            selected_digit_of_dividing_number (int): 割る数の桁数

        Returns:
            latex_answer (str): latex形式の割り算の答え
            latex_problem (str): latex形式の割り算の問題の式
        
        Raises:
            ValueError: 割られる数より割る数のほうが大きいときに挙上
        """
        if selected_digit_of_divided_number < selected_digit_of_dividing_number:
            raise ValueError(
                f"digit of divided number is {selected_digit_of_divided_number}, and digit of dividing number is {selected_digit_of_dividing_number}."\
                "digit of divided number must be digit of dividing number or more."
                )
        min_of_divided_number = 10 ** (selected_digit_of_divided_number - 1)
        max_of_divided_number = 10 ** selected_digit_of_divided_number - 1
        divided_number = randint(min_of_divided_number, max_of_divided_number)
        min_of_dividing_number = 10 ** (selected_digit_of_dividing_number - 1)
        divisors_set = set(sy.divisors(divided_number)) - set(range(1, min_of_dividing_number))
        if with_remainder:
            dividing_numbers_without_divisors = set(range(min_of_dividing_number, divided_number + 1)) - divisors_set
            if not(dividing_numbers_without_divisors):
                dividing_number = 1
            else:
                dividing_number = choice(list(dividing_numbers_without_divisors))
            quotient, remainder = divmod(divided_number, dividing_number)
            if remainder == 0:
                latex_answer = f"\\( {quotient} \\)"
            else:
                latex_answer = f"\\( {quotient} \\) あまり \\( {remainder} \\)"
        else:
            dividing_number = choice(list(divisors_set))
            quotient, remainder = divmod(divided_number, dividing_number)
            latex_answer = f"\\( {quotient} \\)"
        latex_problem = f"\\( {divided_number} \\div {dividing_number} \\)"
        return latex_answer, latex_problem
