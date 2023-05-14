"""
5/14
作成開始
    まずは1/6公式から
        ありうるパターンは、2次関数と直線の間の面積、2つの2次関数の間の面積、3次の係数が等しい3次関数の間の面積
"""
from random import choice


import sympy


class CalculateAreaByIntegration:
    
    def __init__(self, **settings):
        used_formula = choice(settings["used_formulas"])
        if used_formula == "one_sixth":
            self.latex_answer, self.latex_problem = self._make_one_sixth_problem()
        else:
            raise ValueError(f"'used_formula' is {used_formula}. This isn't expected value.")
    
    def _make_one_sixth_problem(self):
        latex_answer = "dummy answer in one_sixth"
        latex_problem = "dummy problem in one_sixth"
        return latex_answer, latex_problem
