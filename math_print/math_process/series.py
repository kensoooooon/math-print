from random import choice, randint, random
from typing import Dict, Tuple

import sympy as sy


class Series:
    """種々の数列の和を求める問題と解答を、指定された条件に応じて作成・格納
    
    Attributes:
        latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
        latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題 
    """
    def __init__(self, **settings: Dict) -> None:
        """初期設定
        
        Args:
            settings (dict): 問題の設定を格納
            - 出力すべき問題のタイプ(多項式の和、等比数列の和など)を格納
        
        Raises:
            ValueError: 想定されていないタイプの問題が指定されたときに挙上
        """
        sy.init_printing(order='grevlex')
        selected_series_type = choice(settings["series_types"])
        if selected_series_type == "sum_from_linear_to_cubic":
            self.latex_answer, self.latex_problem = self._make_sum_from_linear_to_cubic_problem()
        elif selected_series_type == "sum_of_geometric":
            self.latex_answer, self.latex_problem = self._make_sum_of_geometric_problem()
        elif selected_series_type == "sum_of_arithmetic_times_geometric":
            self.latex_answer, self.latex_problem = self._make_sum_of_arithmetic_times_geometric_problem()
        elif selected_series_type == "sum_of_sum":
            self.latex_answer, self.latex_problem = self._make_sum_of_sum_problem()
        else:
            raise ValueError(f"'selected_series_type is {selected_series_type}. This isn't expected value.")
    
    def _make_sum_from_linear_to_cubic_problem(self) -> Tuple[str, str]:
        """1~3次式の和の問題と解答を作成
        
        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題 
        """
        k = sy.Symbol("k")
        n = sy.Symbol("n")
        if random() > 0.4:
            constant = sy.Integer(randint(-3, 3))
            linear_coeff = sy.Integer(randint(-3, 3))
            quadratic_coeff = sy.Integer(randint(-3, 3))
            cubic_coeff = sy.Integer(randint(-3, 3))
            function = cubic_coeff * k ** 3 + quadratic_coeff * k ** 2 + linear_coeff * k + constant
        else:
            dimension = choice([2, 3])
            if dimension == 2:
                alpha = sy.Integer(randint(-3, 3))
                beta = sy.Integer(randint(-3, 3))
                function = (k - alpha) * (k - beta)
            elif dimension == 3:
                alpha = sy.Integer(randint(-3, 3))
                beta = sy.Integer(randint(-3, 3))
                gamma = sy.Integer(randint(-3, 3))
                function = (k - alpha) * (k - beta) * (k - gamma)
        if random() > 0.3:
            problem_mode = "character"
            start = 1
            end = choice([n, n-1])
        else:
            problem_mode = "number"
            start = sy.Integer(randint(1, 3))
            end = sy.Integer(randint(start + 2, 10))
        series = sy.Sum(function, (k, start, end))
        latex_problem = f"\\( \\displaystyle {sy.latex(series)} \\)"
        if problem_mode == "character":
            answer = sy.factor(series.doit())
        elif problem_mode == "number":
            answer = series.doit()
        latex_answer = f"\\( = {sy.latex(answer)} \\)"
        return latex_answer, latex_problem
    
    def _make_sum_of_geometric_problem(self):
        """等比数列の和
        
        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題 
        """
        n = sy.Symbol("n")
        k = sy.Symbol("k")
        if random() > 0.3:
            base = sy.Integer(randint(2, 5))
        else:
            numerator = sy.Integer(randint(1, 5))
            denominator = sy.Integer(randint(2, 5))
            base = sy.Rational(numerator, denominator)
        if base == 1:
            base = sy.Integer(randint(2, 5))
        if random() > 0.3:
            function = base ** k
        else:
            function = base ** (k - 1)
        if random() > 0.3:
            problem_mode = "character"
            start = 1
            end = choice([n, n-1])
        else:
            problem_mode = "number"
            start = sy.Integer(randint(1, 3))
            end = sy.Integer(randint(start + 2, 7))
        series = sy.Sum(function, (k, start, end))
        latex_problem = f"\\( \\displaystyle {sy.latex(series)} \\)"
        if problem_mode == "character":
            answer = sy.factor(series.doit())
        elif problem_mode == "number":
            answer = series.doit()
        latex_answer = f"\\( = {sy.latex(answer)} \\)"
        return latex_answer, latex_problem

    def _make_sum_of_arithmetic_times_geometric_problem(self):
        """等差x等比数列の和
        
        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題 
        """
        n = sy.Symbol("n")
        k = sy.Symbol("k")
        first_term_of_arithmetic = sy.Integer(randint(1, 3))
        common_difference = sy.Integer(randint(1, 3))
        arithmetic_sequence = first_term_of_arithmetic + (k - 1) * common_difference
        common_ratio = sy.Integer(choice([2, 3, 5]))
        first_term_of_geometric = common_ratio ** sy.Integer(randint(0, 2))
        geometric_sequence = sy.powsimp(first_term_of_geometric * (common_ratio ** (k - 1)))
        a1 = arithmetic_sequence.subs(k, 1)
        g1 = geometric_sequence.subs(k, 1)
        a2 = arithmetic_sequence.subs(k, 2)
        g2 = geometric_sequence.subs(k, 2)
        a3 = arithmetic_sequence.subs(k, 3)
        g3 = geometric_sequence.subs(k, 3)
        an = arithmetic_sequence.subs(k, n)
        if an.subs(n, 0) == 0:
            an_latex = sy.latex(an)
        else:
            an_latex = f"({sy.latex(an)})"
        gn = geometric_sequence.subs(k, n)
        latex_problem = f"和\\( S = {a1} \\cdot {g1} + {a2} \\cdot {g2} + {a3} \\cdot {g3} + \\cdots + {an_latex} \\cdot {sy.latex(gn)} \\)を求めよ。"
        latex_answer = f"両辺に \\( {common_ratio} \\)を掛けると、\n"
        an_minus1 = arithmetic_sequence.subs(k, n-1)
        if an_minus1.subs(n, 0) == 0:
            an_minus_latex = sy.latex(an_minus1)
        else:
            an_minus_latex = f"({sy.latex(an_minus1)})"
        gn_minus1 = geometric_sequence.subs(k, n-1)
        an_plus1 = arithmetic_sequence.subs(k, n+1)
        gn_plus1 = geometric_sequence.subs(k, n+1)
        latex_answer += f"\\( {common_ratio} S = {a1} \\cdot {g2} + {a2} \\cdot {g3} + \\cdots + {an_minus_latex} \\cdot {sy.latex(gn)} + {an_latex} \\cdot {sy.latex(gn_plus1)} \\)\n"
        latex_answer += f"ここで元の式からこの式を引くと、\n"
        S_coeff = 1 - common_ratio
        if S_coeff == -1:
            S_latex = "-S"
        else:
            S_latex = f"{S_coeff}S"
        # sum_of_geometric_part = sy.powsimp(sy.Sum(g2 * common_ratio ** (k - 1), (k, 1, n-2)).doit())
        # sum_of_geometric_part = sy.geometry.sequence.GeometricSum(g2, common_ratio, n-2)
        """
        geometric_sum_formula = a*(1 - r**n)/(1 - r)
        
        if common_ratio > 1:
            sum_of_geometric_part = g2 * (common_ratio ** (n - 2) - 1) / (common_ratio - 1)
        else:
            sum_of_geometric_part = g2 * (1 - common_ratio ** (n - 2)) / (1 - common_ratio)
        """
        sum_of_geometric_part_latex = f"\\dfrac{{{g2}({common_ratio}^{{n-2}} - 1)}}{{{common_ratio} - 1}}"
        if common_difference == 1:
            latex_answer += f"\\( {S_latex} = {a1} \\cdot {g1} + ({g2} + {g3} + \\cdots + {sy.latex(gn)}) - {an_latex} \\cdot {sy.latex(gn_plus1)} \\)\n"
            latex_answer += f"\\( {S_latex} = {a1} \\cdot {g1} + \\left({sum_of_geometric_part_latex}\\right) - {an_latex} \\cdot {sy.latex(gn_plus1)} \\)"
        else:
            latex_answer += f"\\( {S_latex} = {a1} \\cdot {g1} + {common_difference}({g2} + {g3} + \\cdots + {sy.latex(gn)}) - {an_latex} \\cdot {sy.latex(gn_plus1)} \\)\n"
            latex_answer += f"\\( {S_latex} = {a1} \\cdot {g1} + {common_difference}\\left({sum_of_geometric_part_latex}\\right) - {an_latex} \\cdot {sy.latex(gn_plus1)} \\)"
        return latex_answer, latex_problem
    
    def _make_sum_of_sum_problem(self):
        """数列の和が一般項となる数列の和
        
        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題 
        """
        latex_answer = "dummy answer in _make_sum_of_sum_problem"
        latex_problem = "dummy problem in _make_sum_of_sum_problem"
        return latex_answer, latex_problem
