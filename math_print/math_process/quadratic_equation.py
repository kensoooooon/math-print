from random import choice, randint, random

import sympy as sy


class QuadraticEquationProblem:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._quadratic_equation_type_list = settings["quadratic_equation_type_list"]
        self._used_coefficient = settings["used_coefficient"]
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
            latex_answer, latex_problem = self._make_square_mins_square_problem()
        
        return latex_answer, latex_problem
        
    def _make_square_plus_problem(self):
        # (x+a)^2 => (ax+b)^2 <- after
        x = sy.Symbol("x", real=True)
        number_mode = self._used_coefficient
        # a = self._make_random_number(8, -8, number_mode)
        if number_mode == "only_integer":
            b = self._make_random_number(integer_or_frac_specification="integer", positive_or_negative_specification="positive")
        else:
            b = self._make_random_number(positive_or_negative_specification="positive")
        problem = sy.expand((x + b) ** 2)
        latex_problem = sy.latex(problem)
        answer = sy.factor(problem)
        latex_answer = f"= {sy.latex(answer)}"
        
        return latex_answer, latex_problem

    def _make_square_minus_problem(self):
        x = sy.Symbol("x", real=True)
        number_mode = self._used_coefficient
        if number_mode == "only_integer":
            b = self._make_random_number(integer_or_frac_specification="integer", positive_or_negative_specification="negative")
        else:
            b = self._make_random_number(positive_or_negative_specification="negative")
        problem = sy.expand((x + b) ** 2)
        latex_problem = sy.latex(problem)
        answer = sy.factor(problem)
        latex_answer = f"= {sy.latex(answer)}"
        
        return latex_answer, latex_problem
    
    def _make_cross_multiplication_problem(self):
        x = sy.Symbol("x", real=True)
        number_mode = self._used_coefficient
        if number_mode == "only_integer":
            a = self._make_random_number(integer_or_frac_specification="integer")
            b = self._make_random_number(integer_or_frac_specification="integer")
        else:
            a = self._make_random_number()
            b = self._make_random_number()
        
        problem = sy.expand((x + a) * (x + b))
        latex_problem = sy.latex(problem)
        answer = sy.factor(problem)
        latex_answer = f"= {sy.latex(answer)}"
        
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
