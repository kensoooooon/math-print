"""
5/14
作成開始
    まずは1/6公式から
        ありうるパターンは、2次関数と直線の間の面積、2つの2次関数の間の面積、3次の係数が等しい3次関数の間の面積
    記入の流れとしては、vector_cross_pointに近い
        latexとそうでないものをこちらで混在させてhtmlに渡す感じになる

5/15
引き続き作成
    そこそこによさげだが、細かいところで表記が甘い
        面積が無限小数になってしまう問題は解決済み
        混在型の式の表記が甘い
            ・ちゃんと上-下、つまり符号が調整されていない
                
            ・最後の3乗の部分で、β-αの3乗の部分のカッコ回りがガバい
                ちょっと試してみたが、手作業で追加してくのが妥当？
                    とりあえずok
"""
from random import choice, random, randint
from typing import Dict, Tuple


import sympy as sy


class CalculateAreaByIntegration:
    """積分の公式を用いて面積を求める問題と解答を出力
    
    Attributes:
        latex_answer (str): latex形式と通常の文字が混在した解答
        latex_problem (str): latex形式と通常の文字が混在した問題
    
    Raises:
        ValueError: 想定されていない公式が抽選されたときに挙上
    """
    def __init__(self, **settings: Dict) -> None:
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
    
    def _make_one_sixth_problem(self) -> Tuple[str, str]:
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
            if random() > 0.5:
                quadratic_coefficient = randint(-3, 3)
                answer1 = randint(-3, 3)
                if random() > 0.5:
                    answer2 = answer1 + randint(1, 3)
                else:
                    answer2 = answer1 + randint(-3, -1)
                if answer1 > answer2:
                    bigger_answer, smaller_answer = answer1, answer2
                else:
                    bigger_answer, smaller_answer = answer2, answer1
                quadratic_function = sy.expand(quadratic_coefficient * (x - smaller_answer) * (x - bigger_answer))
                latex_problem = f"\\( {sy.latex(quadratic_function)} \\)"\
                    "と\\( x \\)軸で囲まれた部分の面積を求めよ。"
                area = abs(quadratic_coefficient * sy.Rational(1, 6) * (answer1 - answer2) ** 3)
                latex_answer = f"\\( {sy.latex(quadratic_function)} \\)"\
                    f"\\( = {sy.latex(sy.factor(quadratic_function))}\\)となる。 \n"\
                    f"そのため、2次関数と\\( x \\)軸との交点は、\\( x = {sy.latex(smaller_answer)}, {sy.latex(bigger_answer)} \\)である。そのため、2次関数と\\( x \\)軸で囲まれた面積は、\n"\
                    f"\\( \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} ({sy.latex(quadratic_function)}) dx\\)"\
                    f"\\( = \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} {sy.latex(sy.factor(quadratic_function))} dx\\)\n"
                if smaller_answer >= 0:
                    latex_answer += f"\\( = \\frac{{|{quadratic_coefficient}|}}{{6}} ({bigger_answer} - {smaller_answer})^3\\)"
                else:
                    if bigger_answer >= 0:
                        latex_answer += f"\\( = \\frac{{|{quadratic_coefficient}|}}{{6}} \\lbrace {bigger_answer} - ({smaller_answer}) \\rbrace ^3 \\) "
                    else:
                        latex_answer += f"\\( = \\frac{{|{quadratic_coefficient}|}}{{6}} \\lbrace {bigger_answer}) - ({smaller_answer}) \\rbrace ^3 \\) "
                latex_answer += f"\\( = {sy.latex(area)} \\)"
                # latex_answer = f"\\(\\lbrace  5 - 3 \\rbrace \\)"
            else:
                latex_answer = "dummy answer of quadratic_function and line in one_sixth"
                latex_problem = "dummy problem of quadratic_function and line in one_sixth"
        elif problem_type == "between_quadratic_functions":
            latex_answer = "dummy answer in between_quadratic_functions"
            latex_problem = "dummy problem in between_quadratic_functions"
        elif problem_type == "between_cubic_functions":
            latex_answer = "dummy answer in between_cubic_functions"
            latex_problem = "dummy problem in between_cubic_functions"
        return latex_answer, latex_problem