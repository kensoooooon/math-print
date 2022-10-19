"""
import sympy as sy
from random import randint, choice

def _make_base_and_numbers():
    # base_candidates = [2, 3, 4, 5, 6, 7, 8, 16]
    # base = choice(base_candidates)
    base = 16
    print(f"selected base: {base}")
    if base == 16:
        integer_part_num = 0
        for i in range(0, 3):
            integer_part_num += (sy.Pow(16, i) * randint(0, 16))
        print(f"integer_part_num: {integer_part_num}")
        hexed_num = hex(integer_part_num)
        print(f"hexed_num: {hexed_num}")
        replaced_hexed_num = hexed_num.replace("0x", "").upper()
        print(f"replaced_hexed_num: {replaced_hexed_num}")
        decimal_part_num = 0
        for i in range(-1, 3, -1):
            decimal_part_num += (sy.Pow(16, i) * randint(0, 16))
        print(f"decimal_part_num: {decimal_part_num}")
        replaced_hexed_decimal_num = hex(decimal_part_num).replace("0x", "").upper()
        print(f"replace_hexed_decimal_num: {replaced_hexed_decimal_num}")
    else:
        # integer number
        integer_num = 0
        integer_part_digits = []
        for i in range(2):
            digit = randint(0, base - 1)
            if digit != 0:
                integer_part_digits.append(digit)
            # minimum catch
            if (i == 1) and (not(integer_part_digits)):
                integer_part_digits.append(randint(1, base - 1))
        print(f"integer_part_digits: {integer_part_digits}")
        ten_base_integer_num = 0
        for index, digit in enumerate(integer_part_digits):
            ten_base_integer_num += (digit * sy.Pow(base, index))
        print(f"ten_base_integer_num: {ten_base_integer_num}")
        # decimal number
        decimal_num = 0
        decimal_part_digits = []
        for i in range(2):
            digit = randint(0, base - 1)
            if digit != 0:
                decimal_part_digits.append(digit)
            if (i == 1) and (not(decimal_part_digits)):
                decimal_part_digits.append(randint(1, base - 1))
        print(f"decimal_part_digits: {decimal_part_digits}")
        ten_base_decimal_num = 0
        for index, digit in enumerate(decimal_part_digits):
            ten_base_decimal_num += (digit * sy.Pow(base, -(index + 1)))
        print(f"ten_base_decimal_num: {ten_base_decimal_num}")
        print(f"floated ten_base_decimal_num: {sy.Float(ten_base_decimal_num)}")

for _ in range(10):
    _make_base_and_numbers()
    print("--------------------------")

from random import randint, choice
import sympy as sy

def _make_base_and_number():
    n_base_integer_part = ""
    n_base_decimal_part = ""
    ten_base_integer_part = ""
    ten_base_decimal_part = ""
    # base_candidates = [2, 3, 4, 5, 6, 7, 8, 16]
    # base = choice(base_candidates)
    base = 16
    if base == 16:
        ten_base_integer = 0
        for i in range(0, 3):
            coeff = randint(0, 16)
            print(f"coeff: {coeff}")
            ten_base_integer += (sy.Pow(base, i) * coeff)
            n_base_integer_part = str(hex(coeff)).replace("0x", "").upper() + n_base_integer_part
    print(f"ten_base_integer: {ten_base_integer}")
    print(f"n_base_integer_part: {n_base_integer_part}")
    print(f"lstriped: {n_base_integer_part.lstrip('0')}")

for _ in range(10):
          _make_base_and_number()
          print("------------")


base = 5
number_10 = 0.76
digit = []
while True:
    number_10 *= base
    print(f"number_10: {number_10}")
    number_10_integer_part = int(number_10)
    print(f"number_10_integer_part: {number_10_integer_part}")
    number_10_decimal_part = round(number_10 - number_10_integer_part, 6)
    print(f"number_10_decimal_part: {number_10_decimal_part}")
    digit.append(number_10_integer_part)
    print(f"digit: {digit}")
    print("----------------")
    if number_10_decimal_part == 0:
        break
    number_10 = number_10_decimal_part
print(digit)
"""
from collections import namedtuple
from random import choice, randint, random
from typing import NamedTuple

import sympy as sy


class BaseNNumbersProblem:
    def __init__(self, **settings):
        self._convert_from_to_types = settings["convert_from_to_types"]
        self._numbers_to_convert = settings["numbers_to_convert"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        selected_convert_from_to = choice(self._convert_from_to_types)
        if selected_convert_from_to == "from_n_base_to_ten_base":
            latex_answer, latex_problem = self._make_from_n_base_to_ten_base_problem()
        elif selected_convert_from_to == "from_ten_base_to_n_base":
            latex_answer, latex_problem = self._make_from_ten_base_to_n_base_problem()
        elif selected_convert_from_to == "from_n_base_to_n_dash_base":
            latex_answer, latex_problem = self._make_from_n_base_to_n_dash_base_problem()
        return latex_answer, latex_problem
    
    def _make_from_n_base_to_ten_base_problem(self):
        number_and_base = self._make_random_10_and_n_base_number()
        print(number_and_base)
        latex_answer = f"= {number_and_base.number_10_latex}"
        latex_problem = f"{number_and_base.number_n_latex} \\rightarrow \\underline{{\\quad \\quad \\quad}}_{{(10)}}"
        return latex_answer, latex_problem

    def _make_from_ten_base_to_n_base_problem(self):
        number_and_base = self._make_random_10_and_n_base_number()
        print(number_and_base)
        latex_answer = f" = {number_and_base.number_n_latex}"
        latex_problem = f"{number_and_base.number_10_latex} \\rightarrow \\underline{{\\quad \\quad \\quad}}_{{({number_and_base.base})}}"
        return latex_answer, latex_problem

    def _make_from_n_base_to_n_dash_base_problem(self):
        latex_answer = f"dduuudududuummmmmyy"
        latex_problem = f"dummmyymmmy"
        return latex_answer, latex_problem
    
    def _make_random_10_and_n_base_number(self):
        """10進数とそれに対応するn進数の文字列をランダムに作成する
        
        Returns:
            number_and_base (NumberAndBase): n,10それぞれの進数と、使用された底を格納         
        Raise:
            ValueError: 想定されていない数のタイプが入ってきたときに挙上
        
        Developing:
            x_{(10)}, y_{(n)}
        """
        class NumberAndBase(NamedTuple):
            number_10_latex_with_frac : str
            number_10_latex_with_decimal : str
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
                number_10_latex = f"{sy.latex(number_10)}_{{(10)}}"
                number_n_latex = f"{number_n_str}_{{({selected_base})}}"
        elif selected_number_type == "decimal":
            base_candidates = [2, 4, 5, 8, 16]
            selected_base = choice(base_candidates)
            # selected_base = 16
            if selected_base == 16:
                number_10 = 0
                number_n_str = ""
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
                # number_10_str = number_10_integer_part_latex  + sy.latex(sy.Float(number_10_decimal_part)).lstrip("0")
                number_10_str_with_decimal = number_10_integer_part_latex + f". {sy.latex(sy.Float(round(number_10_decimal_part, 5)))}"
                number_10_str_with_frac = number_10_integer_part_latex + f"+ {sy.latex(sy.Rational(number_10_decimal_part))}"
                number_10_with_frac_latex = f"{number_10_str_with_frac}_{{(10)}}"
                number_10_with_decimal_latex = f"{number_10_str_with_decimal}_{{(10)}}"
                number_n_str = number_n_integer_str + "." + number_n_decimal_str
                number_n_latex = f"{sy.latex(number_n_str)}_{{(16)}}"
            else:
                number_10 = 0
                number_n_str = ""
                # integer_part
                number_10_integer_part = 0
                number_n_str_integer_part = ""
                for index in range(0, 3):
                    digit = randint(0, selected_base - 1)
                    number_n_str_integer_part = str(digit) + number_n_str_integer_part
                    number_10_integer_part += sy.Pow(selected_base, index)
                # decimal_part
                
                number_10_latex = "dummmy"
                number_n_latex = "dummmmyy"
        else:
            raise ValueError(f"selected_number_type is {repr(selected_number_type)}. This may be wrong.")
        number_and_base = NumberAndBase(number_10_latex=number_10_latex, number_n_latex=number_n_latex, base=selected_base)
        return number_and_base
