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

5/25
    引き続き作成。
        2次関数の接線の傾きがちょうど0になるタイミングがある
            問題の設定的に、ゼロにならないようにしておくべき
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
        elif (problem_type == "between_quadratic_function_and_tangent_and_parallel_line_with_y_axis") or (problem_type == "between_two_quadratic_functions_that_touch_each_other_and_parallel_line_with_y_axis") or (problem_type == "between_quadratic_function_and_two_tangents"):
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
            a = self._random_integer(min_num=-2, max_num=2, remove_zero=True)
            b = self._random_integer(min_num=-3, max_num=3)
            c = self._random_integer(min_num=-3, max_num=3)
            quadratic_function = a * x ** 2 + b * x + c
            differentiated_quadratic_function = sy.diff(quadratic_function)
            # new added part not to become tangent is 0.
            tangent_x_with_zero_slope = sy.solve(differentiated_quadratic_function)[0]
            tangent_x = self._random_integer(min_num=-3, max_num=3)
            if tangent_x == tangent_x_with_zero_slope:
                tangent_x += self._random_integer(min_num=-2, max_num=2, remove_zero=True)
            tangent_y = quadratic_function.subs(x, tangent_x)
            tangent_slope = differentiated_quadratic_function.subs(x, tangent_x)
            tangent = tangent_slope * (x - tangent_x) + tangent_y
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
            latex_answer += f"そのため、接点\\( ({sy.latex(tangent_x)}, {sy.latex(tangent_y)}) \\)における接線は、\n"
            if tangent_x == 0:
                if tangent_y == 0:
                    latex_answer += f"\\( y = {sy.latex(tangent_slope)}({sy.latex(x)}) = {sy.latex(sy.expand(tangent))} \\)である。\n"
                elif tangent_y > 0:
                    latex_answer += f"\\( y = {sy.latex(tangent_slope)}({sy.latex(x)}) + {sy.latex(tangent_y)} = {sy.latex(sy.expand(tangent))} \\)である。\n"
                elif tangent_y < 0:
                    latex_answer += f"\\( y = {sy.latex(tangent_slope)}({sy.latex(x)}) {sy.latex(tangent_y)} = {sy.latex(sy.expand(tangent))} \\)である。\n"
            else:
                if tangent_y == 0:
                    latex_answer += f"\\( y = {sy.latex(tangent_slope)}({sy.latex(x - tangent_x)})= {sy.latex(sy.expand(tangent))} \\)である。\n"
                elif tangent_y > 0:
                    latex_answer += f"\\( y = {sy.latex(tangent_slope)}({sy.latex(x - tangent_x)}) + {sy.latex(tangent_y)} = {sy.latex(sy.expand(tangent))} \\)である。\n"
                elif tangent_y < 0:
                    latex_answer += f"\\( y = {sy.latex(tangent_slope)}({sy.latex(x - tangent_x)}) {sy.latex(tangent_y)} = {sy.latex(sy.expand(tangent))} \\)である。\n"
            latex_answer += "また、今回の2次関数は"
            if a > 0:
                latex_answer += "下に凸なので、2次関数が上、接線が下にある。\n"
            elif a < 0:
                latex_answer += "上に凸なので、2次関数が下、接線が上にある。\n"
            latex_answer += "よって、求める面積は\n"
            if tangent_x > parallel_line_with_y_axis:
                start_x, end_x = parallel_line_with_y_axis, tangent_x
            elif tangent_x < parallel_line_with_y_axis:
                start_x, end_x = tangent_x, parallel_line_with_y_axis
            if a > 0:
                upper_function = quadratic_function
                lower_function = tangent
            elif a < 0:
                upper_function = tangent
                lower_function = quadratic_function
            latex_answer += f"\\( \\int_{{{sy.latex(start_x)}}}^{{{sy.latex(end_x)}}} \\lbrace ({sy.latex(sy.expand(upper_function))}) - ({sy.latex(sy.expand(lower_function))}) \\rbrace dx \\)\n"
            quadratic_function_after_subtraction = upper_function - lower_function
            factored_quadratic_function_after_subtraction = sy.factor(quadratic_function_after_subtraction)
            quadratic_coefficient = sy.expand(quadratic_function_after_subtraction).coeff(x, 2)
            divided_and_factored_quadratic_function_after_subtraction = sy.Rational(1, quadratic_coefficient) * factored_quadratic_function_after_subtraction
            if quadratic_coefficient == 1:
                if tangent_x == 0:
                    latex_answer += f"\\( = \\int_{{{sy.latex(start_x)}}}^{{{sy.latex(end_x)}}} {sy.latex(divided_and_factored_quadratic_function_after_subtraction)} dx \\)\n"
                    latex_answer += f"\\( = \\left \\lbrack \\dfrac{{{sy.latex(x)}^ 3}}{{3}} \\right\\rbrack_{{{sy.latex(start_x)}}}^{{{sy.latex(end_x)}}} \\)\n"
                else:
                    latex_answer += f"\\( = \\int_{{{sy.latex(start_x)}}}^{{{sy.latex(end_x)}}} {sy.latex(divided_and_factored_quadratic_function_after_subtraction)} dx \\)\n"
                    latex_answer += f"\\( = \\left \\lbrack \\dfrac{{({sy.latex(x - tangent_x)})^ 3}}{{3}} \\right\\rbrack_{{{sy.latex(start_x)}}}^{{{sy.latex(end_x)}}} \\)\n"
            else:
                if tangent_x == 0:
                    latex_answer += f"\\( = {sy.latex(quadratic_coefficient)} \\int_{{{sy.latex(start_x)}}}^{{{sy.latex(end_x)}}} {sy.latex(divided_and_factored_quadratic_function_after_subtraction)} dx \\)\n"
                    latex_answer += f"\\( = {sy.latex(quadratic_coefficient)} \\left\\lbrack \\dfrac{{{sy.latex(x)}^ 3}}{{3}} \\right\\rbrack_{{{sy.latex(start_x)}}}^{{{sy.latex(end_x)}}} \\)\n"
                else:
                    latex_answer += f"\\( = {sy.latex(quadratic_coefficient)} \\int_{{{sy.latex(start_x)}}}^{{{sy.latex(end_x)}}} {sy.latex(divided_and_factored_quadratic_function_after_subtraction)} dx \\)\n"
                    latex_answer += f"\\( = {sy.latex(quadratic_coefficient)} \\left\\lbrack \\dfrac{{({sy.latex(x - tangent_x)})^ 3}}{{3}} \\right\\rbrack_{{{sy.latex(start_x)}}}^{{{sy.latex(end_x)}}} \\)\n"
            left_x_for_area = ((x - tangent_x) ** 3).subs(x, end_x) * sy.Rational(1, 3)
            right_x_for_area = ((x - tangent_x) ** 3).subs(x, start_x) * sy.Rational(1, 3)
            if quadratic_coefficient == 1:
                if left_x_for_area >= 0:
                    if right_x_for_area >= 0:
                        latex_answer += f"\\( = ({sy.latex(left_x_for_area)} - {sy.latex(right_x_for_area)}) \\)\n"
                    else:
                        latex_answer += f"\\( = \\lbrace {sy.latex(left_x_for_area)} - ({sy.latex(right_x_for_area)}) \\rbrace \\)\n"
                else:
                    if right_x_for_area >= 0:
                        latex_answer += f"\\( = \\lbrace ({sy.latex(left_x_for_area)}) - {sy.latex(right_x_for_area)} \\rbrace \\)\n"
                    else:
                        latex_answer += f"\\( = \\lbrace ({sy.latex(left_x_for_area)}) - ({sy.latex(right_x_for_area)}) \\rbrace \\)\n"
            else:
                if left_x_for_area >= 0:
                    if right_x_for_area >= 0:
                        latex_answer += f"\\( = {sy.latex(quadratic_coefficient)} ({sy.latex(left_x_for_area)} - {sy.latex(right_x_for_area)}) \\)\n"
                    else:
                        latex_answer += f"\\( = {sy.latex(quadratic_coefficient)} \\lbrace {sy.latex(left_x_for_area)} - ({sy.latex(right_x_for_area)}) \\rbrace \\)\n"
                else:
                    if right_x_for_area >= 0:
                        latex_answer += f"\\( = {sy.latex(quadratic_coefficient)} \\lbrace ({sy.latex(left_x_for_area)}) - {sy.latex(right_x_for_area)} \\rbrace \\)\n"
                    else:
                        latex_answer += f"\\( = {sy.latex(quadratic_coefficient)} \\lbrace ({sy.latex(left_x_for_area)}) - ({sy.latex(right_x_for_area)}) \\rbrace \\)\n"
            area = sy.Abs(a) * sy.Rational(1, 3) * (end_x - start_x) ** 3
            latex_answer += f"\\(  = {sy.latex(area)} \\)"
        # f(x) = a1x^2 + b1x + c1, g(x) = a2x^2 + b2x + c2, f(x) - g(x) = k(x - t)^2 = ax^2 + bx + c
        elif problem_type == "between_two_quadratic_functions_that_touch_each_other_and_parallel_line_with_y_axis":
            k = self._random_integer(min_num=1, max_num=3)
            t = self._random_integer(min_num=-4, max_num=4)
            quadratic_function_after_subtraction = sy.expand(k * (x - t) ** 2)
            a = quadratic_function_after_subtraction.coeff(x, 2)
            b = quadratic_function_after_subtraction.coeff(x, 1)
            c = quadratic_function_after_subtraction.coeff(x, 0)
            another_integration_point = t + self._random_integer(min_num=-3, max_num=3, remove_zero=True)
            area = sy.Rational(1, 3) * k * sy.Abs((t - another_integration_point) ** 3)
            # not to become a = a1
            while True:    
                a1 = a + self._random_integer(min_num=-2, max_num=2, remove_zero=True)
                if a1 != 0:
                    break                
            b1 = self._random_integer(min_num=-3, max_num=3)
            c1 = self._random_integer(min_num=-3, max_num=3)
            # not to become b = b1 and c = c1
            if (b == b1) and (c == c1):
                increment_checker = choice(["b1_only", "c1_only", "b1_and_c1"])
                if increment_checker == "b1_only":
                    b1 += self._random_integer(min_num=-2, max_num=2, remove_zero=True)
                elif increment_checker == "c1_only":
                    c1 += self._random_integer(min_num=-2, max_num=2, remove_zero=True)
                elif increment_checker == "b1_and_c1":
                    b1 += self._random_integer(min_num=-2, max_num=2, remove_zero=True)
                    c1 += self._random_integer(min_num=-2, max_num=2, remove_zero=True)
            upper_quadratic_function = a1 * x ** 2 + b1 * x + c1
            # a1 - a2 = a <--> a2 = a1 - a
            a2 = a1 - a
            # b1 - b2 = b <--> b2 = b1 - b
            b2 = b1 - b
            # c1 - c2 = c <--> c2 = c1 - c
            c2 = c1 - c
            lower_quadratic_function = a2 * x ** 2 + b2 * x + c2
            display_mode = choice(["upper_is_first", "lower_is_first"])
            if display_mode == "upper_is_first":
                latex_problem = f"\\( y = {sy.latex(sy.expand(upper_quadratic_function))} \\)と、"
                latex_problem += f"\\( y = {sy.latex(sy.expand(lower_quadratic_function))} \\)、\n"
                latex_problem += f"および\\( x = {sy.latex(another_integration_point)} \\)で囲まれた面積を求めよ。"
            elif display_mode == "lower_is_first":
                latex_problem = f"\\( y = {sy.latex(sy.expand(lower_quadratic_function))} \\)と、"
                latex_problem += f"\\( y = {sy.latex(sy.expand(upper_quadratic_function))} \\)、\n"
                latex_problem += f"および\\( x = {sy.latex(another_integration_point)} \\)で囲まれた面積を求めよ。"
            latex_answer = "まず、2次関数同士の位置関係を確認するために、"
            if display_mode == "upper_is_first":
                latex_answer += f"\\( {sy.latex(sy.expand(upper_quadratic_function))} \\geqq {sy.latex(sy.expand(lower_quadratic_function))} \\)を解くと、\n"
                quadratic_function_for_display = upper_quadratic_function - lower_quadratic_function
                latex_answer += f"\\( {sy.latex(sy.expand(quadratic_function_for_display))} \\geqq 0 \\)\n"
                factored_quadratic_function_for_display = sy.factor(quadratic_function_for_display)
                latex_answer += f"\\( {sy.latex(factored_quadratic_function_for_display)} \\geqq 0 \\)\n"
                # quadratic_coefficient > 0
                quadratic_coefficient_for_display = sy.expand(factored_quadratic_function_for_display).coeff(x, 2)
                divided_and_factored_quadratic_function_for_display = factored_quadratic_function_for_display * sy.Rational(1, quadratic_coefficient_for_display)
                latex_answer += f"\\( {sy.latex(divided_and_factored_quadratic_function_for_display)} \\geqq 0 \\)\n"
                # (x - t)^2 >= 0
                latex_answer += "\\( x \\)は全ての実数。\n"
            elif display_mode == "lower_is_first":
                latex_answer += f"\\( {sy.latex(sy.expand(lower_quadratic_function))} \\geqq {sy.latex(sy.expand(upper_quadratic_function))} \\)を解くと、\n"
                quadratic_function_for_display = lower_quadratic_function - upper_quadratic_function
                latex_answer += f"\\( {sy.latex(sy.expand(quadratic_function_for_display))} \\geqq 0 \\)\n"
                factored_quadratic_function_for_display = sy.factor(quadratic_function_for_display)
                latex_answer += f"\\( {sy.latex(factored_quadratic_function_for_display)} \\geqq 0 \\)\n"
                # quadratic_coefficient < 0
                quadratic_coefficient_for_display = sy.expand(factored_quadratic_function_for_display).coeff(x, 2)
                divided_and_factored_quadratic_function_for_display = factored_quadratic_function_for_display * sy.Rational(1, quadratic_coefficient_for_display)
                latex_answer += f"\\( {sy.latex(divided_and_factored_quadratic_function_for_display)} \\leqq 0 \\)\n"
                latex_answer += f"\\( x \\)は\\( x = {sy.latex(t)} \\)を除く、全ての実数。\n"
            latex_answer += f"以上より、\\( y = {sy.latex(upper_quadratic_function)} \\)が上、\\( y = {sy.latex(lower_quadratic_function)}\\)が下であり、"
            latex_answer += f"\\( x = {sy.latex(t)} \\)で接する。\n"
            latex_answer += f"よって、求める面積\\( S \\)は、\n"
            if t > another_integration_point:
                start_x = another_integration_point
                end_x = t
            elif t < another_integration_point:
                start_x = t
                end_x = another_integration_point
            factored_quadratic_function_after_subtraction = sy.factor(quadratic_function_after_subtraction)
            divided_and_factored_quadratic_function_after_subtraction = sy.Rational(1, a) * factored_quadratic_function_after_subtraction
            if a == 1:
                if t == 0:
                    latex_answer += f"\\( = \\int_{{{sy.latex(start_x)}}}{{{sy.latex(end_x)}}} {sy.latex(divided_and_factored_quadratic_function_after_subtraction)} dx \\)"
                    latex_answer += f"\\( = \\left \\lbrack \\dfrac{{{sy.latex(x)}^ 3}}{{3}} \\right\\rbrack_{{{sy.latex(start_x)}}}^{{{sy.latex(end_x)}}} \\)\n"
                else:
                    latex_answer += f"\\( = \\int_{{{sy.latex(start_x)}}}^{{{sy.latex(end_x)}}} {sy.latex(divided_and_factored_quadratic_function_after_subtraction)} dx \\)\n"
                    latex_answer += f"\\( = \\left \\lbrack \\dfrac{{({sy.latex(x - t)})^ 3}}{{3}} \\right\\rbrack_{{{sy.latex(start_x)}}}^{{{sy.latex(end_x)}}} \\)\n"
            else:
                if t == 0:
                    latex_answer += f"\\( = {sy.latex(a)} \\int_{{{sy.latex(start_x)}}}^{{{sy.latex(end_x)}}} {sy.latex(divided_and_factored_quadratic_function_after_subtraction)} dx \\)\n"
                    latex_answer += f"\\( = {sy.latex(a)} \\left\\lbrack \\dfrac{{{sy.latex(x)}^ 3}}{{3}} \\right\\rbrack_{{{sy.latex(start_x)}}}^{{{sy.latex(end_x)}}} \\)\n"
                else:
                    latex_answer += f"\\( = {sy.latex(a)} \\int_{{{sy.latex(start_x)}}}^{{{sy.latex(end_x)}}} {sy.latex(divided_and_factored_quadratic_function_after_subtraction)} dx \\)\n"
                    latex_answer += f"\\( = {sy.latex(a)} \\left\\lbrack \\dfrac{{({sy.latex(x - t)})^ 3}}{{3}} \\right\\rbrack_{{{sy.latex(start_x)}}}^{{{sy.latex(end_x)}}} \\)\n"
            left_x_for_area = ((x - t) ** 3).subs(x, end_x) * sy.Rational(1, 3)
            right_x_for_area = ((x - t) ** 3).subs(x, start_x) * sy.Rational(1, 3)
            if a == 1:
                if left_x_for_area >= 0:
                    if right_x_for_area >= 0:
                        latex_answer += f"\\( = ({sy.latex(left_x_for_area)} - {sy.latex(right_x_for_area)}) \\)\n"
                    else:
                        latex_answer += f"\\( = \\lbrace {sy.latex(left_x_for_area)} - ({sy.latex(right_x_for_area)}) \\rbrace \\)\n"
                else:
                    if right_x_for_area >= 0:
                        latex_answer += f"\\( = \\lbrace ({sy.latex(left_x_for_area)}) - {sy.latex(right_x_for_area)} \\rbrace \\)\n"
                    else:
                        latex_answer += f"\\( = \\lbrace ({sy.latex(left_x_for_area)}) - ({sy.latex(right_x_for_area)}) \\rbrace \\)\n"
            else:
                if left_x_for_area >= 0:
                    if right_x_for_area >= 0:
                        latex_answer += f"\\( = {sy.latex(a)} ({sy.latex(left_x_for_area)} - {sy.latex(right_x_for_area)}) \\)\n"
                    else:
                        latex_answer += f"\\( = {sy.latex(a)} \\lbrace {sy.latex(left_x_for_area)} - ({sy.latex(right_x_for_area)}) \\rbrace \\)\n"
                else:
                    if right_x_for_area >= 0:
                        latex_answer += f"\\( = {sy.latex(a)} \\lbrace ({sy.latex(left_x_for_area)}) - {sy.latex(right_x_for_area)} \\rbrace \\)\n"
                    else:
                        latex_answer += f"\\( = {sy.latex(a)} \\lbrace ({sy.latex(left_x_for_area)}) - ({sy.latex(right_x_for_area)}) \\rbrace \\)\n"
            area = sy.Abs(a) * sy.Rational(1, 3) * (end_x - start_x) ** 3
            latex_answer += f"\\(  = {sy.latex(area)} \\)"
        elif problem_type == "between_quadratic_function_and_two_tangents":
            a = self._random_integer(-2, 2, remove_zero=True)
            b = self._random_integer(-3, 3)
            c = self._random_integer(-3, 3)
            quadratic_function = a * x ** 2 + b * x + c
            tangent_x1 = self._random_integer(-2, 3)
            tangent_x2 = tangent_x1 + self._random_integer(-2, 3, remove_zero=True)
            if tangent_x1 < tangent_x2:
                left_tangent_x, right_tangent_x = tangent_x1, tangent_x2
            elif tangent_x2 < tangent_x1:
                left_tangent_x, right_tangent_x = tangent_x2, tangent_x1
            latex_problem = f"\\( y = {sy.latex(sy.expand(quadratic_function))} \\)と、2つの接点\\( x = {sy.latex(left_tangent_x)}, {sy.latex(right_tangent_x)} \\)における接線で囲まれた面積を求めよ。"
            mid_x = sy.Rational(left_tangent_x + right_tangent_x, 2)
            latex_answer = "まずは接線を求める。\n"
            latex_answer += f"与えられた2次関数\\( y = {sy.latex(sy.expand(quadratic_function))} \\)に\\( x = {sy.latex(left_tangent_x)} \\)を代入すると、"
            left_tangent_y = quadratic_function.subs(x, left_tangent_x)
            latex_answer += f"\\( ({sy.latex(left_tangent_x)}, {sy.latex(left_tangent_y)}) \\)と接点を求められる。\n"
            differentiated_quadratic_function = sy.diff(quadratic_function, x)
            latex_answer += f"\( y' = {sy.latex(sy.expand(differentiated_quadratic_function))} \)なので、\\( ({sy.latex(left_tangent_x)}, {sy.latex(left_tangent_y)}) \\)における接線は、\n"
            # left tangent line part
            left_tangent_slope = differentiated_quadratic_function.subs(x, left_tangent_x)
            left_tangent = left_tangent_slope * (x - left_tangent_x) + left_tangent_y
            if left_tangent_x == 0:
                if left_tangent_y == 0:
                    latex_answer += f"\\( y = {sy.latex(left_tangent_slope)}({sy.latex(x)} - 0) = {sy.latex(sy.expand(left_tangent))} \\)である。\n"
                elif left_tangent_y > 0:
                    latex_answer += f"\\( y = {sy.latex(left_tangent_slope)}({sy.latex(x)} - 0) + {sy.latex(left_tangent_y)} = {sy.latex(sy.expand(left_tangent))} \\)である。\n"
                elif left_tangent_y < 0:
                    latex_answer += f"\\( y = {sy.latex(left_tangent_slope)}({sy.latex(x)} - 0) {sy.latex(left_tangent_y)} = {sy.latex(sy.expand(left_tangent))} \\)である。\n"
            else:
                if left_tangent_y == 0:
                    latex_answer += f"\\( y = {sy.latex(left_tangent_slope)}({sy.latex(x - left_tangent_x)})= {sy.latex(sy.expand(left_tangent))} \\)である。\n"
                elif left_tangent_y > 0:
                    latex_answer += f"\\( y = {sy.latex(left_tangent_slope)}({sy.latex(x - left_tangent_x)}) + {sy.latex(left_tangent_y)} = {sy.latex(sy.expand(left_tangent))} \\)である。\n"
                elif left_tangent_y < 0:
                    latex_answer += f"\\( y = {sy.latex(left_tangent_slope)}({sy.latex(x - left_tangent_x)}) {sy.latex(left_tangent_y)} = {sy.latex(sy.expand(left_tangent))} \\)である。\n"
            # right tangent line part
            latex_answer += f"同様に、与えられた2次関数に\\( x = {sy.latex(right_tangent_x)} \\)を代入すると、"
            right_tangent_y = quadratic_function.subs(x, right_tangent_x)
            latex_answer += f"\\( ({sy.latex(right_tangent_x)}, {sy.latex(right_tangent_y)}) \\)と接点を求められ、\n"
            right_tangent_slope = differentiated_quadratic_function.subs(x, right_tangent_x)
            right_tangent = right_tangent_slope * (x - right_tangent_x) + right_tangent_y
            if right_tangent_x == 0:
                if right_tangent_y == 0:
                    latex_answer += f"\\( y = {sy.latex(right_tangent_slope)}({sy.latex(x)}) = {sy.latex(sy.expand(right_tangent))} \\)が接線となる。\n"
                elif right_tangent_y > 0:
                    latex_answer += f"\\( y = {sy.latex(right_tangent_slope)}({sy.latex(x)}) + {sy.latex(right_tangent_y)} = {sy.latex(sy.expand(right_tangent))} \\)が接線となる。\n"
                elif right_tangent_y < 0:
                    latex_answer += f"\\( y = {sy.latex(right_tangent_slope)}({sy.latex(x)}) {sy.latex(right_tangent_y)} = {sy.latex(sy.expand(right_tangent))} \\)が接線となる。\n"
            else:
                if right_tangent_y == 0:
                    latex_answer += f"\\( y = {sy.latex(right_tangent_slope)}({sy.latex(x - right_tangent_x)})= {sy.latex(sy.expand(right_tangent))} \\)が接線となる。\n"
                elif right_tangent_y > 0:
                    latex_answer += f"\\( y = {sy.latex(right_tangent_slope)}({sy.latex(x - right_tangent_x)}) + {sy.latex(right_tangent_y)} = {sy.latex(sy.expand(right_tangent))} \\)が接線となる。\n"
                elif right_tangent_y < 0:
                    latex_answer += f"\\( y = {sy.latex(right_tangent_slope)}({sy.latex(x - right_tangent_x)}) {sy.latex(right_tangent_y)} = {sy.latex(sy.expand(right_tangent))} \\)が接線となる。\n"
            latex_answer += "次に、接線同士の交点を求めると、\n"
            latex_answer += f"\\( {sy.latex(sy.expand(left_tangent))} = {sy.latex(sy.expand(right_tangent))} \\)より、"
            cross_x = sy.solve(left_tangent - right_tangent, x)[0]
            assert cross_x == mid_x
            latex_answer += f"\\( x = {sy.latex(cross_x)} \\)となる。\n"
            latex_answer += "最後に接線ごとに面積を求めていく。\n"
            # s1 part.
            latex_answer += f"\\( x = {sy.latex(left_tangent_x)} \\)における接線\\( y = {sy.latex(sy.expand(left_tangent))} \\)と、2次関数\\( y = {sy.latex(sy.expand(quadratic_function))} \\)における面積を\\( S_1 \\)とすると、\n"
            if a > 0:
                latex_answer += "2次関数は下に凸であり、2次関数が上、接線が下になることから、\n"
                latex_answer += f"\\( S_1 = \\int_{{{sy.latex(left_tangent_x)}}}^{{{sy.latex(cross_x)}}}  \\left\\lbrace ({sy.latex(sy.expand(quadratic_function))}) - ({sy.latex(sy.expand(left_tangent))}) \\right\\rbrace dx \\)\n"
                factored_quadratic_function_after_subtraction1 = sy.factor(quadratic_function - left_tangent)
            elif a < 0:
                latex_answer += "2次関数は上に凸であり、接線が上、2次関数が下になることから、\n"
                latex_answer += f"\\( S_1 = \\int_{{{sy.latex(left_tangent_x)}}}^{{{sy.latex(cross_x)}}}  \\left\\lbrace ({sy.latex(sy.expand(left_tangent))}) - ({sy.latex(sy.expand(quadratic_function))}) \\right\\rbrace dx \\)\n"
                factored_quadratic_function_after_subtraction1 = sy.factor(left_tangent - quadratic_function)
            latex_answer += f"\\( = \\int_{{{sy.latex(left_tangent_x)}}}^{{{sy.latex(cross_x)}}} {sy.latex(factored_quadratic_function_after_subtraction1)} dx \\)\n"
            quadratic_coefficient_after_subtraction1 = sy.expand(factored_quadratic_function_after_subtraction1).coeff(x, 2)
            divided_and_factored_quadratic_function_after_subtraction1 = factored_quadratic_function_after_subtraction1 * sy.Rational(1, quadratic_coefficient_after_subtraction1)
            if quadratic_coefficient_after_subtraction1 == 1:
                latex_answer += f"\\( = \\int_{{{sy.latex(left_tangent_x)}}}^{{{sy.latex(cross_x)}}} {sy.latex(divided_and_factored_quadratic_function_after_subtraction1)} dx\\)\n"
                latex_answer += f"\\( = \\left\\lbrack \\dfrac{{({sy.latex(x - left_tangent_x)})^3}}{{3}} \\right\\rbrack_{{{sy.latex(left_tangent_x)}}}^{{{sy.latex(cross_x)}}} \\)\n"
            else:
                latex_answer += f"\\( = {sy.latex(quadratic_coefficient_after_subtraction1)} \\int_{{{sy.latex(left_tangent_x)}}}^{{{sy.latex(cross_x)}}} {sy.latex(divided_and_factored_quadratic_function_after_subtraction1)} dx\\)\n"
                latex_answer += f"\\( = {sy.latex(quadratic_coefficient_after_subtraction1)} \\left\\lbrack \\dfrac{{({sy.latex(x - left_tangent_x)})^3}}{{3}} \\right\\rbrack_{{{sy.latex(left_tangent_x)}}}^{{{sy.latex(cross_x)}}} \\)\n"
            left_value1 = ((x - left_tangent_x) ** 3).subs(x, cross_x) * sy.Rational(1, 3)
            right_value1 = ((x - left_tangent_x) ** 3).subs(x, left_tangent_x) * sy.Rational(1, 3)
            if quadratic_coefficient_after_subtraction1 == 1:
                if left_value1 >= 0:
                    if right_value1 >= 0:
                        latex_answer += f"\\( = {sy.latex(left_value1)} - {sy.latex(right_value1)} \\)\n"
                    else:
                        latex_answer += f"\\( = \\left\\lbrace {sy.latex(left_value1)} - \\left({sy.latex(right_value1)}\\right) \\right\\rbrace \\)\n"
                else:
                    if right_value1 >= 0:
                        latex_answer += f"\\( = \\left\\lbrace \\left({sy.latex(left_value1)}\\right) - {sy.latex(right_value1)} \\right\\rbrace \\)\n"
                    else:
                        latex_answer += f"\\( = \\left\\lbrace \\left({sy.latex(left_value1)}\\right) - \\left({sy.latex(right_value1)} \\right) \\right\\rbrace \\)\n"
            else:
                if left_value1 >= 0:
                    if right_value1 >= 0:
                        latex_answer += f"\\( = {sy.latex(quadratic_coefficient_after_subtraction1)} \\left( {sy.latex(left_value1)} - {sy.latex(right_value1)} \\right) \\)\n"
                    else:
                        latex_answer += f"\\( = {sy.latex(quadratic_coefficient_after_subtraction1)} \\left\\lbrace {sy.latex(left_value1)} - \\left({sy.latex(right_value1)}\\right) \\right\\rbrace \\)\n"
                else:
                    if right_value1 >= 0:
                        latex_answer += f"\\( = {sy.latex(quadratic_coefficient_after_subtraction1)} \\left\\lbrace \\left({sy.latex(left_value1)}\\right) - {sy.latex(right_value1)} \\right\\rbrace \\)\n"
                    else:
                        latex_answer += f"\\( = {sy.latex(quadratic_coefficient_after_subtraction1)} \\left\\lbrace \\left({sy.latex(left_value1)}\\right) - \\left({sy.latex(right_value1)} \\right) \\right\\rbrace \\)\n"
            area1 = quadratic_coefficient_after_subtraction1 * (left_value1 - right_value1)
            latex_answer += f"\\( = {sy.latex(area1)} \\)\n"
            # s2 part.
            latex_answer += f"同様に、\\( x = {sy.latex(right_tangent_x)} \\)における接線\\( y = {sy.latex(sy.expand(right_tangent))} \\)と、2次関数\\( y = {sy.latex(sy.expand(quadratic_function))} \\)における面積を\\( S_2 \\)とすると、\n"
            if a > 0:
                latex_answer += "2次関数は下に凸であり、2次関数が上、接線が下になることから、\n"
                latex_answer += f"\\( S_2 = \\int_{{{sy.latex(cross_x)}}}^{{{sy.latex(right_tangent_x)}}}  \\left\\lbrace ({sy.latex(sy.expand(quadratic_function))}) - ({sy.latex(sy.expand(right_tangent))}) \\right\\rbrace dx \\)\n"
                factored_quadratic_function_after_subtraction2 = sy.factor(quadratic_function - right_tangent)
            elif a < 0:
                latex_answer += "2次関数は上に凸であり、接線が上、2次関数が下になることから、\n"
                latex_answer += f"\\( S_2 = \\int_{{{sy.latex(cross_x)}}}^{{{sy.latex(right_tangent_x)}}}  \\left\\lbrace ({sy.latex(sy.expand(right_tangent))}) - ({sy.latex(sy.expand(quadratic_function))}) \\right\\rbrace dx \\)\n"
                factored_quadratic_function_after_subtraction2 = sy.factor(right_tangent - quadratic_function)
            latex_answer += f"\\( = \\int_{{{sy.latex(cross_x)}}}^{{{sy.latex(right_tangent_x)}}} {sy.latex(factored_quadratic_function_after_subtraction2)} dx \\)\n"
            quadratic_coefficient_after_subtraction2 = sy.expand(factored_quadratic_function_after_subtraction2).coeff(x, 2)
            divided_and_factored_quadratic_function_after_subtraction2 = factored_quadratic_function_after_subtraction2 * sy.Rational(1, quadratic_coefficient_after_subtraction2)
            if quadratic_coefficient_after_subtraction2 == 1:
                latex_answer += f"\\( = \\int_{{{sy.latex(cross_x)}}}^{{{sy.latex(right_tangent_x)}}} {sy.latex(divided_and_factored_quadratic_function_after_subtraction2)} dx\\)\n"
                latex_answer += f"\\( = \\left\\lbrack \\dfrac{{({sy.latex(x - right_tangent_x)})^3}}{{3}} \\right\\rbrack_{{{sy.latex(cross_x)}}}^{{{sy.latex(right_tangent_x)}}} \\)\n"
            else:
                latex_answer += f"\\( = {sy.latex(quadratic_coefficient_after_subtraction2)} \\int_{{{sy.latex(right_tangent_x)}}}^{{{sy.latex(cross_x)}}} {sy.latex(divided_and_factored_quadratic_function_after_subtraction2)} dx\\)\n"
                latex_answer += f"\\( = {sy.latex(quadratic_coefficient_after_subtraction2)} \\left\\lbrack \\dfrac{{({sy.latex(x - right_tangent_x)})^3}}{{3}} \\right\\rbrack_{{{sy.latex(cross_x)}}}^{{{sy.latex(right_tangent_x)}}} \\)\n"
            left_value2 = ((x - right_tangent_x) ** 3).subs(x, right_tangent_x) * sy.Rational(1, 3)
            right_value2 = ((x - right_tangent_x) ** 3).subs(x, cross_x) * sy.Rational(1, 3)
            if quadratic_coefficient_after_subtraction2 == 1:
                if left_value2 >= 0:
                    if right_value2 >= 0:
                        latex_answer += f"\\( = {sy.latex(left_value2)} - {sy.latex(right_value2)} \\)\n"
                    else:
                        latex_answer += f"\\( = \\left\\lbrace {sy.latex(left_value2)} - \\left({sy.latex(right_value2)}\\right) \\right\\rbrace \\)\n"
                else:
                    if right_value2 >= 0:
                        latex_answer += f"\\( = \\left\\lbrace \\left({sy.latex(left_value2)}\\right) - {sy.latex(right_value2)} \\right\\rbrace \\)\n"
                    else:
                        latex_answer += f"\\( = \\left\\lbrace \\left({sy.latex(left_value2)}\\right) - \\left({sy.latex(right_value2)} \\right) \\right\\rbrace \\)\n"
            else:
                if left_value2 >= 0:
                    if right_value2 >= 0:
                        latex_answer += f"\\( = {sy.latex(quadratic_coefficient_after_subtraction2)} \\left( {sy.latex(left_value2)} - {sy.latex(right_value2)} \\right) \\)\n"
                    else:
                        latex_answer += f"\\( = {sy.latex(quadratic_coefficient_after_subtraction2)} \\left\\lbrace {sy.latex(left_value2)} - \\left({sy.latex(right_value2)}\\right) \\right\\rbrace \\)\n"
                else:
                    if right_value1 >= 0:
                        latex_answer += f"\\( = {sy.latex(quadratic_coefficient_after_subtraction2)} \\left\\lbrace \\left({sy.latex(left_value2)}\\right) - {sy.latex(right_value2)} \\right\\rbrace \\)\n"
                    else:
                        latex_answer += f"\\( = {sy.latex(quadratic_coefficient_after_subtraction2)} \\left\\lbrace \\left({sy.latex(left_value2)}\\right) - \\left({sy.latex(right_value2)} \\right) \\right\\rbrace \\)\n"
            area2 = quadratic_coefficient_after_subtraction2 * (left_value2 - right_value2)
            latex_answer += f"\\( = {sy.latex(area2)} \\)\n"
            total_area = area1 + area2
            latex_answer += "よって、求めたい面積を\\( S \\)とすると、\n"
            latex_answer += "\\( S = S_1 + S_2 \\)\n"
            latex_answer += f"\\( = {sy.latex(total_area)}\\)"
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
