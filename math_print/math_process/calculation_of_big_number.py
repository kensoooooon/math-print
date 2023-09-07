"""
from random import randint

def list_reversed_splitter(split_to_list, chunk_size):
    for i in range(len(split_to_list), 0, -chunk_size):
        right = i
        if right - 4 < 0:
            left = 0
        else:
            left = right - 4
        yield split_to_list[left: right]

chinese_numerical_dict = {
    "1": "一", "2": "二", "3": "三", "4": "四",
    "5": "五", "6": "六", "7": "七", "8": "八", "9": "九"
}

num = randint(1, 10 ** 15)
num_str = str(num)
if len(num_str) % 4 == 0:
    pass
else:
    empty = 4 - (len(num_str) % 4)
    num_str = num_str.zfill(len(num_str) + empty)
num_list = list(num_str)
print(f"num_list: {num_list}")

outer_replaced_nums = []
for four_num, outer_japanese_unit in zip(list_reversed_splitter(num_list, 4), ["", "万", "億", "兆", "京"]):
    replaced_num_str = ""
    for num_str, japanese_unit in zip(four_num, ["千", "百", "十", ""]):
        if num_str == "0":
            continue
        elif num_str == "1":
            if japanese_unit == "":
                replaced_num_str += chinese_numerical_dict[num_str]
            else:
                replaced_num_str += japanese_unit
        else:
            replaced_num_str += (chinese_numerical_dict[num_str] + japanese_unit)
    if replaced_num_str == "千":
        replaced_num_str = "一" + replaced_num_str
    if replaced_num_str != "":
        outer_replaced_nums.append(replaced_num_str + outer_japanese_unit)
outer_replaced_nums.reverse()
chinese_numerical_number = "".join(outer_replaced_nums)
print(chinese_numerical_number)
"""

from random import choice, randint
from typing import Dict, Tuple
from collections.abc import Generator

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
    
    def _make_conversion_from_chinese_numerical_to_alphanumeric_problem(self) -> Tuple[str, str]:
        """漢数字からアラビア数字に直す問題と解答を作成

        Returns:
            latex_answer (str): latex形式の解答
            latex_problem (str): 通常の文字列で記載された問題
        """
        selected_unit = choice(self._units_of_used_number)
        if selected_unit == "hundred_million":
            number = randint(1, 10 ** 5 - 1) * (10 ** 7)
        elif selected_unit == "trillion":
            number = randint(1, 10 ** 5 - 1) * (10 ** 11)
        elif selected_unit == "ten_quadrillion":
            number = randint(1, 10 ** 5 - 1) * (10 ** 15)
        chinese_numerical = self._convert_alphanumeric_into_chinese_numerical(number)
        latex_problem = f"{chinese_numerical}を数字に直しなさい。"
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
            number = randint(1, 10 ** 5 - 1) * (10 ** 7)
        elif selected_unit == "trillion":
            number = randint(1, 10 ** 5 - 1) * (10 ** 11)
        elif selected_unit == "ten_quadrillion":
            number = randint(1, 10 ** 5 - 1) * (10 ** 15)
        chinese_numerical = self._convert_alphanumeric_into_chinese_numerical(number)
        latex_problem = f"\\( {sy.latex(number)} \\)を漢数字に直しなさい。"
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
        latex_problem.rstrip("、")
        latex_problem += "あわせた数を、数字で書きなさい。"
        latex_answer = f"\\( {sy.latex(answer_number)} \\)"
        return latex_answer, latex_problem
    
    def _convert_alphanumeric_into_chinese_numerical(self, number: int) -> str:
        """アラビア数字を漢数字に変換して出力する

        Args:
            number (int): 変換したいアラビア数字
        
        Returns:
            chinese_numerical (str): 変換された漢数字
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
