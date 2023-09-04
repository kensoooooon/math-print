"""
eg. 1023->千二十三
eg2. 23584 ->二万三千五百八十四
eg3. 12345678 -> 千二百三十四万 五千六百七十八
eg4. 1234567891234 -> 1 2345 6789 1234 --> 一 兆 二千三百四十五 億 六千七百八十九 万 千二百三十四

4桁ずつ区切って、そこから何もなし→万→億→兆に切り替える？
-> 一の有りなし
-> 区切りの付け方

# 4桁区切り
str_num = "12"
print(str_num[-4:])
str_num2 = "1234567891234"
print(str_num2[-4:])
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
    