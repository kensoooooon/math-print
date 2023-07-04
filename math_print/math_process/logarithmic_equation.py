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
        # selected_equation_type = choice(["log(a)(bx + c) = d", "log(a)(x + b)(x + c) = d", "log(a)(x + b) + log(a)(x + c) = d", "log(x)(a) = b"])
        selected_equation_type = "log(a)(x + b) + log(a)(x + c) = d"
        if selected_equation_type == "log(a)(bx + c) = d":
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
        elif selected_equation_type == "log(a)(x + b)(x + c) = d":
            smaller_answer = self._random_number(max_num=3, integer_or_frac="integer")
            bigger_answer = smaller_answer + self._random_number(max_num=3, integer_or_frac="integer", positive_or_negative="positive", remove_zero=True)
            smaller_k = self._random_number(max_num=2, integer_or_frac="integer", positive_or_negative="positive")
            bigger_k = smaller_k + self._random_number(max_num=2, integer_or_frac="integer", positive_or_negative="positive", remove_zero=True)
            before = (x - (smaller_answer - smaller_k)) * (x - (bigger_answer + smaller_k))
            after = (x - (smaller_answer - bigger_k)) * (x - (bigger_answer + bigger_k))
            diff = sy.expand(before - after)
            diff_dict = sy.factorint(diff)
            if len(diff_dict.keys()) != 1:
                base = diff
                constant = 1
            else:
                for key, value in diff_dict.items():
                    base = key
                    constant = value
            left_antilog = x - (smaller_answer - smaller_k)
            right_antilog = x - (bigger_answer + smaller_k)
            if (left_antilog != x) and (right_antilog == x):
                latex_problem = f"\\( \\log_{{{sy.latex(base)}}} \\left( {sy.latex(left_antilog)} \\right) {sy.latex(right_antilog)} = {sy.latex(constant)} \\)を満たす\\( x \\)を求めよ。"
                latex_answer = f"真数条件より、\\( \\left( {sy.latex(left_antilog)} \\right) {sy.latex(right_antilog)} > 0 \\)、すなわち\\( x < {sy.latex(smaller_answer - smaller_k)}, {sy.latex(bigger_answer + smaller_k)} < x\\)でなければならない。\n"
            elif (left_antilog == x) and (right_antilog != x):
                latex_problem = f"\\( \\log_{{{sy.latex(base)}}}  {sy.latex(left_antilog)}  \\left( {sy.latex(right_antilog)} \\right) = {sy.latex(constant)} \\)を満たす\\( x \\)を求めよ。"
                latex_answer = f"真数条件より、\\( {sy.latex(left_antilog)}  \\left( {sy.latex(right_antilog)} \\right) > 0 \\)、すなわち\\( x < {sy.latex(smaller_answer - smaller_k)}, {sy.latex(bigger_answer + smaller_k)} < x\\)でなければならない。\n"
            else:
                latex_problem = f"\\( \\log_{{{sy.latex(base)}}} \\left( {sy.latex(left_antilog)} \\right) \\left( {sy.latex(right_antilog)} \\right) = {sy.latex(constant)} \\)を満たす\\( x \\)を求めよ。"
                latex_answer = f"真数条件より、\\( \\left( {sy.latex(left_antilog)} \\right) \\left( {sy.latex(right_antilog)} \\right) > 0 \\)、すなわち\\( x < {sy.latex(smaller_answer - smaller_k)}, {sy.latex(bigger_answer + smaller_k)} < x\\)でなければならない。\n"
            latex_answer += f"また、\\( {sy.latex(constant)} = \\log_{{{sy.latex(base)}}} {sy.latex(base)}^{{{sy.latex(constant)}}} = \\log_{{{sy.latex(base)}}} {sy.latex(base ** constant)} \\)より、\n"
            if (left_antilog != x) and (right_antilog == x):
                latex_answer += f"与えられた対数方程式は、\\( \\log_{{{sy.latex(base)}}} \\left( {sy.latex(left_antilog)} \\right) {sy.latex(right_antilog)} = \\log_{{{sy.latex(base)}}} {sy.latex(base ** constant)} \\)と書き換えられる。\n"
                latex_answer += f"真数同士を比較すると、\\( \\left( {sy.latex(left_antilog)} \\right) {sy.latex(right_antilog)} = {sy.latex(base ** constant)} \\)となり、これを解くと、\n"
            elif (left_antilog == x) and (right_antilog != x):
                latex_answer += f"与えられた対数方程式は、\\( \\log_{{{sy.latex(base)}}}  {sy.latex(left_antilog)}  \\left( {sy.latex(x - (bigger_answer - smaller_k))} \\right) = \\log_{{{sy.latex(base)}}} {sy.latex(base ** constant)} \\)と書き換えられる。\n"
                latex_answer += f"真数同士を比較すると、\\( {sy.latex(left_antilog)}  \\left( {sy.latex(right_antilog)} \\right) = {sy.latex(base ** constant)} \\)となり、これを解くと、\n"
            else:
                latex_answer += f"与えられた対数方程式は、\\( \\log_{{{sy.latex(base)}}} \\left( {sy.latex(left_antilog)} \\right) \\left( {sy.latex(right_antilog)} \\right) = \\log_{{{sy.latex(base)}}} {sy.latex(base ** constant)} \\)と書き換えられる。\n"
                latex_answer += f"真数同士を比較すると、\\( \\left( {sy.latex(left_antilog)} \\right)  \\left( {sy.latex(right_antilog)} \\right) = {sy.latex(base ** constant)} \\)となり、これを解くと、\n"
            latex_answer += f"\\( {sy.latex(sy.expand(after))} = 0\\)\n"
            latex_answer += f"\\( {sy.latex(sy.factor(after))} = 0\\)\n"
            latex_answer += f"\\( x = {sy.latex(smaller_answer - bigger_k)}, {sy.latex(bigger_answer + bigger_k)} \\)\n"
            latex_answer += f"\\( x < {sy.latex(smaller_answer - smaller_k)}, {sy.latex(bigger_answer + smaller_k)} < x \\)より、\\( x =  {sy.latex(smaller_answer - bigger_k)}, {sy.latex(bigger_answer + bigger_k)} \\)"
        elif selected_equation_type == "log(x)(a) = b":
            base = self._random_number(max_num=5, integer_or_frac="integer", positive_or_negative="positive", remove_zero=True, remove_one=True)
            right = self._random_number(max_num=4, integer_or_frac="integer", remove_zero=True)
            antilog = base ** right
            latex_problem = f"\\( \\log_{{{sy.latex(x)}}} {sy.latex(antilog)} = {right} \\)を満たす\\( x \\)を求めよ。"
            latex_answer = f"底の条件より、\\( x > 0, x \\neq 1 \\)でなければならない。\n"
            latex_answer += f"また、\\( \\log_{{{sy.latex(x)}}} {sy.latex(antilog)} = {right} \\)より、\\( x^{{{sy.latex(right)}}} = {sy.latex(antilog)} \\)が成り立つ。\n"
            if right < 0:
                latex_answer += f"これを変形すると、\\( x^{{{sy.latex(-right)}}} = {sy.latex(sy.Rational(1, antilog))} \\)となる。\n"
            if (right % 2 == 0):
                latex_answer += f"よって、\\( x = \\pm {sy.latex(base)} \\)である。\\( x > 0, x \\neq 1 \\)より、\\( x = {sy.latex(base)} \\)"
            else:
                latex_answer += f"よって、\\( x = {sy.latex(base)} \\)である。これは\\( x > 0, x \\neq 1 \\)を満たす。"
        elif selected_equation_type == "log(a)(x + b) + log(a)(x + c) = d":
            smaller_answer = self._random_number(max_num=3, integer_or_frac="integer")
            bigger_answer = smaller_answer + self._random_number(max_num=3, integer_or_frac="integer", positive_or_negative="positive", remove_zero=True)
            smaller_k = self._random_number(max_num=2, integer_or_frac="integer", positive_or_negative="positive")
            bigger_k = smaller_k + self._random_number(max_num=2, integer_or_frac="integer", positive_or_negative="positive", remove_zero=True)
            before_left = x - (smaller_answer - smaller_k)
            before_right = x - (bigger_answer + smaller_k)
            after_left = x - (smaller_answer - bigger_k)
            after_right = x - (bigger_answer + bigger_k)
            before = before_left * before_right
            after = after_left * after_right
            diff = sy.expand(before - after)
            diff_dict = sy.factorint(diff)
            if len(diff_dict.keys()) != 1:
                base = diff
                constant = 1
            else:
                for key, value in diff_dict.items():
                    base = key
                    constant = value
            if (before_left != x) and (before_right == x):
                latex_problem = f"\\( \\log_{{{sy.latex(base)}}} \\left( {sy.latex(before_left)} \\right) + \\log_{{{sy.latex(base)}}} {sy.latex(before_right)} = {sy.latex(constant)} \\)を満たす\\( x \\)を求めよ。"
            elif (before_left == x) and (before_right != x):
                latex_problem = f"\\( \\log_{{{sy.latex(base)}}}  {sy.latex(before_left)}  + \\log_{{{sy.latex(base)}}} \\left( {sy.latex(before_right)} \\right) = {sy.latex(constant)} \\)を満たす\\( x \\)を求めよ。"
            else:
                latex_problem = f"\\( \\log_{{{sy.latex(base)}}} \\left( {sy.latex(before_left)} \\right) + \\log_{{{sy.latex(base)}}} \\left( {sy.latex(before_right)} \\right) = {sy.latex(constant)} \\)を満たす\\( x \\)を求めよ。"
            latex_answer = f"真数条件より、\\( {sy.latex(before_left)} > 0 \\)かつ\\( {sy.latex(before_right)} > 0 \\)、すなわち\\( x > {sy.latex(bigger_answer + smaller_k)} \\)でなければならない。\n"
            latex_answer += f"\\( {sy.latex(constant)} = \\log_{{{sy.latex(base)}}} {sy.latex(base)}^{{{sy.latex(constant)}}} = \\log_{{{sy.latex(base)}}} {sy.latex(base ** constant)} \\)より、\n"
            if (before_left != x) and (before_right == x):
                latex_answer += f"与えられた対数方程式は、\\( \\log_{{{sy.latex(base)}}} \\left( {sy.latex(before_left)} \\right) {sy.latex(before_right)} = \\log_{{{sy.latex(base)}}} {sy.latex(base ** constant)} \\)と書き換えられる。\n"
                latex_answer += f"真数同士を比較すると、\\( \\left( {sy.latex(before_left)} \\right) {sy.latex(before_right)} = {sy.latex(base ** constant)} \\)となり、これを解くと、\n"
            elif (before_left == x) and (before_right != x):
                latex_answer += f"与えられた対数方程式は、\\( \\log_{{{sy.latex(base)}}}  {sy.latex(before_left)}  \\left( {sy.latex(x - (bigger_answer - smaller_k))} \\right) = \\log_{{{sy.latex(base)}}} {sy.latex(base ** constant)} \\)と書き換えられる。\n"
                latex_answer += f"真数同士を比較すると、\\( {sy.latex(before_left)}  \\left( {sy.latex(before_right)} \\right) = {sy.latex(base ** constant)} \\)となり、これを解くと、\n"
            else:
                latex_answer += f"与えられた対数方程式は、\\( \\log_{{{sy.latex(base)}}} \\left( {sy.latex(before_left)} \\right) \\left( {sy.latex(before_right)} \\right) = \\log_{{{sy.latex(base)}}} {sy.latex(base ** constant)} \\)と書き換えられる。\n"
                latex_answer += f"真数同士を比較すると、\\( \\left( {sy.latex(before_left)} \\right)  \\left( {sy.latex(before_right)} \\right) = {sy.latex(base ** constant)} \\)となり、これを解くと、\n"
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
