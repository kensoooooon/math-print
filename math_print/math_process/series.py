"""
import cProfile
import pstats

class MyClass:
    def method_to_profile(self):
        # 何らかの処理
        print("Method is running...")
        for _ in range(1000000):
            pass

# インスタンスを作成
my_instance = MyClass()

# プロファイラを作成してメソッドを実行
profiler = cProfile.Profile()
profiler.enable()  # プロファイリングを開始

my_instance.method_to_profile()  # プロファイルしたいメソッドを実行

profiler.disable()  # プロファイリングを終了
stats = pstats.Stats(profiler).sort_stats('cumulative')
stats.print_stats()  # プロファイル結果を表示

"""
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
        elif selected_series_type == "difference_sequence":
            self.latex_answer, self.latex_problem = self._make_difference_sequence_problem()
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
        latex_problem = f"数列\\( {a1} \\cdot {g1}, {a2} \\cdot {g2}, {a3} \\cdot {g3}, \\cdots , {an_latex} \\cdot {sy.latex(gn)} \\)の\n和を求めよ。"
        latex_answer = "求める和を\\( S \\)とすると、"
        latex_answer += f"\\( S = {a1} \\cdot {g1} + {a2} \\cdot {g2} + {a3} \\cdot {g3} + \\cdots + {an_latex} \\cdot {sy.latex(gn)} \\)と表される。\n"
        latex_answer += f"両辺に \\( {common_ratio} \\)を掛けると、\n"
        an_minus1 = arithmetic_sequence.subs(k, n-1)
        if an_minus1.subs(n, 0) == 0:
            an_minus_latex = sy.latex(an_minus1)
        else:
            an_minus_latex = f"({sy.latex(an_minus1)})"
        gn_minus1 = geometric_sequence.subs(k, n-1)
        an_plus1 = arithmetic_sequence.subs(k, n+1)
        gn_plus1 = geometric_sequence.subs(k, n+1)
        latex_answer += f"\\( {common_ratio} S = {a1} \\cdot {g2} + {a2} \\cdot {g3}\\) \n \\( + \\cdots + {an_minus_latex} \\cdot {sy.latex(gn)} + {an_latex} \\cdot {sy.latex(gn_plus1)} \\)となる。\n"
        latex_answer += f"ここで\\( S \\)から\\( {common_ratio} S \\)を引くと、\n"
        S_coeff = 1 - common_ratio
        if S_coeff == -1:
            S_latex = "-S"
        else:
            S_latex = f"{S_coeff}S"
        sum_of_geometric_part_latex = f"\\dfrac{{{g2}({common_ratio}^{{n-1}} - 1)}}{{{common_ratio} - 1}}"
        if common_difference == 1:
            latex_answer += f"\\( {S_latex} = {a1} \\cdot {g1} + ({g2} + {g3} + \\cdots + {sy.latex(gn)}) - {an_latex} \\cdot {sy.latex(gn_plus1)} \\)となる。\n"
            latex_answer += "等比数列の和の公式を使って一部を置き換えると、\n"
            latex_answer += f"\\( {S_latex} = {a1} \\cdot {g1} + \\left\\lbrace{sum_of_geometric_part_latex}\\right\\rbrace - {an_latex} \\cdot {sy.latex(gn_plus1)} \\)\n"
        else:
            latex_answer += f"\\( {S_latex} = {a1} \\cdot {g1} + {common_difference}({g2} + {g3} + \\cdots + {sy.latex(gn)}) - {an_latex} \\cdot {sy.latex(gn_plus1)} \\)となる。\n"
            latex_answer += "等比数列の和の公式を使って一部を置き換えると、\n"
            latex_answer += f"\\( {S_latex} = {a1} \\cdot {g1} + {common_difference}\\left\\lbrace{sum_of_geometric_part_latex}\\right\\rbrace - {an_latex} \\cdot {sy.latex(gn_plus1)} \\)\n"
        latex_answer += f"これを整理すると、\n"
        sum = sy.collect(sy.Sum(arithmetic_sequence * geometric_sequence, (k, 1, n)).doit(), common_ratio ** n)
        latex_answer += f"\\( S = {sy.latex(sum)} \\)"
        return latex_answer, latex_problem
    
    def _make_sum_of_sum_problem(self):
        """数列の和が一般項となる数列の和
        
        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題 
        """
        k = sy.Symbol("k")
        n = sy.Symbol("n")
        sequence = choice(["arithmetic", "geometric"])
        if sequence == "arithmetic":
            first_term = sy.Integer(randint(-3, 3))
            common_difference = sy.Integer(randint(1, 3))
            ak = first_term + (k - 1) * common_difference
        elif sequence == "geometric":
            common_ratio = sy.Integer(choice([2, 3, 5]))
            first_term = common_ratio ** sy.Integer(randint(0, 3))
            ak = first_term * common_ratio ** (k - 1)
        a1 = ak.subs(k, 1)
        if a1 < 0:
            a1_latex = f"({sy.latex(a1)})"
        else:
            a1_latex = sy.latex(a1)
        a2 = ak.subs(k, 2)
        if a2 < 0:
            a2_latex = f"({sy.latex(a2)})"
        else:
            a2_latex = sy.latex(a2)
        a3 = ak.subs(k, 3)
        if a3 < 0:
            a3_latex = f"({sy.latex(a3)})"
        else:
            a3_latex = sy.latex(a3)
        an_minus1 = ak.subs(k, n-1)
        if (sequence == "arithmetic") and (an_minus1.subs(n, 0) != 0):
            an_minus1_latex = f"({sy.latex(an_minus1)})"
        else:
            an_minus1_latex = sy.latex(an_minus1)
        an = ak.subs(k, n)
        if (sequence == "arithmetic") and (an.subs(n, 0) != 0):
            an_latex = f"({sy.latex(an)})"
        else:
            an_latex = sy.latex(an)
        latex_problem = f"数列\\( {a1_latex}, {a1_latex} + {a2_latex}, {a1_latex} + {a2_latex} + {a3_latex}, \\cdots \\)の\n初項から第\\( n \\)項までの和を求めよ。"
        m = sy.Symbol("m")
        sum = sy.Sum(ak, (k, 1, m))
        sum_value = sum.doit()
        latex_answer = f"この数列の第m項は、\n"
        am_minus1 = ak.subs(k, m-1)
        if (sequence == "arithmetic") and (am_minus1.subs(m, 0) != 0):
            am_minus1_latex = f"({sy.latex(am_minus1)})"
        else:
            am_minus1_latex = sy.latex(am_minus1)
        am = ak.subs(k, m)
        if (sequence == "arithmetic") and (am.subs(m, 0) != 0):
            am_latex = f"({sy.latex(am)})"
        else:
            am_latex = sy.latex(am)
        latex_answer += f"\\( {a1_latex} + {a2_latex} + \\cdots + {am_minus1_latex} + {am_latex} \n = \\displaystyle {sy.latex(sum)} = {sy.latex(sum_value)} \\)である。\n"
        latex_answer += "よって求める和は、\n"
        sum_of_sum = sy.Sum(sum_value, (m, 1, n))
        sum_of_sum_value = sum_of_sum.doit()
        latex_answer += f"\\( \\displaystyle {sy.latex(sum_of_sum)} = {sy.latex(sum_of_sum_value)} \\)"
        return latex_answer, latex_problem
    
    def _make_difference_sequence_problem(self):
        """階差数列の一般項を求める
        
        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題 
        """
        k = sy.Symbol("k")
        n = sy.Symbol("n")
        selected_sequence = choice(["arithmetic", "geometric"])
        if selected_sequence == "arithmetic":
            first_term = sy.Integer(randint(-3, 3))
            common_difference = sy.Integer(choice([-3, -2, -1, 1, 2, 3]))
            bk = first_term + (k - 1) * common_difference
        elif selected_sequence == "geometric":
            common_ratio = sy.Integer(choice([2, 3, 5]))
            first_term = common_ratio ** randint(0, 2)
            bk = first_term * common_ratio ** (k - 1)
        a1 = sy.Integer(randint(-3, 3))
        an = a1 + sy.Sum(bk, (k, 1, n-1)).doit()
        a1 = an.subs(n, 1)
        a2 = an.subs(n, 2)
        a3 = an.subs(n, 3)
        a4 = an.subs(n, 4)
        a5 = an.subs(n, 5)
        a6 = an.subs(n, 6)
        an_minus1 = an.subs(n, n-1)
        latex_problem = f"数列\\( {{a_n}}: {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, \\cdots \\)\nの一般項を求めよ。"
        b1 = bk.subs(k, 1)
        b2 = bk.subs(k, 2)
        b3 = bk.subs(k, 3)
        b4 = bk.subs(k, 4)
        bn_minus1 = bk.subs(k, n-1)
        bn = bk.subs(k, n)
        latex_answer = f"数列\\( {{a_n}} \\)階差数列を\\( {{b_n}} \\)とすると、数列\\( {{b_n}} \\)は\\(  {b1}, {b2}, {b3}, {b4} \\cdots \\)となっている。\n"
        if selected_sequence == "arithmetic":
            latex_answer += f"これは初項\\( {first_term} \\)、公差\\( {common_difference} \\)の等差数列なので、\n"
        elif selected_sequence == "geometric":
            latex_answer += f"これは初項\\( {first_term} \\)、公比\\( {common_ratio} \\)の等比数列なので、\\( b_n = {sy.latex(bn)} \\)と表せる。\n"
        latex_answer += f"よって\\( n \\geqq 2 \\)のとき、\n"
        bk_sum = sy.Sum(bk, (k, 1, n-1))
        latex_answer += f"\\( a_n = a_1 + \\displaystyle \\sum_{{k=1}}^{{n-1}} b_k = {a1} + {sy.latex(bk_sum)} \\)\n"
        bk_sum_value = bk_sum.doit()
        an_value = an.doit()
        latex_answer += f"\\( = {a1} + \\left( {sy.latex(bk_sum_value)} \\right) = {sy.latex(an_value)} \\)となる。\n"
        latex_answer += f"この式に\\( n = 1 \\)を代入すると、\\( a_1 = {a1} \\)であり、これは実際の初項と一致する。\n"
        latex_answer += f"したがって、一般項は\\( a_n = {sy.latex(an_value)} \\)である。"
        return latex_answer, latex_problem
