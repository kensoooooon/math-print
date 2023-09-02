from random import randint, choice
from typing import Dict, Tuple


import sympy as sy


class AdditionAndSubtractionFor3rdGrade:
    """指定された桁数の足し算引き算の問題と、その解答を出力
    
    Attributes:
        latex_answer (str): latex形式で記述された解答
        latex_problem (str): latex形式で記述された問題
    """
    def __init__(self, **settings: Dict) -> None:
        """初期設定
        
        Args:
            settings (dict): 問題の設定
        """
        self._digits_of_number = settings["digits_of_number"]
        selected_calculation = choice(settings["used_calculations"])
        if selected_calculation == "addition":
            self.latex_answer, self.latex_problem = self._make_addition_problem()
        elif selected_calculation == "subtraction":
            self.latex_answer, self.latex_problem = self._make_subtraction_problem()
    
    def _make_addition_problem(self) -> Tuple[str, str]:
        """足し算の問題と解答の出力
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        selected_digit_of_number1 = int(choice(self._digits_of_number))
        if selected_digit_of_number1 == 3:
            number1 = randint(100, 999)
        elif selected_digit_of_number1 == 4:
            number1 = randint(1000, 9999)
        elif selected_digit_of_number1 == 5:
            number1 = randint(10000, 99999)
        selected_digit_of_number2 = int(choice(self._digits_of_number))
        if selected_digit_of_number2 == 3:
            number2 = randint(100, 999)
        elif selected_digit_of_number2 == 4:
            number2 = randint(1000, 9999)
        elif selected_digit_of_number2 == 5:
            number2 = randint(10000, 99999)
        answer = number1 + number2
        latex_problem = f"{sy.latex(number1)} + {sy.latex(number2)}"
        latex_answer = f"= {sy.latex(answer)}"
        return latex_answer, latex_problem

    def _make_subtraction_problem(self) -> Tuple[str, str]:
        """引き算の問題と解答の出力
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        selected_digit_of_number1 = int(choice(self._digits_of_number))
        if selected_digit_of_number1 == 3:
            number1 = randint(100, 999)
        elif selected_digit_of_number1 == 4:
            number1 = randint(1000, 9999)
        elif selected_digit_of_number1 == 5:
            number1 = randint(10000, 99999)
        selected_digit_of_number2 = int(choice(self._digits_of_number))
        if selected_digit_of_number2 == 3:
            number2 = randint(100, 999)
        elif selected_digit_of_number2 == 4:
            number2 = randint(1000, 9999)
        elif selected_digit_of_number2 == 5:
            number2 = randint(10000, 99999)
        if number1 >= number2:
            answer = number1 - number2
            latex_problem = f"{sy.latex(number1)} - {sy.latex(number2)}"
        else:
            answer = number2 - number1
            latex_problem = f"{sy.latex(number2)} - {sy.latex(number1)}"
        latex_answer = f"= {sy.latex(answer)}"
        return latex_answer, latex_problem
    