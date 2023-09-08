from random import choice, randint, random
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
        elif selected_problem_type == "addition":
            self.latex_answer, self.latex_problem = self._make_addition_problem()
        elif selected_problem_type == "subtraction":
            self.latex_answer, self.latex_problem = self._make_subtraction_problem()
    
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
            # 10 ** 12
            number = randint(1, 10 ** 8 - 1) * (10 ** 4)
        elif selected_unit == "trillion":
            # 10 ** 16
            number = randint(1, 10 ** 8 - 1) * (10 ** 8)
        elif selected_unit == "ten_quadrillion":
            # 10 ** 20
            number = randint(1, 10 ** 8 - 1) * (10 ** 12)
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
        latex_problem = latex_problem.rstrip("、")
        if random() > 0.5:
            latex_problem += "あわせた数を、数字で書きなさい。"
            latex_answer = f"\\( {sy.latex(answer_number)} \\)"
        else:
            latex_problem += "あわせた数を、漢数字で書きなさい。"
            chinese_numerical = self._convert_alphanumeric_into_chinese_numerical(answer_number)
            latex_answer = chinese_numerical
        return latex_answer, latex_problem

    def _make_addition_problem(self) -> Tuple[str, str]:
        """大きい数の足し算の問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式と通常の文字列が混在した解答
            latex_problem (str): latex形式と通常の文字列が混在した問題
        """
        selected_unit1 = choice(self._units_of_used_number)
        if selected_unit1 == "hundred_million":
            number1 = randint(1, 999) * (10 ** 8)
        elif selected_unit1 == "trillion":
            number1 = randint(1, 999) * (10 ** 12)
        elif selected_unit1 == "ten_quadrillion":
            number1 = randint(1, 999) * (10 ** 16)
        selected_unit2 = choice(self._units_of_used_number)
        if selected_unit2 == "hundred_million":
            number2 = randint(1, 999) * (10 ** 8)
        elif selected_unit2 == "trillion":
            number2 = randint(1, 999) * (10 ** 12)
        elif selected_unit2 == "ten_quadrillion":
            number2 = randint(1, 999) * (10 ** 16)
        answer = number1 + number2
        chinese_numerical_answer = self._convert_alphanumeric_into_chinese_numerical(answer)
        latex_answer = chinese_numerical_answer
        chinese_numerical1 = self._convert_alphanumeric_into_chinese_numerical(number1)
        chinese_numerical2 = self._convert_alphanumeric_into_chinese_numerical(number2)
        latex_problem = f"{chinese_numerical1} \\( + \\) {chinese_numerical2}"
        return latex_answer, latex_problem
    
    def _make_subtraction_problem(self) -> Tuple[str, str]:
        """大きい数の引き算の問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式と通常の文字列が混在した解答
            latex_problem (str): latex形式と通常の文字列が混在した問題
        """
        selected_unit1 = choice(self._units_of_used_number)
        coeff1 = randint(1, 999)
        if selected_unit1 == "hundred_million":
            number1 = coeff1 * (10 ** 8)
            chinese_numerical1 = f"\\( {sy.latex(coeff1)} \\)億"
        elif selected_unit1 == "trillion":
            number1 = coeff1 * (10 ** 12)
            chinese_numerical1 = f"\\( {sy.latex(coeff1)} \\)兆"
        elif selected_unit1 == "ten_quadrillion":
            number1 = coeff1 * (10 ** 16)
            chinese_numerical1 = f"\\( {sy.latex(coeff1)} \\)京"
        selected_unit2 = choice(self._units_of_used_number)
        coeff2 = randint(1, 999)
        if selected_unit2 == "hundred_million":
            number2 = coeff2 * (10 ** 8)
            chinese_numerical2 = f"\\( {sy.latex(coeff2)} \\)億"
        elif selected_unit2 == "trillion":
            number2 = coeff2 * (10 ** 12)
            chinese_numerical2 = f"\\( {sy.latex(coeff2)} \\)兆"
        elif selected_unit2 == "ten_quadrillion":
            number2 = coeff2 * (10 ** 16)
            chinese_numerical2 = f"\\( {sy.latex(coeff2)} \\)京"
        if number1 < number2:
            number1, number2 = number2, number1
            chinese_numerical1, chinese_numerical2 = chinese_numerical2, chinese_numerical1
        answer = number1 - number2
        chinese_numerical_answer = self._convert_alphanumeric_into_chinese_numerical(answer)
        latex_answer = chinese_numerical_answer
        chinese_numerical1 = self._convert_alphanumeric_into_chinese_numerical(number1)
        chinese_numerical2 = self._convert_alphanumeric_into_chinese_numerical(number2)
        latex_problem = f"{chinese_numerical1} \\( - \\) {chinese_numerical2}"
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
