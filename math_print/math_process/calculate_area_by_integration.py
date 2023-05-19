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

5/16
    引き算のきちんとした表示
        おおむねok
    次は別のパターン(二次関数と直線)
        多分ok
    次の次は2次関数間
    
5/17
    一部計算がガバ
        具体的には1次の係数が怪しい
            初めに制定した2次関数のcoeffの扱いが怪しい
                expandで解決

5/18
    上下関係が怪しい
        そもそも正負で分けるという発想がおかしい？
            a1=3, a2=5, a=a1-a2=-2でも普通に成立する
    とりあえず2次関数と2次関数の面積は仮に作成完了
        まだチェックが終わってない
    あと、直線側と2次関数側で、直線側がy=k、つまり一次の係数が0になっているケースがある
        こちらも要チェックアンド修正
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
            # between quadratic function and x-axis
            if random() > 0.5:
                quadratic_coefficient = self._random_integer(remove_zero=True)
                answer1 = self._random_integer(min_num=-3, max_num=3)
                answer2 = answer1 + self._random_integer(min_num=-3, max_num=3, remove_zero=True)
                if answer1 > answer2:
                    bigger_answer, smaller_answer = answer1, answer2
                elif answer1 < answer2:
                    bigger_answer, smaller_answer = answer2, answer1
                quadratic_function = sy.expand(quadratic_coefficient * (x - smaller_answer) * (x - bigger_answer))
                latex_problem = f"\\( y = {sy.latex(quadratic_function)} \\)"\
                    "と\\( x \\)軸で囲まれた部分の面積を求めよ。"
                area = abs(quadratic_coefficient) * sy.Rational(1, 6) * (bigger_answer - smaller_answer) ** 3
                latex_answer = f"\\( {sy.latex(quadratic_function)} \\)"\
                    f"\\( = {sy.latex(sy.factor(quadratic_function))}\\)となる。 \n"\
                    f"そのため、2次関数と\\( x \\)軸との交点は、\\( x = {sy.latex(smaller_answer)}, {sy.latex(bigger_answer)} \\)である。\n"\
                    "よって、2次関数と\\( x \\)軸で囲まれた面積は、\n"
                if quadratic_coefficient > 0:
                    quadratic_function_for_integration = 0 - quadratic_function
                else:
                    quadratic_function_for_integration = quadratic_function - 0
                latex_answer += f"\\( \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} ({sy.latex(quadratic_function_for_integration)}) dx\\)"
                divided_quadratic_function = sy.factor(quadratic_function_for_integration / quadratic_coefficient)
                if quadratic_coefficient == 1:
                    latex_answer += f"\\( = \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} {sy.latex(divided_quadratic_function)} dx\\)\n"
                elif quadratic_coefficient == -1:
                    latex_answer += f"\\( = - \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} {sy.latex(divided_quadratic_function)} dx\\)\n"
                else:
                    latex_answer += f"\\( = {sy.latex(quadratic_coefficient)} \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} {sy.latex(divided_quadratic_function)} dx\\)\n"
                if smaller_answer >= 0:
                    latex_answer += f"\\( = {-1 * abs(quadratic_coefficient)} \\cdot (-\\frac{{1}}{{6}}) ({bigger_answer} - {smaller_answer})^3\\)"
                else:
                    if bigger_answer >= 0:
                        latex_answer += f"\\( = {-1 * abs(quadratic_coefficient)} \\cdot (-\\frac{{1}}{{6}}) \\lbrace {bigger_answer} - ({smaller_answer}) \\rbrace ^3 \\) "
                    else:
                        latex_answer += f"\\( = {-1 * abs(quadratic_coefficient)} \\cdot (-\\frac{{1}}{{6}}) \\lbrace ({bigger_answer}) - ({smaller_answer}) \\rbrace ^3 \\) "
                latex_answer += f"\\( = {sy.latex(area)} \\)"
                # latex_answer = f"\\(\\lbrace  5 - 3 \\rbrace \\)"
            else:
                answer1 = self._random_integer(min_num=-3, max_num=3)
                answer2 = answer1 + self._random_integer(min_num=-3, max_num=3, remove_zero=True)
                if answer1 > answer2:
                    bigger_answer, smaller_answer = answer1, answer2
                elif answer1 < answer2:
                    bigger_answer, smaller_answer = answer2, answer1
                quadratic_coefficient = self._random_integer(min_num=-3, max_num=3, remove_zero=True)
                if quadratic_coefficient > 0:
                    quadratic_function_after_subtraction = sy.expand(-quadratic_coefficient * (x - smaller_answer) * (x - bigger_answer))
                elif quadratic_coefficient < 0:
                    quadratic_function_after_subtraction = sy.expand(quadratic_coefficient * (x - smaller_answer) * (x - bigger_answer))
                linear_coefficient_after_subtraction = quadratic_function_after_subtraction.coeff(x, 1)
                constant_term_after_subtraction = quadratic_function_after_subtraction.coeff(x, 0)
                linear_coefficient_of_quadratic_function = self._random_integer()
                constant_term_of_quadratic_function = self._random_integer()
                quadratic_function = quadratic_coefficient * x ** 2 + linear_coefficient_of_quadratic_function * x + constant_term_of_quadratic_function
                if quadratic_coefficient > 0:
                    linear_coefficient_of_linear_function = linear_coefficient_of_quadratic_function + linear_coefficient_after_subtraction
                    constant_term_of_linear_function = constant_term_of_quadratic_function + constant_term_after_subtraction
                elif quadratic_coefficient < 0:
                    linear_coefficient_of_linear_function = linear_coefficient_of_quadratic_function - linear_coefficient_after_subtraction
                    constant_term_of_linear_function = constant_term_of_quadratic_function - constant_term_after_subtraction
                linear_function = linear_coefficient_of_linear_function * x + constant_term_of_linear_function
                latex_problem = f"\\( y = {sy.latex(sy.expand(quadratic_function))} \\)"\
                    f"と\\( y = {sy.latex(sy.expand(linear_function))} \\)で囲まれた部分の面積を求めよ。"
                area = abs(quadratic_coefficient) * sy.Rational(1, 6) * (bigger_answer - smaller_answer) ** 3
                latex_answer = "今、2次関数と直線は、"
                if quadratic_coefficient > 0:
                    latex_answer += "直線の方が上にある。\n"
                    latex_answer += f"また、その交点は、\n \\( ({sy.latex(linear_function)}) - ({sy.latex(quadratic_function)}) = 0\\)\n"
                elif quadratic_coefficient < 0:
                    latex_answer += "2次関数の方が上にある。\n"
                    latex_answer += f"また、その交点は、\n \\( ({sy.latex(quadratic_function)}) - ({sy.latex(linear_function)}) = 0\\)\n"
                latex_answer += f"\\( {sy.latex(sy.expand(quadratic_function_after_subtraction))} = 0\\)\n"
                latex_answer += f"\\( {sy.latex(sy.factor(quadratic_function_after_subtraction))} = 0\\)\n"
                latex_answer += f"より、\\( x = {sy.latex(smaller_answer)}, {sy.latex(bigger_answer)} \\)である。\n"
                latex_answer += "そのため、2次関数と直線で囲まれた面積は、\n"
                latex_answer += f"\\( \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} {sy.latex(sy.factor(quadratic_function_after_subtraction))}\\)\n"
                # coefficient_before_integration = quadratic_function_after_subtraction.coeff(x, 2)
                divided_quadratic_function_after_subtraction = quadratic_function_after_subtraction * sy.Rational(1, quadratic_coefficient)
                latex_answer += f"\\( = {sy.latex(quadratic_coefficient)} \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} {sy.latex(sy.factor(divided_quadratic_function_after_subtraction))} \\)\n"
                if smaller_answer > 0:
                    latex_answer += f"\\( = {sy.latex(quadratic_coefficient)} \\cdot (-\\frac{{1}}{{6}}) ({bigger_answer} - {smaller_answer})^3\\)"
                else:
                    if bigger_answer >= 0:
                        latex_answer += f"\\( = {sy.latex(quadratic_coefficient)} \\cdot (-\\frac{{1}}{{6}}) \\lbrace {bigger_answer} - ({smaller_answer}) \\rbrace ^3\\)\n"
                    else:
                        latex_answer += f"\\( = {sy.latex(quadratic_coefficient)} \\cdot (-\\frac{{1}}{{6}}) \\lbrace ({bigger_answer}) - ({smaller_answer}) \\rbrace ^3\\)\n"
                latex_answer += f"\\( = {sy.latex(area)} \\)"
        elif problem_type == "between_quadratic_functions":
            ## ax^2 + bx + c = (a1x^2 + b1x+ c1) - (a2x^2 + b2x + c2), a<0
            a = self._random_integer(min_num=-3, max_num=-1, remove_zero=True)
            answer1 = self._random_integer(min_num=-3, max_num=3)
            answer2 = answer1 + self._random_integer(min_num=-3, max_num=3, remove_zero=True)
            if answer1 > answer2:
                bigger_answer, smaller_answer = answer1, answer2
            elif answer1 < answer2:
                bigger_answer, smaller_answer = answer2, answer1
            quadratic_function_after_subtraction = sy.expand(a * (x - smaller_answer) * (x - bigger_answer))
            b = quadratic_function_after_subtraction.coeff(x, 1)
            c = quadratic_function_after_subtraction.coeff(x, 0)
            # a1x^2 + b1x + c1
            a1 = a + self._random_integer(min_num=-3, max_num=3, remove_zero=True)
            b1 = self._random_integer(min_num=-3, max_num=3)
            c1 = self._random_integer(min_num=-3, max_num=3)
            upper_quadratic_function = a1 * x ** 2 + b1 * x + c1
            # a2x^2 + b2x + c2 (to become 'a = a1 - a2', 'b = b1 - b2', 'c = c1 - c2')
            a2 = a1 - a
            b2 = b1 - b
            c2 = c1 - c
            lower_quadratic_function = a2 * x ** 2 + b2 * x + c2
            if random() > 0.5:
                latex_problem = f"\\( y = {sy.latex(sy.expand(upper_quadratic_function))}\\)"\
                    f"と\\( y = {sy.latex(sy.expand(lower_quadratic_function))} \\)で囲まれた部分の面積を求めよ。"
            else:
                latex_problem = f"\\( y = {sy.latex(sy.expand(lower_quadratic_function))}\\)"\
                    f"と\\( y = {sy.latex(sy.expand(upper_quadratic_function))} \\)で囲まれた部分の面積を求めよ。"
            area = abs(a) * sy.Rational(1, 6) * (bigger_answer - smaller_answer) ** 3
            latex_answer = f"今、2次関数のうち、\\( y = {sy.latex(sy.expand(upper_quadratic_function))} \\)が上、"
            latex_answer += f"\\( y = {sy.latex(sy.expand(lower_quadratic_function))} \\)が下にある。"
            latex_answer += "また、その交点は、\n"
            latex_answer += f"\\( ({sy.latex(sy.expand(upper_quadratic_function))}) - ({sy.latex(sy.expand(lower_quadratic_function))}) = 0\\)\n"
            latex_answer += f"\\( {sy.latex(sy.expand(quadratic_function_after_subtraction))} = 0 \\)\n"
            latex_answer += f"\\( {sy.latex(sy.factor(quadratic_function_after_subtraction))} = 0\\)\n"
            latex_answer += f"より、\\( x = {sy.latex(smaller_answer)}, {sy.latex(bigger_answer)} \\)である。\n"
            latex_answer += f"そのため、2次関数と直線で囲まれた面積は、\n"
            latex_answer += f"\\( \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} {sy.latex(sy.factor(quadratic_function_after_subtraction))} \\)\n"
            divided_quadratic_function_after_subtraction = quadratic_function_after_subtraction * sy.Rational(1, a)
            latex_answer += f"\\( = {sy.latex(a)} \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} {sy.latex(sy.factor(divided_quadratic_function_after_subtraction))} \\)\n"
            if smaller_answer > 0:
                latex_answer += f"\\( = {sy.latex(a)} \\cdot (-\\frac{{1}}{{6}}) ({bigger_answer} - {smaller_answer})^3\\)"
            else:
                if bigger_answer >= 0:
                    latex_answer += f"\\( = {sy.latex(a)} \\cdot (-\\frac{{1}}{{6}}) \\lbrace {bigger_answer} - ({smaller_answer}) \\rbrace ^3\\)\n"
                else:
                    latex_answer += f"\\( = {sy.latex(a)} \\cdot (-\\frac{{1}}{{6}}) \\lbrace ({bigger_answer}) - ({smaller_answer}) \\rbrace ^3\\)\n"
            latex_answer += f"\\( = {sy.latex(area)} \\)"
        elif problem_type == "between_cubic_functions":
            latex_answer = "dummy answer in between_cubic_functions"
            latex_problem = "dummy problem in between_cubic_functions"
        return latex_answer, latex_problem
    
    def _random_integer(self, min_num: int=-5, max_num: int=5, *, remove_zero: bool=False) -> sy.Integer:
        """指定された条件と範囲でランダムな整数を出力
        
        Args:
            min_num (int, optional): 最小値
            max_num (int, optional): 最大値
            remove_zero(bool, optional): 返す値に0が入るか
        
        Return:
            integer (sy.Integer): sympyで計算に用いられる整数
        """
        integer = randint(min_num, max_num)
        if (integer == 0) and (remove_zero == True):
            if random() > 0.5:
                integer +=  randint(1, max_num)
            else:
                integer += randint(min_num, -1)
        return sy.Integer(integer)