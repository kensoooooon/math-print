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
            log(a)(bx + c)(dx + e) = f
        """
        x = sy.Symbol("x", real=True)
        selected_equation_type = choice(["log(a)(bx + c) = d", "log(a)(bx + c)(dx + e) = f"])
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
            """
            a = randint(2, 4)
            b = randint(1, 6)
            c = randint(0, 6)
            d = randint(1, 3)
            
        elif selected_equation_type == "log(a)(bx + c)(dx + e) = f":
            pass
        latex_answer = "dummy answer in _make_only_with_calculation_problem"
        latex_problem = "dummy problem in _make_only_with_calculation_problem"
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
    
    def _random_number(self, integer_or_frac=None, positive_or_negative=None, remove_zero=None, remove_one=None):
        # not one == not zero, frac, 

        if positive_or_negative is None:
            pass
        elif positive_or_negative == "positive":
            number = sy.Abs(number)
        elif positive_or_negative == "negative":
            number = -1 * sy.Abs(number)
        return number
    
    def _random_integer(self, positive_or_negative: Optional[str] = None, remove_zero: Optional[bool] = None, remove_one: Optional[bool]=None) -> sy.Integer:
        """指定された条件の整数を出力し、底や真数などに利用する
        
        Args:
            positive_or_negative (:obj:`str`, optional): 正負の指定。 Defaults to None.
            remove_zero (:obj:`bool`, optional): 1を除くかどうかの指定。 Defaults to None.
            remove_one (:obj:`bool`, optional): 1を除くかどうかの指定。 Defaults to None.
        """
        if remove_one is None:
            if remove_zero is None:
                integer = sy.Integer(randint(0, 6))
            else:
                integer = sy.Integer(randint(1, 6))
        else:
            if remove_zero is None:
                integer = sy.Integer(choice[0, 2, 3, 4, 5, 6])
            else:
                integer = sy.Integer(randint(2, 6))
        
        if positive_or_negative is None:
            pass
        elif positive_or_negative == "positive":
            integer = sy.Abs(integer)
        elif positive_or_negative == "negative":
            integer = -1 * sy.Abs(integer)
        return integer
        
    def _random_frac(self, positive_or_negative=None, remove_zero=None):
