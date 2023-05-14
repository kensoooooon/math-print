"""
5/14
作成開始
    まずは1/6公式から
        ありうるパターンは、2次関数と直線の間の面積、2つの2次関数の間の面積、3次の係数が等しい3次関数の間の面積
    記入の流れとしては、vector_cross_pointに近い
        latexとそうでないものをこちらで混在させてhtmlに渡す感じになる
"""
from random import choice, random, randint


import sympy as sy


class CalculateAreaByIntegration:
    """積分の公式を用いて面積を求める問題と解答を出力
    
    Attributes:
        latex_answer (str): latex形式と通常の文字が混在した解答
        latex_problem (str): latex形式と通常の文字が混在した問題
    
    Raises:
        ValueError: 想定されていない公式が抽選されたときに挙上
    """
    def __init__(self, **settings: dict) -> None:
        """初期設定
        
        Args:
            settings (dict): 問題を決定する各種設定を格納
        """
        sy.init_printing(order="grevlex")
        used_formula = choice(settings["used_formulas"])
        if used_formula == "one_sixth":
            self.latex_answer, self.latex_problem = self._make_one_sixth_problem()
        else:
            raise ValueError(f"'used_formula' is {used_formula}. This isn't expected value. Please check {settings['used_formulas']}.")
    
    def _make_one_sixth_problem(self) -> tuple[str, str]:
        """1/6公式を利用する問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式と通常の文字が混在した解答
            latex_problem (str): latex形式と通常の文字が混在した問題
            
        
        Developing:
            2次関数と直線の間の面積、2つの2次関数の間の面積、3次の係数が等しい3次関数の3種を実装
        """
        x = sy.Symbol("x", real=True)
        problem_type = choice(["between_quadratic_function_and_line", "between_quadratic_functions", "between_cubic_functions"])
        if problem_type == "between_quadratic_function_and_line":
            quadratic_coefficient = randint(-3, 3)
            answer1 = randint(-3, 3)
            if random() > 0.5:
                answer2 = answer1 + randint(1, 3)
            else:
                answer2 = answer1 + randint(-3, -1)
            quadratic_function = quadratic_coefficient * (x - answer1) * (x - answer2)
        elif problem_type == "between_quadratic_functions":
            pass
        elif problem_type == "between_cubic_functions":
            pass
        latex_answer = "dummy answer in one_sixth"
        latex_problem = "dummy problem in one_sixth"
        return latex_answer, latex_problem
