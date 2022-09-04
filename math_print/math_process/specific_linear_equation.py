"""
8/19
ax = bでa=1になる問題
→characterとnumberでごちゃごちゃになっているのが問題？
→→整理した上で判定ではじくる

9/2
ax=b型でa=1....
from random import randint, random

import sympy as sy

def make_random_decimal(max_num, min_num):

    checker = random()
    if checker > 0.5:
        numerator = randint(1, max_num)
    else:
        numerator = randint(min_num, -1)

    frac_for_decimal = sy.Rational(numerator, 10)

    if frac_for_decimal == 1:
        decimal = 1
    else:
        decimal = float(frac_for_decimal)
    
    decimal_latex = sy.latex(decimal)
    return frac_for_decimal, decimal_latex

for _ in range(10):
    decimal, decimal_latex = make_random_decimal(10, -10)
    print(f"decimal: {decimal}")
    print(f"decimal_latex: {decimal_latex}")
    print("-------------------")

に変更？
"""
from random import choice, randint, random

import sympy as sy


class SpecificLinearEquation:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._number_to_use_list = settings['number_to_use_list']
        self._linear_equation_type_list = settings['linear_equation_type_list']
        self._used_character_type_list = ["x"]
        self._character_dict = {}
        for character in self._used_character_type_list:
            self._character_dict[character] = sy.Symbol(character, real=True)

        self.latex_answer, self.latex_problem = self._make_specific_linear_equation_problem()
    
    def _make_specific_linear_equation_problem(self):
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
        answer = self._make_random_number()
        
        
        a_type_checker = choice(self._number_to_use_list)
        
        if a_type_checker == 'integer':
            a, a_latex = self._make_random_integer(10, -10)
        elif a_type_checker == 'frac':
            a, a_latex = self._make_random_frac(6, -6)
        elif a_type_checker == 'decimal':
            a, a_latex = self._make_random_decimal(8, -8)

        c_type_checker = choice(self._number_to_use_list)
        
        if c_type_checker == 'integer':
            c, c_latex = self._make_random_integer(10, -10)
        elif c_type_checker == 'frac':
            c, c_latex = self._make_random_frac(6, -6)
        elif c_type_checker == 'decimal':
            c, c_latex = self._make_random_decimal(8, -8)

        while(c == a):
            c_type_checker = choice(self._number_to_use_list)
            
            if c_type_checker == 'integer':
                c, c_latex = self._make_random_integer(10, -10)
            elif c_type_checker == 'frac':
                c, c_latex = self._make_random_frac(6, -6)
            elif c_type_checker == 'decimal':
                c, c_latex = self._make_random_decimal(10, -10)
        
        answer, answer_latex = self._make_random_integer(8, -8)
        d_minus_b = (a - c) * answer
        
        d_type_checker = choice(self._number_to_use_list)
        
        if d_type_checker == 'integer':
            d, d_latex = self._make_random_integer(10, -10)
        elif d_type_checker == 'frac':
            d, d_latex = self._make_random_frac(6, -6)
        elif d_type_checker == 'decimal':
            d, d_latex = self._make_random_decimal(8, -8)
        
        b = d - d_minus_b
        b_latex = sy.latex(b)
        
        left_latex = ""
        if a == 1:
            left_latex = left_latex + "x"
        elif a == -1:
            left_latex = left_latex + "-x"
        else:
            left_latex = left_latex + f"{a_latex}x"
        
        if ('decimal' in self._number_to_use_list) and ('frac' not in self._number_to_use_list):
            b_latex = sy.latex(float(b))
            answer_latex = sy.latex(float(answer))

        if b > 0:
            left_latex = left_latex + f"+ {b_latex}"
        elif b < 0:
            left_latex = left_latex + f"{b_latex}"
        
        right_latex = ""
        
        if c == 1:
            right_latex = right_latex + "x"
        elif c == -1:
            right_latex = right_latex + "-x"
        else:
            right_latex = right_latex +  f"{c_latex}x"
        
        if ('decimal' in self._number_to_use_list) and ('frac' not in self._number_to_use_list):
            d_latex = sy.latex(float(d))
        
        if d > 0:
            right_latex = right_latex + f"+ {d_latex}"
        elif d < 0:
            right_latex = right_latex + f"{d_latex}"

        latex_problem = f"{left_latex} = {right_latex}"
        latex_answer = f"x = {answer_latex}"     
        return latex_answer, latex_problem

    def _make_ax_plus_b_equal_cx_plus_d_all_number(self):
        a_type_checker = choice(self._number_to_use_list)
        
        if a_type_checker == 'integer':
            a, a_latex = self._make_random_integer(10, -10)
        elif a_type_checker == 'frac':
            a, a_latex = self._make_random_frac(6, -6)
        elif a_type_checker == 'decimal':
            a, a_latex = self._make_random_decimal(8, -8)        

        c_type_checker = choice(self._number_to_use_list)
        
        if c_type_checker == 'integer':
            c, c_latex = self._make_random_integer(10, -10)
        elif c_type_checker == 'frac':
            c, c_latex = self._make_random_frac(6, -6)
        elif c_type_checker == 'decimal':
            c, c_latex = self._make_random_decimal(8, -8)

        while(c == a):
            c_type_checker = choice(self._number_to_use_list)
            
            if c_type_checker == 'integer':
                c, c_latex = self._make_random_integer(10, -10)
            elif c_type_checker == 'frac':
                c, c_latex = self._make_random_frac(6, -6)
            elif c_type_checker == 'decimal':
                c, c_latex = self._make_random_decimal(6, -6)

        b_type_checker = choice(self._number_to_use_list)
        
        if b_type_checker == 'integer':
            b, b_latex = self._make_random_integer(10, -10)
        elif b_type_checker == 'frac':
            b, b_latex = self._make_random_frac(6, -6)
        elif b_type_checker == 'decimal':
            b, b_latex = self._make_random_decimal(8, -8)

        d_type_checker = choice(self._number_to_use_list)
        
        if d_type_checker == 'integer':
            d, d_latex = self._make_random_integer(10, -10)
        elif d_type_checker == 'frac':
            d, d_latex = self._make_random_frac(6, -6)
        elif d_type_checker == 'decimal':
            d, d_latex = self._make_random_decimal(8, -8)
        
        left = a * self._character_dict["x"] + b
        right = c * self._character_dict["x"] + d
        diff = left - right
        solve_result = sy.solve(diff, self._character_dict["x"])
        answer = solve_result[0]
        answer_latex = sy.latex(answer)
        
        left_latex = ""
        if a == 1:
            left_latex = left_latex + "x"
        elif a == -1:
            left_latex = left_latex + "-x"
        else:
            left_latex = left_latex + f"{a_latex}x"
        

        if b > 0:
            left_latex = left_latex + f"+ {b_latex}"
        elif b < 0:
            left_latex = left_latex + f"{b_latex}"
        
        right_latex = ""
        
        if c == 1:
            right_latex = right_latex + "x"
        elif c == -1:
            right_latex = right_latex + "-x"
        else:
            right_latex = right_latex +  f"{c_latex}x"
        
        if ('decimal' in self._number_to_use_list) and ('frac' not in self._number_to_use_list):
            d_latex = sy.latex(float(d))
        
        if d > 0:
            right_latex = right_latex + f"+ {d_latex}"
        elif d < 0:
            right_latex = right_latex + f"{d_latex}"

        latex_problem = f"{left_latex} = {right_latex}"
        latex_answer = f"x = {answer_latex}"     
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
                decimal_latex or integer_latex (str): latex形式で記述された整数もしくは分数
            
            Note:
                小数と分数が混在している時の計算は分数で進める原則と、
                本当にランダムな値を与えると無限小数が出てくることを鑑みて、
                実際の計算は分数で、表示は小数でという設計になっている。
            """
            checker = random()
            if checker > 0.5:
                numerator = randint(1, max_num * 10)
            else:
                numerator = randint(min_num * 10, -1)

            decimal_as_frac = sy.Rational(numerator, 10)

            if isinstance(decimal_as_frac, sy.Integer):
                integer = decimal_as_frac
                integer_latex = sy.latex(integer)
                return decimal_as_frac, integer_latex
            else:
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
