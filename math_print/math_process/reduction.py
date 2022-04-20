from random import choice, randint, random

import sympy as sy

class ReductionProblem:
    
    def __init__(self, **settings):
        self._fraction_type_list = settings["fraction_type_list"]
        self._min_number_to_denominator = settings["min_number_to_denominator"]
        self._max_number_to_denominator = settings["max_number_to_denominator"]
        self._min_number_to_numerator = settings["min_number_to_numerator"]
        self._max_number_to_numerator = settings["max_number_to_numerator"]
        self._min_number_on_the_left_of_frac = settings["min_number_on_the_left_of_frac"]
        self._max_number_on_the_left_of_frac = settings["max_number_on_the_left_of_frac"]
        self._min_number_to_reduction = settings["min_number_to_reduction"]
        self._max_number_to_reduction = settings["max_number_to_reduction"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        if self._fraction_type_list:
            selected_fraction_type = choice(self._fraction_type_list)
        else:
            selected_fraction_type = choice(
                ["proper_fraction", "improper_fraction", "mixed_fraction"]
            )
        
        if selected_fraction_type == "proper_fraction":
            latex_answer, latex_problem = self._make_proper_fraction_problem()
        elif selected_fraction_type == "improper_fraction":
            latex_answer, latex_problem = self._make_improper_fraction_problem()
        elif selected_fraction_type == "mixed_fraction":
            latex_answer, latex_problem = self._make_mixed_fraction_problem()
        
        return latex_answer, latex_problem

    def _make_proper_fraction_problem(self):
        
        while True:
            numerator = randint(self._min_number_to_numerator, self._max_number_to_numerator)
            denominator = randint(self._min_number_to_denominator, self._max_number_to_denominator)
            
            if numerator < denominator:
                break

        fraction = sy.Rational(numerator, denominator)
        latex_answer = f"= \\dfrac{{ {fraction.numerator} }}{{ {fraction.denominator} }}"
        
        multiplied_number = randint(self._min_number_to_reduction, self._max_number_to_reduction)
        multiplied_numerator = numerator * multiplied_number
        multiplied_denominator = denominator * multiplied_number
        multiplied_fraction_latex = f"\\dfrac{{ {multiplied_numerator} }}{{ {multiplied_denominator} }}"
        latex_problem = multiplied_fraction_latex
        
        return latex_answer, latex_problem
    
    def _make_improper_fraction_problem(self):
        while True:
            numerator = randint(self._min_number_to_numerator, self._max_number_to_numerator)
            denominator = randint(self._min_number_to_denominator, self._max_number_to_denominator)
            
            if numerator != denominator:
                break

        fraction = sy.Rational(numerator, denominator)
        if fraction.denominator == 1:
            latex_answer = f"= {fraction.numerator}"
        else:
            latex_answer = f"= \\dfrac{{ {fraction.numerator} }}{{ {fraction.denominator} }}"
        
        multiplied_number = randint(self._min_number_to_reduction, self._max_number_to_reduction)
        multiplied_numerator = numerator * multiplied_number
        multiplied_denominator = denominator * multiplied_number
        multiplied_fraction_latex = f"\\dfrac{{ {multiplied_numerator} }}{{ {multiplied_denominator} }}"
        latex_problem = f"{multiplied_fraction_latex}"
        
        return latex_answer, latex_problem
    
    def _make_mixed_fraction_problem(self):
        while True:
            numerator = randint(self._min_number_to_numerator, self._max_number_to_numerator)
            denominator = randint(self._min_number_to_denominator, self._max_number_to_denominator)
            
            if numerator < denominator:
                break
        
        number_on_the_left_of_fraction = randint(self._min_number_on_the_left_of_frac, self._max_number_on_the_left_of_frac)
        
        fraction = sy.Rational(numerator, denominator)
        latex_answer = f"= {number_on_the_left_of_fraction} \\dfrac{{ {fraction.numerator} }}{{ {fraction.denominator} }}"
        
        multiplied_number = randint(self._min_number_to_reduction, self._max_number_to_reduction)
        multiplied_numerator = numerator * multiplied_number
        multiplied_denominator = denominator * multiplied_number
        multiplied_fraction_latex =f"\\dfrac{{ {multiplied_numerator} }}{{ {multiplied_denominator} }}"
        latex_problem = f"{number_on_the_left_of_fraction}{multiplied_fraction_latex}"
        
        return latex_answer, latex_problem
    