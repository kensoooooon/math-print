from collections.abc import Generator
from math import floor
from random import choice, randint, random
import re
from typing import Dict, Tuple


import sympy as sy


class CalculationOfBigNumber:
    """1億を超える数を用いた計算の問題と解答を出力
    
    Attributes:
        latex_answer (str): latex形式と通常の文字列が混在した解答
        latex_problem (str): latex形式と通常の文字列が混在した解答
    """
    def __init__(self, **settings: Dict) -> None:
        """初期設定
        
        Args:
            settings (dict): 問題の設定
        """
        self._units_of_used_number = settings["units_of_used_number"]
        selected_problem_type = choice(settings["problem_types"])
        if selected_problem_type == "conversion_from_chinese_numerical_to_alphanumeric":
            self.latex_answer, self.latex_problem = self._make_conversion_from_chinese_numerical_to_alphanumeric_problem()
        elif selected_problem_type == "conversion_from_alphanumeric_to_chinese_numerical":
            self.latex_answer, self.latex_problem = self._make_conversion_from_alphanumeric_to_chinese_numerical_problem()
        elif selected_problem_type == "unite_numbers":
            self.latex_answer, self.latex_problem = self._make_unite_numbers_problem()
        elif selected_problem_type == "addition":
            self.latex_answer, self.latex_problem = self._make_addition_problem()
        elif selected_problem_type == "subtraction":
            self.latex_answer, self.latex_problem = self._make_subtraction_problem()
        elif selected_problem_type == "multiplication":
            self.latex_answer, self.latex_problem = self._make_multiplication_problem()
        elif selected_problem_type == "division":
            self.latex_answer, self.latex_problem = self._make_division_problem()
    
    def _make_conversion_from_chinese_numerical_to_alphanumeric_problem(self) -> Tuple[str, str]:
        """漢数字からアラビア数字に直す問題と解答を作成

        Returns:
            latex_answer (str): latex形式の解答
            latex_problem (str): 通常の文字列で記載された問題
        """
        selected_unit = choice(self._units_of_used_number)
        if selected_unit == "hundred_million":
            # 10 ** 12
            number = randint(1, 10 ** 8 - 1) * (10 ** 4)
        elif selected_unit == "trillion":
            # 10 ** 16
            number = randint(1, 10 ** 8 - 1) * (10 ** 8)
        elif selected_unit == "ten_quadrillion":
            # 10 ** 20
            number = randint(1, 10 ** 8 - 1) * (10 ** 12)
        chinese_numerical = self._convert_alphanumeric_into_chinese_numerical(number)
        latex_problem = f"{chinese_numerical}\nを数字に直しなさい。"
        latex_answer = f"\\( {sy.latex(number)} \\)"
        return latex_answer, latex_problem
    
    def _make_conversion_from_alphanumeric_to_chinese_numerical_problem(self) -> Tuple[str, str]:
        """アラビア数字から漢数字に直す問題と解答を作成

        Returns:
            latex_answer (str): 通常の文字列で記載された解答
            latex_problem (str): latexと通常の文字列が混在板問題
        """
        selected_unit = choice(self._units_of_used_number)
        if selected_unit == "hundred_million":
            # 10 ** 12
            number = randint(1, 10 ** 8 - 1) * (10 ** 4)
        elif selected_unit == "trillion":
            # 10 ** 16
            number = randint(1, 10 ** 8 - 1) * (10 ** 8)
        elif selected_unit == "ten_quadrillion":
            # 10 ** 20
            number = randint(1, 10 ** 8 - 1) * (10 ** 12)
        chinese_numerical = self._convert_alphanumeric_into_chinese_numerical(number)
        latex_problem = f"\\( {sy.latex(number)} \\)\nを漢数字に直しなさい。"
        latex_answer = f"{chinese_numerical}"
        return latex_answer, latex_problem
    
    def _make_unite_numbers_problem(self) -> Tuple[str, str]:
        """「あわせた数」という形式で大きい数の計算を行う問題
        
        Returns:
            latex_answer (str): latex形式の解答
            latex_problem (str): latexと通常の文字列が混在した解答
        """
        latex_problem = ""
        answer_number = 0
        reversed_list = reversed(self._units_of_used_number)
        for selected_unit in reversed_list:
            # 10 ** 16
            if selected_unit == "ten_quadrillion":
                coeff = randint(1, 99) * 100
                answer_number += coeff * (10 ** 16)
                latex_problem += f"\\( 1 \\)京を\\( {sy.latex(coeff)} \\)こ、"
            # 10 ** 12
            elif selected_unit == "trillion":
                coeff = randint(1, 99) * 100
                answer_number += coeff * (10 ** 12)
                latex_problem += f"\\( 1 \\)兆を\\( {sy.latex(coeff)} \\)こ、"
            # 10 ** 8
            elif selected_unit == "hundred_million":
                coeff = randint(1, 99) * 100
                answer_number += coeff * (10 ** 8)
                latex_problem += f"\\( 1 \\)億を\\( {sy.latex(coeff)} \\)こ、"
        latex_problem = latex_problem.rstrip("、")
        if random() > 0.5:
            latex_problem += "\nあわせた数を、数字で書きなさい。"
            latex_answer = f"\\( {sy.latex(answer_number)} \\)"
        else:
            latex_problem += "\nあわせた数を、漢数字で書きなさい。"
            chinese_numerical = self._convert_alphanumeric_into_chinese_numerical(answer_number)
            latex_answer = chinese_numerical
        return latex_answer, latex_problem

    def _make_addition_problem(self) -> Tuple[str, str]:
        """大きい数の足し算の問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式と通常の文字列が混在した解答
            latex_problem (str): latex形式と通常の文字列が混在した問題
        """
        selected_unit = choice(self._units_of_used_number)
        coeff1 = randint(1, 999)
        coeff2 = randint(1, 999)
        answer_number = coeff1 + coeff2
        if selected_unit == "hundred_million":
            chinese_numerical1 = f"\\( {sy.latex(coeff1)} \\)億"
            chinese_numerical2 = f"\\( {sy.latex(coeff2)} \\)億"
            latex_answer = f"\\( {sy.latex(answer_number)} \\)億"
        elif selected_unit == "trillion":
            chinese_numerical1 = f"\\( {sy.latex(coeff1)} \\)兆"
            chinese_numerical2 = f"\\( {sy.latex(coeff2)} \\)兆"
            latex_answer = f"\\( {sy.latex(answer_number)} \\)兆"
        elif selected_unit == "ten_quadrillion":
            chinese_numerical1 = f"\\( {sy.latex(coeff1)} \\)兆"
            chinese_numerical2 = f"\\( {sy.latex(coeff2)} \\)兆"
            latex_answer = f"\\( {sy.latex(answer_number)} \\)兆"
        latex_problem = f"{chinese_numerical1} + {chinese_numerical2}\nを計算しなさい。"
        return latex_answer, latex_problem
    
    def _make_subtraction_problem(self) -> Tuple[str, str]:
        """大きい数の引き算の問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式と通常の文字列が混在した解答
            latex_problem (str): latex形式と通常の文字列が混在した問題
        """
        selected_unit = choice(self._units_of_used_number)
        larger_coeff = randint(1, 999)
        smaller_coeff = randint(1, 999)
        if larger_coeff < smaller_coeff:
            larger_coeff, smaller_coeff = smaller_coeff, larger_coeff
        answer_number = larger_coeff - smaller_coeff
        if selected_unit == "hundred_million":
            larger_chinese_numerical = f"\\( {sy.latex(larger_coeff)} \\)億"
            smaller_chinese_numerical = f"\\( {sy.latex(smaller_coeff)} \\)億"
            latex_answer = f"\\( {sy.latex(answer_number)} \\)億"
        elif selected_unit == "trillion":
            larger_chinese_numerical = f"\\( {sy.latex(larger_coeff)} \\)兆"
            smaller_chinese_numerical = f"\\( {sy.latex(smaller_coeff)} \\)兆"
            latex_answer = f"\\( {sy.latex(answer_number)} \\)兆"
        elif selected_unit == "ten_quadrillion":
            larger_chinese_numerical = f"\\( {sy.latex(larger_coeff)} \\)兆"
            smaller_chinese_numerical = f"\\( {sy.latex(smaller_coeff)} \\)兆"
            latex_answer = f"\\( {sy.latex(answer_number)} \\)兆"
        latex_problem = f"{larger_chinese_numerical} - {smaller_chinese_numerical}\nを計算しなさい。"
        return latex_answer, latex_problem
    
    def _make_multiplication_problem(self) -> Tuple[str, str]:
        """大きい数のかけ算の問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式と通常の文字列が混在した解答
            latex_problem (str): latex形式と通常の文字列が混在した問題
        """
        selected_unit = choice(self._units_of_used_number)
        # 10 ** 8 ~ 10 ** 12 - 1
        if selected_unit == "hundred_million":
            coeff = randint(10 ** 2, 10 ** 6 - 1)
            multiplied_number = coeff * 10 ** 6
        # 10 ** 12 ~ 10 ** 16 - 1
        elif selected_unit == "trillion":
            coeff = randint(10 ** 2, 10 ** 6 - 1)
            multiplied_number = coeff * 10 ** 10
        # 10 ** 16 ~ 10 ** 20 - 1(less than 10 ** 2 if max)
        elif selected_unit == "ten_quadrillion":
            coeff = randint(1, 10 ** 3 - 1)
            multiplied_number = coeff * 10 ** 14
        mixed_multiplied_number = self._convert_alphanumeric_into_mixed_style(multiplied_number)
        multiplying_number = choice([10, 100, 1000])
        latex_problem = f"{mixed_multiplied_number} \\( \\times {sy.latex(multiplying_number)} \\)\nを計算しなさい。"
        answer_number = multiplied_number * multiplying_number
        mixed_answer_number = self._convert_alphanumeric_into_mixed_style(answer_number)
        latex_answer = mixed_answer_number
        return latex_answer, latex_problem
    
    def _make_division_problem(self):
        """大きい数のわり算の問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式と通常の文字列が混在した解答
            latex_problem (str): latex形式と通常の文字列が混在した問題
        """
        selected_unit = choice(self._units_of_used_number)
        # 10 ** 8 ~ 10 ** 12 - 1
        if selected_unit == "hundred_million":
            coeff = randint(10 ** 2, 10 ** 6 - 1)
            divided_number = coeff * 10 ** 6
        # 10 ** 12 ~ 10 ** 16 - 1
        elif selected_unit == "trillion":
            coeff = randint(10 ** 2, 10 ** 6 - 1)
            divided_number = coeff * 10 ** 10
        # 10 ** 16 ~ 10 ** 20 - 1(less than 10 ** 2 if max)
        elif selected_unit == "ten_quadrillion":
            coeff = randint(10 ** 2, 10 ** 6 - 1)
            divided_number = coeff * 10 ** 14
        mixed_divided_number = self._convert_alphanumeric_into_mixed_style(divided_number)
        dividing_number = choice([10, 100, 1000])
        latex_problem = f"{mixed_divided_number} \\( \\div {sy.latex(dividing_number)} \\)\nを計算しなさい。"
        answer_number = floor(divided_number / dividing_number)
        mixed_answer_number = self._convert_alphanumeric_into_mixed_style(answer_number)
        latex_answer = mixed_answer_number
        return latex_answer, latex_problem

    def _convert_alphanumeric_into_chinese_numerical(self, number: int) -> str:
        """アラビア数字を漢数字に変換して出力する

        Args:
            number (int): 変換したいアラビア数字
        
        Returns:
            chinese_numerical (str): 変換された漢数字
        
        Raise:
            ValueError: 想定されていない大きさの数(1該以上)が入力されたときに挙上
        """
        def list_reserved_splitter_in_four_chunk(split_to_list: list) -> Generator:
            """リストを逆順で、4つずつ分割して出力し、数の変換に利用してもらう

            Args:
                split_to_list (list): 分割したいリスト

            Yields:
                Generator: 分割したリストを順次出してくれる
            """
            for i in range(len(split_to_list), 0, -4):
                right = i
                if right - 4 < 0:
                    left = 0
                else:
                    left = right - 4
                yield split_to_list[left: right]
        
        if number >= 10 ** 20:
            raise ValueError(f"The number must be less than 10 ** 20.")
        chinese_numerical_dict = {
            "1": "一", "2": "二", "3": "三", "4": "四",
            "5": "五", "6": "六", "7": "七", "8": "八", "9": "九"
        }
        number_str = str(number)
        if len(number_str) % 4 == 0:
            pass
        else:
            empty = 4 - (len(number_str) % 4)
            number_str = number_str.zfill(len(number_str) + empty)
        number_list = list(number_str)
        replaced_numbers_with_outer_japanese_unit = []
        for four_number_str, outer_japanese_unit in zip(list_reserved_splitter_in_four_chunk(number_list), ["", "万", "億", "兆", "京"]):
            replaced_numbers_with_inner_japanese_unit = ""
            for single_number_str, inner_japanese_unit in zip(four_number_str, ["千", "百", "十", ""]):
                if single_number_str == "0":
                    continue
                elif single_number_str == "1":
                    if inner_japanese_unit == "":
                        replaced_numbers_with_inner_japanese_unit += chinese_numerical_dict[single_number_str]
                    else:
                        replaced_numbers_with_inner_japanese_unit += inner_japanese_unit
                else:
                    replaced_numbers_with_inner_japanese_unit += (chinese_numerical_dict[single_number_str] + inner_japanese_unit)
            if replaced_numbers_with_inner_japanese_unit != "":
                replaced_numbers_with_outer_japanese_unit.append(replaced_numbers_with_inner_japanese_unit + outer_japanese_unit)
        replaced_numbers_with_outer_japanese_unit.reverse()
        chinese_numerical = "".join(replaced_numbers_with_outer_japanese_unit)
        return chinese_numerical

    def _convert_alphanumeric_into_mixed_style(self, number: int) -> str:
        """アラビア数字を、日本語の単位(万、億、....)が用いられた混合スタイルに変換する
        
        Args:
            number (int): 変換したいアラビア数字
        
        Returns:
            mixed_number_str (str): 変換した混合スタイルの数
        
        Raises:
            ValueError: 想定されていない1該以上の大きさの数が入力されたときに挙上
        """
        def reverser_with_four_chunk(number_str):
            for i in range(len(number_str), 0, -4):
                right = i
                if right - 4 < 0:
                    left = 0
                else:
                    left = right - 4
                yield number_str[left: right]
        if number >= 10 ** 20:
            raise ValueError(f"The number must be less than 10 ** 20.")
        number_str = str(number)
        replaced_numbers_with_unit = []
        for four_numbers_str, japanese_unit in zip(reverser_with_four_chunk(number_str), ["", "万", "億", "兆", "京"]):
            if four_numbers_str != "0000":
                zero_removed_four_numbers_str = re.sub("^0+", "", four_numbers_str)
                replaced_numbers_with_unit.append(f"\\( {zero_removed_four_numbers_str} \\)" + japanese_unit)
        replaced_numbers_with_unit.reverse()
        mixed_number_str = "".join(replaced_numbers_with_unit)
        return mixed_number_str
