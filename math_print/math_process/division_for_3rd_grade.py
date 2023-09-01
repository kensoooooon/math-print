from random import choice, randint, random
from typing import Dict, Tuple, Union

import sympy as sy


class DivisionFor3rdGrade:
    def __init__(self, **settings: Dict) -> None:
        sy.init_printing(order="grevlex")
        selected_remainder_type = choice(settings["remainder_types"])
        if selected_remainder_type == "with_remainder":
            with_remainder = True
        elif selected_remainder_type == "without_remainder":
            with_remainder = False
        selected_digit_of_divided_number = int(choice(settings["digit_of_divided_numbers"]))
        self.latex_answer, self.latex_problem = self._make_problem(with_remainder, selected_digit_of_divided_number)
    
    def _make_problem(self, with_remainder: bool, selected_digit_of_divided_number: int) -> Tuple[str, str]:
        """指定された余りの有無と、割られる数の桁数に応じた問題と解答を出力する
        
        Args:
            selected_remainder_type (str): 余りの有無
            selected_digit_of_divided_number (int): 割られる数の桁数
        
        Returns:
            latex_answer (str): latex形式で表記された割り算の答え
            latex_problem (str): latex形式で表示された割り算の問題の式
        """
        if with_remainder:
            if selected_digit_of_divided_number == 1:
                divided_number = randint(1, 9)
            elif selected_digit_of_divided_number == 2:
                divided_number = randint(10, 99)
            one_digit_divisors = [divisor for divisor in sy.divisors(divided_number) if divisor < 10]
            dividing_numbers = [dividing_number for dividing_number in range(1, 10) if dividing_number not in one_digit_divisors]
            dividing_number = choice(dividing_numbers)
            quotient, remainder = divmod(divided_number, dividing_number)
            if remainder == 0:
                raise ValueError(f"remainder is {remainder}. It must not be 0.")
            latex_answer = f"\\( {quotient} \\) あまり\\( {remainder} \\)"
        else:
            if selected_digit_of_divided_number == 1:
                divided_number = randint(0, 9)
            elif selected_digit_of_divided_number == 2:
                divided_number = randint(10, 99)
            if divided_number == 0:
                dividing_number = randint(1, 9)
            else:
                one_digit_divisors = [divisor for divisor in sy.divisors(divided_number) if divisor < 10]
                if one_digit_divisors == [1]:
                    dividing_number = 1
                else:
                    one_digit_divisors.remove(1)
                    dividing_number = choice(one_digit_divisors)
            quotient, remainder = divmod(divided_number, dividing_number)
            if remainder != 0:
                raise ValueError(f"remainder is {remainder}. It must be 0.")
            latex_answer = f"\\( {quotient} \\)"
        latex_problem = f"\\( {divided_number} \\div {dividing_number} \\)"
        return latex_answer, latex_problem
    