"""
8/30
側作成
"""
from random import choice
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
        
        Developing:
            a = bq + r <=> a ÷ b = q 余り r
                割られる数aは1or2桁(0含む)
                割る数bは常に1桁
                余りrはある場合とない場合がある
                商qは上記を満たすもの
                
                割られる数ありきだと、余りが出る可能性がある？気がする
                ->割られる数からその約数を生成して、余りがある場合はそこに+or-?
                -->約数を出す方法は？<--sy.divisors(数)でリストが返ってくる
                
        from random import choice, randint, random
        import sympy as sy

        for _ in range(10):
            digit_of_divided_number = choice([1, 2])
            remainder_type = choice(["with_remainder", "without_remainder"])
            print(remainder_type)
            if digit_of_divided_number == 1:
                a = randint(0, 9)
            elif digit_of_divided_number == 2:
                a = randint(10, 99)
            b = randint(1, 9)
            q, r = divmod(a, b)
            if remainder_type == "without_remainder":
                a = a - r
                q, r = divmod(a, b)
            print(f"{a} ÷ {b} = {q} ... {r}")
            print("---------------------")
        """
        latex_answer = "dummy answer"
        latex_problem = "dummy problem"
        return latex_answer, latex_problem
    