from random import choice, randint, random

import sympy as sy


class SimultaneousEquations:
    """連立方程式を出力する
    
    Attributes:
        _used_coefficients (list): 優先的に使用される係数(整数, 分数, 小数)
        _equation_types (list): 連立方程式の形式(ax+by=c, ax+by=c+dx+ey, ax+by=c+f(dx+ey))
        _answer_type (str): (整数解のみ, 分数解も含む)
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
        self._answer_type = settings["answer_type"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        """問題作成のコントローラー

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        Note:
            解を決定して、それに沿うような方程式を作成するという順序で進む
        """
        (answer1, answer1_latex), (answer2, answer2_latex) = self._make_two_answers(self._answer_type)
        latex_answer = f"x = {answer1_latex}, y = {answer2_latex}"
        
        equations_list = []
        for _ in range(2):
            selected_equation_type = choice(self._equation_types)
            if selected_equation_type == "ax+by=c":
                latex_equation = self._make_simple_problem(answer1, answer2)
            elif selected_equation_type == "ax+by=c+dx+ey":
                latex_equation = self._make_including_transposition_problem(answer1, answer2)
            elif selected_equation_type == "ax+by=c+d(ex+fy)":
                latex_equation = self._make_including_expansion_and_transposition_problem(answer1, answer2)
            equations_list.append(latex_equation)
        latex_equation1, latex_equation2 = equations_list
        latex_problem = f"{latex_equation1} \\\\ {latex_equation2}"
        return latex_answer, latex_problem

    def _make_two_answers(self, answer_type):
        """2つの解を選択された解のタイプに基づいて出力

        Args:
            answer_type (str): 解のタイプ("only_integer", "including_fraction")

        Returns:
            answer1 (sy.Integer or sy.Rational): 計算に用いる1つ目の解
            answer1_latex (str): 表示に用いる1つ目の解
            answer2 (sy.Integer or sy.Rational): 計算に用いる2つ目の解
            answer2_latex (str): 表示に用いる2つ目の解
        """
        if answer_type == "only_integer":
            answer1, answer1_latex = self._make_random_integer()
            answer2, answer2_latex = self._make_random_integer()
        elif answer_type == "including_fraction":
            num_checker = random()
            if num_checker < 0.25:
                answer1, answer1_latex = self._make_random_integer()
                answer2, answer2_latex = self._make_random_integer()
            elif 0.25 <= num_checker < 0.5:
                answer1, answer1_latex = self._make_random_frac()
                answer2, answer2_latex = self._make_random_integer()
            elif 0.5 <= num_checker < 0.75:
                answer1, answer1_latex = self._make_random_integer()
                answer2, answer2_latex = self._make_random_frac()
            else:
                answer1, answer1_latex = self._make_random_frac()
                answer2, answer2_latex = self._make_random_frac()
        return (answer1, answer1_latex), (answer2, answer2_latex)
    
    def _make_simple_problem(self, answer1, answer2):
        """ax+by=c型の問題文を出力する

        Args:
            answer1 (sy.Integer or sy.Rational): 解その1
            answer2 (sy.Integer or sy.Rational): 解その2
        
        Return:
            latex_equation (str): latex形式で記述された方程式
        
        Note:
            cは登場する係数に小数しか選択されていない場合、かつ有限小数で、さらに整数でない時だけfloat型に変換する
        """
        a, a_latex = self._random_num_maker()
        b, b_latex = self._random_num_maker() 
        c = a * answer1 + b * answer2
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
        
        return latex_equation
    
    def _make_including_transposition_problem(self, answer1, answer2):
        """ax+by=c+dx+ey型の問題を出力する

        Args:
            answer1 (sy.Integer or sy.Rational): 解その1
            answer2 (sy.Integer or sy.Rational): 解その2
        
        Return:
            latex_equation (str): latex形式で記述された方程式

        Note:
            cは登場する係数に小数しか選択されていない場合、かつ有限小数で、さらに整数でない時だけfloat型に変換する
        """        
        a, a_latex = self._random_num_maker()
        b, b_latex = self._random_num_maker()
        d, d_latex = self._random_num_maker()
        e, e_latex = self._random_num_maker()
        c = (a - d) * answer1 + (b - e) * answer2
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
        
        return latex_equation       

    def _make_including_expansion_and_transposition_problem(self, answer1, answer2):
        """ax+by=c+d(ex+fy)型の方程式を出力

        Args:
            answer1 (sy.Integer or sy.Rational): 解その1
            answer2 (sy.Integer or sy.Rational): 解その2
        
        Return:
            latex_equation (str): latex形式で記述された方程式

        Note:
            cは登場する係数に小数しか選択されていない場合、かつ有限小数で、さらに整数でない時だけfloat型に変換する
        """
        a, a_latex = self._random_num_maker()
        b, b_latex = self._random_num_maker()
        d, d_latex = self._random_num_maker()
        e, e_latex = self._random_num_maker()
        f, f_latex = self._random_num_maker()
        c = (a - d * e) * answer1 + (b - d * f) * answer2
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
        
        return latex_equation

    def _random_num_maker(self, max_num=6, min_num=-6):
        """問題設定と最大最小から任意の数を値とlatex形式でランダムに出力

        Args:
            max_num (int, optional): 最大値
            min_num (int, optional): 最小値

        Returns:
            num (sy.Integer or sy.Rational): 計算に用いる数
            num_latex (str): 表記に用いる数
        
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
        
