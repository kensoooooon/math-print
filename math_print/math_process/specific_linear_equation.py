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
        if self._linear_equation_type_list:
            selected_linear_equation_type = choice(self._linear_equation_type_list)
        else:
            selected_linear_equation_type = choice(
                ["ax_equal_b_only_integer", "ax_equal_b_all_number",
                 'ax_plus_b_equal_c_only_integer', 'ax_plus_b_equal_c_all_number',
                 'ax_plus_b_equal_cx_plus_d_only_integer', 'ax_plus_b_equal_cx_plus_d_all_number',]
            )
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
        number_type_checker = choice(self._number_to_use_list)
        while True:
            if number_type_checker == "integer":
                linear_coefficient, linear_coefficient_latex = self._make_random_integer(10, -10, "number")
                answer, answer_latex = self._make_random_integer(10, -10, "number")
            elif number_type_checker == "frac":
                linear_coefficient, linear_coefficient_latex = self._make_random_frac(10, -10, "number")
                answer, answer_latex = self._make_random_integer(10, -10, "number")
            elif number_type_checker == "decimal":
                linear_coefficient, linear_coefficient_latex = self._make_random_decimal(10, -10, 10, "number")
                answer, answer_latex = self._make_random_integer(10, -10, "number")
            
            if linear_coefficient != 1:
                break
        print(f"linear_coefficient: {linear_coefficient}")
            
        intercept = linear_coefficient * answer
        
        if linear_coefficient_latex == "-1":
            left_latex = "-x"
        else:
            left_latex = f"{linear_coefficient_latex} x"
        
        right = intercept
        if number_type_checker == "decimal":
            right_latex = sy.latex(float(right))
        else:
            right_latex = sy.latex(right)
        
        latex_answer = f"x = {answer_latex}"
        latex_problem = f"{left_latex} = {right_latex}"
        
        return latex_answer, latex_problem
    
    def _make_ax_equal_b_all_number(self):
        number_type_checker = self._number_type_selector()
        while True:
            if number_type_checker == "integer":
                left, left_latex = self._make_random_integer(10, -10, "character")
                print(f"before_left: {left}")
                print(f"before_left_latex: {left_latex}")
                if left == -1:
                    left_latex = "-x"
            elif number_type_checker == "frac":
                left, left_latex = self._make_random_frac(10, -10, "character")
            elif number_type_checker == "decimal":
                left, left_latex = self._make_random_decimal(10, -10, 10, "character")
            if left != 1:
                break
        print(f"left: {left}")

        number_type_checker = self._number_type_selector()

        if number_type_checker == "integer":
            right, right_latex = self._make_random_integer(10, -10, "number")
        elif number_type_checker == "frac":
            right, right_latex = self._make_random_frac(10, -10, "number")
        elif number_type_checker == "decimal":
            right, right_latex = self._make_random_decimal(10, -10, 10, "number")
        

        latex_problem = f"{left_latex} = {right_latex}"
        diff = left - right
        solve_result = sy.solve(diff, self._character_dict["x"])
        equation_answer = solve_result[0]
        answer = sy.collect(equation_answer, self._character_dict["x"])
        latex_answer = f"x = {sy.latex(answer)}"
        return latex_answer, latex_problem

    def _make_ax_plus_b_equal_c_only_integer(self):
        a_type_checker = self._number_type_selector()
        
        if a_type_checker == 'integer':
            a, a_latex = self._make_random_integer(10, -10, "number")
        elif a_type_checker == 'frac':
            a, a_latex = self._make_random_frac(10, -10, "number")
        elif a_type_checker == 'decimal':
            a, a_latex = self._make_random_decimal(10, -10, 10, "number")
        
        c_type_checker = self._number_type_selector()
        
        if c_type_checker == 'integer':
            c, c_latex = self._make_random_integer(10, -10, "number")
        elif c_type_checker == 'frac':
            c, c_latex = self._make_random_frac(10, -10, "number")
        elif c_type_checker == 'decimal':
            c, c_latex = self._make_random_decimal(10, -10, 10, "number")
        
        answer, answer_latex = self._make_random_integer(10, -10, "number")
        b = c - a * answer
        b_latex = sy.latex(b)
        
        left = a * self._character_dict["x"] + b
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
        if c_type_checker == 'decimal':
            right_latex = right_latex + f"{sy.latex(float(c))}"
        else:
            right_latex = right_latex + f"{c_latex}"
        latex_problem = f"{left_latex} = {right_latex}"
        latex_answer = f"x = {answer_latex}"     
        return latex_answer, latex_problem

    def _make_ax_plus_b_equal_c_all_number(self):
        a_type_checker = self._number_type_selector()
        
        if a_type_checker == 'integer':
            a, a_latex = self._make_random_integer(10, -10, "number")
        elif a_type_checker == 'frac':
            a, a_latex = self._make_random_frac(6, -6, "number")
        elif a_type_checker == 'decimal':
            a, a_latex = self._make_random_decimal(10, -10, 10, "number")
    
        b_type_checker = self._number_type_selector()
        
        if b_type_checker == 'integer':
            b, b_latex = self._make_random_integer(10, -10, "number")
        elif b_type_checker == 'frac':
            b, b_latex = self._make_random_frac(6, -6, "number")
        elif b_type_checker == 'decimal':
            b, b_latex = self._make_random_decimal(10, -10, 10, "number")

        c_type_checker = self._number_type_selector()
        
        if c_type_checker == 'integer':
            c, c_latex = self._make_random_integer(10, -10, "number")
        elif c_type_checker == 'frac':
            c, c_latex = self._make_random_frac(6, -6, "number")
        elif c_type_checker == 'decimal':
            c, c_latex = self._make_random_decimal(10, -10, 10, "number")

        left = a * self._character_dict["x"] + b
        right = c
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
        
        if ('decimal' in self._number_to_use_list) and ('frac' not in self._number_to_use_list):
            b_latex = sy.latex(float(b))
            answer_latex = sy.latex(float(answer))

        if b > 0:
            left_latex = left_latex + f"+ {b_latex}"
        elif b < 0:
            left_latex = left_latex + f"{b_latex}"

        right_latex = ""
        if c_type_checker == 'decimal':
            right_latex = right_latex + f"{sy.latex(float(c))}"
        else:
            right_latex = right_latex + f"{c_latex}"
        latex_problem = f"{left_latex} = {right_latex}"
        latex_answer = f"x = {answer_latex}"        
        return latex_answer, latex_problem

    def _make_ax_plus_b_equal_cx_plus_d_only_integer(self):
        a_type_checker = self._number_type_selector()
        
        if a_type_checker == 'integer':
            a, a_latex = self._make_random_integer(10, -10, "number")
        elif a_type_checker == 'frac':
            a, a_latex = self._make_random_frac(6, -6, "number")
        elif a_type_checker == 'decimal':
            a, a_latex = self._make_random_decimal(8, -8, 10, "number")

        c_type_checker = self._number_type_selector()
        
        if c_type_checker == 'integer':
            c, c_latex = self._make_random_integer(10, -10, "number")
        elif c_type_checker == 'frac':
            c, c_latex = self._make_random_frac(6, -6, "number")
        elif c_type_checker == 'decimal':
            c, c_latex = self._make_random_decimal(8, -8, 10, "number")

        while(c == a):
            c_type_checker = self._number_type_selector()
            
            if c_type_checker == 'integer':
                c, c_latex = self._make_random_integer(10, -10, "number")
            elif c_type_checker == 'frac':
                c, c_latex = self._make_random_frac(6, -6, "number")
            elif c_type_checker == 'decimal':
                c, c_latex = self._make_random_decimal(10, -10, 10, "number")
        
        answer, answer_latex = self._make_random_integer(8, -8, "number")
        d_minus_b = (a - c) * answer
        
        d_type_checker = self._number_type_selector()
        
        if d_type_checker == 'integer':
            d, d_latex = self._make_random_integer(10, -10, "number")
        elif d_type_checker == 'frac':
            d, d_latex = self._make_random_frac(6, -6, "number")
        elif d_type_checker == 'decimal':
            d, d_latex = self._make_random_decimal(8, -8, 10, "number")
        
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
        a_type_checker = self._number_type_selector()
        
        if a_type_checker == 'integer':
            a, a_latex = self._make_random_integer(10, -10, "number")
        elif a_type_checker == 'frac':
            a, a_latex = self._make_random_frac(6, -6, "number")
        elif a_type_checker == 'decimal':
            a, a_latex = self._make_random_decimal(8, -8, 10, "number")        

        c_type_checker = self._number_type_selector()
        
        if c_type_checker == 'integer':
            c, c_latex = self._make_random_integer(10, -10, "number")
        elif c_type_checker == 'frac':
            c, c_latex = self._make_random_frac(6, -6, "number")
        elif c_type_checker == 'decimal':
            c, c_latex = self._make_random_decimal(8, -8, 10, "number")

        while(c == a):
            c_type_checker = self._number_type_selector()
            
            if c_type_checker == 'integer':
                c, c_latex = self._make_random_integer(10, -10, "number")
            elif c_type_checker == 'frac':
                c, c_latex = self._make_random_frac(6, -6, "number")
            elif c_type_checker == 'decimal':
                c, c_latex = self._make_random_decimal(6, -6, 10, "number")

        b_type_checker = self._number_type_selector()
        
        if b_type_checker == 'integer':
            b, b_latex = self._make_random_integer(10, -10, "number")
        elif b_type_checker == 'frac':
            b, b_latex = self._make_random_frac(6, -6, "number")
        elif b_type_checker == 'decimal':
            b, b_latex = self._make_random_decimal(8, -8, 10, "number")

        d_type_checker = self._number_type_selector()
        
        if d_type_checker == 'integer':
            d, d_latex = self._make_random_integer(10, -10, "number")
        elif d_type_checker == 'frac':
            d, d_latex = self._make_random_frac(6, -6, "number")
        elif d_type_checker == 'decimal':
            d, d_latex = self._make_random_decimal(8, -8, 10, "number")
        
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

    def _make_random_frac(self, max_num, min_num):
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
        
    
    def _make_random_decimal(self, max_num, min_num, denominator):
        checker = random()
        if checker > 0.5:
            numerator = randint(1, max_num)
        else:
            numerator = randint(min_num, -1)
        
        frac_for_decimal = sy.Rational(numerator, denominator)
        if frac_for_decimal == 1:
            decimal = 1
        else:
            decimal = float(frac_for_decimal)

        decimal_with_number = frac_for_decimal
        decimal_with_number_latex = sy.latex(decimal)
        return decimal_with_number, decimal_with_number_latex
    
    def _make_random_integer(self, max_num, min_num):
        checker = random()
        if checker > 0.5:
            numerator = randint(1, max_num)
        else:
            numerator = randint(min_num, -1)
        
        integer = sy.Integer(numerator)
        integer_with_number_latex = sy.latex(integer)
        return integer, integer_with_number_latex
    