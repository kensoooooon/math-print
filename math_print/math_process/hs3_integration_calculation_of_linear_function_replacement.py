from collections import namedtuple
from random import choice, randint, random
import re
from typing import Dict, NamedTuple, Optional, Tuple, Union

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
        return f"IntegralCalculationOfLinearFunctionReplacement(latex_answer: {self.latex_answer}, latex_problem: {self.latex_problem})"

    def _make_indefinite_substitution_of_linear_expression_problem(self, used_formula: str) -> Tuple[str, str]:
        """1次式の置換を用いるタイプの不定積分計算問題を作成

        Args:
            used_function (str): 使用される関数

        Returns:
            Tuple[str, str]: 問題と解答
            - latex_answer (str): latex形式と通常の文字列が混在していることを前提とした解答
            - latex_problem (str): latex形式と通常の文字列が混在していることを前提とした問題
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
            
            Note:
                1/xで出てくる積分の絶対値記号の追加や、a^xで出てくるlog(a)のカッコの消去など、特別な措置が必要なものは別枠にて文字列の処理
            """
            latex_answer = f"={function_latex_for_answer} + C"
            latex_problem = f"\\int {function_latex_for_problem} \\, dx"
            return latex_answer, latex_problem
    
        function, differentiated_function = self._make_and_differentiate_function(used_formula)
        if used_formula == "1/x":
            pattern = r'\\left\((.*?)\\right\)'
            function_latex = re.sub(pattern, r'| \1 |', sy.latex(function))
        elif used_formula == "a^x":
            pattern = r'\\log\\{\\left\((.*?)\\right\)\\}' 
            result = re.sub(pattern, r'log\1', sy.latex(function))
            result = re.sub(r'\\left\(|\\right\)', '', result)
            function_latex = re.sub(r'\s+', '', result)
        elif used_formula == "x^(1/2)":
            latex_str = sy.latex(function)
            sqrt_part = re.search(r"\\sqrt{[^}]+}", latex_str).group(0)
            if "\\cdot" in latex_str:
                other_part = re.sub(r"\\sqrt{[^}]+} \\cdot ", "", latex_str)
            else:
                other_part = re.sub(r"\\sqrt{[^}]+}", "", latex_str)
            function_latex = f"{other_part} {sqrt_part}"
        else:
            function_latex = sy.latex(function)
        differentiated_function_latex = sy.latex(differentiated_function)
        latex_answer, latex_problem = problem_and_answer(function_latex, differentiated_function_latex)
        return latex_answer, latex_problem

    def _make_definite_substitution_of_linear_expression_problem(self, used_formula: str) -> Tuple[str, str]:
        """1次式の置換を用いるタイプの定積分計算問題を作成
        
        Args:
            used_formula (str): 使用する公式
        
        Returns:
            Tuple[str, str]: latex形式の問題と解答
            - latex_answer (str): latex形式の解答
            - latex_problem (str): latex形式の問題
        
        Developing:
            4/8
            スタート
            まずは対応する式の形やproblem_and_answerを考える必要がある
                返ってくるのは関数(解答用)と微分された関数(問題用)
                    -> それにプラスして、積分範囲を設定し、問題の情報に追加
                    あわせて、積分計算を実施する。
                    ∫^{end}_{start} f'(x) dx = [f(x)]^{end}_{start} = value.
                
            4/10
            継続
            namedtupleに必要な要素とは？というお話
                積分元の関数, 積分先の関数, 
                積分範囲, それらを代入したときのそれぞれの値
                計算結果
                
                以上が必要そう。問題は渡し方だが、どこまでを委任するかが重要
                -> 不定積分での利用と、役割の収まりの良さを意識すると、全部文字列が良さそう
        """
        
        class DefiniteIntegralInformation(NamedTuple):
            """定積分に必要な情報を格納する

            Attributes:
                end (str): 積分範囲の終点
                start (str): 積分範囲の始点
                original_function (str): 積分前の関数
                integral_of_function (str): 積分後の関数
                end_value (str): 終点を代入したときの具体的な値
                start_value (str): 始点を代入したときの具体的な値
                result (str): 定積分の計算結果
            """
            end: str
            start: str
            original_function: str
            integral_of_function: str
            end_value: str
            start_value: str
            result: str
        
        def problem_and_answer(definite_integral_information: DefiniteIntegralInformation) -> Tuple[str, str]:
            """定積分用の問題と解答を出力
            
            Args:
                definite_integral_information (DefiniteIntegralInformation): 式を書くための情報を格納
            
            Returns:
                Tuple[str, str]: latex形式の問題と解答
                - latex_answer (str): 解答
                - latex_problem (str): 問題
            """
            end = definite_integral_information.end
            start = definite_integral_information.start
            original_function = definite_integral_information.start
            integral_of_function = definite_integral_information.integral_of_function
            end_value = definite_integral_information.end_value
            start_value = definite_integral_information.start_value
            result = definite_integral_information.result
            latex_problem = f"\\int^{{{end}}}_{{{start}}} {original_function} \, dx \n"
            latex_answer = f"= \\left[ {integral_of_function} \\right]^{{{end}}}_{{{start}}} \n"
            latex_answer += f"= {end_value} - {start_value} \n"
            latex_answer += f"= {result}"
            return latex_answer, latex_problem
        
        function, differentiated_function = self._make_and_differentiate_function(used_formula)
        if used_formula == "1/x":
            pattern = r'\\left\((.*?)\\right\)'
            function_latex = re.sub(pattern, r'| \1 |', sy.latex(function))
        elif used_formula == "a^x":
            pattern = r'\\log\\{\\left\((.*?)\\right\)\\}' 
            result = re.sub(pattern, r'log\1', sy.latex(function))
            result = re.sub(r'\\left\(|\\right\)', '', result)
            function_latex = re.sub(r'\s+', '', result)
        elif used_formula == "x^(1/2)":
            latex_str = sy.latex(function)
            sqrt_part = re.search(r"\\sqrt{[^}]+}", latex_str).group(0)
            if "\\cdot" in latex_str:
                other_part = re.sub(r"\\sqrt{[^}]+} \\cdot ", "", latex_str)
            else:
                other_part = re.sub(r"\\sqrt{[^}]+}", "", latex_str)
            function_latex = f"{other_part} {sqrt_part}"
        else:
            function_latex = sy.latex(function)
        differentiated_function_latex = sy.latex(differentiated_function)
        # setting for definite integral
        if used_formula in ["sin", "cos", "1/cos^2x", "1/sin^2x"]:
            start_denominator = choice([2, 3, 4, 6])
            start_numerator = self._random_integer(max_abs = start_denominator * 2,  positive_or_negative="positive")
            start = sy.pi * sy.Rational(start_numerator, start_denominator)
            end_denominator = choice([2, 3, 4, 6])
            end_numerator = start_numerator + self._random_integer(max_abs = end_denominator * 2, positive_or_negative="positive")
            end = sy.pi * sy.Rational(end_numerator, end_denominator)
        else:
            end = self._random_integer
        end_latex = sy.latex(end)
        start_latex = sy.latex(start)
        original_function_latex = differentiated_function_latex
        integral_function_latex = function_latex
        end_value = function.subs(x, end)
        end_value_latex = sy.latex(end_value)
        start_value = function.subs(x, start)
        start_value_latex = sy.latex(start_value)
        result = end_value - start_value
        result_latex = sy.latex(result)
        information = DefiniteIntegralInformation(
            
        )
    
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
        if used_formula == "x^n":
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
        elif used_formula == "e^x":
            k = self._random_number(use_frac=True, including_zero=False)
            function = k * sy.E ** linear_function
            differentiated_function = k * a * (sy.E ** linear_function)
        elif used_formula == "a^x":
            k = self._random_number(use_frac=True, including_zero=False)
            base = self._random_integer(min_abs=2, max_abs=8, positive_or_negative="positive")
            function = k * (base ** linear_function) / sy.log(base)
            differentiated_function = k * a * (base ** linear_function)
        elif used_formula == "1/x^(1/2)":
            k = self._random_number(use_frac=True, including_zero=False)
            function = k * 2 * sy.sqrt(linear_function)
            differentiated_function = k * a * (1 / sy.sqrt(linear_function))
        elif used_formula == "x^(1/2)":
            k = self._random_number(use_frac=True, including_zero=False)
            function = k * sy.Rational(2, 3) * linear_function * sy.sqrt(linear_function)
            differentiated_function = k * a * sy.sqrt(linear_function)
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
