from random import choice, randint, random

import sympy as sy


class CompletingTheSquareProblem:
    
    def __init__(self, **settings):
        sy.init_printing(order='grevlex', long_frac_ration=2)
        self._used_number_type_list = settings["used_number_type_list"]
        self._character_dict = {}
        self._character_dict["x"] = sy.Symbol("x", real=True)
        # add to character in coefficient 4.25
        # t may occur problem?? y is correct???????
        self._character_dict["y"] = sy.Symbol("y", real=True)
        # True or False
        self._include_character_in_coefficient = settings["include_character_in_coefficient"]
        
        if settings["number_including_in_bracket"] == "not_including_fraction":
            self.latex_answer, self.latex_problem = self._make_only_integer_completing_the_square()
        elif settings["number_including_in_bracket"] == "including_fraction":
            self.latex_answer, self.latex_problem = self._make_completing_the_square()
    
    def _make_only_integer_completing_the_square(self):
        # a(x+b)^2+c
        a_num = self._make_random_number(integer_or_frac_specification="integer")
        b_num = self._make_random_number(integer_or_frac_specification="integer")
        if self._include_character_in_coefficient:
            b_num = b_num * self._character_dict["y"]
        c_num = self._make_random_number(integer_or_frac_specification="integer")
        if self._include_character_in_coefficient:
            if random() > 0.5:
                c_num = c_num * self._character_dict["y"] 
        
        answer = a_num * (self._character_dict["x"] + b_num) ** 2 + c_num
        latex_answer = f"= {sy.latex(answer)}"
        problem = sy.expand(answer)
        latex_problem = sy.latex(problem)
        
        return latex_answer, latex_problem

    def _make_completing_the_square(self):
        # a(x+b)^2+c
        a_num = self._make_random_number()
        b_num = self._make_random_number()
        if self._include_character_in_coefficient:
            b_num = b_num * self._character_dict["y"]
        c_num = self._make_random_number()
        if self._include_character_in_coefficient:
            if random() > 0.5:
                c_num = c_num * self._character_dict["y"]

        answer = a_num * (self._character_dict["x"] + b_num) ** 2 + c_num
        latex_answer = f"= {sy.latex(answer)}"
        problem = sy.expand(answer)
        latex_problem = sy.latex(problem)
        
        return latex_answer, latex_problem
    
    def _number_type_selector(self):
        if self._used_number_type_list:
            selected_number_type = choice(self._used_number_type_list)
        else:
            selected_number_type = choice(["integer", "frac"])
        return selected_number_type

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
