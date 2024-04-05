from random import choice, randint, random
import re
from typing import Dict, Optional, Tuple, Union

import sympy as sy

class IntegralCalculationOfLinearFunctionReplacement:
    """高校3年生用の積分計算の問題と解答を出力
    
    Attributes:
        latex_answer (str): LaTeX形式を前提とした解答
        latex_problem (str): LaTeX形式を前提とした問題
    """
    def __init__(self, **settings: Dict):
        """初期設定
        
        Args:
            settings (dict): 問題の各種設定を格納
            - integral_types: indefinite_integral(不定積分)か、definite_integral(定積分)のいずれか
            - used_formulas: n_dimension_function(n次関数)などの利用される積分公式の確認
        """
        sy.init_printing(order='grevlex')
        selected_integral_type = choice(settings["integral_types"])
        used_formula = choice(settings["used_formulas"])
        if selected_integral_type == "indefinite_integral":
            self.latex_answer, self.latex_problem = self._make_indefinite_substitution_of_linear_expression_problem(used_formula)
        elif selected_integral_type == "definite_integral":
            self.latex_answer, self.latex_problem = self._make_definite_substitution_of_linear_expression_problem(used_formula)
    
    def __repr__(self):
        return f"latex_answer: {self.latex_answer}, latex_problem: {self.latex_problem}"

    def _make_indefinite_substitution_of_linear_expression_problem(self, used_formula: str) -> Tuple[str, str]:
        """1次式の置換を用いるタイプの不定計算問題を作成

        Args:
            used_function (str): 使用される関数

        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題
        
        Developing:
            n次関数, 分数関数
            
            どこまで分離する？
                n次関数, 三角関数などの関数単位で作成してくれるように?
                    使い勝手は悪くなさそうだが、ランダムなものが返ってくるせいで計算が難しくなる可能性はありそう
                    →とりあえず作ってみて、あれそうだったら改修なり撤去するなりでよさそう
            
            基本的に積分後を主体として、微分先をやらせたほうがよい場合が多い
            
            3/31
            おおむねうまくいっているが、
                ・重複した表現が多いのが気にかかる。同じ処理をひとまとめにして、分岐も含めてまとめるべき？
                ・cosやsinは、何だかマイナスが勝手に消されている雰囲気を感じる。チェックする
                    ->勝手に消されているでファイナルアンサー。ただ、そこまでの影響もないような気はするので、いったん保留
            4/2
            引き続き作業。三角関数の続き
                sin^2=-1/tanxはどうも難しそう。30分程度苦戦したが、うまくいかなかった。
                そのため、とりあえず手作業で実装するべき

            4/4
            問題ばらけすぎ問題
                結局「1次式の置換」「部分積分」のようにわけて実装することにした
            なんかx^nの値がでかすぎね？問題
                そんな設定をしているつもりはないのに、なぜか4桁の数が飛び出てくる
                別に解けないことはないが、問題の趣旨からは外れるので、原因を確認して修正したい系
                ->gpt君に聞いてみた結果、おそらくx^n+0の形式で、自動的に展開が行われているのがその原因っぽいと判明。
                x^n+0の形式では、当然6 * (6x)**6のような値がでる
                ↑ax+b(b≠0)でかいけつ
            
            計算遅くね問題
                微分がシンプルに遅い。10~20秒程度待たされる。
                →わりとかったるいので、微分も手作業で実装する？手順が決まっていることを考えれば、さして無理筋でもなさそう
            
            4/5
            そこそこ解決
            あとはリファクタリングというか、再構成をどうするか
                この後定積分に用いることを考えたら、手作業は別に分離しておいて、いつでも引っ張り出せるようにしておくというのも一つの手段。
                問題になるのが、途中経過をどこまで記すか？ということ
                    月みたいに事細かにかくのであれば、あまり隠蔽しすぎると、欲しいものがなくなって困ってしまうかも？
                    とりあえず作ってみて考える？
                    すなわち、関数の作成部分と関数・被積分関数の作成を一元化
                    関数ができた後は、定積分と否定積分で共通の部分と、逆に共通でない部分を見抜く必要がある。
                    →とりあえず作ってみる
                        機能としては、
                        ・与えられたモード(n_dimension_functionや1/cos^2x)などに応じて、f_latex, f_down_latex
                            ここちょっと怪しい？全体的に
                                結局、微分した関数がほしいのん？？
        """
        
        def problem_and_answer(function_latex_for_answer: str, function_latex_for_problem: str) -> Tuple[str, str]:
            """不定積分用の問題と解答を出力

            Args:
                function_for_answer (str): 解答に利用したいlatex形式の式
                function_for_problem (str): 問題に利用したいlatex形式の式

            Returns:
                Tuple[str, str]: latex形式の問題と解答
                - latex_answer (str): 解答
                - latex_problem (str): 問題
            """
            latex_answer = f"={function_latex_for_answer} + C"
            latex_problem = f"\\int {function_latex_for_problem} \\, dx"
            return latex_answer, latex_problem
    
        function, differentiated_function = self._make_and_differentiate_function(used_formula)
        if used_formula == "1/x":
            pattern = r'\\left\((.*?)\\right\)'
            function_latex = re.sub(pattern, r'| \1 |', sy.latex(function))
        else:
            function_latex = sy.latex(function)
        differentiated_function_latex = sy.latex(differentiated_function)
        latex_answer, latex_problem = problem_and_answer(function_latex, differentiated_function_latex)
        return latex_answer, latex_problem
    
    def _make_and_differentiate_function(self, used_formula: str) -> Tuple:
        """与えられた積分公式に応じて、ランダムな関数の作成と微分を行う
        
        Args:
            used_formula (str): 使用する積分公式
        
        Returns:
            Tuple: 元の関数と微分した関数
            - function: 元の関数
            - differentiated_function: 微分した関数
        """
        x = sy.Symbol("x")
        a = self._random_integer()
        b = self._random_integer()
        linear_function = a * x + b
        if used_formula == "n_dimension_function":
            n = self._random_integer(min_abs=3, max_abs=6, positive_or_negative="positive")
            k = self._random_integer(min_abs=2, max_abs=3)
            function = k * linear_function ** n
            differentiated_function = k * n * a * linear_function ** (n - 1)
        elif used_formula == "1/x":
            k = self._random_integer(min_abs=2, max_abs=4)
            function = k * sy.log(linear_function)
            differentiated_function = k * (a / linear_function)
        elif used_formula == "1/x^2":
            k = self._random_integer(min_abs=2, max_abs=4)
            function = k * (1 / linear_function)
            differentiated_function = -1 * k * a * (1 / linear_function ** 2)
        elif used_formula == "sin":
            k = self._random_number(use_frac=True, including_zero=False)
            function = k * sy.sin(linear_function)
            differentiated_function = k * a * sy.cos(linear_function)
        elif used_formula == "cos":
            k = self._random_number(use_frac=True, including_zero=False)
            function = k * sy.cos(linear_function)
            differentiated_function = -k * a * sy.sin(linear_function)
        elif used_formula == "1/cos^2x":
            k = self._random_number(use_frac=True, including_zero=False)
            function = k * sy.tan(linear_function)
            differentiated_function = k * a * (1 / sy.cos(linear_function) ** 2)
        elif used_formula == "1/sin^2x":
            k = self._random_number(use_frac=True, including_zero=False)
            function = k * (-1 * sy.tan(linear_function))
            differentiated_function = k * a * (1 / sy.sin(linear_function) ** 2)
        return function, differentiated_function
    
    def _random_integer(self, min_abs: int = 1, max_abs: int = 6, positive_or_negative=None):
        """ゼロを含まない整数をランダムに返す
        
        Args:
            max_abs (int): 大きさの調整に使う整数の絶対値の最大値。デフォルトは6
            min_abs (int): 大きさの調整に使う整数の絶対値の最小値。デフォルトは1
            positive_or_negative (Optional[str]): 正負の指定。デフォルトはNone
            
        Returns:
            integer (sy.Integer): 整数
        """
        if max_abs < min_abs:
            raise ValueError(f"'min_abs' is {min_abs}, and 'max_abs' is {max_abs}. 'min_abs' must be less than 'max_abs'.")
        if min_abs <= 0:
            raise ValueError(f"'min_abs' is {min_abs}. 'min_abs' must be more than Zero.")
        integer = sy.Integer(randint(min_abs, max_abs))
        if ((positive_or_negative is None) and (random() > 0.5)) or (positive_or_negative == "negative"):
            integer *= -1
        return integer
    
    def _random_number(self, use_frac: bool = True, including_zero: bool = True) -> Union[sy.Integer, sy.Rational]:
        """指定されたタイプのランダムな数を出力

        Args:
            use_frac (bool): 分数を出力するか否か。デフォルトはTrue
            
        Returns:
            number (Union[sy.Integer, sy.Rational]): 指定された条件を満たす数
        """
        if (including_zero) and (random() < sy.Rational(1, 8)):
            return 0
        if use_frac:
            number_type = choice(["integer", "frac"])
        else:
            number_type = "integer"
        if number_type == "integer":
            number = sy.Integer(randint(1, 6))
        elif number_type == "frac":
            denominator = sy.Integer(randint(2, 6))
            divisors = set(sy.divisors(denominator))
            numbers = set(range(1, denominator+1))
            candidates = numbers - divisors
            candidates.add(1)
            numerator = choice(list(candidates))
            number = sy.Rational(numerator, denominator)
            if (number.numerator != 1) and (random() > 0.5):
                number = sy.Rational(denominator, numerator)
        if random() > 0.5:
            number *= -1
        return number
