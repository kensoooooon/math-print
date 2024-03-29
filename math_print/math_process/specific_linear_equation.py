from random import choice, randint, random

import sympy as sy


class SpecificLinearEquation:
    """特定の形を持つ1次方程式の解を求める問題を出力する
    
    Attributes:
        _number_to_use_list (list): 係数に利用する数字のタイプを格納する
        _linear_equation_type_list (list): 問題に出力される1次方程式の形を格納する
        latex_answer (str): latex形式で記述された解答
        latex_problem (str): latex形式で記述された問題
    
    Note:
        解としては基本的に整数、分数が優先されて、小数だけが選択されているときに例外的に小数へと変換される
        また、解とつじつま合わせをするために計算されて出てくる係数も、同様の仕様となっている。
    """
    def __init__(self, **settings):
        """初期化
        
        Args:
            settings (dict): 問題の設定が格納されている
        """
        sy.init_printing(order='grevlex')
        self._number_to_use_list = settings['number_to_use_list']
        self._linear_equation_type_list = settings['linear_equation_type_list']
        self.latex_answer, self.latex_problem = self._make_specific_linear_equation_problem()
    
    def _make_specific_linear_equation_problem(self):
        """選択された1次方程式の形に応じて、問題と解答を出力する
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述されたされた問題
        """
        selected_linear_equation_type = choice(self._linear_equation_type_list)
        
        if selected_linear_equation_type == "ax_equal_b_only_integer":
            latex_answer, latex_problem = self._make_ax_equal_b_only_integer()
        elif selected_linear_equation_type == "ax_equal_b_all_number":
            latex_answer, latex_problem = self._make_ax_equal_b_all_number()
        elif selected_linear_equation_type == 'ax_plus_b_equal_c_only_integer':
            latex_answer, latex_problem = self._make_ax_plus_b_equal_c_only_integer()
        elif selected_linear_equation_type == 'ax_plus_b_equal_c_all_number':
            latex_answer, latex_problem = self._make_ax_plus_b_equal_c_all_number()
        elif selected_linear_equation_type == 'ax_plus_b_equal_cx_plus_d_only_integer':
            latex_answer, latex_problem = self._make_ax_plus_b_equal_cx_plus_d_only_integer()
        elif selected_linear_equation_type == 'ax_plus_b_equal_cx_plus_d_all_number':
            latex_answer, latex_problem = self._make_ax_plus_b_equal_cx_plus_d_all_number()
        
        return latex_answer, latex_problem
        
    def _make_ax_equal_b_only_integer(self):
        """ax=b型(整数解)の1次方程式を作成

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        answer, answer_latex = self._make_random_number(number_type="integer")
        latex_answer = f"x = {answer_latex}"
        
        while True:
            a, a_latex = self._make_random_number()
            if (a != 1) and (a != 0):
                break
        
        b =  a * answer
        if ("decimal" in self._number_to_use_list) and ("frac" not in self._number_to_use_list) and ("integer" not in self._number_to_use_list):
            b_latex = sy.latex(sy.Float(b))
        else:
            b_latex = sy.latex(b)
        
        if a == -1:
            latex_problem = f"-x = {b_latex}"
        else:
            latex_problem = f"{a_latex}x = {b_latex}"
        
        return latex_answer, latex_problem
    
    def _make_ax_equal_b_all_number(self):
        """ax=b型(分数、小数解含む)の1次方程式を作成

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        if ("decimal" in self._number_to_use_list) and ("frac" not in self._number_to_use_list) and ("integer" not in self._number_to_use_list):
            answer, answer_latex = self._make_random_number(number_type="decimal")
        else:
            answer, answer_latex = self._make_random_number(number_type=choice(["frac", "integer"]))
        latex_answer = f"x = {answer_latex}"
        
        while True:
            a, a_latex = self._make_random_number()
            if (a != 1) and (a != 0):
                break
        
        b =  a * answer
        if ("decimal" in self._number_to_use_list) and ("frac" not in self._number_to_use_list) and ("integer" not in self._number_to_use_list):
            b_latex = sy.latex(sy.Float(b))
        else:
            b_latex = sy.latex(b)
        
        if a == -1:
            latex_problem = f"-x = {b_latex}"
        else:
            latex_problem = f"{a_latex}x = {b_latex}"
        
        return latex_answer, latex_problem

    def _make_ax_plus_b_equal_c_only_integer(self):
        """ax+b=c型(整数解)の1次方程式を作成

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        answer, answer_latex = self._make_random_number(number_type="integer")
        latex_answer = f"x = {answer_latex}"
        while True:
            a, a_latex = self._make_random_number()
            if a != 0:
                break
        c, c_latex = self._make_random_number()
        b = c - a * answer
        
        if ("decimal" in self._number_to_use_list) and ("frac" not in self._number_to_use_list) and ("integer" not in self._number_to_use_list):
            b_latex = sy.latex(sy.Float(b))
        else:
            b_latex = sy.latex(b)
        
        latex_problem = ""
        # a add part
        if a == 1:
            latex_problem += "x"
        elif a == -1:
            latex_problem += "-x"
        else:
            latex_problem += f"{a_latex}x"
        # b add part
        if b == 0:
            pass
        elif b > 0:
            latex_problem += f"+ {b_latex}"
        else:
            latex_problem += f"{b_latex}"
        # c add part
        latex_problem += f"= {c_latex}"
        
        return latex_answer, latex_problem

    def _make_ax_plus_b_equal_c_all_number(self):
        """ax+b=c型(分数解含む)の1次方程式を作成

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        if ("decimal" in self._number_to_use_list) and ("frac" not in self._number_to_use_list) and ("integer" not in self._number_to_use_list):
            answer, answer_latex = self._make_random_number(number_type="decimal")
        else:
            answer, answer_latex = self._make_random_number(number_type=choice(["frac", "integer"]))
        latex_answer = f"x = {answer_latex}"
        
        while True:
            a, a_latex = self._make_random_number()
            if a != 0:
                break
        c, c_latex = self._make_random_number()
        b = c - a * answer
        
        if ("decimal" in self._number_to_use_list) and ("frac" not in self._number_to_use_list) and ("integer" not in self._number_to_use_list):
            b_latex = sy.latex(sy.Float(b))
        else:
            b_latex = sy.latex(b)
        
        latex_problem = ""
        # a add part
        if a == 1:
            latex_problem += "x"
        elif a == -1:
            latex_problem += "-x"
        else:
            latex_problem += f"{a_latex}x"
        # b add part
        if b == 0:
            pass
        elif b > 0:
            latex_problem += f"+ {b_latex}"
        else:
            latex_problem += f"{b_latex}"
        # c add part
        latex_problem += f"= {c_latex}"
        
        return latex_answer, latex_problem

    def _make_ax_plus_b_equal_cx_plus_d_only_integer(self):
        """ax+b=cx+d型(整数解のみ)の1次方程式を作成

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        answer, answer_latex = self._make_random_number(number_type="integer")
        latex_answer = f"x = {answer_latex}"
        while True:
            a, a_latex = self._make_random_number()
            c, c_latex = self._make_random_number()
            if (a != 0) and (c != 0) and (a != c):
                break 
        
        if random() > 0.5:
            b, b_latex = self._make_random_number()
            d = a * answer + b - c * answer
            if ("decimal" in self._number_to_use_list) and ("frac" not in self._number_to_use_list) and ("integer" not in self._number_to_use_list):
                d_latex = sy.latex(sy.Float(d))
            else:
                d_latex = sy.latex(d)
        else:
            d, d_latex = self._make_random_number()
            b = -1 * a * answer + c * answer + d
            if ("decimal" in self._number_to_use_list) and ("frac" not in self._number_to_use_list) and ("integer" not in self._number_to_use_list):
                b_latex = sy.latex(sy.Float(b))
            else:
                b_latex = sy.latex(b)
        
        latex_problem = ""
        # a add part
        if a == 1:
            latex_problem += "x"
        elif a == -1:
            latex_problem += "-x"
        else:
            latex_problem += f"{a_latex}x"
        # b add part
        if b == 0:
            pass
        elif b > 0:
            latex_problem += f"+ {b_latex}"
        else:
            latex_problem += f"{b_latex}"
        # c add part
        if c == 1:
            latex_problem += "= x"
        elif c == -1:
            latex_problem += "= -x"
        else:
            latex_problem += f"= {c_latex}x"
        # d add part
        if d == 0:
            pass
        elif d > 0:
            latex_problem += f"+ {d_latex}"
        else:
            latex_problem += f"{d_latex}"
        
        return latex_answer, latex_problem

    def _make_ax_plus_b_equal_cx_plus_d_all_number(self):
        """ax+b=cx+d型(分数解含む)の1次方程式を作成
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        if ("decimal" in self._number_to_use_list) and ("frac" not in self._number_to_use_list) and ("integer" not in self._number_to_use_list):
            answer, answer_latex = self._make_random_number(number_type="decimal")
        else:
            answer, answer_latex = self._make_random_number(number_type=choice(["frac", "integer"]))
        latex_answer = f"x = {answer_latex}"
        while True:
            a, a_latex = self._make_random_number()
            c, c_latex = self._make_random_number()
            if (a != 0) and (c != 0) and (a != c):
                break 

        if random() > 0.5:
            b, b_latex = self._make_random_number()
            d = a * answer + b - c * answer
            if ("decimal" in self._number_to_use_list) and ("frac" not in self._number_to_use_list) and ("integer" not in self._number_to_use_list):
                d_latex = sy.latex(sy.Float(d))
            else:
                d_latex = sy.latex(d)
        else:
            d, d_latex = self._make_random_number()
            b = -1 * a * answer + c * answer + d
            if ("decimal" in self._number_to_use_list) and ("frac" not in self._number_to_use_list) and ("integer" not in self._number_to_use_list):
                b_latex = sy.latex(sy.Float(b))
            else:
                b_latex = sy.latex(b)
        
        latex_problem = ""
        # a add part
        if a == 1:
            latex_problem += "x"
        elif a == -1:
            latex_problem += "-x"
        else:
            latex_problem += f"{a_latex}x"
        # b add part
        if b == 0:
            pass
        elif b > 0:
            latex_problem += f"+ {b_latex}"
        else:
            latex_problem += f"{b_latex}"
        # c add part
        if c == 1:
            latex_problem += "= x"
        elif c == -1:
            latex_problem += "= -x"
        else:
            latex_problem += f"= {c_latex}x"
        # d add part
        if d == 0:
            pass
        elif d > 0:
            latex_problem += f"+ {d_latex}"
        else:
            latex_problem += f"{d_latex}"
        
        return latex_answer, latex_problem
    
    def _make_random_number(self, number_type=None, max_num=5, min_num=-5):
        """指定された型のランダムな数を出力する

        Args:
            number_type (Union[str, NoneType], optional): 整数、分数、小数のいずれかの型を指定
            max_num (int, optional): 値決定に使用される数の最大値
            min_num (int, optional): 値決定に使用される数の最小値
        
        Returns:
            number (Union[sy.Integer, sy.Rational]): 計算に使用される数
            number_latex (str): latex形式で記述された数
        
        Raises:
            ValueError: 指定された数の型が存在しない場合発生
        """
        
        def make_random_frac(max_num, min_num):
            """ランダムな分数とlatexを返す

            Args:
                max_num (int): 値決定に使用される数の最大値
                min_num (int): 値決定に使用される数の最小値

            Returns:
                frac (sy.Rational): 計算用の分数
                frac_latex (str): latex形式で記述された表示用の分数
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
            
        
        def make_random_decimal(max_num, min_num):
            """ランダムな小数とlatexを返す

            Args:
                max_num (int): 値決定に使用される数の最大値
                min_num (int): 値決定に使用される数の最小値

            Returns:
                decimal_as_frac (sy.Rational): 計算用の分数
                decimal_latex or integer_latex (str): latex形式で記述された小数
            
            Note:
                小数と分数が混在している時の計算は分数で進める原則と、
                本当にランダムな値を与えると無限小数が出てくることを鑑みて、
                実際の計算は分数で、表示は小数でという設計になっている。
            """
            if random() > 0.5:
                numerator = randint(1, max_num * 10)                    
            else:
                numerator = randint(min_num * 10, -1)
            
            if numerator % 10 == 0:
                if random() > 0.5:
                    numerator += randint(1, 9)
                else:
                    numerator -= randint(1, 9)
            
            decimal_as_frac = sy.Rational(numerator, 10)

            decimal = sy.Float(decimal_as_frac)
            decimal_latex = sy.latex(decimal)
            return decimal_as_frac, decimal_latex
        
        def make_random_integer(max_num, min_num):
            """ランダムな整数とlatexを返す

            Args:
                max_num (int): 値決定に使用される数の最大値
                min_num (int): 値決定に使用される数の最小値

            Returns:
                integer (sy.Integer): 計算用の整数
                integer_latex (str): latex形式で記述された整数
            """
            checker = random()
            if checker > 0.5:
                number = randint(1, max_num)
            else:
                number = randint(min_num, -1)
            
            integer = sy.Integer(number)
            integer_latex = sy.latex(integer)
            return integer, integer_latex
        
        if number_type is not None:
            selected_number_type = number_type
        else:
            selected_number_type = choice(self._number_to_use_list)
            
        if selected_number_type == "integer":
            number, number_latex = make_random_integer(max_num=max_num, min_num=min_num)
        elif selected_number_type == "frac":
            number, number_latex = make_random_frac(max_num=max_num, min_num=min_num)
        elif selected_number_type == "decimal":
            number, number_latex = make_random_decimal(max_num=max_num, min_num=min_num)
        else:
            raise ValueError(f"'selected_number_type' is {selected_number_type}. This may be wrong.")
        
        return number, number_latex
