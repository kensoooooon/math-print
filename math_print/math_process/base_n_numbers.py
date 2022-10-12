"""
from random import randint
import sympy as sy

base = 5
digit1 = randint(0, base - 1)
print(f"digit1: {digit1}")
digit2 = randint(0, base - 1)
print(f"digit2: {digit2}")
integer_part_digits = [digit1, digit2]
digit3 = randint(0, base - 1)
print(f"digit3: {digit3}")
digit4 = randint(0, base - 1)
print(f"digit4: {digit4}")
decimal_part_digits = [digit3, digit4]

number_of_digits = len(integer_part_digits)
index = number_of_digits - 1
integer_num = 0
for i, digit in enumerate(integer_part_digits):
    integer_num += (digit * sy.Pow(base, index - i))
decimal_num = 0
index = -1
for i, digit in enumerate(decimal_part_digits):
    print(f"index - i: {index - i}")
    decimal_num += (digit * sy.Pow(base, index - i))
                            
print(f"integer_num: {integer_num}")
print(f"decimal_num: {decimal_num}")
print(f"sy.Float(decimal_num): {sy.Float(decimal_num)}")
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
    