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
        if selected_problem_type == "from_chinese_numerical_to_alphanumeric":
            self.latex_answer, self.latex_problem = self._make_from_chinese_numerical_to_alphanumeric_problem()
        elif selected_problem_type == "from_alphanumeric_to_chinese_numerical":
            self.latex_answer, self.latex_problem = self._make_from_alphanumeric_to_chinese_numerical_problem()
    
    def _make_from_chinese_numerical_to_alphanumeric_problem(self):
        latex_answer = "dummy answer in _make_from_chinese_numerical_to_alphanumeric_problem"
        latex_problem = "dummy problem in _make_from_chinese_numerical_to_alphanumeric_problem"
        return latex_answer, latex_problem
    
    def _make_from_alphanumeric_to_chinese_numerical_problem(self):
        latex_answer = "dummy answer in from_alphanumeric_to_chinese_numerical_problem"
        latex_problem = "dummy problem in from_alphanumeric_to_chinese_numerical_problem"
        return latex_answer, latex_problem
    