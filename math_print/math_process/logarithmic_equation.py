from random import choice, random, randint
from typing import Dict, Optional, Tuple, Union


import sympy as sy


class LogarithmicEquation:
    """指定されたタイプの対数方程式の問題とその解答を出力
    
    Attributes:
        latex_answer (str): latex形式と通常の文字が混在した解答
        latex_problem (str): latex形式と通常の文字が混在した問題
    """
    def __init__(self, **settings: Dict) -> None:
        """初期設定
        
        Args:
            settings (dict): 問題の各種設定を格納
        
        Raises:
            ValueError: 想定されていない問題のタイプが混入したときに挙上
        """
        sy.init_printing(order='grevlex')
        problem_type = choice(settings["problem_types"])
        if problem_type == "only_with_calculation":
            self.latex_answer, self.latex_problem = self._make_only_with_calculation_problem()
        elif problem_type == "with_calculation_and_change_base_of_formula":
            self.latex_answer, self.latex_problem = self._make_with_calculation_and_change_base_of_formula_problem()
        elif problem_type == "with_replacement":
            self.latex_answer, self.latex_problem = self._make_with_replacement_problem()
        else:
            raise ValueError(f"problem_type is {problem_type}. This isn't expected value.")
    
    def _make_only_with_calculation_problem(self) -> Tuple[str, str]:
        """対数の計算のみを行う対数方程式の問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式と通常の文字が混在した解答
            latex_problem (str): latex形式と通常の文字が混在した問題
        
        Developing:
            log(a)(bx + c) = d
                b,cが整数でないとノイズになるっぽい
            
            log(a)(bx + c)(dx + e) = f
        """
        x = sy.Symbol("x", real=True)
        # selected_equation_type = choice(["log(a)(bx + c) = d", "log(a)(bx + c)(dx + e) = f"])
        selected_equation_type = "log(a)(bx + c)(dx + e) = f"
        if selected_equation_type == "log(a)(bx + c) = d":
            """
            log(a)(bx + c) = log(a)(a^d)
            bx + c = a^d
            bx = a^d - c
            x = (a^d - c) / b
                bx + c > 0
                    x > -c/b(b > 0)
                    x < -c/b(b < 0)
            a > 0
            b > 0
            c: any?
            d: int
            
            b,c: 分数だとノイジー？問題のバリエーションは出る
                ->とりあえず整数だけで
            c = 0
                ->場合分けが面倒ではある。
            
            結局バリュエーション最優先とするのであれば、分数も0も許容すべき
            """
            a = self._random_number(max_num=3, positive_or_negative="positive", remove_one=True, remove_zero=True)
            b = self._random_number(positive_or_negative="positive", remove_zero=True, )
            c = self._random_number()
            d = self._random_number(integer_or_frac="integer", max_num=4)
            if c == 0:
                latex_problem = f"\\( \\log_{{{sy.latex(a)}}} {sy.latex(b * x)} = {sy.latex(d)} \\)を満たす\\( x \\)を求めよ。"
            else:
                latex_problem = f"\\( \\log_{{{sy.latex(a)}}}\\left({sy.latex(b * x + c)}\\right) = {sy.latex(d)} \\)を満たす\\( x \\)を求めよ。"
            latex_answer = f"真数条件より、\\( {sy.latex(b * x + c)} > 0 \\)、すなわち\\( x > {sy.latex(sy.Rational(-c, b))} \\) でなければならない。\n"
            latex_answer += f"また、\\( {sy.latex(d)} = \\log_{{{sy.latex(a)}}} {sy.latex(a)}^{{{sy.latex(d)}}} = \\log_{{{sy.latex(a)}}} {sy.latex(a ** d)} \\)より、\n"
            if c == 0:
                latex_answer += f"与えられた対数方程式は、\\( \\log_{{{sy.latex(a)}}}{sy.latex(b * x)} = \\log_{{{sy.latex(a)}}} {sy.latex(a ** d)} \\)と書き換えられる。\n"
                latex_answer += f"真数同士を比較すると、\\( {sy.latex(b * x)} = {sy.latex(a ** d)} \\)となり、これを解くと、\n"
            else:
                latex_answer += f"与えられた対数方程式は、\\( \\log_{{{sy.latex(a)}}}\\left({sy.latex(b * x + c)}\\right) = \\log_{{{sy.latex(a)}}} {sy.latex(a ** d)} \\)と書き換えられる。\n"
                latex_answer += f"真数同士を比較すると、\\( {sy.latex(b * x + c)} = {sy.latex(a ** d)} \\)となり、これを解くと、\n"
            answer = (a ** d - c) / b
            latex_answer += f"\\( x = {sy.latex(answer)} \\)となる。これは\\( x > {sy.latex(sy.Rational(-b, c))} \\)を満たすので、解である。"
        elif selected_equation_type == "log(a)(bx + c)(dx + e) = f":
            """
            bdx^2 + (be + cd)x + ce - a^f = 0
            bx + c > 0, dx + e > 0
            [(a, (-\beta*c*d - c*e + 1)/(\alpha*(\beta*d + e)), c, d, e)]
            で通りそう
            
            f = 0, or 1で簡略化
            a = 0, 1は通らない
            
            一番シンプルな# f = 0かつb=d=1 <--> log_a(x+c)(x+e)=0から実装
            
            log_a(x+c)(x+e)=0
            alpha is answer, beta is not answer.
            [(a, (-\alpha**2 - \alpha*e + 1)/(\alpha + e), e)]
            c = (-\alpha**2 - \alpha*e + 1)/(\alpha + e)
            """
            # log_a(x + c)(x + e) = 0, 
            if random() > 0.5:
                answer1 = self._random_number(max_num=4, integer_or_frac="integer")
                answer2 = answer1 + self._random_number(max_num=4, integer_or_frac="integer", remove_zero=True)
                e = 1 - answer2
                a = self._random_number(max_num=3, integer_or_frac="integer", positive_or_negative="positive", remove_one=True, remove_zero=True)
                c_numerator = -answer1 * answer2 - answer1 * e + 1
                c_denominator = answer2 + e
                c = sy.Rational(c_numerator, c_denominator)
                left_bracket = x + c
                right_bracket = x + e
                antilog = sy.factor(left_bracket * right_bracket)
                latex_problem = f"\\( \\log_{{{sy.latex(a)}}} {sy.latex(antilog)} = 0 \\)を満たす\\( x \\)を求めよ。"
                left_bracket_min = -c
                right_bracket_min = -e
                if left_bracket_min > right_bracket_min:
                    smaller_x = right_bracket_min
                    larger_x = left_bracket_min
                else:
                    smaller_x = left_bracket_min
                    larger_x = right_bracket_min
                latex_answer = f"真数条件より、\\( {sy.latex(antilog)} > 0 \\)、すなわち\\( x < {sy.latex(smaller_x)}, x < {sy.latex(larger_x)} \\)でなければならない。"
                
            else:
                latex_answer = "dummy answer in _make_only_with_calculation_problem of log(a)(bx + c)(dx + e) = f"
                latex_problem = "dummy problem in _make_only_with_calculation_problem of log(a)(bx + c)(dx + e) = f"
        return latex_answer, latex_problem
    
    def _make_with_calculation_and_change_base_of_formula_problem(self):
        """対数の計算と底の変換を行う対数方程式の問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式と通常の文字が混在した解答
            latex_problem (str): latex形式と通常の文字が混在した問題
        """
        latex_answer = "dummy answer in _make_with_calculation_and_change_base_of_formula_problem"
        latex_problem = "dummy problem in _make_with_calculation_and_change_base_of_formula_problem"
        return latex_answer, latex_problem
    
    def _make_with_replacement_problem(self):
        """置換を伴う対数方程式の問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式と通常の文字が混在した解答
            latex_problem (str): latex形式と通常の文字が混在した問題
        """
        latex_answer = "dummy answer in _make_with_replacement_problem"
        latex_problem = "dummy problem in _make_with_replacement_problem"
        return latex_answer, latex_problem
    
    def _random_number(self, max_num: int = 6, integer_or_frac: Optional[str] = None, positive_or_negative: Optional[str] = None, remove_zero: Optional[bool] = False, remove_one: Optional[bool] = False) -> Union[sy.Integer, sy.Rational]:
        """指定された条件の数を出力し、底や真数などに利用

        Args:
            max_num (int, optional): 出力に利用する数の最大値. Defaults to 6.
            integer_or_frac (str, optional): 整数か分数かの指定. Defaults to None.
            positive_or_negative (str, optional): 正か負かの指定. Defaults to None.
            remove_zero (bool, optional): ゼロを除くか否か. Defaults to False
            remove_one (bool, optional): 1を除くか否か. Defaults to False.
        """
    
        def random_integer(max_num: int, positive_or_negative: str, remove_zero: bool, remove_one: bool) -> sy.Integer:
            """指定された条件の整数を出力し、底や真数などに利用する
            
            Args:
                max_num (int): 出力に利用する数の最大値
                positive_or_negative (str): 正負の指定。 
                remove_zero (bool): 0を除くかどうかの指定。 
                remove_one (bool): 1を除くかどうかの指定。
            
            Returns:
                integer (sy.Integer): 整数
            """
            if remove_one:
                # 0なし1なし
                if remove_zero:
                    integer = sy.Integer(randint(2, max_num))
                # 0あり1なし
                else:
                    candidates = [0] + list(range(2, max_num+1))
                    integer = sy.Integer(choice(candidates))
            else:
                # 0なし1あり
                if remove_zero:
                    integer = sy.Integer(randint(1, max_num))
                # 0あり1あり
                else:
                    integer = sy.Integer(randint(0, max_num))
            
            if positive_or_negative is None:
                if random() > 0.5:
                    integer *= -1
            elif positive_or_negative == "positive":
                pass
            elif positive_or_negative == "negative":
                integer *= -1
            else:
                raise ValueError(f"'positive_or_negative' is {positive_or_negative}. this isn't expected value.")
            return integer
        
        def random_frac(max_num: int, positive_or_negative: str) -> sy.Rational:
            """指定された条件の分数を出力し、底や真数などに利用する
            
            Args:
                max_num (int): 出力に利用する数の最大値
                positive_or_negative (str): 正負の指定。
            
            Returns:
                frac (sy.Rational): 分数
            """
            while True:
                numerator = randint(1, max_num)
                denominator = randint(1, max_num)
                frac = sy.Rational(numerator, denominator)
                if not(frac.is_integer):
                    break
            
            if positive_or_negative is None:
                if random() > 0.5:
                    frac *= -1
            elif positive_or_negative == "positive":
                pass
            elif positive_or_negative == "negative":
                frac *= -1
            else:
                raise ValueError(f"'positive_or_negative is {positive_or_negative}. this isn't expected value.")
            return frac
        
        if integer_or_frac is None:
            if random() > 0.5:
                number = random_integer(max_num=max_num, positive_or_negative=positive_or_negative, remove_zero=remove_zero, remove_one=remove_one)
            else:
                number = random_frac(max_num=max_num, positive_or_negative=positive_or_negative)
        elif integer_or_frac == "integer":
            number = random_integer(max_num=max_num, positive_or_negative=positive_or_negative, remove_zero=remove_zero, remove_one=remove_one)
        elif integer_or_frac == "frac":
            number = random_frac(max_num=max_num, positive_or_negative=positive_or_negative)
        else:
            raise ValueError(f"'integer_or_frac' is {integer_or_frac}. this isn't expected value.")
        return number
