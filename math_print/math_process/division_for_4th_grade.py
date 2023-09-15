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
        """
        if selected_digit_of_divided_number < selected_digit_of_dividing_number:
            raise ValueError(
                f"digit of divided number is {selected_digit_of_divided_number}, and digit of dividing number is {selected_digit_of_dividing_number}."\
                "digit of divided number must be digit of dividing number or more."
                )
        min_of_divided_number = 10 ** (selected_digit_of_divided_number - 1)
        print(f"min_of_divided_number: {min_of_divided_number}")
        max_of_divided_number = 10 ** selected_digit_of_divided_number - 1
        print(f"max_of_divided_number: {max_of_divided_number}")
        divided_number = randint(min_of_divided_number, max_of_divided_number)
        print(f"divided_number: {divided_number}")
        min_of_dividing_number = 10 ** (selected_digit_of_dividing_number - 1)
        max_of_dividing_number = 10 ** selected_digit_of_dividing_number - 1
        """
        divisors = []
        for divisor in sy.divisors(divided_number):
            if min_of_dividing_number <= divisor:
                divisors.append(divisor)
        """
        divisors_set = set(sy.divisors(divided_number)) - set(range(1, min_of_dividing_number))
        if with_remainder:
            print("with_remainder")
            print(f"divisors_set: {divisors_set}")
            # dividing_numbers = [dividing_number for dividing_number in range(min_of_dividing_number, divided_number + 1) if dividing_number not in divisors]
            dividing_numbers_without_divisors = set(range(min_of_dividing_number, divided_number + 1)) - divisors_set
            print(f"dividing_numbers_without_divisors: {dividing_numbers_without_divisors}")
            if not(dividing_numbers_without_divisors):
                dividing_number = 1
            else:
                dividing_number = choice(list(dividing_numbers_without_divisors))
            print(f"dividing_number: {dividing_number}")
            quotient, remainder = divmod(divided_number, dividing_number)
            print(f"quotient: {quotient}, remainder: {remainder}")
            if remainder == 0:
                latex_answer = f"\\( {quotient} \\)"
            else:
                latex_answer = f"\\( {quotient} \\) あまり \\( {remainder} \\)"
        else:
            print("without_remainder")
            print(f"divisors_set: {divisors_set}")
            dividing_number = choice(list(divisors_set))
            print(f"dividing_number: {dividing_number}")
            quotient, remainder = divmod(divided_number, dividing_number)
            print(f"quotient: {quotient}, remainder: {remainder}")
            latex_answer = f"\\( {quotient} \\)"
        print("--------------------------------")
        latex_problem = f"\\( {divided_number} \\div {dividing_number} \\)"
        return latex_answer, latex_problem
