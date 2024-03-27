from random import choice, randint, random
import re
from typing import Dict, Optional, Tuple, Union

import sympy as sy

class IntegralCalculationOfHighSchool3:
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
            - calculation_types: substitution_of_linear_expression(1次式の置換)などの計算ギミックの設定
            - used_formulas: n_dimension_function(n次関数)などの利用される積分公式の確認
        """
        sy.init_printing(order='grevlex')
        selected_integral_type = choice(settings["integral_types"])
        selected_calculation_type = choice(settings["calculation_types"])
        used_function = choice(settings["used_formula"])
        if selected_integral_type == "indefinite_integral":
            if selected_calculation_type == "substitution_of_linear_expression":
                self.latex_answer, self.latex_problem = self._make_indefinite_substitution_of_linear_expression_problem(used_function)
        elif selected_integral_type == "definite_integral":
            if selected_calculation_type == "substitution_of_linear_expression":
                self.latex_answer, self.latex_problem = self._make_definite_substitution_of_linear_expression_problem(used_function)

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
        linear_function = self._random_n_dimension_function(1, use_frac=False)
        if used_formula == "n_dimension_function":
            n = sy.Integer(randint(3, 6))
            k = self._random_number(use_frac=False, including_zero=False)
            f = k * (linear_function ** n)
            f_latex = sy.latex(f)
            f_down_latex = self._differentiate_latex(f)
            latex_answer, latex_problem = problem_and_answer(f_latex, f_down_latex)
        # k/(ax+b)
        elif used_formula == "1/x":
            n = sy.Integer(randint(1, 2))
            k = self._random_number(use_frac=False, including_zero=False)
            f = k * 1 / (linear_function)
            f_latex = sy.latex(f)
            f_down_latex = self._differentiate_latex(f)
            latex_answer, latex_problem = problem_and_answer(f_latex, f_down_latex)
        # k/(ax+b)^2
        elif used_formula == "1/x^2":
            f = k * sy.log(linear_function)
            pattern = r'\\left\((.*?)\\right\)'
            f_latex = re.sub(pattern, r'| \1 |', sy.latex(f))
            f_down_latex = self._differentiate_latex(f)
            latex_answer, latex_problem = problem_and_answer(f_latex, f_down_latex)
        elif used_formula == "sin":
            k = self._random_number(use_frac=True, including_zero=False)
            f = k * sy.sin(linear_function)
            f_latex = sy.latex(f)
            f_down_latex = self._differentiate_latex(f)
            latex_answer, latex_problem = problem_and_answer(f_latex, f_down_latex)
        elif used_formula == "cos":
            k = self._random_number(use_frac=True, including_zero=False)
            f = k * sy.cos(linear_function)
            f_latex = sy.latex(f)
            f_down_latex = self._differentiate_latex(f)
            latex_answer, latex_problem = problem_and_answer(f_latex, f_down_latex)
        return latex_answer, latex_problem
    
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

    def _differentiate_latex(self, function) -> str:
        """関数を微分し、latexを作成・出力するための関数

        Args:
            function: 微分対象となる関数
        
        Returns:
            f_down_latex (str): 微分された関数のlatex形式
        """
        x = sy.Symbol("x")
        f_down = sy.diff(function, x)
        f_down_latex = sy.latex(f_down)
        return f_down_latex
    
    def _random_n_dimension_function(self, dimension: int, use_frac: bool=True) -> sy.Add:
        """指定された次数のn次関数をランダムに出力する

        Args:
            dimension (int): 次数
            use_frac (bool, optional): 係数に分数を利用するか。通常はTrue

        Returns:
            sy.Add: 指定された次数が保証されたn次関数
        
        Developing:
            dimensionの指定はきっちりやった方が良いか、それとも最大最小で示される方が楽か？
                計算方法とかごりごりに変わりそう（部分積分など）だから、いったんはきっちりと次数を指定する形式で
            
            次数を順次追加していくときに、すべて分けずにやる方法はないか？
                どうせ繰り返し作業（係数決定、xをくっつける）なのだから、for文などで回すと良い？
        """
        x = sy.Symbol("x")
        function = 0
        for i in range(dimension):
            function += self._random_number(use_frac=use_frac) * (x ** i)
        function += self._random_number(use_frac=use_frac, including_zero=False) * (x ** dimension)
        return function
    
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
