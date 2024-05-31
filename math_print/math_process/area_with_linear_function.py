"""
5/30

どこに1次関数の情報をねじ込むか？
    linear_function_with_graphでは、
        self.selected_problem_type, self.graph_to_use, self.linear_functionでreturnした上で、
        "{{ information_tuple.0.selected_problem_type }}" == "with_grid_to_linear_function"や
        var left_x1 = Number({{ information_tuple.0.linear_function.x1 }});
        として渡している
    
    同じように渡せるのは渡せるが、問題は渡し方
        リストやタプルでは番号になるため、linear_function1.x1, linear_function2.y2のように、名前を変えられた方が望ましい
            とりあえずself....で渡せば、名前で呼び出せることはわかっているので、それを使う？
            何かしらを使ってよりわかりやすい構造にできないか？？というのもある
            他のものを使うか。あるいは同じにしつつも、構造だけは変えるか。
            ↑スピード重視で、そのまま使う。こっちのPythonファイルの見づらさはとりあえず目をつむる系で
    
    何を渡すか？
        with_graphでなければ、そもそも通る点を使う必要がなさそうではある
        with_graphなら当然に必須
        
        問題文や答えが必要な点も要注目
            あちらはグラフを描くことだけに絞っていたが、こちらは最低限「～～～の面積を求めよ。が必要になる。」
            同様に、解答もある程度解説する必要がありそう。
            超大作～
        
        概ね方針がお定まりした上で、どこから取り組むか？？
            テスト速度優先であれば、とりあえずグラフだけ渡して読ませるというのも一つの手段。
                そもそも3本の直線とその交点、三角形をすんなり描写できるかというのが怪しい
                手順としては、まずはこちら側でいじって、それから向こうでグラフの描写を行う
                + 問題設定にグラフの表示の有無を設定？
                    全部一律で表示するのでなければ、問題文もあわせて切り替える必要が出てくる
                    結局のところ、単純に手間が増加するのは間違いないため、それに見合うほどか？？という話になる
                        eナビもカワセミも、ざっと確認した限りはグラフありきの問題なので、それはなしでokそう
        
        というわけで、とりあえずlinear_functionを3つ分ここに用意することから始める

5/31
linear_function3つ分の用意から始める

jsのdrawLinearFunctionが悪さをしている
    そもそも、値が存在していない説？
        中で確認したら、0, 0, 0, 0だった。たまたま？
        でもなさそう。もう一つ遡って確認する
        
    
    多分self.をlinear_function1, 2, 3につけ忘れていたのが原因っぽい
    
"""
from random import choice, randint, random
from typing import Dict, NamedTuple


import sympy as sy


class AreaWithLinearFunction:
    """中学2年生用の、直線で囲まれた面積の問題と解答を出力
    
    Attributes:
        latex_answer (str): LaTeX形式を前提とした解答
        latex_problem (str): LaTeX形式を前提とした問題
    """
    def __init__(self, **settings: Dict):
        sy.init_printing(order='grevlex')
        selected_problem_type = choice(settings["problem_types"])
        if selected_problem_type == "one_side_on_axis":
            self.latex_answer, self.latex_problem, self.linear_function1, self.linear_function2, self.linear_function3 = self._make_one_side_on_axis_problem()
        elif selected_problem_type == "no_side_on_axis":
            self.latex_answer, self.latex_problem, self.linear_function1, self.linear_function2, self.linear_function3 = self._make_no_side_on_axis_problem()
    
    def _make_one_side_on_axis_problem(self):
        linear_function1 = self._decide_linear_function_status()
        linear_function2 = self._decide_linear_function_status()
        linear_function3 = self._decide_linear_function_status()
        latex_answer = "dummy answer"
        latex_problem = "dummy problem"
        return latex_answer, latex_problem, linear_function1, linear_function2, linear_function3
    
    def _make_no_side_on_axis_problem(self):
        linear_function1 = self._decide_linear_function_status()
        linear_function2 = self._decide_linear_function_status()
        linear_function3 = self._decide_linear_function_status()
        latex_answer = "dummy answer"
        latex_problem = "dummy problem"
        return latex_answer, latex_problem, linear_function1, linear_function2, linear_function3

    def _decide_linear_function_status(self):
        """1次関数のステータスを決定

        Returns:
            linear_function (LinearFunction): 1次関数の式と通る点を格納
        """
        class LinearFunction(NamedTuple):
            """1次関数の通る点と式を格納

            Args:
                x1, y1, x2, y2 (str): 1次関数が通る2点
                linear_function_latex (str): latex形式で記述された1次関数の式
                linear_coefficient_latex (str): latex形式で記述された1次関数の傾き
                intercept_latex (str): latex形式で記述された切片
            """
            x1: str
            y1: str
            x2: str
            y2: str
            linear_equation_latex: str
            linear_coefficient_latex: str
            intercept_latex: str

        x = sy.Symbol("x", real=True)
        y = sy.Symbol("y", real=True)
        x1 = randint(-5, 5 - 1)
        x2 = x1 + randint(1, 5 - x1)
        y1 = randint(-5, 5 - 1)
        y2 = y1 + randint(1, 5 - y1)
        if random() > 0.5:
            y1, y2 = y2, y1
        linear_coefficient = sy.Rational(y2 - y1, x2 - x1)
        right_of_equation = sy.expand(linear_coefficient * x - linear_coefficient * x1 + y1)
        right_of_equation_latex = sy.latex(right_of_equation)
        linear_equation_latex = f"\( y = {right_of_equation_latex} \)".replace("\\", "\\\\")
        linear_coefficient_latex = f"\( {sy.latex(linear_coefficient)} \)".replace("\\", "\\\\")
        intercept = -linear_coefficient * x1 + y1
        intercept_latex = f"\( {sy.latex(intercept)} \)".replace("\\", "\\\\")
        linear_function = LinearFunction(
            x1=str(x1), y1=str(y1),
            x2=str(x2), y2=str(y2),
            linear_equation_latex=linear_equation_latex,
            linear_coefficient_latex=linear_coefficient_latex, intercept_latex=intercept_latex
        )
        return linear_function
    