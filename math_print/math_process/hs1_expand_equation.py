from random import choice, randint, random

import sympy as sy

class HS1ExpandEquationProblem:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex')
        self._expand_equation_type_list = settings["expand_equation_type_list"]
        self._another_character_existence = settings["another_character_existence"]
        self._used_character_dict = {}
        for symbol in ["x", "y", "z"]:
            self._used_character_dict[symbol] = sy.Symbol(symbol, real=True)
        self.latex_answer, self.latex_problem = self._make_problem()

    def _make_problem(self):
        # not empty due to views.py
        selected_equation_type = choice(self._expand_equation_type_list)
        
        """
        '(a+b)^2=a^2+2ab+b^2', '(a-b)^2=a^2-2ab+b^2',
        '(a+b)(a-b)=a^2-b^2',
        '(ax+b)(cx+d)=acx^2+(ad+bc)x+ab', '(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca',
        '(a+b)^3=a^3+3a^2b+3ab^2+b^3', '(a-b)^3=a^3-3a^2b+3ab^2-b^3',
        '(a+b)(a^2-ab+b^2)=a^3+b^3', '(a-b)(a^2+ab+b^2)=a^3-b^3'
        """
        if selected_equation_type == '(a+b)^2=a^2+2ab+b^2':
            latex_answer, latex_problem = self._make_plus_square()
        elif selected_equation_type == '(a-b)^2=a^2-2ab+b^2':
            latex_answer, latex_problem = self._make_minus_square()
        elif selected_equation_type == '(a+b)(a-b)=a^2-b^2':
            latex_answer, latex_problem = self._make_plus_minus_product()
        elif selected_equation_type == '(ax+b)(cx+d)=acx^2+(ad+bc)x+ab':
            latex_answer, latex_problem = self._make_cross_multiplication()
        elif selected_equation_type == '(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca':
            latex_answer, latex_problem = self._make_three_terms_square()
        elif selected_equation_type == '(a+b)^3=a^3+3a^2b+3ab^2+b^3':
            latex_answer, latex_problem = self._make_plus_cubed_problem()
        elif selected_equation_type == '(a-b)^3=a^3-3a^2b+3ab^2-b^3':
            latex_answer, latex_problem = self._make_minus_cubed_problem()
        elif selected_equation_type == '(a+b)(a^2-ab+b^2)=a^3+b^3':
            latex_answer, latex_problem = self._plus_minus_to_cubed_sum_problem()
        elif selected_equation_type == '(a-b)(a^2+ab+b^2)=a^3-b^3':
            latex_answer, latex_problem = self._minus_plus_to_cubed_sum_problem()
                
        return latex_answer, latex_problem
    
    def _make_plus_square(self):
        # '(a+b)^2=a^2+2ab+b^2'
        a_num = self._make_random_number(positive_or_negative="positive")
        b_num = self._make_random_number(positive_or_negative="positive")
        
        a_term = a_num * self._used_character_dict["x"]
        if self._another_character_existence:
            b_term = b_num * self._used_character_dict["y"]
        else:
            b_term = b_num
        
        problem = (a_term + b_term) ** 2
        latex_problem = sy.latex(problem)
        answer = sy.expand(problem)
        latex_answer = f"= {sy.latex(answer)}"
        
        return latex_answer, latex_problem

    def _make_minus_square(self):
        # '(a-b)^2=a^2-2ab+b^2'
        a_num = self._make_random_number(positive_or_negative="positive")
        b_num = self._make_random_number(positive_or_negative="negative")
        
        a_term = a_num * self._used_character_dict["x"]
        if self._another_character_existence:
            b_term = b_num * self._used_character_dict["y"]
        else:
            b_term = b_num
        
        problem = (a_term + b_term) ** 2
        latex_problem = sy.latex(problem)
        answer = sy.expand(problem)
        latex_answer = f"= {sy.latex(answer)}"
        
        return latex_answer, latex_problem

    def _make_plus_minus_product(self):
        # (a+b)(a-b)=a^2-b^2
        a_num = self._make_random_number(positive_or_negative="positive")
        b_num = self._make_random_number(positive_or_negative="positive")
        
        a_term = a_num * self._used_character_dict["x"]
        if self._another_character_existence:
            b_term = b_num * self._used_character_dict["y"]
        else:
            b_term = b_num
        
        problem =(a_term + b_term) * (a_term - b_term)
        latex_problem = sy.latex(problem)
        answer = sy.expand(problem)
        latex_answer = f"= {sy.latex(answer)}"
        
        return latex_answer, latex_problem
    
    def _make_cross_multiplication(self):
        # '(ax+b)(cx+d)=acx^2+(ad+bc)x+ab'
        a_num = self._make_random_number(positive_or_negative="positive")
        b_num = self._make_random_number()
        c_num = self._make_random_number(positive_or_negative="positive")
        d_num = self._make_random_number()
        
        a_term = a_num * self._used_character_dict["x"]
        c_term = c_num * self._used_character_dict["x"]
        if self._another_character_existence:
            b_term = b_num * self._used_character_dict["y"]
            d_term = d_num * self._used_character_dict["y"]
        else:
            b_term = b_num
            d_term = d_num
        
        problem = (a_term + b_term) * (c_term + d_term)
        latex_problem = sy.latex(problem)
        answer = sy.expand(problem)
        latex_answer = f"= {sy.latex(answer)}"
        
        return latex_answer, latex_problem
    
    def _make_three_terms_square(self):
        # (a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca
        a_num = self._make_random_number(positive_or_negative="positive")
        b_num = self._make_random_number()
        c_num = self._make_random_number()
        
        a_term = a_num * self._used_character_dict["x"]
        if self._another_character_existence:
            b_term = b_num * self._used_character_dict["y"]
            c_term = c_num * self._used_character_dict["z"]
        else:
            b_term = b_num
            c_term = c_num
        
        problem = (a_term + b_term + c_term) ** 2
        latex_problem = sy.latex(problem)
        """
        answer = sy.expand(problem)
        latex_answer = f"= {sy.latex(answer)}"
        """
        # manual adding
        latex_answer = "="
        if (a_num ** 2) == 1:
            latex_answer += "x^2"
        else:
            latex_answer += f"{sy.latex(a_num ** 2)}x^2"
        
        if (b_num ** 2) == 1:
            latex_answer += f"+ y^2"
        else:
            latex_answer += f"+ {sy.latex(b_num ** 2)}y^2"
    
        if (c_num ** 2) == 1:
            latex_answer += f"+ z^2"
        else:
            latex_answer += f"+ {sy.latex(c_num ** 2)}z^2"
        
        if (a_num * b_num) > 0:
            latex_answer += f"+ {sy.latex(2 * a_num * b_num)}xy"
        else:
            latex_answer += f"{sy.latex(2 * a_num * b_num)}xy"
        
        if (b_num * c_num) > 0:
            latex_answer += f"+ {sy.latex(2 * b_num * c_num)}yz"
        else:
            latex_answer += f"{sy.latex(2 * b_num * c_num)}yz"
        
        if (c_num * a_num) > 0:
            latex_answer += f"+ {sy.latex(2 * c_num * a_num)}zx"
        else:
            latex_answer += f"{sy.latex(2 * c_num * a_num)}zx"
        
        return latex_answer, latex_problem

    def _make_plus_cubed_problem(self):
        # '(a+b)^3=a^3+3a^2b+3ab^2+b^3'
        a_num = self._make_random_number(positive_or_negative="positive")
        b_num = self._make_random_number(positive_or_negative="positive")
        
        a_term = a_num * self._used_character_dict["x"]
        if self._another_character_existence:
            b_term = b_num * self._used_character_dict["y"]
        else:
            b_term = b_num
        
        problem = (a_term + b_term) ** 3
        latex_problem = sy.latex(problem)
        answer = sy.expand(problem)
        latex_answer = f"= {sy.latex(answer)}"
        
        return latex_answer, latex_problem

    def _make_minus_cubed_problem(self):
        # '(a-b)^3=a^3-3a^2b+3ab^2-b^3'
        a_num = self._make_random_number(positive_or_negative="positive")
        b_num = self._make_random_number(positive_or_negative="negative")
        
        a_term = a_num * self._used_character_dict["x"]
        if self._another_character_existence:
            b_term = b_num * self._used_character_dict["y"]
        else:
            b_term = b_num
        
        problem = (a_term + b_term) ** 3
        latex_problem = sy.latex(problem)
        answer = sy.expand(problem)
        latex_answer = f"= {sy.latex(answer)}"
        
        return latex_answer, latex_problem

    def _plus_minus_to_cubed_sum_problem(self):
        # (a+b)(a^2-ab+b^2)=a^3+b^3
        a_num = self._make_random_number(positive_or_negative="positive")
        b_num = self._make_random_number(positive_or_negative="positive")
        
        a_term = a_num * self._used_character_dict["x"]
        if self._another_character_existence:
            b_term = b_num * self._used_character_dict["y"]
        else:
            b_term = b_num
        
        problem = (a_term + b_term) * (a_term ** 2 - a_term * b_term + b_term ** 2)
        latex_problem = sy.latex(problem)
        answer = sy.expand(problem)
        latex_answer = f"= {sy.latex(answer)}"
        
        return latex_answer, latex_problem
    
    def _minus_plus_to_cubed_sum_problem(self):
        # '(a-b)(a^2+ab+b^2)=a^3-b^3'
        a_num = self._make_random_number(positive_or_negative="positive")
        b_num = self._make_random_number(positive_or_negative="positive")
        
        a_term = a_num * self._used_character_dict["x"]
        if self._another_character_existence:
            b_term = b_num * self._used_character_dict["y"]
        else:
            b_term = b_num
        
        problem = (a_term - b_term) * (a_term ** 2 + a_term * b_term + b_term ** 2)
        latex_problem = sy.latex(problem)
        answer = sy.expand(problem)
        latex_answer = f"= {sy.latex(answer)}"
        
        return latex_answer, latex_problem

    def _make_random_number(self, positive_or_negative=None):
        number = sy.Integer(randint(1, 6))
        
        if positive_or_negative is None:
            if random() > 0.5:
                number = -1 * number
        elif positive_or_negative == "negative":
            number = -1 * number
        elif positive_or_negative == "positive":
            pass
        
        return number
