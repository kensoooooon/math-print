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
            base = sy.Symbol("a", real=True)
            index1 = self._random_index_without_zero_and_one(min_num=-8, max_num=8)
            index2 = self._random_index_without_zero_and_one(min_num=-8, max_num=8)
            index3 = self._random_index_without_zero_and_one(min_num=-8, max_num=8)
            index4 = self._random_index_without_zero_and_one(min_num=-8, max_num=8)
            index_list = [index1, index2, index3, index4]
            
            first_index = index_list.pop()
            first_num, first_latex = exp(base, first_index)
            answer = first_num
            latex_problem = first_latex
            for index in index_list:
                num, num_latex = exp(base, index)
                if random() > 0.5:
                    answer *= num
                    latex_problem += f"\\times {num_latex}"
                else:
                    answer /= num
                    latex_problem += f"\\div {num_latex}"
            
            latex_answer = f"= {sy.latex(answer)}"
            
            return latex_answer, latex_problem
            
        elif selected_base_type == "number":
            base = choice([2, 3, 5, 7])
            # redefine 2->6, 3->5, 4->4, 5->3: 
            final_index = self._random_index_without_zero_and_one(min_num=-(8 - base), max_num=8 - base)
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
        def exp(base, inner_index=1, outer_index=1):
            if (inner_index == 1) and (outer_index == 1):
                exp_num = sy.Pow(base, 1)
                exp_num_latex = f"{base}"
            elif (inner_index == 1) and (outer_index != 1):
                exp_num = sy.Pow(base, outer_index)
                exp_num_latex = f"{base}^{{{outer_index}}}"
            elif (inner_index != 1) and (outer_index == 1):
                exp_num = sy.Pow(base, inner_index)
                exp_num_latex = f"{base}^{{{inner_index}}}"
            else:
                exp_num = sy.Pow(base, inner_index * outer_index)
                exp_num_latex = f"\\left( {base}^{{{inner_index}}} \\right)^{{{outer_index}}}"
            return exp_num, exp_num_latex
        
        selected_base_type = choice(self._base_type_list)
        
        if selected_base_type == "character":
            base = sy.Symbol("a", real=True)
            inner_index1 = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            outer_index1 = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            index1 = (inner_index1, outer_index1)
            inner_index2 = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            outer_index2 = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            index2 = (inner_index2, outer_index2)
            inner_index3 = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            outer_index3 = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            index3 = (inner_index3, outer_index3)
            inner_index4 = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            outer_index4 = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            index4 = (inner_index4, outer_index4)
            index_list = [index1, index2, index3, index4]
            
            first_inner_index, first_outer_index = index_list.pop()
            first_num, first_latex = exp(base, inner_index=first_inner_index, outer_index=first_outer_index)
            answer = first_num
            latex_problem = first_latex
            for inner_index, outer_index in index_list:
                num, num_latex = exp(base, inner_index=inner_index, outer_index=outer_index)
                if random() > 0.5:
                    answer *= num
                    latex_problem += f"\\times {num_latex}"
                else:
                    answer /= num
                    latex_problem += f"\\div {num_latex}"
            
            latex_answer = f"= {sy.latex(answer)}"

            return latex_answer, latex_problem

        elif selected_base_type == "number":
            base = choice([2, 3, 5, 7])
            final_index = self._random_index_without_zero_and_one(min_num=-(8 - base), max_num=8 - base)
            print(f"final_index: {final_index}")
            inner_index1 = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            outer_index1 = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            index1 = (inner_index1, outer_index1)
            print(f"index1: {index1}")
            inner_index2 = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            outer_index2 = self._random_index_without_zero_and_one(min_num=-3, max_num=3)
            index2 = (inner_index2, outer_index2)
            print(f"index2: {index2}")
            coordinate_index = final_index - (inner_index1 * outer_index1 + inner_index2 * outer_index2)
            print(f"coordinate_index: {coordinate_index}")
            if coordinate_index > 0:
                for num_for_div in range(coordinate_index - 1, 1, -1):
                    # print(f"num_for_div: {num_for_div}")
                    # print(f"coordinate_index: {coordinate_index}")
                    if (coordinate_index % num_for_div == 0):
                        inner_index3 = num_for_div
                        outer_index3 = int(coordinate_index / num_for_div)
                        # print(f"inner_index3 is {inner_index3}, outer_index is {outer_index3}")
                        break
                else:
                    inner_index3 = 1
                    outer_index3 = coordinate_index
            elif coordinate_index < 0:
                for num_for_div in range(coordinate_index + 1, -1, 1):
                    # print(f"num_for_div: {num_for_div}")
                    # print(f"coordinate_index: {coordinate_index}")
                    if (coordinate_index % num_for_div == 0):
                        inner_index3 = num_for_div
                        outer_index3 = int(coordinate_index / num_for_div)
                        # print(f"inner_index3 is {inner_index3}, outer_index is {outer_index3}")
                        break
                else:
                    inner_index3 = 1
                    outer_index3 = coordinate_index
            else:
                inner_index3 = 1
                outer_index3 = 0
            # print("--------------------")
            index3 = (inner_index3, outer_index3)
            print(f"index3: {index3}")
            index_list = [index1, index2, index3]
            shuffle(index_list)
            
            first_inner_index, first_outer_index = index_list.pop()
            print(f"first_inner_index: {first_inner_index}, first_outer_index: {first_outer_index}")
            first_num, first_latex = exp(base, inner_index=first_inner_index, outer_index=first_outer_index)
            print(f"first_num: {first_num}, first_latex: {first_latex}")
            answer = first_num
            latex_problem = first_latex
            
            for inner_index, outer_index in index_list:
                if random() > 0.5:  # add as times
                    if random() > 0.5:
                        num, num_latex = exp(base, inner_index=inner_index, outer_index=outer_index)
                    else:
                        num, num_latex = exp(base, inner_index=-inner_index, outer_index=-outer_index)
                    answer *= num
                    latex_problem += f" \\times {num_latex}"
                else:  # add as division
                    if random() > 0.5:
                        num, num_latex = exp(base, inner_index=-inner_index, outer_index=outer_index)
                    else: 
                        num, num_latex = exp(base, inner_index=inner_index, outer_index=-outer_index)
                    answer /= num
                    latex_problem += f"\\div {num_latex}"
                
            latex_answer = f"= {sy.latex(answer)}"
            print("------------------------------")
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