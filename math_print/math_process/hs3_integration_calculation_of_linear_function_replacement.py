from collections import namedtuple
import math
from random import choice, randint, random, sample
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
            latex_answer = f"\\( ={function_latex_for_answer} + C \\)"
            latex_problem = f"\\( \\int {function_latex_for_problem} \\, dx \\)"
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
                
            4/11
            継続
            大枠はできたが、細かい問題が散見される
                値が無駄にでかい
                    3乗4乗を扱っているので仕方ないといえば仕方ないが、もう少し抑えないとシンプルな計算問題ではなくなってしまう
                定積分の途中表示がガバい
                    -(-a)のあたりが表現できていない。単純にこの段階をスキップするか、どこかの段階(latex化しているところ？)
                    で書き換える必要がある
                
                Invalid comparison of non-real 4*log(4) + 4*I*piが1/xで発生。
                おそらくlogの計算でひっかかった模様。
                    シンプルに考えれば、linear_functionを読み取った上で、それが0より大きくなるような範囲で積分範囲を設定する必要がある。
                    面倒そうではあるが、それ以前にそもそもこれは可能なのか？
                        ・真数は読み取れる？
                        あれこれやったらいけそう
            4/12
            引き続きlogに関連する問題
                値の取得は完了。あとは()を取り除く
            
            1/x^2の担当
            denom=0になる瞬間があるので、こちらもlog同様に関数の分母をなんとかかんとか取得してやる必要がありそう
            
            4/13
                ここまでの問題は大体解決
                次は、√xの積分でInvalid comparison of non-real 4*I/3が発生
                ->おそらく、これまでと同じようにルートの中身が負になっているから、個別に調整が必要そう
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
            original_function = definite_integral_information.original_function
            integral_of_function = definite_integral_information.integral_of_function
            end_value = definite_integral_information.end_value
            start_value = definite_integral_information.start_value
            result = definite_integral_information.result
            latex_problem = f"\\( \\int^{{{end}}}_{{{start}}} {original_function} \, dx \\)"
            latex_answer = f"\\( = \\left[ {integral_of_function} \\right]^{{{end}}}_{{{start}}} \\)\n"
            latex_answer += f"\\( = {end_value} - {start_value} \\) \n"
            latex_answer += f"\\( = {result} \\)"
            return latex_answer, latex_problem
        
        x = sy.Symbol("x")
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
        # setting value for definite integral
        if used_formula in ["sin", "cos", "1/cos^2x", "1/sin^2x"]:
            start_denominator = choice([2, 3, 4, 6])
            start_numerator = self._random_integer(max_abs = start_denominator * 2,  positive_or_negative="positive")
            start = sy.pi * sy.Rational(start_numerator, start_denominator)
            end_denominator = choice([2, 3, 4, 6])
            end_numerator = start_numerator + self._random_integer(max_abs = end_denominator * 2, positive_or_negative="positive")
            end = sy.pi * sy.Rational(end_numerator, end_denominator)
        elif used_formula == "1/x":
            def get_log_argument(expression):
                """logの真数部分を取得し、与えるべきxの判断材料とする

                Args:
                    expression: 式

                Returns:
                    1次式
                """
                if expression.func is sy.log:
                    return expression.args[0]
                elif expression.func is sy.Mul:
                    for arg in expression.args:
                        result = get_log_argument(arg)
                        if result is not None:
                            return result
                return None
            linear_function = get_log_argument(function)
            a = linear_function.coeff(x)
            b = linear_function.subs(x, 0)
            if a > 0:
                min_value = math.ceil(-b / a)
                start = randint(min_value + 1, min_value + 3)
                end = start + randint(1, 2)
            elif a < 0:
                max_value = math.floor(-b / a)
                end = randint(max_value - 3, max_value - 1)
                start = end - randint(1, 2)
            else:
                raise ValueError(f"a mustn't be 0. 'linear_function' is {linear_function}.")
        elif used_formula == "1/x^2":
            
            def find_singular_point(function):
                """分母を0にする点(極)を求めることで、無限大を出すことを防ぐ
                
                Args:
                    function (分数関数): 分母が1次関数である分数関数
                
                Returns:
                    singular_point (Union[sy.Integer, sy.Rational]): 分母を0にする
                """
                function_apart = sy.apart(function, x)
                linear_function = function_apart.as_numer_denom()[1]
                a = linear_function.coeff(x, 1)
                b = linear_function.subs(x, 0)
                # ax + b = 0
                singular_point = sy.Rational(-b, a)
                return singular_point

            singular_point = find_singular_point(function)
            candidates = [i for i in range(-5, 5) if i != singular_point]
            start, end = sorted(sample(candidates, 2))
        elif used_formula == "x^(1/2)":
            pass
        else:
            start = self._random_integer(max_abs=1)
            end = start + self._random_integer(max_abs=2, positive_or_negative="positive")
        end_latex = sy.latex(end)
        start_latex = sy.latex(start)
        original_function_latex = differentiated_function_latex
        integral_function_latex = function_latex
        end_value = function.subs(x, end)
        start_value = function.subs(x, start)
        result = end_value - start_value
        # for display check
        if used_formula == "1/x":
            pattern_for_removing_left_right = r"\\left\(|\\right\)"
            pattern_for_removing_bracket = r"log\{\((\d+)\)\}"
            after_removing = r"log{\1}"
            by_expression = re.sub(pattern_for_removing_left_right, "", sy.latex(end_value))
            if end_value >= 0:
                end_value_latex = re.sub(pattern_for_removing_bracket, after_removing, by_expression)
            else:
                end_value_latex = f"\\left( {re.sub(pattern_for_removing_bracket, after_removing, by_expression)} \\right)"
            by_expression = re.sub(pattern_for_removing_left_right, "", sy.latex(start_value))
            if start_value >= 0:
                start_value_latex = re.sub(pattern_for_removing_bracket, after_removing, by_expression)
            else:
                start_value_latex = f"\\left( {re.sub(pattern_for_removing_bracket, after_removing, by_expression)} \\right)"
            by_expression = re.sub(pattern_for_removing_left_right, "", sy.latex(result))
            result_latex = re.sub(pattern_for_removing_bracket, after_removing, by_expression)
        else:
            if end_value >= 0:
                end_value_latex = sy.latex(end_value)
            else:
                end_value_latex = f"\\left( {sy.latex(end_value)} \\right)"
            if start_value >= 0:
                start_value_latex = sy.latex(start_value)
            else:
                start_value_latex = f"\\left( {sy.latex(start_value)} \\right)"
            result_latex = sy.latex(result)
        information = DefiniteIntegralInformation(
            end=end_latex, start=start_latex,
            original_function=original_function_latex, integral_of_function=integral_function_latex,
            end_value=end_value_latex, start_value=start_value_latex,
            result=result_latex
        )
        latex_answer, latex_problem = problem_and_answer(information)
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
        a = self._random_integer(max_abs=2)
        b = self._random_integer(max_abs=2)
        linear_function = a * x + b
        if used_formula == "x^n":
            n = self._random_integer(min_abs=3, max_abs=4, positive_or_negative="positive")
            k = self._random_integer(min_abs=1, max_abs=2)
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
