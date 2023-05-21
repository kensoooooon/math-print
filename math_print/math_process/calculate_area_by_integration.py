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

5/19
    おおむね修正終わり。
    2次関数でy=kが登場する
        わりと終わり
    上下関係の示し方が少し怪しい？
        不等式で示す？

5/20
    上下の示し方について追加
        f(x) > g(x)....でカウントする？
        示し方はいくらか考えられるが、印刷したときの表示エリアなんかも踏まえると、絶対必須というわけでもなさそう
        とりあえず追加しとく
            2次関数とx軸には追加完了。とりあえずよさげ？何もないよりは        
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
            # between quadratic function and x-axis(y = ax^2 + bx + c, y = 0)
            if random() > 0.5:
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
                if random() > 0.5:
                    quadratic_function = quadratic_function_after_subtraction
                else:
                    quadratic_function = -1 * quadratic_function_after_subtraction
                latex_problem = f"\\( y = {sy.latex(quadratic_function)} \\)と\\( x \\)軸で囲まれた部分の面積を求めよ。"
                area = abs(a) * sy.Rational(1, 6) * (bigger_answer - smaller_answer) ** 3
                a1 = quadratic_function.coeff(x, 2)
                latex_answer = f"まず、\\( x \\)軸と2次関数の関係を確認するために、"
                latex_answer += f"\\( {sy.latex(sy.expand(quadratic_function))} \\geqq 0\\)を解くと、\n"
                if a1 > 0:
                    latex_answer += f"\\( {sy.latex(sy.factor(quadratic_function))} \\geqq 0\\)\n"
                    latex_answer += f"\\( {sy.latex(sy.factor(quadratic_function * sy.Rational(1, a1)))} \\geqq 0\\)\n"
                    latex_answer += f"\\( x \\leqq {sy.latex(smaller_answer)}, {sy.latex(bigger_answer)} \\leqq x\\)\n"
                elif a1 < 0:
                    latex_answer += f"\\( {sy.latex(sy.factor(quadratic_function))} \\geqq 0\\)\n"
                    latex_answer += f"\\( {sy.latex(sy.factor(quadratic_function * sy.Rational(1, a1)))} \\leqq 0\\)\n"
                    latex_answer += f"\\( {sy.latex(smaller_answer)} \\leqq x \\leqq {sy.latex(bigger_answer)} \\)\n"
                latex_answer += f"となるため、2次関数と\\( x \\)軸で囲まれた面積は、\\( {sy.latex(smaller_answer)} \\leqq x \\leqq {sy.latex(bigger_answer)}\\)の範囲にある。\n"
                latex_answer += "また、その範囲において、2次関数と\\( x \\)軸の位置関係は、"
                if a1 > 0:
                    latex_answer += "\\( x \\)軸の方が上にある。\n"
                elif a1 < 0:
                    latex_answer += f"\\( x \\)軸の方が下にある。\n"
                latex_answer += f"よって、2次関数と\\( x \\)軸で囲まれた面積は、\n"
                latex_answer += f"\\( \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} ({sy.latex(sy.expand(quadratic_function_after_subtraction))}) dx\\)\n"
                latex_answer += f"\\( = \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} {sy.latex(sy.factor(quadratic_function_after_subtraction))} dx\\)\n"
                divided_quadratic_function_after_subtraction = quadratic_function_after_subtraction * sy.Rational(1, a)
                if a == -1:
                    latex_answer += f"\\( = - \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} {sy.latex(sy.factor(divided_quadratic_function_after_subtraction))} dx\\)\n"
                else:
                    latex_answer += f"\\( = {sy.latex(a)} \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} {sy.latex(sy.factor(divided_quadratic_function_after_subtraction))} dx\\)\n"
                if smaller_answer >= 0:
                    latex_answer += f"\\( = {sy.latex(a)} \\cdot (-\\frac{{1}}{{6}}) ({bigger_answer} - {smaller_answer})^3\\)"
                else:
                    if bigger_answer >= 0:
                        latex_answer += f"\\( = {sy.latex(a)} \\cdot (-\\frac{{1}}{{6}}) \\lbrace {bigger_answer} - ({smaller_answer}) \\rbrace ^3 \\) "
                    else:
                        latex_answer += f"\\( = {sy.latex(a)} \\cdot (-\\frac{{1}}{{6}}) \\lbrace ({bigger_answer}) - ({smaller_answer}) \\rbrace ^3 \\) "
                latex_answer += f"\\( = {sy.latex(area)} \\)"
            # between quadratic function and line(y = ax^2 + bx + c, y = mx + n)
            else:
                answer1 = self._random_integer(min_num=-3, max_num=3)
                answer2 = answer1 + self._random_integer(min_num=-3, max_num=3, remove_zero=True)
                if answer1 > answer2:
                    bigger_answer, smaller_answer = answer1, answer2
                elif answer1 < answer2:
                    bigger_answer, smaller_answer = answer2, answer1
                a = self._random_integer(min_num=-3, max_num=-1, remove_zero=True)
                quadratic_function_after_subtraction = sy.expand(a * (x - smaller_answer) * (x - bigger_answer))
                b = quadratic_function_after_subtraction.coeff(x, 1)
                c = quadratic_function_after_subtraction.coeff(x, 0)
                # a1 > 0
                if random() > 0.5:
                    a1 = -a
                else:
                    a1 = a
                # prevent not to be b1 == 0
                b1 = b + self._random_integer(remove_zero=False)
                c1 = self._random_integer(remove_zero=False)
                quadratic_function = a1 * x ** 2 + b1 * x + c1
                if a1 > 0:
                    m = b1 + b
                    n = c1 + c
                elif a1 < 0:
                    m = b1 - b
                    n = c1 - c
                linear_function = m * x + n
                latex_problem = f"\\( y = {sy.latex(sy.expand(quadratic_function))} \\)"\
                    f"と\\( y = {sy.latex(sy.expand(linear_function))} \\)で囲まれた部分の面積を求めよ。"
                area = abs(a) * sy.Rational(1, 6) * (bigger_answer - smaller_answer) ** 3
                latex_answer = "まず、 2次関数と直線の位置関係を確認するために、"
                latex_answer += f"\\( {sy.latex(sy.expand(quadratic_function))} \\geqq {sy.latex(sy.expand(linear_function))} \\)を解くと、\n"
                quadratic_function_for_display = quadratic_function - linear_function
                if a1 > 0:
                    latex_answer += f"\\( {sy.latex(sy.expand(quadratic_function_for_display))} \\geqq 0 \\)\n"
                    latex_answer += f"\\( {sy.latex(sy.factor(quadratic_function_for_display))} \\geqq 0 \\)\n"
                    latex_answer += f"\\( {sy.latex(sy.factor(quadratic_function_for_display * sy.Rational(1, a1)))} \\geqq 0 \\)\n"
                    latex_answer += f"\\( x \\leqq {sy.latex(smaller_answer)}, {sy.latex(bigger_answer)} \\leqq x \\)\n"
                elif a1 < 0:
                    latex_answer += f"\\( {sy.latex(sy.expand(quadratic_function_for_display))} \\geqq 0 \\)\n"
                    latex_answer += f"\\( {sy.latex(sy.factor(quadratic_function_for_display))} \\geqq 0 \\)\n"
                    latex_answer += f"\\( {sy.latex(sy.factor(quadratic_function_for_display * sy.Rational(1, a1)))} \\leqq 0 \\)\n"
                    latex_answer += f"\\( {sy.latex(smaller_answer)} \\leqq x \\leqq {sy.latex(bigger_answer)} \\)\n"
                latex_answer += f"となるため、2次関数と直線で囲まれた面積は、\\( {sy.latex(smaller_answer)} \\leqq x \\leqq {sy.latex(bigger_answer)} \\)の範囲にある。\n"
                latex_answer += "また、その範囲において、2次関数と直線の位置関係は、"
                if a1 > 0:
                    latex_answer += "直線の方が上にある。\n"
                elif a1 < 0:
                    latex_answer += "2次関数のほうが上にある。\n"
                latex_answer += "よって、2次関数と直線で囲まれた面積は、\n"
                latex_answer += f"\\( \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} ({sy.latex(sy.expand(quadratic_function_after_subtraction))}) dx \\)\n"
                latex_answer += f"\\( = \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} {sy.latex(sy.factor(quadratic_function_after_subtraction))} dx \\)\n"
                divided_quadratic_function_after_subtraction = quadratic_function_after_subtraction * sy.Rational(1, a)
                if a == -1:
                    latex_answer += f"\\( = - \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} {sy.latex(sy.factor(divided_quadratic_function_after_subtraction))} dx \\)\n"
                else:
                    latex_answer += f"\\( = {sy.latex(a)} \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} {sy.latex(sy.factor(divided_quadratic_function_after_subtraction))} dx \\)\n"
                if smaller_answer > 0:
                    latex_answer += f"\\( = {sy.latex(a)} \\cdot (-\\frac{{1}}{{6}}) ({bigger_answer} - {smaller_answer})^3\\)"
                else:
                    if bigger_answer >= 0:
                        latex_answer += f"\\( = {sy.latex(a)} \\cdot (-\\frac{{1}}{{6}}) \\lbrace {bigger_answer} - ({smaller_answer}) \\rbrace ^3\\)\n"
                    else:
                        latex_answer += f"\\( = {sy.latex(a)} \\cdot (-\\frac{{1}}{{6}}) \\lbrace ({bigger_answer}) - ({smaller_answer}) \\rbrace ^3\\)\n"
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
            # a1 == 0 and a != 0
            if a1 == 0:
                a1 = self._random_integer(min_num=1, max_num=3)
            b1 = self._random_integer(min_num=-3, max_num=3)
            c1 = self._random_integer(min_num=-3, max_num=3)
            upper_quadratic_function = a1 * x ** 2 + b1 * x + c1
            # a2x^2 + b2x + c2 (to become 'a = a1 - a2', 'b = b1 - b2', 'c = c1 - c2')
            a2 = a1 - a
            b2 = b1 - b
            c2 = c1 - c
            lower_quadratic_function = a2 * x ** 2 + b2 * x + c2
            area = abs(a) * sy.Rational(1, 6) * (bigger_answer - smaller_answer) ** 3
            display_mode = choice(["upper_is_first", "lower_is_first"])
            if display_mode == "upper_is_first":
                first_display_quadratic_function = sy.expand(upper_quadratic_function)
                second_display_quadratic_function = sy.expand(lower_quadratic_function)
            elif display_mode == "lower_is_first":
                first_display_quadratic_function = sy.expand(lower_quadratic_function)
                second_display_quadratic_function = sy.expand(upper_quadratic_function)
            latex_problem = f"\\( y = {sy.latex(first_display_quadratic_function)}\\)"\
                    f"と\\( y = {sy.latex(sy.expand(second_display_quadratic_function))} \\)で囲まれた部分の面積を求めよ。"
            # new added part describe which is upper
            latex_answer = "まず、2次関数同士の位置関係を確認するために、"
            if display_mode == "upper_is_first":
                latex_answer += f"\\( {sy.latex(sy.expand(upper_quadratic_function))} \\geqq {sy.latex(sy.expand(lower_quadratic_function))} \\)を解くと、\n"
                quadratic_function_for_display = upper_quadratic_function - lower_quadratic_function
                latex_answer += f"\\( {sy.latex(sy.expand(quadratic_function_for_display))} \\geqq 0 \\)\n"
                factored_quadratic_function_display = sy.factor(quadratic_function_for_display)
                latex_answer += f"\\( {sy.latex(factored_quadratic_function_display)} \\geqq 0 \\)\n"
                quadratic_coefficient = sy.expand(factored_quadratic_function_display).coeff(x, 2)
                divided_and_factored_quadratic_function_for_display = factored_quadratic_function_display * sy.Rational(1, quadratic_coefficient)
                latex_answer += f"\\( {sy.latex(divided_and_factored_quadratic_function_for_display)} \\leqq 0 \\)\n"
                latex_answer += f"\\( {sy.latex(smaller_answer)} \\leqq x \\leqq {sy.latex(bigger_answer)} \\)\n"
            elif display_mode == "lower_is_first":
                latex_answer += f"\\( {sy.latex(sy.expand(lower_quadratic_function))} \\geqq {sy.latex(sy.expand(upper_quadratic_function))} \\)を解くと、\n"
                quadratic_function_for_display = lower_quadratic_function - upper_quadratic_function
                latex_answer += f"\\( {sy.latex(sy.expand(quadratic_function_for_display))} \\geqq 0 \\)\n"
                factored_quadratic_function_display = sy.factor(quadratic_function_for_display)
                latex_answer += f"\\( {sy.latex(factored_quadratic_function_display)} \\geqq 0 \\)\n"
                quadratic_coefficient = sy.expand(factored_quadratic_function_display).coeff(x, 2)
                divided_and_factored_quadratic_function_for_display = factored_quadratic_function_display * sy.Rational(1, quadratic_coefficient)
                latex_answer += f"\\( {sy.latex(divided_and_factored_quadratic_function_for_display)} \\geqq 0 \\)\n"
                latex_answer += f"\\( x \\leqq {sy.latex(smaller_answer)}, {sy.latex(bigger_answer)} \\leqq x \\)\n"
            latex_answer += f"となるため、2次関数同士で囲まれた面積は、\\( {sy.latex(smaller_answer)} \\leqq x \\leqq {sy.latex(bigger_answer)} \\)の範囲にある。\n"
            latex_answer += "また、その範囲において、2次関数同士の位置関係は、"
            latex_answer += f"\\( y = {sy.latex(sy.expand(upper_quadratic_function))} \\)が上、\\( y = {sy.latex(sy.expand(lower_quadratic_function))} \\)が下にある。\n"
            latex_answer += f"よって、2つの2次関数で囲まれた面積は、\n"
            latex_answer += f"\\( \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} ({sy.latex(sy.expand(quadratic_function_after_subtraction))}) dx \\)\n"
            latex_answer += f"\\( = \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} {sy.latex(sy.factor(quadratic_function_after_subtraction))} dx \\)\n"
            divided_quadratic_function_after_subtraction = quadratic_function_after_subtraction * sy.Rational(1, a)
            if a == -1:
                latex_answer += f"\\( = - \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} {sy.latex(sy.factor(divided_quadratic_function_after_subtraction))} dx \\)\n"
            else:
                latex_answer += f"\\( = {sy.latex(a)} \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} {sy.latex(sy.factor(divided_quadratic_function_after_subtraction))} dx \\)\n"
            # bigger_answer > 0
            if smaller_answer > 0:
                latex_answer += f"\\( = {sy.latex(a)} \\cdot (-\\frac{{1}}{{6}}) ({bigger_answer} - {smaller_answer})^3\\)"
            # bigger_answer > 0 or < 0
            elif smaller_answer < 0:
                if bigger_answer > 0:
                    latex_answer += f"\\( = {sy.latex(a)} \\cdot (-\\frac{{1}}{{6}}) \\lbrace {bigger_answer} - ({smaller_answer}) \\rbrace ^3\\)\n"
                elif bigger_answer < 0:
                    latex_answer += f"\\( = {sy.latex(a)} \\cdot (-\\frac{{1}}{{6}}) \\lbrace ({bigger_answer}) - ({smaller_answer}) \\rbrace ^3\\)\n"
                elif bigger_answer == 0:
                    latex_answer += f"\\( = {sy.latex(a)} \\cdot (-\\frac{{1}}{{6}}) \\lbrace {bigger_answer} - ({smaller_answer}) \\rbrace ^3\\)\n"
            # bigger_answer > 0
            elif smaller_answer == 0:
                latex_answer += f"\\( = {sy.latex(a)} \\cdot (-\\frac{{1}}{{6}}) ({bigger_answer} - {smaller_answer}) ^3\\)\n"
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
