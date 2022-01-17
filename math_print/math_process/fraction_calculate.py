from random import choice, randint, random

import sympy as sy

class FractionCalculateProblem:
    
    def __init__(self, **settings):
        self._calculate_types_list = settings["calculate_type_list"]
        self._fraction_type_list = settings["fraction_type_list"]
        self._term_number = settings["term_number"]
        self._min_number_to_denominator = settings["min_number_to_denominator"]
        self._max_number_to_denominator = settings["max_number_to_denominator"]
        self._min_number_to_numerator = settings["min_number_to_numerator"]
        self._max_number_to_numerator = settings["max_number_to_numerator"]
        self._min_number_on_the_left_of_frac = settings["min_number_on_the_left_of_frac"]
        self._max_number_on_the_left_of_frac = settings["max_number_on_the_left_of_frac"]
        self.latex_answer, self.latex_problem = self._make_problem()
        
    
    def _make_problem(self):
        while True:
            latex_problem = ""
            string_for_eval = ""
            
            selected_fraction_type = choice(self._fraction_type_list)
            
            if selected_fraction_type == "proper_fraction":
                denominator = self._make_random_positive_integer(self._max_number_to_denominator, self._min_number_to_denominator)
                if denominator == 1:
                    numerator = 1
                else:
                    numerator = denominator - self._make_random_positive_integer(denominator-1, 1)
                first_frac = sy.Rational(numerator, denominator)
                if first_frac.denominator == 1:
                    latex_problem += f"{first_frac.numerator}"
                else:
                    latex_problem += f"\\frac{{ {numerator} }}{{ {denominator} }}"
                string_for_eval += f"sy.Rational({first_frac.numerator}, {first_frac.denominator})"

            elif selected_fraction_type == "improper_fraction":
                denominator = self._make_random_positive_integer(self._max_number_to_denominator, self._min_number_to_denominator)
                numerator = self._make_random_positive_integer(self._max_number_to_numerator, self._min_number_to_numerator)
                first_frac = sy.Rational(numerator, denominator)
                if first_frac.denominator == 1:
                    latex_problem += f"{first_frac.numerator}"
                else:
                    latex_problem += f"\\frac{{ {numerator} }}{{ {denominator} }}"
                string_for_eval = f"sy.Rational({first_frac.numerator}, {first_frac.denominator})"
            
            elif selected_fraction_type == "mixed_fraction":
                number_on_the_left_side_of_frac = self._make_random_positive_integer(self._max_number_on_the_left_of_frac, self._min_number_on_the_left_of_frac)
                denominator = self._make_random_positive_integer(self._max_number_to_denominator, self._min_number_to_denominator)
                if denominator == 1:
                    numerator = 1
                else:
                    numerator = denominator - self._make_random_positive_integer(denominator-1, 1)
                
                first_frac = number_on_the_left_side_of_frac + sy.Rational(numerator, denominator)
                if first_frac.denominator == 1:
                    latex_problem += f"{first_frac.numerator}"
                else:
                    latex_problem += f"{number_on_the_left_side_of_frac} \\frac{{{numerator}}}{{{denominator}}}"
                string_for_eval += f"sy.Rational({first_frac.numerator}, {first_frac.denominator})"

            else:
                raise ValueError(f"selected_fraction_type: {selected_fraction_type}. It may be wrong.")
            
            for _ in range(self._term_number - 1):
                selected_operator_type = choice(self._calculate_types_list)
                
                if selected_operator_type == "plus":
                    operator_for_eval = "+"
                    operator_for_latex = "+"
                elif selected_operator_type == "minus":
                    operator_for_eval = "-"
                    operator_for_latex = "-"
                elif selected_operator_type == "times":
                    operator_for_eval = "*"
                    operator_for_latex = "\\times"
                elif selected_operator_type == "division":
                    operator_for_eval = "/"
                    operator_for_latex = "\\div"
                else:
                    raise ValueError(f"selected_operator_type: {selected_operator_type}. It may be wrong.")
                
                selected_fraction_type = choice(self._fraction_type_list)
                if selected_fraction_type == "proper_fraction":
                    denominator = self._make_random_positive_integer(self._max_number_to_denominator, self._min_number_to_denominator)
                    if denominator == 1:
                        numerator = 1
                    else:
                        numerator = denominator - self._make_random_positive_integer(denominator-1, 1)
                    frac = sy.Rational(numerator, denominator)
                    if frac.denominator == 1:
                        latex_problem += f"{operator_for_latex} {frac.numerator}"
                    else: 
                        latex_problem += f"{operator_for_latex} \\frac{{{frac.numerator}}}{{{frac.denominator}}}"
                    string_for_eval += f"{operator_for_eval} sy.Rational({frac.numerator}, {frac.denominator})"

                elif selected_fraction_type == "improper_fraction":
                    denominator = self._make_random_positive_integer(self._max_number_to_denominator, self._min_number_to_denominator)
                    numerator = self._make_random_positive_integer(self._max_number_to_numerator, self._max_number_to_numerator)
                    frac = sy.Rational(numerator, denominator)
                    if frac.denominator == 1:
                        latex_problem += f"{operator_for_latex} {frac.numerator}"
                    else:
                        latex_problem += f"{operator_for_latex} \\frac{{{frac.numerator}}}{{{frac.denominator}}}"
                    string_for_eval += f"{operator_for_eval} sy.Rational({frac.numerator}, {frac.denominator})"

                elif selected_fraction_type == "mixed_fraction":
                    number_on_the_left_side_of_frac = self._make_random_positive_integer(self._max_number_on_the_left_of_frac, self._min_number_on_the_left_of_frac)
                    denominator = self._make_random_positive_integer(self._max_number_to_denominator, self._min_number_to_denominator)
                    if denominator == 1:
                        numerator = 1
                    else:
                        numerator = denominator - self._make_random_positive_integer(denominator-1, 1)
                    frac = number_on_the_left_side_of_frac + sy.Rational(numerator, denominator)
                    if frac.denominator == 1:
                        latex_problem += f"{operator_for_latex} {frac.numerator}"
                    else:
                        latex_problem += f"{operator_for_latex} {number_on_the_left_side_of_frac} \\frac{{{numerator}}}{{{denominator}}}"
                    string_for_eval += f"{operator_for_eval} sy.Rational({frac.numerator}, {frac.denominator})"
                else:
                    raise ValueError(f"selected_fraction_type: {selected_fraction_type}. It may be wrong.")
            
            answer = eval(string_for_eval)
            if answer >= 0:
                break

        latex_answer = f"= {sy.latex(answer)}"
        
        return latex_answer, latex_problem

    def _make_random_positive_integer(self, max_num, min_num):
        
        integer = sy.Integer(randint(min_num, max_num))
        
        return integer
    
    def _make_random_positive_frac_number(self, max_num, min_num, denominator=randint(2, 15)):
        numerator = randint(min_num, max_num)
        frac = sy.Rational(numerator, denominator)
               
        return frac