from random import choice, randint, random, shuffle

import sympy as sy

"""
(times, division)<-(power, root)
"""

"""
# decide the answer at first sample
from random import randint, random
import sympy as sy

def exp_num_latex(base, index):
    if isinstance(base, int):
        exp_num = sy.Rational(base ** index)
        if index == 1:
            exp_latex = f"{base}"
        else:
            exp_latex = f"{base}^{{{index}}}"
    elif (isinstance(base, sy.core.symbol.Symbol)):
        exp_num = base ** index
        exp_latex = f"{sy.latex(exp_num)}"
    return exp_num, exp_latex

base = 2
final_index = randint(-5, 5)
answer = 2 ** 5

index1 = randint(-5, 5)
if index1 == 0:
    if random() > 0.5:
        index1 += randint(1, 3)
    else:
        index1 -= randint(1, 3)
        
index2 = randint(-5, 5)
if index2 == 0:
    if random() > 0.5:
        index2 += randint(1, 3)
    else:
        index2 -= randint(1, 3)
# index1 + index2 + index3 = final_index -> index3 = final_index - (index1 + index2)
index3 = final_index - (index1 + index2)

num1, num1_latex = exp_num_latex(base, index1)
num2, num2_latex = exp_num_latex(base, index2)
num3, num3_latex = exp_num_latex(base, index3)

answer = num1 * num2 * num3
latex_answer = f"= {answer}"
latex_problem = f"{num1_latex} \\times {num2_latex} \\times {num3_latex}"
print(latex_answer)
print(latex_problem)
"""

class ExponentCalculation:
    
    def __init__(self, **settings):
        # times, division, power, root
        self._calculation_type = settings["calculation_type"]
        # number, character
        self._base_type_list = settings["base_type_list"]
        
        self.latex_answer, self.latex_problem = self._make_problem()
        
    def _make_problem(self):
        if self._calculation_type == "only_times_and_division":
            latex_answer, latex_problem = self._make_only_times_and_division_problem()
        elif self._calculation_type == "include_power":
            latex_answer, latex_problem = self._make_include_power_problem()
        elif self._calculation_type == "include_power_and_root":
            latex_answer, latex_problem = self._make_include_power_and_root_problem()
        return latex_answer, latex_problem

    def _make_only_times_and_division_problem(self):
        def exp(base, index):
            """
            if isinstance(base, int):
                exp_num = sy.Rational(base ** index)
            elif isinstance(base, sy.core.symbol.Symbol):
                exp_num = base ** index
            """
            exp_num = sy.Pow(base, index)
            exp_num_latex = f"{base}^{{{index}}}"
            return exp_num, exp_num_latex
        
        selected_base_type = choice(self._base_type_list)
        
        if selected_base_type == "character":
            base1 = sy.Symbol("a", real=True)
            index1 = self._random_index_without_zero_and_one(min_num=-8, max_num=8)
            base2 = sy.Symbol("b", real=True)
            index2 = self._random_index_without_zero_and_one(min_num=-8, max_num=8)
            base3 = sy.Symbol("c", real=True)
            index3 = self._random_index_without_zero_and_one(min_num=-8, max_num=8)
            num1, num1_latex = exp(base1, index1)
            num2, num2_latex = exp(base2, index2)
            num3, num3_latex = exp(base3, index3)
            
            answer = num1
            latex_problem = f"{num1_latex}"
            
            if random() > 0.5:
                answer *= num2
                latex_problem += f"\\times {num2_latex}"
            else:
                answer /= num2
                latex_problem += f"\\div {num2_latex}"

            if random() > 0.5:
                answer *= num3
                latex_problem += f"\\times {num3_latex}"
            else:
                answer /= num2
                latex_problem += f"\\div {num3_latex}"
            
            latex_answer = f"= {sy.latex(answer)}"
            
            return latex_answer, latex_problem
            
        elif selected_base_type == "number":
            base = choice([2, 3, 5, 7])
            # redefine 2->6, 3->5, 4->4, 5->3: 
            final_index = self._random_index_without_zero_and_one(-(8 - base), 8 - base)
            index1 = self._random_index_without_zero_and_one(min_num=-6, max_num=6)
            index2 = self._random_index_without_zero_and_one(min_num=-6, max_num=6)
            index3 = final_index - (index1 + index2)
            index_list = [index1, index2, index3]
            shuffle(index_list)
            
            first_index = index_list.pop()
            first_num, first_latex = exp(base, first_index)
            answer = first_num
            latex_problem = first_latex
            
            for index in index_list:
                if random() > 0.5: # add as times
                    num, num_latex = exp(base, index)
                    answer *= num
                    latex_problem += f" \\times {num_latex}"
                else: # add as division
                    num, num_latex = exp(base, -index)
                    answer /= num
                    latex_problem += f" \\div {num_latex}"

            latex_answer = f"= {sy.latex(answer)}"
        
            return latex_answer, latex_problem

    def _make_include_power_problem(self):
        def exp_num_latex(number):
            if random() > 0.5:
                # a^k
                index = randint(2, 5)
                if random() > 0.5:
                    index *= -1
                exp_num = sy.Rational(number ** index)
                exp_num_latex = f"{number} ^ {{{index}}}"
            else:
                # (a ^ k) ^ l
                base_index = randint(2, 3)
                index_coefficient = randint(2, 3)
                index = base_index * index_coefficient
                if random() > 0.5:
                    index *= -1
                    exp_num = sy.Rational(number ** index)
                    if random() > 0.5:
                        exp_num_latex = f"\left( {number} ^ {{{base_index}}} \right) ^ {{{-1 * index_coefficient}}}"
                    else:
                        exp_num_latex = f"\left( {number} ^ {{{-1 * base_index}}} \right) ^ {{{index_coefficient}}}"
                else:
                    exp_num = sy.Rational(number ** (index))
                    exp_num_latex = f"\left( {number} ^ {{{base_index}}} \right) ^ {{{index_coefficient}}}"
            return exp_num, exp_num_latex
        
        def exp_character_latex(character):
            index = randint(2, 5)
            exp_character = character ** index
            exp_character_latex = f"{sy.latex(exp_character)}"
            return exp_character, exp_character_latex
        
        selected_base_type = choice(self._base_type_list)
        
        if selected_base_type == "character":
            base1 = sy.Symbol("a", real=True)
            base2 = sy.Symbol("b", real=True)
            base3 = sy.Symbol("c", real=True)
            num1, num1_latex = exp_num_latex(base1, randint(1, 5))
            num2, num2_latex = exp_num_latex(base2, randint(1, 5))
            num3, num3_latex = exp_num_latex(base3, randint(1, 5))
            
        elif selected_base_type == "number":
            base1 = randint(2, 5)
            base2 = randint(2, 5)
            base3 = randint(2, 5)
            num1, num1_latex = exp_num_latex(base1, randint(2, 4))
            num2, num2_latex = exp_num_latex(base2, randint(2, 4))
        
        answer = num1
        latex_problem = f"{num1_latex}"
        
        if random() > 0.5:
            answer *= num2
            latex_problem += f"\\times {num2_latex}"
        else:
            answer /= num2
            latex_problem += f"\\div {num2_latex}"

        if random() > 0.5:
            answer *= num3
            latex_problem += f"\\times {num3_latex}"
        else:
            answer /= num2
            latex_problem += f"\\div {num3_latex}"
        
        latex_answer = f"= {sy.latex(answer)}"
        
        return latex_answer, latex_problem
    
    def _random_index_without_zero_and_one(self, min_num=-5, max_num=5):
        index = randint(min_num, max_num)
        if index == 0:
            if random() > 0.5:
                index = 2
            else:
                index = -2
        elif index == -1:
            index -= 1
        elif index == 1:
            index += 1
        return index