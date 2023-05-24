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

5/22
    追加説明は一通り。次は3次関数間

5/23
    引き続き3次関数間
        ひとまず作成完了
    あとは出題の選択肢をもっと細かくとって、解説と続きの問題を追加

5/24
    1/3公式に着手
        とりあえずガワは整えた
        まずは2次関数と接線、およびy軸に平行な直線の間の面積
            微分等の計算は確認したが、接点のx座標と、x=kのkの大小関係を縛るべきか否かが不明
                まず等しいのはそもそも囲めないのでアウツ
                問題は、「左側にできようが右側にできようが、結局同じ計算方法でいけるのか？」という点
                    手計算してみる系か~
"""
from random import choice, random, randint
from typing import Dict, Tuple


import sympy as sy


class CalculateAreaByIntegration:
    """積分の公式を用いて面積を求める問題と解答を出力
    
    Attributes:
        latex_answer (str): latex形式と通常の文字が混在した解答
        latex_problem (str): latex形式と通常の文字が混在した問題
    """
    def __init__(self, **settings: Dict) -> None:
        """初期設定
        
        Args:
            settings (dict): 問題を決定する各種設定を格納

        Raises:
            ValueError: 想定されていない問題のタイプが混入したときに挙上
        """
        sy.init_printing(order="grevlex")
        problem_type = choice(settings["problem_types"])
        if (problem_type == "between_quadratic_function_and_x_axis") or (problem_type == "between_quadratic_function_and_line") or (problem_type == "between_quadratic_functions") or (problem_type == "between_cubic_functions"):
            self.latex_answer, self.latex_problem = self._make_one_sixth_problem(problem_type)
        elif (problem_type == "between_quadratic_function_and_tangent_and_parallel_line_with_y_axis") or (problem_type == "between_two_quadratic_functions_that_touch_each_other_and_parallel_line_with_y_axis"):
            self.latex_answer, self.latex_problem = self._make_one_third_problem(problem_type)
        else:
            raise ValueError(f"'problem_type' is {problem_type}. This isn't expected value. Please check {settings['problem_types']}.")
    
    def _make_one_sixth_problem(self, problem_type: str) -> Tuple[str, str]:
        """1/6公式を利用する問題と解答を出力
        
        Args:
            problem_type (str): 1/6公式を使う問題のうち、選択されたもの
        
        Returns:
            latex_answer (str): latex形式と通常の文字が混在した解答
            latex_problem (str): latex形式と通常の文字が混在した問題
            
        
        Raises:
            ValueError: 1/6公式を利用する問題として想定されていないものが指定されたときに挙上
        
        Note:
            2次関数と直線の間の面積、2つの2次関数の間の面積、3次の係数が等しい3次関数の3種を実装
        """
        x = sy.Symbol("x", real=True)
        # between quadratic function and x-axis(y = ax^2 + bx + c, y = 0)
        if problem_type == "between_quadratic_function_and_x_axis":
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
                latex_answer += f"\\( = {sy.latex(a)} \\cdot (-\\frac{{1}}{{6}}) ({bigger_answer} - {smaller_answer})^3 \\)\n"
            else:
                if bigger_answer >= 0:
                    latex_answer += f"\\( = {sy.latex(a)} \\cdot (-\\frac{{1}}{{6}}) \\lbrace {bigger_answer} - ({smaller_answer}) \\rbrace ^3 \\)\n"
                else:
                    latex_answer += f"\\( = {sy.latex(a)} \\cdot (-\\frac{{1}}{{6}}) \\lbrace ({bigger_answer}) - ({smaller_answer}) \\rbrace ^3 \\)\n"
            latex_answer += f"\\( = {sy.latex(area)} \\)"
        # between quadratic function and line(y = ax^2 + bx + c, y = mx + n)
        elif problem_type == "between_quadratic_function_and_line":
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
        # ax^2 + bx + c = (a1x^2 + b1x+ c1) - (a2x^2 + b2x + c2), a<0
        elif problem_type == "between_quadratic_functions":
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
                factored_quadratic_function_for_display = sy.factor(quadratic_function_for_display)
                latex_answer += f"\\( {sy.latex(factored_quadratic_function_for_display)} \\geqq 0 \\)\n"
                quadratic_coefficient = sy.expand(factored_quadratic_function_for_display).coeff(x, 2)
                divided_and_factored_quadratic_function_for_display = factored_quadratic_function_for_display * sy.Rational(1, quadratic_coefficient)
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
        # (ax^3+b1x^2+c1x+d1) - (ax^3+b2x^2+c2x+d2) = b(x-a)(x-b) = bx^2 + cx + d
        elif problem_type == "between_cubic_functions":
            b = self._random_integer(min_num=-3, max_num=-1, remove_zero=True)
            answer1 = self._random_integer(min_num=-3, max_num=3)
            answer2 = answer1 + self._random_integer(min_num=-3, max_num=3, remove_zero=True)
            if answer1 > answer2:
                bigger_answer, smaller_answer = answer1, answer2
            elif answer1 < answer2:
                bigger_answer, smaller_answer = answer2, answer1
            quadratic_function_after_subtraction = sy.expand(b * (x - smaller_answer) * (x - bigger_answer))
            c = quadratic_function_after_subtraction.coeff(x, 1)
            d = quadratic_function_after_subtraction.coeff(x, 0)
            # ax^3 + b1x^2 + c1x + d1
            a = self._random_integer(min_num=-3, max_num=3, remove_zero=True)
            b1 = self._random_integer(min_num=-3, max_num=3)
            c1 = self._random_integer(min_num=-3, max_num=3)
            d1 = self._random_integer(min_num=-3, max_num=3)
            upper_cubic_function = a * x ** 3 + b1 * x ** 2 + c1 * x + d1
            # ax^3 + b2x^2 + c2x + d2
            b2 = b1 - b
            c2 = c1 - c
            d2 = d1 - d
            lower_cubic_function = a * x ** 3 + b2 * x ** 2 + c2 * x + d2
            area = abs(b) * sy.Rational(1, 6) * (bigger_answer - smaller_answer) ** 3
            display_mode = choice(["upper_is_first", "lower_is_first"])
            if display_mode == "upper_is_first":
                first_display_cubic_function = sy.expand(upper_cubic_function)
                second_display_cubic_function = sy.expand(lower_cubic_function)
            elif display_mode == "lower_is_first":
                first_display_cubic_function = sy.expand(lower_cubic_function)
                second_display_cubic_function = sy.expand(upper_cubic_function)
            latex_problem = f"\\( y = {sy.latex(first_display_cubic_function)} \\)と"
            latex_problem += f"\\( y = {sy.latex(second_display_cubic_function)} \\)で囲まれた部分の面積を求めよ。"
            latex_answer = "まず、3次関数同士の位置関係を確認するために、"
            if display_mode == "upper_is_first":
                latex_answer += f"\\( {sy.latex(sy.expand(upper_cubic_function))} \\geqq {sy.latex(sy.expand(lower_cubic_function))} \\)を解くと、\n"
                quadratic_function_for_display = upper_cubic_function - lower_cubic_function
                latex_answer += f"\\( {sy.latex(sy.expand(quadratic_function_for_display))} \\geqq 0 \\)\n"
                factored_quadratic_function_for_display = sy.factor(quadratic_function_for_display)
                latex_answer += f"\\( {sy.latex(factored_quadratic_function_for_display)} \\geqq 0\\)\n"
                quadratic_coefficient = sy.expand(factored_quadratic_function_for_display).coeff(x, 2)
                divided_and_factored_quadratic_function_for_display = factored_quadratic_function_for_display * sy.Rational(1, quadratic_coefficient)
                latex_answer += f"\\( {sy.latex(divided_and_factored_quadratic_function_for_display)} \\leqq 0 \\)\n"
                latex_answer += f"\\( {sy.latex(smaller_answer)} \\leqq x \\leqq {sy.latex(bigger_answer)} \\)\n"
            elif display_mode == "lower_is_first":
                latex_answer += f"\\( {sy.latex(sy.expand(lower_cubic_function))} \\geqq {sy.latex(sy.expand(upper_cubic_function))} \\)を解くと、\n"
                quadratic_function_for_display = lower_cubic_function - upper_cubic_function
                latex_answer += f"\\( {sy.latex(sy.expand(quadratic_function_for_display))} \\geqq 0 \\)\n"
                factored_quadratic_function_for_display = sy.factor(quadratic_function_for_display)
                latex_answer += f"\\( {sy.latex(factored_quadratic_function_for_display)} \\geqq 0 \\)\n"
                quadratic_coefficient = sy.expand(factored_quadratic_function_for_display).coeff(x, 2)
                divided_and_factored_quadratic_function_for_display = factored_quadratic_function_for_display * sy.Rational(1, quadratic_coefficient)
                latex_answer += f"\\( {sy.latex(divided_and_factored_quadratic_function_for_display)} \\geqq 0 \\)\n"
                latex_answer += f"\\( x \\leqq {sy.latex(smaller_answer)}, {sy.latex(bigger_answer)} \\leqq x \\)\n"
            latex_answer += f"となるため、3次関数同士で囲まれた面積は、\\( {sy.latex(smaller_answer )} \\leqq x \\leqq {sy.latex(bigger_answer)} \\)の範囲にある。\n"
            latex_answer += "また、その範囲において、3次関数同士の位置関係は、"
            latex_answer += f"\\( y = {sy.latex(sy.expand(upper_cubic_function))} \\)が上、\\( y = {sy.latex(sy.expand(lower_cubic_function))} \\)が下にある。\n"
            latex_answer += "よって、2つの3次関数で囲まれた面積は、\n"
            latex_answer += f"\\( \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} ({sy.latex(sy.expand(quadratic_function_after_subtraction))}) dx \\)\n"
            latex_answer += f"\\( = \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} {sy.latex(sy.factor(quadratic_function_after_subtraction))} dx \\)\n"
            divided_quadratic_function_after_subtraction = quadratic_function_after_subtraction * sy.Rational(1, b)
            if b == -1:
                latex_answer += f"\\( = - \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} {sy.latex(sy.factor(divided_quadratic_function_after_subtraction))} dx \\)\n"
            else:
                latex_answer += f"\\( = {sy.latex(b)} \\int_{{{sy.latex(smaller_answer)}}}^{{{sy.latex(bigger_answer)}}} {sy.latex(sy.factor(divided_quadratic_function_after_subtraction))} dx \\)\n"
            # bigger_answer > 0
            if smaller_answer > 0:
                latex_answer += f"\\( = {sy.latex(b)} \\cdot (-\\frac{{1}}{{6}}) ({bigger_answer} - {smaller_answer})^3\\)"
            # bigger_answer > 0 or < 0
            elif smaller_answer < 0:
                if bigger_answer > 0:
                    latex_answer += f"\\( = {sy.latex(b)} \\cdot (-\\frac{{1}}{{6}}) \\lbrace {bigger_answer} - ({smaller_answer}) \\rbrace ^3\\)\n"
                elif bigger_answer < 0:
                    latex_answer += f"\\( = {sy.latex(b)} \\cdot (-\\frac{{1}}{{6}}) \\lbrace ({bigger_answer}) - ({smaller_answer}) \\rbrace ^3\\)\n"
                elif bigger_answer == 0:
                    latex_answer += f"\\( = {sy.latex(b)} \\cdot (-\\frac{{1}}{{6}}) \\lbrace {bigger_answer} - ({smaller_answer}) \\rbrace ^3\\)\n"
            # bigger_answer > 0
            elif smaller_answer == 0:
                latex_answer += f"\\( = {sy.latex(b)} \\cdot (-\\frac{{1}}{{6}}) ({bigger_answer} - {smaller_answer}) ^3\\)\n"
            latex_answer += f"\\( = {sy.latex(area)} \\)"
        else:
            raise ValueError(f"'problem_type' is {problem_type}. This isn't expected value.")
        return latex_answer, latex_problem
    
    def _make_one_third_problem(self, problem_type: str) -> Tuple[str, str]:
        """1/3公式を利用する問題と解答を出力
        
        Args:
            problem_type (str): 1/3公式を使う問題のうち、選択されたもの
        
        Returns:
            latex_answer (str): latex形式と通常の文字が混在した解答
            latex_problem (str): latex形式と通常の文字が混在した問題
            

        Raises:
            ValueError: 1/6公式を利用する問題として想定されていないものが指定されたときに挙上

        Note:
            2次関数とその接線、およびy軸に平行な直線の間の面積、2つの接する2次関数とy軸に平行な直線の間の面積を実装
        """
        x = sy.Symbol("x", real=True)
        # f(x) = ax^2 + bx + c, y = f'(a)(x-a) + y(a), y = k
        if problem_type == "between_quadratic_function_and_tangent_and_parallel_line_with_y_axis":
            """
            x = sy.Symbol("x", real=True)
            y1 = sy.Rational(1, 2) * x ** 2 - x + sy.Rational(1, 2)
            tx = 3
            ty = 2
            tangent_slope = sy.diff(y1).subs(x, tx)
            print(f"tangent_slope: {tangent_slope}")
            tangent = tangent_slope * (x - tx) + ty
            print(f"tangent: {tangent}")
            """
            a = self._random_integer(min_num=-3, max_num=3, remove_zero=True)
            b = self._random_integer()
            c = self._random_integer()
            quadratic_function = a * x ** 2 + b * x + c
            tangent_x = self._random_integer(min_num=-3, max_num=3)
            tangent_y = quadratic_function.subs(x, tangent_x)
            parallel_line_with_y_axis = tangent_x + self._random_integer(remove_zero=True)
            latex_problem = f"\\( y = {sy.latex(sy.expand(quadratic_function))} \\)と、"
            latex_problem += f"その上の点\\( ({sy.latex(tangent_x)}, {sy.latex(tangent_y)}) \\)における接線、\n"
            latex_problem += f"および \\( x = {sy.latex(parallel_line_with_y_axis)} \\)で囲まれた部分の面積を求めよ。"
            latex_answer = "まずは2次関数の接線を求める。\n"
            differentiated_quadratic_function = sy.diff(quadratic_function)
            tangent_slope = differentiated_quadratic_function.subs(x, tangent_x)
            tangent = tangent_slope * (x - tangent_x) + tangent_y
            latex_answer += f"\\( y' =  {sy.latex(sy.expand(differentiated_quadratic_function))} \\)より、\\( x = {sy.latex(tangent_x)} \\)における接線の傾きは、"
            latex_answer += f"\\( {sy.latex(tangent_slope)} \\)である。\n"
            latex_answer += f"よって、接点\\( ({sy.latex(tangent_x)}, {sy.latex(tangent_y)}) \\)における接線は、\n"
            if tangent_y > 0:
                latex_answer += f"\\( y = {sy.latex(tangent_slope)}({sy.latex(x - tangent_x)}) + {sy.latex(tangent_y)} = {sy.latex(sy.expand(tangent))} \\)である。"
            else:
                latex_answer += f"\\( y = {sy.latex(tangent_slope)}({sy.latex(x - tangent_x)}) {sy.latex(tangent_y)} = {sy.latex(sy.expand(tangent))} \\)である。"
        # f(x) = ax^2 + bx + c, y1 = f'(a)(x-a) + y(a), g(x) = ax^2 + bx + c, y2 = g'(a?) ..
        elif problem_type == "between_two_quadratic_functions_that_touch_each_other_and_parallel_line_with_y_axis":
            latex_problem = "dummy problem in between_two_quadratic_functions_that_touch_each_other_and_parallel_line_with_y_axis"
            latex_answer = "dummy answer in between_two_quadratic_functions_that_touch_each_other_and_parallel_line_with_y_axis"
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
