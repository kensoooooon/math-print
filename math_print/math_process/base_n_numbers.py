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
"""
from random import choice, randint, random


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
    