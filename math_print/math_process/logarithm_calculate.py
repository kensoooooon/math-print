from random import choice, randint

import sympy as sy

class LogarithmCalculateProblem:
    
    def __init__(self, **settings):
        self._problem_type_list = settings["problem_type_list"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        selected_problem_type = choice(self._problem_type_list)
        
        if selected_problem_type == "change_of_base_formula":
            latex_answer, latex_problem = self._change_of_base_problem()
        
        return latex_answer, latex_problem
    
    def _change_of_base_problem(self):
        common_base = choice([2, 3, 5, 7, 9, 11])
        logarithm_base = common_base ** randint(2, 5)
        logarithm_antilog = common_base ** randint(2, 5)
        latex_problem = f"log_{logarithm_base} {logarithm_antilog}"
        
        denominator = int(sy.log(logarithm_base, common_base))
        numerator = int(sy.log(logarithm_antilog, common_base))
        answer = sy.Rational(numerator, denominator)
        latex_answer = f" = {sy.latex(answer)}" 
        
        return latex_answer, latex_problem