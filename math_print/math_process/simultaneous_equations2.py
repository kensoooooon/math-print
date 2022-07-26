"""
# randomのやつ
import sympy as sy

from pprint import pprint
from random import choice, randint, random
from time import perf_counter

def random_num_maker(used_coefficients, max_num=3, min_num=-3):

    def _make_random_frac(max_num=6, min_num=-6):

        checker = random()
        if checker > 0.5:
            numerator = randint(2, max_num)
            denominator = randint(2, max_num)
        else:
            numerator = randint(min_num, -2)
            denominator = randint(2, max_num)

        frac = sy.Rational(numerator, denominator)

        frac_latex = sy.latex(frac)
        return frac, frac_latex

    def _make_random_decimal(max_num=60, min_num=-60):

        checker = random()
        if checker > 0.5:
            numerator = randint(1, max_num)
        else:
            numerator = randint(min_num, -1)

        if numerator % 10 == 0:
            numerator += randint(1, 5)
        frac_as_decimal = sy.Rational(numerator, 10)
        decimal = float(frac_as_decimal)
        decimal_latex = sy.latex(decimal)
        return frac_as_decimal, decimal_latex

    def _make_random_integer(max_num=6, min_num=-6):

        checker = random()
        if checker > 0.5:
            numerator = randint(1, max_num)
        else:
            numerator = randint(min_num, -1)

        integer = sy.Integer(numerator)
        integer_latex = sy.latex(integer)
        return integer, integer_latex
    
    number_type = choice(used_coefficients)
    if number_type == "integer":
        num, num_latex = _make_random_integer(max_num=max_num, min_num=min_num)
    elif number_type == "frac":
        num, num_latex = _make_random_frac(max_num=max_num, min_num=min_num)
    elif number_type == "decimal":
        num, num_latex = _make_random_decimal(max_num=max_num * 5, min_num=min_num * 5)
    return num, num_latex

def denominator_checker(numbers_list):
    for number in numbers_list:
        denominator = number.denominator
        numerator = number.numerator
        if (denominator >= 10) or (numerator >=10) or (numerator <= -10):
            return False
    else:
        return True

start_time = perf_counter()

used_coefficients = ["integer", "frac", "decimal"]

x, y = sy.symbols("x y")

all_numbers_list = []
for _ in range(100):
    while True:

        a1, _ = random_num_maker(used_coefficients)
        b1, _ = random_num_maker(used_coefficients)
        c1, _ = random_num_maker(used_coefficients)

        a2, _ = random_num_maker(used_coefficients)
        b2, _ = random_num_maker(used_coefficients)
        c2, _ = random_num_maker(used_coefficients)

        eq1 = sy.Eq(a1 * x + b1 * y, c1)
        eq2 = sy.Eq(a2 * x + b2 * y, c2)
        answers = sy.solve([eq1, eq2], [x, y])
        if (isinstance(answers, list)):
            continue
        # print(answers)
        if y in answers.keys():
            x_value, y_value = answers.values()
        else:
            pass
        numbers = [a1, b1, c1, a2, b2, c2, x_value, y_value]
        
        if denominator_checker(numbers):
            break
    # print(f"numbers have been appended: {numbers}")
    all_numbers_list.append(numbers)
    print("------------------------")
    

end_time = perf_counter()
print(f"time: {end_time - start_time}")
print(f"count: {len(all_numbers_list)}")
pprint(all_numbers_list)
"""
from random import choice, randint, random

import sympy as sy


class SimultaneousEquations:
    """連立方程式を出力する(解の指定なし)
    
    Attributes:
        _used_coefficients (list): 優先的に使用される係数(整数, 分数, 小数)
        _equation_types (list): 連立方程式の形式(ax+by=c, ax+by=c+dx+ey, ax+by=c+f(dx+ey))
        # _answer_type (str): (整数解のみ, 分数解も含む)
        latex_answer (str): latex形式で記述された解答
        latex_problem (str): latex形式で記述された問題
    """
    def __init__(self, **settings):
        """
        Args:
            settings (dict): 問題の設定
        """
        sy.init_printing(order='grevlex')
        self._used_coefficients = settings["used_coefficients"]
        self._equation_types = settings["equation_types"]
        # self._answer_type = settings["answer_type"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        """問題作成のコントローラー

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        Note:
            解を指定しない代わりに、係数をしっかりと指定するタイプ
        """
        x = sy.Symbol("x", real=True)
        y = sy.Symbol("y", real=True)
        while True:
            equations_list = []
            latex_equations_list = []
            for _ in range(2):
                selected_equation_type = choice(self._equation_types)
                if selected_equation_type == "ax+by=c":
                    equation, latex_equation = self._make_simple_problem(x, y)
                elif selected_equation_type == "ax+by=c+dx+ey":
                    equation, latex_equation = self._make_including_transposition_problem(x, y)
                elif selected_equation_type == "ax+by=c+d(ex+fy)":
                    equation, latex_equation = self._make_including_expansion_and_transposition_problem(x, y)
                equations_list.append(equation)
                latex_equations_list.append(latex_equation)
            equation1, equation2 = equations_list
            latex_equation1, latex_equation2 = latex_equations_list
            latex_problem = f"{latex_equation1} \\\\ {latex_equation2}"
            answers = sy.solve([equation1, equation2], [x, y])
            if (x not in answers.keys()) or (y not in answers.keys()):
                continue
            x_latex = sy.latex(answers[x])
            y_latex = sy.latex(answers[y])
            latex_answer = f"x = {x_latex}, y = {y_latex}"
            break
        return latex_answer, latex_problem
    
    def _make_simple_problem(self, x, y):
        """ax+by=c型の方程式を出力
        
        Args:
            x (sy.Symbol): 変数x
            y (sy.Symbol): 変数y
        
        Returns:
            equation (sy.Eq): 方程式
            latex_equation (str): latex形式で記述された方程式
        
        Note:
            cは登場する係数に小数しか選択されていない場合、かつ有限小数で、さらに整数でない時だけfloat型に変換する
        """
        a, a_latex = self._random_num_maker()
        b, b_latex = self._random_num_maker()
        c, c_latex = self._random_num_maker()
        if (self._used_coefficients == ["decimal"]) and (self._is_finite_decimal(c)) and (not(c.is_Integer)):
            c_latex = sy.latex(float(c))
        else:
            c_latex = sy.latex(c)
            
        latex_equation = ""
        if a == 1:
            latex_equation += "x"
        elif a == -1:
            latex_equation += "-x"
        else:
            latex_equation += f"{a_latex}x"

        if b == 1:
            latex_equation += " +y"
        elif b == -1:
            latex_equation += " -y"
        elif b > 0:
            latex_equation += f"+ {b_latex}y"
        else:
            latex_equation += f"{b_latex}y"
        
        latex_equation += f" = {c_latex}"
        
        equation = sy.Eq(a * x + b * y, c)
        
        return equation, latex_equation
    
    def _make_including_transposition_problem(self, x, y):
        """ax+by=c+dx+ey型の方程式を出力

        Args:
            x (sy.Symbol): 変数x
            y (sy.Symbol): 変数y
        
        Returns:
            equation (sy.Eq): 方程式
            latex_equation (str): latex形式で記述された方程式

        Note:
            cは登場する係数に小数しか選択されていない場合、かつ有限小数で、さらに整数でない時だけfloat型に変換する
        """
        while True:     
            a, a_latex = self._random_num_maker()
            b, b_latex = self._random_num_maker()
            c, c_latex = self._random_num_maker()
            d, d_latex = self._random_num_maker()
            e, e_latex = self._random_num_maker()
            if (a != d) and (b != e):
                break
        if (self._used_coefficients == ["decimal"]) and (self._is_finite_decimal(c)) and (not(c.is_Integer)):
            c_latex = sy.latex(float(c))
        else:
            c_latex = sy.latex(c)
    
        latex_equation = ""
        if a == 1:
            latex_equation += "x"
        elif a == -1:
            latex_equation += "- x"
        else:
            latex_equation += f"{a_latex}x"

        if b == 1:
            latex_equation += " + y"
        elif b == -1:
            latex_equation += " - y"
        elif b > 0:
            latex_equation += f" + {b_latex}y"
        else:
            latex_equation += f" {b_latex}y"
        
        latex_equation += f" = {c_latex}"
        
        if d == 1:
            latex_equation += " + x"
        elif d == -1:
            latex_equation += " - x"
        elif d > 0:
            latex_equation += f" + {d_latex}x"
        else:
            latex_equation += f" {d_latex}x"

        if e == 1:
            latex_equation += " + y"
        elif e == -1:
            latex_equation += " - y"
        elif e > 0:
            latex_equation += f" + {e_latex}y"
        else:
            latex_equation += f" {e_latex}y"
        
        equation = sy.Eq(a * x + b * y, c + d * x + e * y)
        
        return equation, latex_equation

    def _make_including_expansion_and_transposition_problem(self, x, y):
        """ax+by=c+d(ex+fy)型の方程式を出力

        Args:
            x (sy.Symbol): 変数x
            y (sy.Symbol): 変数y
        
        Returns:
            equation (sy.Eq): 方程式
            latex_equation (str): latex形式で記述された方程式

        Note:
            cは登場する係数に小数しか選択されていない場合、かつ有限小数で、さらに整数でない時だけfloat型に変換する
        """
        while True:
            a, a_latex = self._random_num_maker()
            b, b_latex = self._random_num_maker()
            c, c_latex = self._random_num_maker()
            d, d_latex = self._random_num_maker()
            e, e_latex = self._random_num_maker()
            f, f_latex = self._random_num_maker()
            if (a != d * e) and (b != d *f):
                break
        if (self._used_coefficients == ["decimal"]) and (self._is_finite_decimal(c)) and (not(c.is_Integer)):
            c_latex = sy.latex(float(c))
        else:
            c_latex = sy.latex(c)
        
        latex_equation = ""
        latex_equation = ""
        if a == 1:
            latex_equation += "x"
        elif a == -1:
            latex_equation += "- x"
        else:
            latex_equation += f"{a_latex}x"

        if b == 1:
            latex_equation += " + y"
        elif b == -1:
            latex_equation += " - y"
        elif b > 0:
            latex_equation += f" + {b_latex}y"
        else:
            latex_equation += f" {b_latex}y"
        
        latex_equation += f" = {c_latex}"
        
        if d == 1:
            latex_equation += f"+ \\left("
        elif d == -1:
            latex_equation += f"- \\left("
        elif d > 0:
            latex_equation += f"+ {d_latex}\\left("
        else:
            latex_equation += f"{d_latex}\\left("
        
        if e == 1:
            latex_equation += " x"
        elif e == -1:
            latex_equation += " - x"
        elif e > 0:
            latex_equation += f" {e_latex}x"
        else:
            latex_equation += f" {e_latex}x"

        if f == 1:
            latex_equation += " + y \\right)"
        elif f == -1:
            latex_equation += " - y \\right)"
        elif f > 0:
            latex_equation += f" + {f_latex}y \\right)"
        else:
            latex_equation += f" {f_latex}y \\right)"
        
        # ax+by=c+d(ex+fy)
        equation = sy.Eq(a * x + b * y, c + d * (e * x + f * y))
        
        return equation, latex_equation

    def _random_num_maker(self, max_num=6, min_num=-6):
        """問題設定と最大最小から任意の数を値とlatex形式でランダムに出力

        Args:
            max_num (int, optional): 最大値
            min_num (int, optional): 最小値

        Returns:
            num (sy.Integer or sy.Rational): 計算に用いる数
            num_latex (str): 表記に用いる数
        
        Note:
            _make_random_decimalは、分母10で計算されるため、最大最小を5倍している
            
        Caution:
            小数についてはnumがsy.Rational型で、num_latexは小数を変換した文字列である食い違いに注意
        """
        number_type = choice(self._used_coefficients)
        if number_type == "integer":
            num, num_latex = self._make_random_integer(max_num=max_num, min_num=min_num)
        elif number_type == "frac":
            num, num_latex = self._make_random_frac(max_num=max_num, min_num=min_num)
        elif number_type == "decimal":
            num, num_latex = self._make_random_decimal(max_num=max_num * 5, min_num=min_num * 5)
        return num, num_latex
    
    def _make_random_frac(self, max_num=6, min_num=-6):
        """ランダムな分数を返す

        Args:
            max_num (int, optional): 分母と分子の最大値
            min_num (int, optional): 分母と分子の最小値

        Returns:
            frac (sy.Rational): 分数
            frac_latex (str): latex形式で記述された分数
        """
        checker = random()
        if checker > 0.5:
            numerator = randint(2, max_num)
            denominator = randint(2, max_num)
        else:
            numerator = randint(min_num, -2)
            denominator = randint(2, max_num)
        
        frac = sy.Rational(numerator, denominator)
    
        frac_latex = sy.latex(frac)
        return frac, frac_latex
        
    def _make_random_decimal(self, max_num=60, min_num=-60):
        """ランダムで小数を返す

        Args:
            max_num (int, optional): 小数作成用分数の分子の最大値
            min_num (int, optional): 小数作成用分数の分子の最小値
        Returns:
            frac_as_decimal (sy.Rational): 計算に用いる分数
            decimal_latex (str): 表記に用いる小数
        Note:
            計算自体は分数で行うため、表記に用いているものと型が違うことに注意
        """
        checker = random()
        if checker > 0.5:
            numerator = randint(1, max_num)
        else:
            numerator = randint(min_num, -1)
        
        if numerator % 10 == 0:
            numerator += randint(1, 5)
        frac_as_decimal = sy.Rational(numerator, 10)
        decimal = float(frac_as_decimal)
        decimal_latex = sy.latex(decimal)
        return frac_as_decimal, decimal_latex
    
    def _make_random_integer(self, max_num=6, min_num=-6):
        """ランダムな整数を作成する

        Args:
            max_num (int, optional): 値の最大値
            min_num (int, optional): 値の最小値

        Returns:
            integer (sy.Integer): 計算に用いる整数
            integer_latex (str): 表示に用いる整数
        """
        checker = random()
        if checker > 0.5:
            numerator = randint(1, max_num)
        else:
            numerator = randint(min_num, -1)
        
        integer = sy.Integer(numerator)
        integer_latex = sy.latex(integer)
        return integer, integer_latex
    
    def _is_finite_decimal(self, rational_number):
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
