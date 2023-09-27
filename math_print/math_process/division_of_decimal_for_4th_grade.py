from random import randint, choice
from typing import Dict, Tuple, Union


import sympy as sy


class DivisionOfDecimalFor4thGrade:
    """小学4年生用の小数の割り算の問題と解答を出力
    
    Attributes:
        latex_answer (str): latex形式と通常の文字列が混在した解答
        latex_problem (str): latex形式と通常の文字列が混在した問題
    """
    def __init__(self, **settings: Dict) -> None:
        """初期設定
        
        Args:
            settings (dict): 初期設定が格納された辞書
        """
        sy.init_printing(order="grevlex")
        selected_decimal_places_of_divided_number = int(choice(settings["decimal_places_of_divided_number"]))
        selected_decimal_places_of_dividing_number = int(choice(settings["decimal_places_of_dividing_number"]))
        selected_decimal_places_of_quotient = int(choice(settings["decimal_places_of_quotient"]))
        selected_remainder = choice(settings["remainder_types"])
        if selected_remainder == "with_remainder":
            with_remainder = True
        elif selected_remainder == "without_remainder":
            with_remainder = False
        self.latex_answer, self.latex_problem = self._make_problem(
            with_remainder,
            selected_decimal_places_of_divided_number,
            selected_decimal_places_of_dividing_number,
            selected_decimal_places_of_quotient
        )
    
    def _make_problem(self, with_remainder: bool, decimal_places_of_divided_number: int, decimal_places_of_dividing_number: int, decimal_places_of_quotient: int) -> Tuple[str, str]:
        """問題の作成

        Args:
            with_remainder (bool): 余りの有無
            decimal_places_of_divided_number (int): 割られる数の小数点以下桁数
            decimal_places_of_dividing_number (int): 割る数の小数点以下の桁数
            decimal_places_of_quotient (int): 計算する商

        Returns:
            Tuple[str, str]: latex形式と通常の文字列が混在した解答と問題(latex_answer, latex_problem)
    
            Tuple[str, str]:
                この関数は2つの値を返します。
                - latex_answer (str): latex形式と通常の文字列が混在した解答
                - latex_problem (str): latex形式と通常の文字列が混在した問題
        """ 
        if with_remainder:
            divided_number, divided_number_latex = self._random_number(decimal_places_of_divided_number)
            dividing_number, dividing_number_latex = self._random_number(decimal_places_of_dividing_number)
            latex_problem = f"次の割り算の商を\n小数第{decimal_places_of_quotient}位まで求めましょう。"
            latex_problem += "\n また、あまりがあるときは、それもだしなさい。"
            latex_problem += f"\n \\( {divided_number_latex} \\div {dividing_number_latex} \\)"
            answer = divided_number / dividing_number
            truncated_answer, truncated_answer_latex = self._truncate_decimal(answer, decimal_places_of_quotient)
            remainder = divided_number - dividing_number * truncated_answer
            remainder_latex = sy.latex(sy.Float(remainder))
            if remainder == 0:
                latex_answer = f"\\( {truncated_answer_latex} \\)"
            else:
                latex_answer = f"\\( {truncated_answer_latex} \\) あまり \\( {remainder_latex} \\)"
        else:
            divided_number, divided_number_latex = self._random_number(decimal_places_of_divided_number)
            dividing_number, dividing_number_latex = self._random_number(decimal_places_of_dividing_number)
            latex_problem = f"次の割り算の商を四捨五入して、\n小数第{decimal_places_of_quotient}位まで求めましょう。"
            latex_problem += f"\n \\( {divided_number_latex} \\div {dividing_number_latex} \\)"
            answer = divided_number / dividing_number
            round_answer = answer.round(decimal_places_of_quotient)
            latex_answer = f"\\( {sy.latex(round_answer)} \\)"
        return latex_answer, latex_problem
    
    def _random_number(self, number_of_decimal_places: int) -> Tuple[Union[sy.Integer, sy.Rational], str]:
        """ランダムに生成された、指定された条件を満たす整数や小数、および出力用の文字を合わせて返す

        Args:
            number_of_decimal_places (int): 条件として指定される小数点以下の桁数。0のときは小数部は存在せず、整数が返される

        Returns:
            Tuple[Union[sy.Integer, sy.Rational], str]:
                この関数は2つの値を返します。
                - number (Union[sy.Integer, sy.Rational]): 実際の計算に用いる数。問題の設定次第で表示すべき桁数が細かく変わるため、評価が後で行えるように小数型への変換は行わない
                - latex_number (str): latex形式で記述された数
        """
        integer_part = sy.Integer(randint(1, 20))
        if number_of_decimal_places == 0:
            number = integer_part
            latex_number = sy.latex(number)
        else:
            numerator = randint(10 ** (number_of_decimal_places - 1), 10 ** number_of_decimal_places - 1)
            denominator = 10 ** number_of_decimal_places
            decimal_part = sy.Rational(numerator, denominator)
            number = integer_part + decimal_part
            latex_number = sy.latex(sy.Float(number))
        return number, latex_number

    def _truncate_decimal(self, number: sy.Rational, number_of_decimal_places: int) -> Tuple[sy.Rational, str]:
        """指定された桁数より下を切り捨てた小数の文字列を出力

        Args:
            number (sy.Rational): _description_
            number_of_decimal_places (int): _description_

        Returns:
            Tuple[sy.Rational, str]:
                この関数は2つの値を返します。
                - floored_number (sy.Rational): 指定された桁数より下が切り捨てられた分数
                - str_number (str): 指定された桁数より下が切り捨てられた小数のlatex用文字列
        """
        float_number = sy.Float(number)
        floored_number = sy.floor(float_number * 10 ** number_of_decimal_places) / 10 ** number_of_decimal_places
        str_number = sy.latex(sy.Float(floored_number))
        return floored_number, str_number
