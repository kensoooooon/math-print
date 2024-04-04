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
    
        x = sy.Symbol("x")
        # k(ax + b)^n
        # linear_function = self._random_n_dimension_function(1, use_frac=False)
        a = self._random_integer()
        b = self._random_integer()
        linear_function = a * x + b
        if used_formula == "n_dimension_function":
            n = self._random_integer(min_abs=3, max_abs=6, positive_or_negative="positive")
            k = self._random_integer(min_abs=2, max_abs=3)
            f = k * linear_function ** n
            f_latex = sy.latex(f)
            f_down = k * n * a * linear_function ** (n - 1)
            f_down_latex = sy.latex(f_down)
            latex_answer, latex_problem = problem_and_answer(f_latex, f_down_latex)
        # k/(ax+b)
        elif used_formula == "1/x":
            k = self._random_integer(min_abs=2, max_abs=4)
            f = k * sy.log(linear_function)
            pattern = r'\\left\((.*?)\\right\)'
            f_latex = re.sub(pattern, r'| \1 |', sy.latex(f))
            f_down = k * (a / linear_function)
            f_down_latex = sy.latex(f_down)
            latex_answer, latex_problem = problem_and_answer(f_latex, f_down_latex)
        # k/(ax+b)^2
        elif used_formula == "1/x^2":
            # next 怪しい　ポイント
            k = self._random_integer(min_abs=2, max_abs=4)
            f = k * (-1 / linear_function)
            f_latex = sy.latex(f)
            f_down = k * a * (1 / linear_function ** 2)
            f_down_latex = sy.latex(f_down)
            latex_answer, latex_problem = problem_and_answer(f_latex, f_down_latex)
        elif used_formula == "sin":
            k = self._random_number(use_frac=True, including_zero=False)
            f = k * sy.sin(linear_function)
            f_latex = sy.latex(f)
            f_down = k * a * sy.cos(linear_function)
            f_down_latex = sy.latex(f_down)
            latex_answer, latex_problem = problem_and_answer(f_latex, f_down_latex)
        elif used_formula == "cos":
            k = self._random_number(use_frac=True, including_zero=False)
            f = k * sy.cos(linear_function)
            f_latex = sy.latex(f)
            f_down = -k * a * sy.sin(linear_function)
            f_down_latex = sy.latex(f_down)
            latex_answer, latex_problem = problem_and_answer(f_latex, f_down_latex)
        elif used_formula == "1/cos^2x":
            k = self._random_number(use_frac=False, including_zero=False)
            f = k * sy.tan(linear_function)
            f_latex = sy.latex(f)
            f_down = k * a * (1 / sy.cos(linear_function) ** 2)
            f_down_latex = sy.latex(f_down)
            latex_answer, latex_problem = problem_and_answer(f_latex, f_down_latex)
        elif used_formula == "1/sin^2x":
            k = self._random_number(use_frac=False, including_zero=False)
            f = k * (-1 * sy.tan(linear_function))
            f_latex = sy.latex(f)
            f_down = k * a * (1 / sy.sin(linear_function) ** 2)
            f_down_latex = sy.latex(f_down)
            latex_answer, latex_problem = problem_and_answer(f_latex, f_down_latex)
        return latex_answer, latex_problem
    
    def _differentiate(self, used_formula, function):
        """与えられた公式に対応して、関数の微分を行う
        if used_formula == "n_dimension_function":
            n = self._random_integer(min_abs=3, max_abs=6, positive_or_negative="positive")
            k = self._random_integer(min_abs=2, max_abs=3)
            f = k * linear_function ** n
            f_latex = sy.latex(f)
            f_down = k * n * a * linear_function ** (n - 1)
            f_down_latex = sy.latex(f_down)
            latex_answer, latex_problem = problem_and_answer(f_latex, f_down_latex)
        # k/(ax+b)
        elif used_formula == "1/x":
            k = self._random_integer(min_abs=2, max_abs=4)
            f = k * sy.log(linear_function)
            pattern = r'\\left\((.*?)\\right\)'
            f_latex = re.sub(pattern, r'| \1 |', sy.latex(f))
            f_down = k * (a / linear_function)
            f_down_latex = sy.latex(f_down)
            latex_answer, latex_problem = problem_and_answer(f_latex, f_down_latex)
        # k/(ax+b)^2
        elif used_formula == "1/x^2":
            k = self._random_integer(min_abs=2, max_abs=4)
            f = k * (1 / linear_function)
            f_latex = sy.latex(f)
            f_down = k * a * (-1 / linear_function ** 2)
            f_down_latex = sy.latex(f_down)
            latex_answer, latex_problem = problem_and_answer(f_latex, f_down_latex)
        """
        
    
    def _problem_and_answer_for_indefinite_integral(self, function, rewrite_function=None) -> Tuple[str, str]:
        """与えられた関数を微分し、不定積分の問題と解答を出力

        Args:
            function : 微分対象となる関数
            rewrite_function (_type_, optional): 書き換えを行いたい関数. Defaults to None.

        Returns:
            Tuple[str, str]: latex形式で記述された解答と問題
            - latex_answer (str): 解答
            - latex_problem (str): 問題
        
        Developing:
            いったん保留で。対数のときのような特殊な処理を挟むと、こちらに結局全移行してしまいそう
                全体を見てみて、特殊な処理が少なそうだったら、あらためて稼働する
        """
        x = sy.Symbol("x")
        f_down = sy.diff(function, x)

    def _differentiate_latex(self, function, rewrite=False, simplify=False) -> str:
        """関数を微分し、latexを作成・出力するための関数

        Args:
            function: 微分対象となる関数
            rewrite (bool): 書き直しを必要とするか否か。デフォルトはFalse
            simplify (bool): 単純化を必要とするか否か。デフォルトはFalse
        
        Returns:
            f_down_latex (str): 微分された関数のlatex形式
        """
        x = sy.Symbol("x")
        if rewrite:
            f_down = sy.diff(function, x).rewrite(rewrite)
        else:
            f_down = sy.diff(function, x)
        if simplify:
            f_down = sy.simplify(f_down)
        f_down_latex = sy.latex(f_down)
        return f_down_latex
    
    def _random_n_dimension_function(self, dimension: int, use_frac: bool=True) -> sy.Add:
        """指定された次数のn次関数をランダムに出力する

        Args:
            dimension (int): 次数
            use_frac (bool, optional): 係数に分数を利用するか。通常はTrue

        Returns:
            sy.Add: 指定された次数が保証されたn次関数
        """
        x = sy.Symbol("x")
        function = self._random_number(use_frac=False, including_zero=False)
        for i in range(dimension):
            function += self._random_number(use_frac=use_frac) * (x ** i)
        function += self._random_number(use_frac=use_frac, including_zero=False) * (x ** dimension)
        return function
    
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
