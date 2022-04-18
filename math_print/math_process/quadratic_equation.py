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
            latex_answer, latex_problem = self._new_make_quadratic_formula_problem()

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
        latex_problem = f"{sy.latex(problem)} = 0"
        
        answer1, answer2 = sy.solve(problem, x)
        print(f"answer1: {answer1}, type: {type(answer1)}")
        print(f"answer2: {answer2}, type: {type(answer2)}")
        latex_answer = f"x = {sy.latex(sy.factor(answer1, fraction=True, gaussian=True))}, {sy.latex(sy.factor(answer2, fraction=True, gaussian=True))}"
        """
        if b % 2 == 0:
            denominator = a
            left_part = -1 * b / 2
            value_in_root = (b / 2) ** 2 - a * c_value
        else:
            denominator = 2 * a
            left_part = -1 * b
            value_in_root = b ** 2 - 4 * a * c_value
        # right_part = f"{sy.latex(sy.sqrt(discriminant_value))}" 
        if (denominator < 0) and (left_part < 0):
            denominator_latex = sy.latex(-1 * denominator)
            left_part_latex = sy.latex(-1 * left_part)
            root_part_latex = sy.latex(sy.sqrt(value_in_root))
            latex_answer = f"x = \\frac{{{left_part_latex} \pm {root_part_latex}}}{{{denominator_latex}}}"
        elif (a < 0) and (b > 0):
            denominator_latex = sy.latex(-1 * denominator)
            left_part_latex = sy.latex(left_part)
            root_part_latex = sy.latex(sy.sqrt(value_in_root))
            latex_answer = f"x = - \\frac{{{left_part_latex} \pm {root_part_latex}}}{{{denominator_latex}}}"
        else:
            denominator_latex = sy.latex(denominator)
            left_part_latex = sy.latex(left_part)
            root_part_latex = sy.latex(sy.sqrt(value_in_root))
            latex_answer = f"x = \\frac{{{left_part_latex} \pm {root_part_latex}}}{{{denominator_latex}}}"
        """
        return latex_answer, latex_problem
    
    def _new_make_quadratic_formula_problem(self):
        x = sy.Symbol("x", real=True)
        
        left_of_numerator = self._make_random_number(integer_or_frac_specification="integer")
        value_before_root = sy.Integer(randint(2, 4))
        value_in_root = sy.Integer(choice([2, 3, 5, 7]))
        denominator = sy.Integer(randint(2, 4))
        
        if (left_of_numerator % 2 == 0) and (value_before_root % 2 == 0) and (denominator % 2 == 0):
            left_of_numerator = left_of_numerator / 2
            value_before_root = value_before_root / 2
            denominator = denominator / 2
        
        answer1 = (left_of_numerator + value_before_root * sy.sqrt(value_in_root)) / (denominator)
        answer2 = (left_of_numerator - value_before_root * sy.sqrt(value_in_root)) / (denominator)
        
        problem = sy.expand((x - answer1) * (x - answer2))
        print(f"problem: {problem}")
        print(f"coeff: {problem.coeff(x, 0)}, type: {type(problem.coeff(x, 0))}")
        print(f"constant_number_of_problem: {problem.coeff(x, 0).denominator}")
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
