from random import choice, randint, random

import sympy as sy

"""
(times, division)<-(power, root)
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
        
        def exp(base, index):
            exp_num = sy.Rational(base ** index)
            return exp_num
        
        selected_base_type = choice(self._base_type_list)
        
        if selected_base_type == "character":
            base1 = sy.Symbol("a", real=True)
            base2 = sy.Symbol("b", real=True)
            base3 = sy.Symbol("c", real=True)
            num1 = base1 ** randint(1, 4)
            num2 = base2 ** randint(1, 4) 
            num3 = base3 ** randint(1, 4)
            num1_latex = sy.latex(num1)
            num2_latex = sy.latex(num2)
            num3_latex = sy.latex(num3)
            
        elif selected_base_type == "number":
            base1 = randint(2, 5)
            index1 = randint(2, 4)
            base2 = randint(2, 5)
            index2 = randint(2, 4)
            base3 = randint(2, 5)
            index3 = randint(2, 4)
            num1 = exp(base1, index1)
            num2 = exp(base2, index2)
            num3 = exp(base3, index3)
            num1_latex = f"{base1}^{{{index1}}}"
            num2_latex = f"{base2}^{{{index2}}}"
            num3_latex = f"{base3}^{{{index3}}}"
        
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
    