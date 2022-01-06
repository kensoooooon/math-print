from random import choice, randint, random

import sympy as sy

class ReductionProblem:
    
    def __init__(self, **settings):
        self._fraction_type_list = settings["fraction_type_list"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        selected_fraction_type = choice(self._fraction_type_list)
        
        if selected_fraction_type == "proper_fraction":
            latex_answer, latex_problem = self._make_proper_fraction_problem()
        elif selected_fraction_type == "improper_fraction":
            latex_answer, latex_problem = self._make_improper_fraction_problem()
        elif selected_fraction_type == "mixed_fraction":
            latex_answer, latex_problem = self._make_mixed_fraction_problem()
        
        return latex_answer, latex_problem

    def _make_proper_fraction_problem(self):
        
        while True:
            numerator = randint(2, 15)
            denominator = randint(2, 15)
            
            if numerator < denominator:
                break

        fraction = sy.Rational(numerator, denominator)
        # fraction_latex = sy.latex(fraction)
        latex_answer = f"= \\dfrac{{ {fraction.numerator} }}{{ {fraction.denominator} }}"
        
        multiplied_number = randint(2, 6)
        multiplied_numerator = numerator * multiplied_number
        multiplied_denominator = denominator * multiplied_number
        # multiplied_fraction = sy.Rational(multiplied_numerator, multiplied_denominator)
        multiplied_fraction_latex = f"\\dfrac{{ {multiplied_numerator} }}{{ {multiplied_denominator} }}"
        latex_problem = multiplied_fraction_latex
        
        return latex_answer, latex_problem
    
    def _make_improper_fraction_problem(self):
        while True:
            numerator = randint(2, 15)
            denominator = randint(2, 15)
            
            if numerator != denominator:
                break

        fraction = sy.Rational(numerator, denominator)
        # fraction_latex = sy.latex(fraction)
        if fraction.denominator == 1:
            latex_answer = f"= {fraction.numerator}"
        else:
            latex_answer = f"= \\dfrac{{ {fraction.numerator} }}{{ {fraction.denominator} }}"
        
        multiplied_number = randint(2, 6)
        multiplied_numerator = numerator * multiplied_number
        multiplied_denominator = denominator * multiplied_number
        # multiplied_fraction = sy.Rational(multiplied_numerator, multiplied_denominator)
        multiplied_fraction_latex = f"\\dfrac{{ {multiplied_numerator} }}{{ {multiplied_denominator} }}"
        latex_problem = f"{multiplied_fraction_latex}"
        
        return latex_answer, latex_problem
    
    def _make_mixed_fraction_problem(self):
        while True:
            numerator = randint(2, 15)
            denominator = randint(2, 15)
            
            if numerator < denominator:
                break
        
        number_on_the_left_of_fraction = randint(1, 4)
        
        fraction = sy.Rational(numerator, denominator)
        # fraction_latex = sy.latex(fraction)
        latex_answer = f"= {number_on_the_left_of_fraction} \\dfrac{{ {fraction.numerator} }}{{ {fraction.denominator} }}"
        
        multiplied_number = randint(2, 6)
        multiplied_numerator = numerator * multiplied_number
        multiplied_denominator = denominator * multiplied_number
        # multiplied_fraction = sy.Rational(multiplied_numerator, multiplied_denominator)
        multiplied_fraction_latex =f"\\dfrac{{ {multiplied_numerator} }}{{ {multiplied_denominator} }}"
        latex_problem = f"{number_on_the_left_of_fraction}{multiplied_fraction_latex}"
        
        return latex_answer, latex_problem

    def _make_random_integer_positive_number(self, max_num ,min_num):
        number = randint(min_num, max_num)
        
        integer = sy.Integer(number)
        integer_latex = sy.latex(integer)
        
        return integer, integer_latex
    