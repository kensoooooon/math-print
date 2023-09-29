"""
約分なし。
gcd=1で通るが、計算するともとに戻る
"""
from random import choice, randint
from typing import Dict, Tuple, Union

import sympy as sy

class AdditionAndSubtractionOfFraction:
    """小学4年生を対象とした分数の足し算と引き算の問題・解答を出力
    
    Attributes:
        latex_answer (str): latex形式と文字列が混在していることを前提とした解答
        latex_problem (str): latex形式と文字列が混在していることを前提とした問題
    """
    def __init__(self, **settings: Dict) -> None:
        """初期設定と問題作成、格納
        
        Args:
            settings (dict): 問題の設定が格納された辞書

        Raises:
            ValueError: 想定されていない問題が要求されたときに挙上
        """
        sy.init_printing(order="grevlex")
        selected_calculation = choice(settings["used_calculations"])
        selected_integer_part = choice(settings["integer_part"])
        if selected_integer_part == "with_integer_part":
            with_integer_part = True
        elif selected_integer_part == "without_integer_part":
            with_integer_part = False
        if selected_calculation == "from_improper_fraction_to_mixed_number_or_integer":
            self.latex_answer, self.latex_problem = self._make_from_improper_fraction_to_mixed_number_or_integer_problem()
        elif selected_calculation == "from_mixed_number_to_improper_fraction":
            self.latex_answer, self.latex_problem = self._make_from_mixed_number_to_improper_fraction_problem()
        elif selected_calculation == "addition":
            self.latex_answer, self.latex_problem = self._make_addition_problem(with_integer_part)
        elif selected_calculation == "subtraction":
            self.latex_answer, self.latex_problem = self._make_subtraction_problem(with_integer_part)
        elif selected_calculation == "fill_in_the_square":
            self.latex_answer, self.latex_problem = self._make_fill_in_the_square_problem(with_integer_part)
        else:
            raise ValueError(f"'selected_calculation' is {selected_calculation}. It must be 'addition', 'subtraction' or 'fill_in_the_square'.")
    
    def _make_from_improper_fraction_to_mixed_number_or_integer_problem(self):
        """仮分数から帯分数への変換

        Returns:
            Tuple[str, str]: 問題の解答と作成
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題
        """
        denominator = randint(2, 15)
        numerator = randint(denominator, 3 * denominator)
        latex_problem = f"\\( \\dfrac{{{numerator}}}{{{denominator}}} \\)を帯分数か整数に書きかえなさい。"
        integer_part, numerator_part = divmod(numerator, denominator)
        if numerator_part == 0:
            latex_answer = f"\\( {integer_part} \\)"
        else:
            latex_answer = f"\\( {integer_part} \\dfrac{{{numerator_part}}}{{{denominator}}} \\)"
        return latex_answer, latex_problem
    
    def _make_from_mixed_number_to_improper_fraction_problem(self):
        """帯分数から仮分数への変換

        Returns:
            Tuple[str, str]: 問題の解答と作成
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題
        """
        integer_part = randint(1, 3)
        denominator = randint(2, 15)
        numerator_part = randint(1, denominator - 1)
        latex_problem = f"\\( {integer_part} \\dfrac{{{numerator_part}}}{{{denominator}}} \\)を仮分数に書きかえなさい。"
        numerator = integer_part * denominator + numerator_part
        latex_answer = f"\\( \\dfrac{{{numerator}}}{{{denominator}}} \\)"
        return latex_answer, latex_problem
    
    def _make_addition_problem(self, with_integer_part: bool) -> Tuple[str, str]:
        """条件を満たした足し算の問題の作成

        Args:
            with_integer_part (bool): 整数、すなわち帯分数が出力されるか否か

        Returns:
            Tuple[str, str]: 問題の解答と作成
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題
        import sympy as sy
        from random import randint

        for _ in range(100):
            common_denominator = randint(2, 15)
            print(f"common_denominator: {common_denominator}")
            # without integer part
            answer_numerator = randint(2, common_denominator)
            print(f"answer_numerator: {answer_numerator}")
            numerator1 = randint(1, answer_numerator - 1)
            print(f"numerator1: {numerator1}")
            numerator2 = answer_numerator - numerator1
            print(f"numerator2: {numerator2}")
            print("------------")
        """
        common_denominator = randint(2, 15)
        if with_integer_part:
            answer_numerator = randint(2, 2 * common_denominator)
            numerator1 = randint(1, answer_numerator - 1)
            numerator2 = answer_numerator - numerator1
            latex_problem = f"次の計算をしましょう。\n \\( \\dfrac{{{numerator1}}}{{{common_denominator}}} + \\dfrac{{{numerator2}}}{{{common_denominator}}} \\)"
            integer_part, numerator_part = divmod(answer_numerator, common_denominator)
            if numerator_part == 0:
                latex_answer = f"\\( {integer_part} \\)"
            else:
                if integer_part == 0:
                    latex_answer = f"\\( = \\dfrac{{{answer_numerator}}}{{{common_denominator}}} \\)"
                else:
                    latex_answer = f"\\( = \\dfrac{{{answer_numerator}}}{{{common_denominator}}} \\left( {integer_part} \\dfrac{{{numerator_part}}}{{{common_denominator}}} \\right) \\)"
        else:
            answer_numerator = randint(2, common_denominator)
            numerator1 = randint(1, answer_numerator - 1)
            numerator2 = answer_numerator - numerator1
            latex_problem = f"次の計算をしましょう。\n \\( \\dfrac{{{numerator1}}}{{{common_denominator}}} + \\dfrac{{{numerator2}}}{{{common_denominator}}} \\)"
            integer_part, numerator_part = divmod(answer_numerator, common_denominator)
            if integer_part == 0:
                latex_answer = f"\\( = \\dfrac{{{numerator_part}}}{{{common_denominator}}} \\)"
            else:
                latex_answer = f"\\( = {integer_part} \\)"
        return latex_answer, latex_problem
    
    def _make_subtraction_problem(self, with_integer_part):
        latex_answer = "dummy answer in subtraction problem"
        latex_problem = "dummy problem in subtraction problem"
        return latex_answer, latex_problem
    
    def _make_fill_in_the_square_problem(self, with_integer_part):
        latex_answer = "dummy answer in fill_in_the_square problem"
        latex_problem = "dummy problem in fill_in_the_square problem"
        return latex_answer, latex_problem
    
    def _random_frac(self, fraction_type: Union[None, str] = None) -> Tuple[sy.Rational, str]:
        """指定されたタイプのランダムな分数と、そのlatexを返す関数
        
        Args:
            fraction_type (Union[None, str]): 返してほしい分数のタイプ。デフォルト値はNone
                この引数に指定されるタイプと、返される分数の関係は以下のようになっている。
                - proper_fraction: 真分数(分子が分母より小さい値をとる)
                - improper_fraction: 仮分数(分子が分母以下の値をとる)
                - mixed_number: 帯分数
                - None: 上の3つのいずれか
        """
        pass