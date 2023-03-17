"""
operator(checkbox)
    plus
    minus

number type(checkbox)
    one_digit_integer
    two_digit_integer
    decimal
    frac

term (radio button -> checkbox?)
1 ~ 6


"""
from random import choice, randint

import sympy as sy

class NumberWithoutBracketCalculateProblem:
    """指定された演算と数と項で、和と差の問題を出力
    
    Attributes:
    _operators_to_use (list): 計算に用いられる演算(plus, minus)
    _numbers_to_use (list): 計算に用いられる数のタイプ(one_digit_integer, two_digit_integer, frac, decimal)
    _term_numbers (list): 計算に用いられる項数の候補(2~6)
    _latex_answer (str): latex形式で記述された解答
    _latex_problem (str): latex形式で記述された問題
    """
    def __init__(self, **settings):
        """初期化
        
        Args:
            settings (dict): 問題の設定が格納された辞書
        """
        sy.init_printing(order='grevlex')
        self._operators_to_use = settings["operators_to_use"]
        self._numbers_to_use = settings["numbers_to_use"]
        self._term_numbers = settings["term_numbers"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        """問題作成のコントローラ
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        latex_answer = "fugafuga"
        latex_problem = "hogehoge"
        return latex_answer, latex_problem

    def _float_display_checker(self, frac):
        """使用される数に分数が入っておらず、かつ整数でもないとき、かつ有限小数のときに小数表示に切り替える
        
        Args:
            frac (Union[sy.Integer, sy.Rational]): 変換対象の数
        
        Return:
            number_latex (str): チェックを経たlatex形式で表示された数
        """
        def _is_finite_decimal(rational_number):
            """有限小数か否かを判定

            Args:
                rational_number (sy.Rational): 判定したい分数

            Returns:
                (bool): 有限小数ならTrue, 無限小数ならFalse
            """
            denominator_list = list(sy.factorint(rational_number.denominator).keys())
            denominator_set = set(denominator_list)
            if denominator_set == set():
                return True
            elif denominator_set == {2}:
                return True
            elif denominator_set == {5}:
                return True
            elif denominator_set == {2, 5}:
                return True
            else:
                return False
        
        if ("frac" not in self._used_number_list) and (frac.denominator != 1) and (_is_finite_decimal(frac)):
            number_latex = sy.latex(sy.Float(frac))
        else:
            number_latex = sy.latex(frac)
        return number_latex
