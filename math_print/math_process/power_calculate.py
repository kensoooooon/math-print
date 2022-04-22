from random import choice, randint, random

import sympy as sy
from sympy.printing import latex

class PowerCalculateProblem:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._used_number_type_list = settings["number_to_use"]
        self._calculate_type_list = settings["calculate_type"]
        self.latex_answer, self.latex_problem = self._make_power_problem()
    
    def _make_power_problem(self):
        selected_calculate_type = self._calculate_type_selector()
        
        if selected_calculate_type == "single":
            latex_answer, latex_problem = self._make_single_problem()
        elif selected_calculate_type == "double_plus":
            latex_answer, latex_problem = self._make_double_plus()
        elif selected_calculate_type == "double_minus":
            latex_answer, latex_problem = self._make_double_minus()
        elif selected_calculate_type == "double_times":
            latex_answer, latex_problem = self._make_double_times()
        elif selected_calculate_type == "double_div":
            latex_answer, latex_problem = self._make_double_div()
                        
        return latex_answer, latex_problem
    
    def _make_double_plus(self):
        """
        a ** b + c ** dを作成
        下のsingleの繰り返し
        ->関数化
        """
        left_pair, left_pair_latex = self._make_single_pair_of_base_and_index(before_a_number_is="positive")
        right_pair, right_pair_latex = self._make_single_pair_of_base_and_index(before_a_number_is="positive")
        
        answer = left_pair + right_pair
        # 小数周りの処理は?
        if ("frac" not in self._used_number_type_list) and ("integer" not in self._used_number_type_list) and (self._is_finite_decimal(answer)):
            answer = float(answer)
        latex_answer = f"= {sy.latex(answer)}"
        
        if right_pair_latex.startswith('-'):
            latex_problem = f"{left_pair_latex}  + \\left( {right_pair_latex} \\right)"
        else:
            latex_problem = f"{left_pair_latex} + {right_pair_latex}"
        
        return latex_answer, latex_problem

    def _make_double_minus(self):
        """
        a ** b - c ** dを作成
        下のsingleの繰り返し
        ->関数化
        """
        left_pair, left_pair_latex = self._make_single_pair_of_base_and_index(before_a_number_is="positive")
        right_pair, right_pair_latex = self._make_single_pair_of_base_and_index(before_a_number_is="positive")
        
        answer = left_pair - right_pair
        # 小数周りの処理は?
        if ("frac" not in self._used_number_type_list) and ("integer" not in self._used_number_type_list) and (self._is_finite_decimal(answer)):
            answer = float(answer)
        latex_answer = f"= {sy.latex(answer)}"
        
        if right_pair_latex.startswith('-'):
            latex_problem = f"{left_pair_latex}  - \\left( {right_pair_latex} \\right)"
        else:
            latex_problem = f"{left_pair_latex} - {right_pair_latex}"
        
        return latex_answer, latex_problem
    
    def _make_double_times(self):
        """
        a ** b - c ** dを作成
        下のsingleの繰り返し
        ->関数化
        """
        left_pair, left_pair_latex = self._make_single_pair_of_base_and_index(before_a_number_is="positive", is_times_or_div=True)
        right_pair, right_pair_latex = self._make_single_pair_of_base_and_index(before_a_number_is="positive", is_times_or_div=True)
        
        answer = left_pair * right_pair
        # 小数周りの処理は?
        if ("frac" not in self._used_number_type_list) and ("integer" not in self._used_number_type_list) and (self._is_finite_decimal(answer)):
            answer = float(answer)
        latex_answer = f"= {sy.latex(answer)}"
        
        if right_pair_latex.startswith('-'):
            latex_problem = f"{left_pair_latex}  \\times \\left( {right_pair_latex} \\right)"
        else:
            latex_problem = f"{left_pair_latex} \\times {right_pair_latex}"
        
        return latex_answer, latex_problem

    def _make_double_div(self):
        """
        a ** b ÷ c ** dを作成
        下のsingleの繰り返し
        ->関数化
        """
        left_pair, left_pair_latex = self._make_single_pair_of_base_and_index(before_a_number_is="positive", is_times_or_div=True)
        right_pair, right_pair_latex = self._make_single_pair_of_base_and_index(before_a_number_is="positive", is_times_or_div=True)
        
        answer = left_pair / right_pair
        # 小数周りの処理は?<-割り算だとなし
        """
        if ("frac" not in self._used_number_type_list) and ("integer" not in self._used_number_type_list) and (self._is_finite_decimal(answer)):
            answer = float(answer)
        """
        latex_answer = f"= {sy.latex(answer)}"
        
        if right_pair_latex.startswith('-'):
            latex_problem = f"{left_pair_latex} \\div \\left( {right_pair_latex} \\right)"
        else:
            latex_problem = f"{left_pair_latex} \\div {right_pair_latex}"
        
        return latex_answer, latex_problem
    
    def _calculate_type_selector(self):
        if self._calculate_type_list:
            selected_calculate_type = choice(self._calculate_type_list)
        else:
            selected_calculate_type = choice(
                ["single", "double_plus", "double_minus", "double_times", "double_div"]
            )
        return selected_calculate_type
    
    def _number_type_selector(self):
        if self._used_number_type_list:
            selected_number_type = choice(self._used_number_type_list)
        else:
            selected_number_type = choice(
                ["integer", "decimal", "frac"]
            )
        return selected_number_type
    
    def _make_single_pair_of_base_and_index(self, before_a_number_is, is_times_or_div=False):
        if before_a_number_is == "positive":
            before_a_number = sy.Integer(1)
            before_a_number_latex = ""
        elif before_a_number_is == "negative":
            before_a_number = sy.Integer(-1)
            before_a_number_latex = "-"
        
        a_checker = self._number_type_selector()
        
        if a_checker == "integer":
            if is_times_or_div:
                a, a_latex = self._make_random_integer_number(4, -4)
            else:
                a, a_latex = self._make_random_integer_number(6, -6)
        elif a_checker == "decimal":
            a, a_latex = self._make_random_decimal_number(15, -15, 10)
        elif a_checker == "frac":
            a, a_latex = self._make_random_frac_number(6, -6)
        
        if (a_checker == "decimal") or (a_checker == "frac") or (is_times_or_div):
            b = sy.Integer(randint(2, 3))
        else:
            b = sy.Integer(randint(2, 4))
        b_latex = sy.latex(b)
        
        pair = before_a_number * (a ** b)
        
        pair_latex = ""
        pair_latex += before_a_number_latex
        pair_latex += f"{a_latex}"
        
        pair_latex += f"^ {{ {b_latex} }}"
        
        return pair, pair_latex    
    
    def _make_single_problem(self):
        """
        a ** bを作成
        ・aが負か
        ・aの前に-がついているか?
        普通の式の順に
        """
        if random() > 0.5:
            before_a_number = sy.Integer(1)
            before_a_number_latex = ""
        else:
            before_a_number = sy.Integer(-1)
            before_a_number_latex = "-"
        
        a_checker = self._number_type_selector()
        
        if a_checker == "integer":
            a, a_latex = self._make_random_integer_number(6, -6)
        elif a_checker == "decimal":
            a, a_latex = self._make_random_decimal_number(15, -15, 10)
        elif a_checker == "frac":
            a, a_latex = self._make_random_frac_number(6, -6)
        
        if (a_checker == "decimal") or (a_checker == "frac"):
            b = sy.Integer(randint(2, 3))
        else:
            b = sy.Integer(randint(2, 4))
        b_latex = sy.latex(b)
        
        answer = before_a_number * (a ** b)
        # 小数のみ
        if (a_checker == "decimal") and (a != 1):
            answer = float(answer)

        latex_answer = f"= {sy.latex(answer)}"
        
        latex_problem = ""
        latex_problem += before_a_number_latex
        
        """
        # むこうでやってもらう
        if (a_checker == "frac") or (a < 0):
            latex_problem += f"\\left( {a_latex} \\right)"
        else:
            latex_problem += f"{a_latex}"
        """
        latex_problem += f"{a_latex}"
        
        latex_problem += f"^ {{ {b_latex} }}"
            
        return latex_answer, latex_problem
        
    def _make_random_frac_positive_number(self, max_num, min_num):
        numerator = randint(min_num, max_num)
        denominator = randint(min_num, max_num)
        
        frac = sy.Rational(numerator, denominator)
        
        frac_latex = sy.latex(frac)
        
        return frac, frac_latex

    def _make_random_integer_positive_number(self, max_num ,min_num):
        number = randint(min_num, max_num)
        
        integer = sy.Integer(number)
        integer_latex = sy.latex(integer)
        
        return integer, integer_latex

    def _make_random_decimal_positive_number(self, max_num, min_num):
        numerator = randint(min_num, max_num)
        DENOMINATOR = 10
        
        frac_for_decimal = sy.Rational(numerator, DENOMINATOR)
        if frac_for_decimal == 1:
            decimal = 1
        else:
            decimal = float(frac_for_decimal)
    
        decimal_with_number = frac_for_decimal
        decimal_with_number_latex = sy.latex(decimal)
        """
        if decimal < 0:
            decimal_with_number_latex = f"{decimal_with_number_latex}"
        """
        return decimal_with_number, decimal_with_number_latex

    def _make_random_frac_number(self, max_num, min_num):
        while True:
            checker = random()
            if checker > 0.5:
                numerator = randint(2, max_num)
                denominator = randint(2, max_num)
            else:
                numerator = randint(min_num, -2)
                denominator = randint(2, max_num)
            
            frac = sy.Rational(numerator, denominator)
            
            if frac.denominator != 1:
                break

        frac_with_number_latex = f"\\left( {sy.latex(frac)} \\right)"
        return frac, frac_with_number_latex

    def _make_random_decimal_number(self, max_num, min_num, denominator):
        while True:
            checker = random()
            if checker > 0.5:
                numerator = randint(1, max_num)
            else:
                numerator = randint(min_num, -1)
            
            frac_for_decimal = sy.Rational(numerator, denominator)
            decimal = float(frac_for_decimal)
            
            if decimal != 1:
                break

        decimal_with_number = frac_for_decimal
        decimal_with_number_latex = sy.latex(decimal)
        if decimal < 0:
            decimal_with_number_latex = f"\\left({decimal_with_number_latex}\\right)"
        return decimal_with_number, decimal_with_number_latex
    
    def _make_random_integer_number(self, max_num, min_num):
        checker = random()
        if checker > 0.5:
            numerator = randint(2, max_num)
        else:
            numerator = randint(min_num, -2)
        
        integer = sy.Integer(numerator)

        integer_with_number_latex = sy.latex(integer)
        if integer < 0:
            integer_with_number_latex = f"\\left( {integer_with_number_latex} \\right)"
        return integer, integer_with_number_latex

    def _is_finite_decimal(self, number):
        denominator_list = list(sy.factorint(number.denominator).keys())
        denominator_set = set(denominator_list)
        print(f"denominator_set:{denominator_set}")
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
        