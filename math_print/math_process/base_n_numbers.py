from random import choice, randint, random
from typing import NamedTuple

import sympy as sy


class BaseNNumbersProblem:
    """10進数とn進数の相互変換を行う問題を作成
    
    Attributes:
        _convert_from_to_types (list): 変換元と先の候補を格納
        _numbers_to_convert (list): 整数か小数も含むかを格納
        latex_answer (str): latex形式の解答
        latex_problem (str): latex形式の問題
    """
    def __init__(self, **settings):
        """初期処理
        
        Args:
            settings (dict): 問題の設定を格納
        """
        self._convert_from_to_types = settings["convert_from_to_types"]
        self._numbers_to_convert = settings["numbers_to_convert"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        """問題作成のコントローラー

        Returns:
            latex_answer (str): latex形式の解答
            latex_problem (str): latex形式の問題
        """
        selected_convert_from_to = choice(self._convert_from_to_types)
        if selected_convert_from_to == "from_n_base_to_ten_base":
            latex_answer, latex_problem = self._make_from_n_base_to_ten_base_problem()
        elif selected_convert_from_to == "from_ten_base_to_n_base":
            latex_answer, latex_problem = self._make_from_ten_base_to_n_base_problem()
        return latex_answer, latex_problem
    
    def _make_from_n_base_to_ten_base_problem(self):
        """n進数から10進数に変換する問題の解答と文章を作成

        Returns:
            latex_answer (str): latex形式の解答
            latex_problem (str): latex形式の問題
        """
        number_and_base = self._make_random_10_and_n_base_number()
        latex_answer = f"= {number_and_base.number_10_latex}"
        latex_problem = f"{number_and_base.number_n_latex} \\rightarrow \\underline{{\\quad \\quad \\quad}}_{{(10)}}"
        return latex_answer, latex_problem

    def _make_from_ten_base_to_n_base_problem(self):
        """10進数からn進数に変換する問題の解答と文章を作成

        Returns:
            latex_answer (str): latex形式の解答
            latex_problem (str): latex形式の問題
        """
        number_and_base = self._make_random_10_and_n_base_number()
        latex_answer = f" = {number_and_base.number_n_latex}"
        latex_problem = f"{number_and_base.number_10_latex} \\rightarrow \\underline{{\\quad \\quad \\quad}}_{{({number_and_base.base})}}"
        return latex_answer, latex_problem
    
    def _make_random_10_and_n_base_number(self):
        """10進数とそれに対応するn進数の文字列をランダムに作成する
        
        Returns:
            number_and_base (NumberAndBase): n,10それぞれの進数で表記された値と、使用された底を格納         
        Raise:
            ValueError: 想定されていない数のタイプが入ってきたときに挙上
        """
        class NumberAndBase(NamedTuple):
            """数と底を格納する
            
            Attributes:
                number_10_latex (str): 10進数の値。小数が含まれる場合は、小数表記のものと分数表記のものを併記
                number_n_latex (str): n進数の値。
                base (int): 作成に使用された底
            """
            number_10_latex : str
            number_n_latex : str
            base : int
        
        selected_number_type = choice(self._numbers_to_convert)  # integer or decimal
        if selected_number_type == "integer":
            base_candidates = [2, 3, 4, 5, 6, 7, 8, 16]
            selected_base = choice(base_candidates)
            if selected_base == 16:
                number_10 = randint(1, 100)
                number_10_latex = f"{sy.latex(number_10)}_{{(10)}}"
                number_n_str = hex(number_10).replace("0x", "").upper()
                number_n_latex = f"{sy.latex(number_n_str)}_{{(16)}}"
            else:
                number_10 = 0
                number_n_str = ""
                for index in range(2, -1, -1):
                    n_digit = randint(0, selected_base - 1)
                    number_n_str += str(n_digit)
                    number_10 += (n_digit * sy.Pow(selected_base, index))
                if number_n_str == "000":
                    n_digit = randint(1, selected_base - 1)
                    number_n_str = str(n_digit)
                    number_10 = n_digit * sy.Pow(selected_base, 0)
                number_10_latex = f"{sy.latex(number_10)}_{{(10)}}"
                number_n_latex = f"{number_n_str}_{{({selected_base})}}"
        elif selected_number_type == "decimal":
            base_candidates = [2, 4, 5, 8, 16]
            selected_base = choice(base_candidates)
            # selected_base = 16
            if selected_base == 16:
                number_10 = 0
                # integer_part
                number_10_integer_part = randint(1, 100)
                number_10_integer_part_latex = sy.latex(number_10_integer_part)
                number_n_integer_str = hex(number_10_integer_part).replace("0x", "").upper()
                # decimal_part
                number_10_decimal_part = 0
                number_n_decimal_str = ""
                for index in range(-1, -3, -1):
                    digit = randint(0, 15)
                    number_n_decimal_str += hex(digit).replace("0x", "").upper()
                    number_10_decimal_part += (sy.Pow(16, index) * digit)
                if number_n_decimal_str == "00":
                    digit = randint(1, selected_base - 1)
                    number_n_decimal_str = str(hex(digit))
                    number_10_decimal_part = digit * sy.Pow(selected_base, -1)
                number_10_str_with_decimal = sy.latex(sy.Float(number_10_integer_part + number_10_decimal_part))
                number_10_str_with_frac = number_10_integer_part_latex + f"+ {sy.latex(sy.Rational(number_10_decimal_part))}"
                number_10_latex_with_frac = f"{number_10_str_with_frac}_{{(10)}}"
                number_10_latex_with_decimal = f"{number_10_str_with_decimal}_{{(10)}}"
                number_10_latex = f"{number_10_latex_with_frac} \\quad ({number_10_latex_with_decimal})"
                number_n_str = number_n_integer_str + "." + number_n_decimal_str
                number_n_latex = f"{number_n_str}_{{(16)}}"
            else:
                number_10 = 0
                # integer_part
                number_10_integer_part = 0
                number_n_str_integer_part = ""
                for index in range(0, 3):
                    digit = randint(0, selected_base - 1)
                    number_n_str_integer_part = str(digit) + number_n_str_integer_part
                    number_10_integer_part += (sy.Pow(selected_base, index) * digit)
                if number_n_str_integer_part == "000":
                    digit = randint(1, selected_base - 1)
                    number_n_decimal_str = str(digit)
                    number_10_decimal_part = n_digit * sy.Pow(selected_base, 1)
                # decimal_part
                number_10_decimal_part = 0
                number_n_decimal_str = ""
                for index in range(-1, -3, -1):
                    digit = randint(0, selected_base - 1)
                    number_n_decimal_str += str(digit)
                    number_10_decimal_part += (sy.Pow(selected_base, index) * digit)
                if number_n_decimal_str == "00":
                    digit = randint(1, selected_base - 1)
                    number_n_decimal_str = str(digit)
                    number_10_decimal_part = digit * sy.Pow(selected_base, -1)
                number_10_str_with_decimal = sy.latex(sy.Float(number_10_integer_part + number_10_decimal_part))
                number_10_str_with_frac = sy.latex(number_10_integer_part) + f"+ {sy.latex(sy.Rational(number_10_decimal_part))}"
                number_10_latex_with_frac = f"{number_10_str_with_frac}_{{(10)}}"
                number_10_latex_with_decimal = f"{number_10_str_with_decimal}_{{(10)}}"
                number_10_latex = f"{number_10_latex_with_frac} \\quad ({number_10_latex_with_decimal})"
                number_n_str = number_n_str_integer_part + "." + number_n_decimal_str
                number_n_latex = f"{number_n_str}_{{({selected_base})}}"
        else:
            raise ValueError(f"selected_number_type is {repr(selected_number_type)}. This may be wrong.")
        number_and_base = NumberAndBase(
            number_10_latex=number_10_latex, number_n_latex=number_n_latex, base=selected_base
        )            
        return number_and_base
