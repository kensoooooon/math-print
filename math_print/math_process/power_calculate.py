from random import choice, randint, random

import sympy as sy

class PowerCalculateProblem:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._used_number_type_list = settings["number_to_use"]
        self._calculate_type = settings["calculate_type"]
        self.latex_answer, self.latex_problem = self._make_power_problem()
    
    def _make_power_problem(self):
        selected_calculate_type = choice(self._calculate_type)
        
        if selected_calculate_type == "single":
            latex_answer, latex_problem = self._make_single_problem()
        
        return latex_answer, latex_problem
    
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
        
        a_checker = choice(self._used_number_type_list)
        
        if a_checker == "integer":
            a, a_latex = self._make_random_integer_number(8, -8)
        elif a_checker == "decimal":
            a, a_latex = self._make_random_decimal_number(15, -15, 10)
        elif a_checker == "frac":
            a, a_latex = self._make_random_frac_number(6, -6)
        
        b = sy.Integer(randint(2, 4))
        b_latex = sy.latex(b)
        
        answer = before_a_number * (a ** b)
        latex_answer = f"= {sy.latex(answer)}"
        
        latex_problem = ""
        latex_problem += before_a_number_latex
        
        if (a_checker == "frac") or (a < 0):
            latex_problem += f"\\left( {a_latex} \\right)"
        else:
            latex_problem += f"{a_latex}"
        
        latex_problem += f"^ {{ {b_latex} }}"
            
        return latex_answer, latex_problem
        # -2^3 になるか (-2) ** 3になるかをrandomで判定する->positiveのほうが都合が良さそう?   
        
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
        checker = random()
        if checker > 0.5:
            numerator = randint(2, max_num)
            denominator = randint(2, max_num)
        else:
            numerator = randint(min_num, -2)
            denominator = randint(2, max_num)
        
        frac = sy.Rational(numerator, denominator)

        frac_with_number_latex = sy.latex(frac)
        return frac, frac_with_number_latex

    def _make_random_decimal_number(self, max_num, min_num, denominator):
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
        return integer, integer_with_number_latex
        