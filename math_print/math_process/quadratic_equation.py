from random import choice, randint, random
from typing import Dict, Optional, Tuple, Union


import sympy as sy


class QuadraticEquationProblem:
    """指定されたタイプの2次方程式の問題とその解答を出力
    
    Attributes:
        _organization_coefficient (bool): 全体を割ったりかけたりする工程を含むか否か
        latex_answer (str): latex形式で記述された解答
        latex_answer (str): latex形式で記述された問題
    """
    
    def __init__(self, **settings: Dict) -> None:
        """初期設定
        
        Args:
            settings (dict): 問題の各種設定を格納
        """
        sy.init_printing(order='grevlex')
        selected_quadratic_equation_type = choice(settings["quadratic_equation_type_list"])
        self._organization_coefficient = settings["organization_coefficient"]
        self.latex_answer, self.latex_problem = self._make_problem(selected_quadratic_equation_type)
    
    def _make_problem(self, selected_quadratic_equation_type) -> Tuple[str, str]:
        """選択された問題のタイプに応じて、問題と解答を出力
        
        Args:
            selected_equation_type (str): 問題タイプの指定
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Raises:
            ValueError: 想定されていないタイプの問題が出力された場合に挙上
        """
        if selected_quadratic_equation_type == "x^2=k":
            latex_answer, latex_problem = self._make_root_problem()
        elif selected_quadratic_equation_type == "x^2+2ax+a^2=(x+a)^2":
            latex_answer, latex_problem = self._make_square_plus_problem()
        elif selected_quadratic_equation_type == "x^2-2ax+a^2=(x-a)^2":
            latex_answer, latex_problem = self._make_square_minus_problem()
        elif selected_quadratic_equation_type == "x^2+(a+b)x+ab=(x+a)(x+b)":
            latex_answer, latex_problem = self._make_cross_multiplication_problem()
        elif selected_quadratic_equation_type == "x^2-a^2=(x+a)(x-a)":
            latex_answer, latex_problem = self._make_square_minus_square_problem()
        elif selected_quadratic_equation_type == "quadratic_formula":
            latex_answer, latex_problem = self._make_quadratic_formula_problem()
        else:
            raise ValueError(f"selected_quadratic_equation_type is {selected_quadratic_equation_type}. This isn't expected value.")
        return latex_answer, latex_problem
    
    def _make_root_problem(self):
        """x^=k型の2次方程式の問題と解答を出力
        """
        latex_answer = "dummy answer in root problem"
        latex_problem = "dummy problem in root problem."
        return latex_answer, latex_problem
        
    def _make_square_plus_problem(self):
        # (x+a)^2 => (ax+b)^2 <- after
        x = sy.Symbol("x", real=True)
        b = self._make_random_number(positive_or_negative_specification="positive")
        problem = sy.expand((x + b) ** 2)
        if self._organization_coefficient:
            if random() > 0.7:
                k = self._make_random_number(integer_or_frac_specification="frac")
            else:
                k = self._make_random_number(integer_or_frac_specification="integer")
            problem = k * problem
        latex_problem = sy.latex(problem)
        latex_problem += "= 0"
        answers = sy.solve(problem, x)
        latex_answer = f"x = {sy.latex(answers[0])}"
        
        return latex_answer, latex_problem

    def _make_square_minus_problem(self):
        x = sy.Symbol("x", real=True)
        b = self._make_random_number(positive_or_negative_specification="negative")
        problem = sy.expand((x + b) ** 2)
        if self._organization_coefficient:
            if random() > 0.7:
                k = self._make_random_number(integer_or_frac_specification="frac")
            else:
                k = self._make_random_number(integer_or_frac_specification="integer")
            problem = k * problem
        latex_problem = sy.latex(problem)
        latex_problem += "= 0"
        answers = sy.solve(problem, x)
        latex_answer = f"x = {sy.latex(answers[0])}"
        
        return latex_answer, latex_problem
    
    def _make_cross_multiplication_problem(self):
        """
        (x+a)(x+b) = x^2+(a+b)x+ab
        """
        x = sy.Symbol("x", real=True)
        
        answer1 = self._make_random_number(integer_or_frac_specification="integer")
        answer2 = self._make_random_number(integer_or_frac_specification="integer")
        if (answer1 == answer2) or (abs(answer1) == abs(answer2)):
            answer2 += randint(1, 3)
        problem = sy.expand((x - answer1) * (x - answer2))
        if self._organization_coefficient:
            if random() > 0.7:
                k = self._make_random_number(integer_or_frac_specification="frac")
            else:
                k = self._make_random_number(integer_or_frac_specification="integer")
            problem = k * problem
        latex_problem = sy.latex(problem)
        latex_problem += "=0"
        latex_answer = f"x = {sy.latex(answer1)}, {sy.latex(answer2)}"
        
        return latex_answer, latex_problem

    def _make_square_minus_square_problem(self):
        """
        x^2-a^2=(x+a)(x-a)
        """
        x = sy.Symbol("x", real=True)
        
        answer = self._make_random_number(positive_or_negative_specification="positive")
        problem = sy.expand((x + answer) * (x - answer))
        if self._organization_coefficient:
            if random() > 0.7:
                k = self._make_random_number(integer_or_frac_specification="frac")
            else:
                k = self._make_random_number(integer_or_frac_specification="integer")
            problem = k * problem
        latex_problem = f"{sy.latex(problem)} = 0"
        latex_answer = f"x = {sy.latex(answer)}, {sy.latex(-1 * answer)}"
        
        return latex_answer, latex_problem

    def _make_quadratic_formula_problem(self):
        x = sy.Symbol("x", real=True)
        
        left_of_numerator = self._make_random_number(integer_or_frac_specification="integer")
        value_before_root = sy.Integer(randint(1, 4))
        value_in_root = sy.Integer(choice([2, 3, 5, 7]))
        denominator = sy.Integer(randint(2, 4))
        
        if (left_of_numerator % 2 == 0) and (value_before_root % 2 == 0) and (denominator % 2 == 0):
            left_of_numerator = left_of_numerator / 2
            value_before_root = value_before_root / 2
            denominator = denominator / 2
        
        answer1 = (left_of_numerator + value_before_root * sy.sqrt(value_in_root)) / (denominator)
        answer2 = (left_of_numerator - value_before_root * sy.sqrt(value_in_root)) / (denominator)
        
        problem = sy.expand((x - answer1) * (x - answer2))
        constant_number_of_problem = problem.coeff(x, 0).denominator
        if constant_number_of_problem != 1:
            problem = constant_number_of_problem * problem
        
        latex_problem = f"{sy.latex(problem)} = 0"
        if (denominator == 1) or (denominator == -1):
            if value_before_root == 1:
                latex_answer = f"x = {left_of_numerator} \pm \\sqrt{{{value_in_root}}}"
            else:
                latex_answer = f"x = {left_of_numerator} \pm {value_before_root} \\sqrt{{{value_in_root}}}"
        else:
            if value_before_root == 1:
                latex_answer = f"x = \\frac{{{left_of_numerator} \pm \\sqrt{{{value_in_root}}}}}{{{denominator}}}"
            else:    
                latex_answer = f"x = \\frac{{{left_of_numerator} \pm {value_before_root} \\sqrt{{{value_in_root}}}}}{{{denominator}}}"

        return latex_answer, latex_problem


    def _make_random_number(self, integer_or_frac_specification=None, positive_or_negative_specification=None):
        
        def make_random_positive_integer():
            integer = sy.Integer(randint(2, 6))
            return integer
        
        def make_random_positive_frac():
            while True:
                numerator = randint(2, 6)
                denominator = randint(2, 6)
                frac = sy.Rational(numerator, denominator)
                
                if frac.denominator != 1:
                    break
            return frac
        
        if integer_or_frac_specification is None:
            if random() > 0.4:
                number = make_random_positive_integer()
            else:
                number = make_random_positive_frac()
        elif integer_or_frac_specification == "integer":
            number = make_random_positive_integer()
        elif integer_or_frac_specification == "frac":
            number = make_random_positive_frac()
        
        if positive_or_negative_specification is None:
            if random() > 0.5:
                number = -1 * number
        elif positive_or_negative_specification == "negative":
            number = -1 * number
        elif positive_or_negative_specification == "positive":
            pass
        
        return number
