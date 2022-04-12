from random import choice, randint, random

import sympy as sy


class FactorizationProblem:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._factorization_type_list = settings["factorization_type_list"]
        self._used_coefficient = settings["used_coefficient"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        selected_factorization_type = choice(self._factorization_type_list)
        
        if selected_factorization_type == "ax+ab=a(x+b)":
            latex_answer, latex_problem = self._make_ax_plus_ab_problem()
        """
        elif selected_factorization_type == "x^2+2ax+a^2=(x+a)^2":
            latex_answer, latex_problem = self._make_square_plus_problem()
        elif selected_factorization_type == "x^2-2ax+a^2=(x-a)^2":
            latex_answer, latex_problem = self._make_square_minus_problem()
        elif selected_factorization_type == "x^2+(a+b)x+ab=(x+a)(x+b)":
            latex_answer, latex_problem = self._make_cross_multiplication_problem()
        """
        
        return latex_answer, latex_problem

    def _make_ax_plus_ab_problem(self):
        number_mode = self._used_coefficient
        x = sy.Symbol("x", real=True) 
        a = self._make_random_number(8, -8, number_mode)
        a_latex = sy.latex(a)
        # b = self._make_random_number(8, -8, "only_integer")
        b = self._make_random_number(8, -8, "only_integer")
        b_latex = sy.latex(b)
        c = self._make_random_number(8, -8, "only_integer")
        c_latex = sy.latex(c)
        """
        problem = a * b * x + a * c
        answer = sy.factor(problem)
        print(f"problem: {problem}")
        print(f"answer: {answer}")
        
        latex_answer = sy.latex(answer)
        latex_problem = sy.latex(problem)
        """
        latex_problem = f"{sy.latex(a * b * x + a * c)}"
        if c > 0:
            latex_answer = f"= {a_latex} ( {b_latex} x + {c_latex} )"
        else:
            latex_answer = f"= {a_latex} ( {b_latex} x {c_latex} )"
        
        return latex_answer, latex_problem
        

    def _make_random_number(self, max_num, min_num, number_mode):
        # number_mode = self._used_coefficient
        def make_integer_number():
            if random() > 0.4:
                number = randint(2, max_num)
            else:
                number = randint(min_num, -1)
            
            return number
        
        if number_mode == "only_integer":
            number = make_integer_number()
        elif number_mode == "integer_and_frac":
            if random() > 0.3:
                number = make_integer_number()
            else:
                while True:
                    numerator = make_integer_number()
                    denominator = make_integer_number()
                    number = sy.Rational(numerator, denominator)
                    
                    if number.denominator != 1:
                        break
        return number
    