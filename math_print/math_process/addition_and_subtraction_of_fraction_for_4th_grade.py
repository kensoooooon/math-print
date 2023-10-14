from random import choice, randint, random
from typing import Dict, Tuple, Union

import sympy as sy

class AdditionAndSubtractionOfFractionFor4thGrade:
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
    
    def _make_from_improper_fraction_to_mixed_number_or_integer_problem(self) -> Tuple[str, str]:
        """仮分数から帯分数への変換

        Returns:
            Tuple[str, str]: 問題と解答
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
    
    def _make_from_mixed_number_to_improper_fraction_problem(self) -> Tuple[str, str]:
        """帯分数から仮分数への変換

        Returns:
            Tuple[str, str]: 問題と解答
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
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題
        
        Notes:
            - 小学4年生を対象としているため、約分は敢えて実行していない
        """
        common_denominator = randint(2, 15)
        numerator1 = randint(1, 2 * common_denominator)
        numerator2 = randint(1, 2 * common_denominator)
        if (numerator1 % common_denominator == 0) and (numerator2 % common_denominator == 0):
            if random() > 0.5:
                numerator1 += randint(1, common_denominator - 1)
            else:
                numerator2 += randint(1, common_denominator - 1)
        answer_numerator = numerator1 + numerator2
        if with_integer_part:
            if answer_numerator % common_denominator == 0:
                answer_integer = self._frac_latex(answer_numerator, common_denominator)
                latex_answer = f"\\( = {answer_integer} \\)"
            elif answer_numerator > common_denominator:
                answer_frac_latex_without_integer = self._frac_latex(answer_numerator, common_denominator, frac_type="without_integer")
                answer_frac_latex_with_integer = self._frac_latex(answer_numerator, common_denominator, frac_type="with_integer")
                latex_answer = f"\\( = {answer_frac_latex_without_integer}  \\left( {answer_frac_latex_with_integer} \\right) \\)"
            else:
                answer_frac_latex = self._frac_latex(answer_numerator, common_denominator)
                latex_answer = f"\\( = {answer_frac_latex} \\)"
            frac1_latex = self._frac_latex(numerator1, common_denominator)
            frac2_latex = self._frac_latex(numerator2, common_denominator)
            latex_problem = f"次の計算をしましょう。\n \\( {frac1_latex} + {frac2_latex} \\)"
        else:
            answer_frac_latex = self._frac_latex(answer_numerator, common_denominator, frac_type="without_integer")
            latex_answer = f"\\( = {answer_frac_latex} \\)"
            frac1_latex = self._frac_latex(numerator1, common_denominator, frac_type="without_integer")
            frac2_latex = self._frac_latex(numerator2, common_denominator, frac_type="without_integer")
            latex_problem = f"次の計算をしましょう。\n \\( {frac1_latex} + {frac2_latex} \\)"
        return latex_answer, latex_problem
    
    def _make_subtraction_problem(self, with_integer_part: bool) -> Tuple[str, str]:
        """条件を満たした引き算の問題の作成

        Args:
            with_integer_part (bool): 整数、すなわち帯分数が出力されるか否か

        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題
        
        Notes:
            - 小学4年生を対象としているため、約分は敢えて実行していない。また、負になる計算結果も同様の理由で登場しない
        """
        common_denominator = randint(3, 15)
        numerator1 = randint(1, 2 * common_denominator)
        numerator2 = randint(1, 2 * common_denominator)
        if numerator1 < numerator2:
            numerator1, numerator2 = numerator2, numerator1
        if (numerator1 % common_denominator == 0) and (numerator2 % common_denominator == 0):
            numerator1 += randint(1, common_denominator - 1)
        answer_numerator = numerator1 - numerator2
        if with_integer_part:
            if answer_numerator % common_denominator == 0:
                answer_integer = self._frac_latex(answer_numerator, common_denominator)
                latex_answer = f"\\( = {answer_integer} \\)"
            elif answer_numerator > common_denominator:
                answer_frac_latex_without_integer = self._frac_latex(answer_numerator, common_denominator, frac_type="without_integer")
                answer_frac_latex_with_integer = self._frac_latex(answer_numerator, common_denominator, frac_type="with_integer")
                latex_answer = f"\\( = {answer_frac_latex_without_integer}  \\left( {answer_frac_latex_with_integer} \\right) \\)"
            else:
                answer_frac_latex = self._frac_latex(answer_numerator, common_denominator)
                latex_answer = f"\\( = {answer_frac_latex} \\)"
            frac1_latex = self._frac_latex(numerator1, common_denominator)
            frac2_latex = self._frac_latex(numerator2, common_denominator)
            latex_problem = f"次の計算をしましょう。\n \\( {frac1_latex} - {frac2_latex} \\)"
        else:
            answer_frac_latex = self._frac_latex(answer_numerator, common_denominator, frac_type="without_integer")
            latex_answer = f"\\( = {answer_frac_latex} \\)"
            frac1_latex = self._frac_latex(numerator1, common_denominator, frac_type="without_integer")
            frac2_latex = self._frac_latex(numerator2, common_denominator, frac_type="without_integer")
            latex_problem = f"次の計算をしましょう。\n \\( {frac1_latex} - {frac2_latex} \\)"
        return latex_answer, latex_problem
    
    def _make_fill_in_the_square_problem(self, with_integer_part: bool) -> Tuple[str, str]:
        """穴埋め問題と解答を出力

        Args:
            with_integer_part (bool): 計算式に帯分数が利用されるか否か

        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題
        """
        selected_calculation = choice(["addition", "subtraction"])
        if selected_calculation == "addition":
            common_denominator = randint(2, 15)
            numerator1 = randint(1, 2 * common_denominator)
            numerator2 = randint(1, 2 * common_denominator)
            if (numerator1 % common_denominator == 0) and (numerator2 % common_denominator == 0):
                if random() > 0.5:
                    numerator1 += randint(1, common_denominator - 1)
                else:
                    numerator2 += randint(1, common_denominator - 1)
            answer_numerator = numerator1 + numerator2
            selected_replace_side = choice(["left", "right"])
            if selected_replace_side == "left":
                if with_integer_part:
                    if numerator1 % common_denominator == 0:
                        square_integer = self._frac_latex(numerator1, common_denominator)
                        latex_answer = f"\\( \\square = {square_integer} \\)"
                    elif numerator1 > common_denominator:
                        square_frac_with_integer = self._frac_latex(numerator1, common_denominator, frac_type="with_integer")
                        square_frac_without_integer = self._frac_latex(numerator1, common_denominator, frac_type="without_integer")
                        latex_answer = f"\\( \\square = {square_frac_without_integer} \\left( {square_frac_with_integer} \\right) \\)"
                    else:
                        square_frac = self._frac_latex(numerator1, common_denominator, frac_type="without_integer")
                        latex_answer = f"\\( \\square = {square_frac} \\)"
                    frac2 = self._frac_latex(numerator2, common_denominator)
                    answer_frac = self._frac_latex(answer_numerator, common_denominator)
                else:
                    square_frac = self._frac_latex(numerator1, common_denominator, frac_type="without_integer")
                    latex_answer = f"\\( \\square = {square_frac} \\)"
                    frac2 = self._frac_latex(numerator2, common_denominator, frac_type="without_integer")
                    answer_frac = self._frac_latex(answer_numerator, common_denominator, frac_type="without_integer")
                latex_problem = "次の\\( \\square \\)にあてはまる数を答えなさい。"
                latex_problem += f"\\( \\square + {frac2} = {answer_frac} \\)"
            elif selected_replace_side == "right":
                if with_integer_part:
                    if numerator2 % common_denominator == 0:
                        square_integer = self._frac_latex(numerator2, common_denominator)
                        latex_answer = f"\\( \\square = {square_integer} \\)"
                    elif numerator2 > common_denominator:
                        square_frac_with_integer = self._frac_latex(numerator2, common_denominator, frac_type="with_integer")
                        square_frac_without_integer = self._frac_latex(numerator2, common_denominator, frac_type="without_integer")
                        latex_answer = f"\\( \\square = {square_frac_without_integer} \\left( {square_frac_with_integer} \\right) \\)"
                    else:
                        square_frac = self._frac_latex(numerator2, common_denominator, frac_type="without_integer")
                        latex_answer = f"\\( \\square = {square_frac} \\)"
                    frac1 = self._frac_latex(numerator1, common_denominator)
                    answer_frac = self._frac_latex(answer_numerator, common_denominator)
                else:
                    square_frac = self._frac_latex(numerator2, common_denominator, frac_type="without_integer")
                    latex_answer = f"\\( \\square = {square_frac} \\)"
                    frac1 = self._frac_latex(numerator1, common_denominator, frac_type="without_integer")
                    answer_frac = self._frac_latex(answer_numerator, common_denominator, frac_type="without_integer")
                latex_problem = "次の\\( \\square \\)にあてはまる数を答えなさい。"
                latex_problem += f"\\( {frac1} + \\square = {answer_frac} \\)"
        elif selected_calculation == "subtraction":
            common_denominator = randint(3, 15)
            numerator1 = randint(1, 2 * common_denominator)
            numerator2 = randint(1, 2 * common_denominator)
            if numerator1 < numerator2:
                numerator1, numerator2 = numerator2, numerator1
            if (numerator1 % common_denominator == 0) and (numerator2 % common_denominator == 0):
                numerator1 += randint(1, common_denominator - 1)
            answer_numerator = numerator1 - numerator2
            selected_replace_side = choice(["left", "right"])
            if selected_replace_side == "left":
                if with_integer_part:
                    if numerator1 % common_denominator == 0:
                        square_integer = self._frac_latex(numerator1, common_denominator)
                        latex_answer = f"\\( \\square = {square_integer} \\)"
                    elif numerator1 > common_denominator:
                        square_frac_with_integer = self._frac_latex(numerator1, common_denominator, frac_type="with_integer")
                        square_frac_without_integer = self._frac_latex(numerator1, common_denominator, frac_type="without_integer")
                        latex_answer = f"\\( \\square = {square_frac_without_integer} \\left( {square_frac_with_integer} \\right) \\)"
                    else:
                        square_frac = self._frac_latex(numerator1, common_denominator, frac_type="without_integer")
                        latex_answer = f"\\( \\square = {square_frac} \\)"
                    frac2 = self._frac_latex(numerator2, common_denominator)
                    answer_frac = self._frac_latex(answer_numerator, common_denominator)
                else:
                    square_frac = self._frac_latex(numerator1, common_denominator, frac_type="without_integer")
                    latex_answer = f"\\( \\square = {square_frac} \\)"
                    frac2 = self._frac_latex(numerator2, common_denominator, frac_type="without_integer")
                    answer_frac = self._frac_latex(answer_numerator, common_denominator, frac_type="without_integer")
                latex_problem = "次の\\( \\square \\)にあてはまる数を答えなさい。"
                latex_problem += f"\\( \\square - {frac2} = {answer_frac} \\)"
            elif selected_replace_side == "right":
                if with_integer_part:
                    if numerator2 % common_denominator == 0:
                        square_integer = self._frac_latex(numerator2, common_denominator)
                        latex_answer = f"\\( \\square = {square_integer} \\)"
                    elif numerator2 > common_denominator:
                        square_frac_with_integer = self._frac_latex(numerator2, common_denominator, frac_type="with_integer")
                        square_frac_without_integer = self._frac_latex(numerator2, common_denominator, frac_type="without_integer")
                        latex_answer = f"\\( \\square = {square_frac_without_integer} \\left( {square_frac_with_integer} \\right) \\)"
                    else:
                        square_frac = self._frac_latex(numerator2, common_denominator, frac_type="without_integer")
                        latex_answer = f"\\( \\square = {square_frac} \\)"
                    frac1 = self._frac_latex(numerator1, common_denominator)
                    answer_frac = self._frac_latex(answer_numerator, common_denominator)
                else:
                    square_frac = self._frac_latex(numerator2, common_denominator, frac_type="without_integer")
                    latex_answer = f"\\( \\square = {square_frac} \\)"
                    frac1 = self._frac_latex(numerator1, common_denominator, frac_type="without_integer")
                    answer_frac = self._frac_latex(answer_numerator, common_denominator, frac_type="without_integer")
                latex_problem = "次の\\( \\square \\)にあてはまる数を答えなさい。"
                latex_problem += f"\\( {frac1} - \\square = {answer_frac} \\)"
        return latex_answer, latex_problem
    
    def _frac_latex(self, numerator: int, denominator: int, frac_type: Union[None, str] = None) -> str:
        """与えられた分子と分母、および帯分数を許容するかどうかを見て、latex形式の分数を作成する

        Args:
            numerator (int): 分子
            denominator (int): 分母
            with_integer (Union[None, str], optional): 要求される分数のタイプ

        Returns:
            number_latex(str): latex形式で表現された数。分数の場合と整数の場合がある。
        
        Note:
            以下のlatexが出力される
            - 整数にできるときは最優先で整数
            - 指定された条件によって、以下に変化
                - with_integer: 帯分数
                - without_integer: 真分数か仮分数
                - None: 帯分数にできないときは真分数か仮分数。できるときはランダムにいずれか
        """
        integer_part, numerator_part = divmod(numerator, denominator)
        if numerator_part == 0:
            number_latex = sy.latex(integer_part)
        elif frac_type == "with_integer":
            if numerator < denominator:
                raise ValueError(f"numerator is {numerator}, and denominator is {denominator}. numerator must be more than denominator for mixed fraction.")
            number_latex = f"{integer_part} \\dfrac{{{numerator_part}}}{{{denominator}}}"
        elif frac_type == "without_integer":
            number_latex = f"\\dfrac{{{numerator}}}{{{denominator}}}"
        elif frac_type is None:
            if numerator < denominator:
                number_latex = f"\\dfrac{{{numerator}}}{{{denominator}}}"
            else:
                if random() > 0.5:
                    number_latex = f"{integer_part} \\dfrac{{{numerator_part}}}{{{denominator}}}"
                else:
                    number_latex = f"\\dfrac{{{numerator}}}{{{denominator}}}"
        return number_latex
    