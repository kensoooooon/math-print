from random import choice, randint, random

import sympy as sy


class QuadraticEquationProblem:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._quadratic_equation_type_list = settings["quadratic_equation_type_list"]
        self._is_factor_out = settings["factor_out"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        selected_quadratic_equation_type = choice(self._quadratic_equation_type_list)

        if selected_quadratic_equation_type == "x^2+2ax+a^2=(x+a)^2":
            latex_answer, latex_problem = self._make_square_plus_problem()
        elif selected_quadratic_equation_type == "x^2-2ax+a^2=(x-a)^2":
            latex_answer, latex_problem = self._make_square_minus_problem()
        elif selected_quadratic_equation_type == "x^2+(a+b)x+ab=(x+a)(x+b)":
            latex_answer, latex_problem = self._make_cross_multiplication_problem()
        elif selected_quadratic_equation_type == "x^2-a^2=(x+a)(x-a)":
            latex_answer, latex_problem = self._make_square_minus_square_problem()
        elif selected_quadratic_equation_type == "quadratic_formula":
            latex_answer, latex_problem = self._make_quadratic_formula_problem()

        return latex_answer, latex_problem
        
    def _make_square_plus_problem(self):
        # (x+a)^2 => (ax+b)^2 <- after
        x = sy.Symbol("x", real=True)
        b = self._make_random_number(positive_or_negative_specification="positive")
        problem = sy.expand((x + b) ** 2)
        if self._is_factor_out:
            if random() > 0.7:
                k = self._make_random_number()
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
        if self._is_factor_out:
            if random() > 0.7:
                k = self._make_random_number()
                problem = k * problem
        latex_problem = sy.latex(problem)
        latex_problem += "= 0"
        answers = sy.solve(problem, x)
        print(f"answer: {answers}, type: {type(answers)}")
        latex_answer = f"x = {sy.latex(answers[0])}"
        
        return latex_answer, latex_problem
    
    def _make_cross_multiplication_problem(self):
        """
        (x+a)(x+b) = x^2+(a+b)x+ab
        """
        x = sy.Symbol("x", real=True)
        a = self._make_random_number()
        b = self._make_random_number(integer_or_frac_specification="integer")
        if a == b:
            b += randint(1, 3)
        problem = sy.expand((x + a) * (x + b))
        if self._is_factor_out:
            if random() > 0.7:
                k = self._make_random_number()
                problem = k * problem
        latex_problem = sy.latex(problem)
        latex_problem += "= 0"
        answers = sy.solve(problem, x)
        latex_answer = f"x = {sy.latex(answers[0])}, {sy.latex(answers[1])}"
        
        return latex_answer, latex_problem

    def _make_square_minus_square_problem(self):
        """
        x^2-a^2=(x+a)(x-a)
        """
        x = sy.Symbol("x", real=True)
        a1 = self._make_random_number(positive_or_negative_specification="positive")
        a2 = -1 * a1
        problem = sy.expand((x + a1) * (x + a2))
        if self._is_factor_out:
            if random() > 0.7:
                k = self._make_random_number()
                problem = k * problem
        latex_problem = sy.latex(problem)
        latex_problem += "= 0"
        answers = sy.solve(problem, x)
        latex_answer = f"x = {sy.latex(answers[0])}"
        
        return latex_answer, latex_problem

    def _make_quadratic_formula_problem(self):
        """
        x = (-b \pm \sqrt{b^2-4ac}) / 2a
        """
        x = sy.Symbol("x", real=True)
        discriminant_value = self._make_random_number(integer_or_frac_specification="integer", positive_or_negative_specification="positive")
        discriminant_value += randint(1, 8)
        b = self._make_random_number(integer_or_frac_specification="integer")
        a = self._make_random_number(integer_or_frac_specification="integer")
        c = sy.Symbol("c", real=True)
        c_value = sy.solve(b ** 2 - 4 * a * c - discriminant_value, c)[0]
        problem = a * x ** 2 + b * x + c_value
        latex_problem = sy.latex(problem)
        latex_problem += "= 0"
        """
        どうしても細かい調整がうまくいかない。
        ->符号と平方根をいじっても、どうしても中身がーになってしまう
        ratsimp()で一つにまとめる？
        Rational
        cancel
        simplify
        long_fraction
        偶数で割れるかどうかだけ判定いれて主導が楽そう？

        answer1, answer2 = sy.solve(problem, x)
        print(f"answer1: {answer1}, answer2: {answer2}")
        print(f"canceld_answer1: {sy.cancel(answer1)}, canceld_answer2: {sy.cancel(answer2)}")
        latex_answer1 = sy.latex(answer1, long_frac_ratio=2)
        latex_answer2 = sy.latex(answer2, long_frac_ratio=2)
        latex_answer = f"x = {latex_answer1}, {latex_answer2}"
        """
        right_part = f"{sy.latex(sy.sqrt(discriminant_value))}" 
        if (a < 0) and (b < 0):
            denominator = sy.latex(-1 * 2 * a)
            left_part = sy.latex(-1 * b)
            if 
            latex_answer = f"x = \\frac{{{left_part} \pm {right_part}}}{{{denominator}}}"
        elif (a < 0) and (b > 0):
            denominator = sy.latex(-1 * 2 * a)
            left_part = sy.latex(b)
            latex_answer = f"x = - \\frac{{{left_part} \pm {right_part}}}{{{denominator}}}"
        else:
            denominator = sy.latex(2 * a)
            left_part = sy.latex(b)
            latex_answer = f"x = \\frac{{{left_part} \pm {right_part}}}{{{denominator}}}"

        return latex_answer, latex_problem

    def _make_random_number(self, integer_or_frac_specification=None, positive_or_negative_specification=None):
        
        def make_random_positive_integer():
            integer = sy.Integer(randint(2, 8))
            return integer
        
        def make_random_positive_frac():
            while True:
                numerator = randint(2, 8)
                denominator = randint(2, 8)
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
