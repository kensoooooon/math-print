from random import choice, randint, random

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
        self._calculation_type_list = settings["calculation_type_list"]
        # number, character
        self._base_type_list = settings["base_type_list"]
        
        self.latex_answer, self.latex_problem = self._make_problem()
        
    def _make_problem(self):
        
        latex_answer, latex_problem = self._make_only_times_and_division_problem()
        
        return latex_answer, latex_problem

    def _make_only_times_and_division_problem(self):
        
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
    