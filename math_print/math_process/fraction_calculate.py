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
            
            selected_fraction_type = self._fraction_type_selector()
            
            if selected_fraction_type == "proper_fraction":
                latex_problem_to_add, string_for_eval_to_add = self._make_latex_and_eval_proper_fraction()
            elif selected_fraction_type == "improper_fraction":
                latex_problem_to_add, string_for_eval_to_add = self._make_latex_and_eval_improper_fraction()
            elif selected_fraction_type == "mixed_fraction":
                latex_problem_to_add, string_for_eval_to_add = self._make_latex_and_eval_mixed_fraction()
            
            latex_problem += latex_problem_to_add
            string_for_eval += string_for_eval_to_add
            
            for _ in range(self._term_number - 1):
                selected_operator_type = self._operator_type_selector()
                
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
                
                selected_fraction_type = self._fraction_type_selector()

                if selected_fraction_type == "proper_fraction":
                    latex_problem_to_add, string_for_eval_to_add = self._make_latex_and_eval_proper_fraction()
                elif selected_fraction_type == "improper_fraction":
                    latex_problem_to_add, string_for_eval_to_add = self._make_latex_and_eval_improper_fraction()
                elif selected_fraction_type == "mixed_fraction":
                    latex_problem_to_add, string_for_eval_to_add = self._make_latex_and_eval_mixed_fraction()
                else:
                    raise ValueError(f"selected_fraction_type: {selected_fraction_type}. It may be wrong.")
                
                latex_problem += f"{operator_for_latex} {latex_problem_to_add}"
                string_for_eval += f"{operator_for_eval} {string_for_eval_to_add}"
            
            # print(f"string_for_eval: {string_for_eval}")
            answer = eval(string_for_eval)
            # print(f"answer: {answer}")
            if answer >= 0:
                break

        latex_answer = f"= {sy.latex(answer)}"
        
        return latex_answer, latex_problem
    
    def _fraction_type_selector(self):
        if self._fraction_type_list:
            selected_fraction_type = choice(self._fraction_type_list)
        else:
            selected_fraction_type = choice(
                ["proper_fraction", "improper_fraction", "mixed_fraction"]
            )
        return selected_fraction_type

    def _operator_type_selector(self):
        if self._calculate_types_list:
            selected_operator_type = choice(self._calculate_types_list)
        else:
            selected_operator_type = choice(
                ["plus", "minus", "times", "division"]
            )
        
        return selected_operator_type
        
    def _make_random_positive_integer(self, max_num, min_num):
        
        integer = sy.Integer(randint(min_num, max_num))
        
        return integer
    
    def _make_random_positive_frac_number(self, max_num, min_num, denominator=randint(2, 15)):
        numerator = randint(min_num, max_num)
        frac = sy.Rational(numerator, denominator)
               
        return frac
    
    def _make_latex_and_eval_proper_fraction(self):
        denominator = self._make_random_positive_integer(self._max_number_to_denominator, self._min_number_to_denominator)
        if denominator == 1:
            numerator = 1
        else:
            numerator = denominator - self._make_random_positive_integer(denominator-1, 1)
        frac = sy.Rational(numerator, denominator)
        if frac.denominator == 1:
            latex_problem_to_add = f"{frac.numerator}"
        else:
            latex_problem_to_add = f"\\frac{{ {numerator} }}{{ {denominator} }}"
        string_for_eval_to_add = f"sy.Rational({frac.numerator}, {frac.denominator})"
        
        return latex_problem_to_add, string_for_eval_to_add
    
    def _make_latex_and_eval_improper_fraction(self):
        denominator = self._make_random_positive_integer(self._max_number_to_denominator, self._min_number_to_denominator)
        numerator = self._make_random_positive_integer(self._max_number_to_numerator, self._min_number_to_numerator)
        frac = sy.Rational(numerator, denominator)
        if frac.denominator == 1:
            latex_problem_to_add = f"{frac.numerator}"
        else:
            latex_problem_to_add = f"\\frac{{ {numerator} }}{{ {denominator} }}"
        string_for_eval_to_add = f"sy.Rational({frac.numerator}, {frac.denominator})"
        
        return latex_problem_to_add, string_for_eval_to_add
    
    def _make_latex_and_eval_mixed_fraction(self):
        number_on_the_left_side_of_frac = self._make_random_positive_integer(self._max_number_on_the_left_of_frac, self._min_number_on_the_left_of_frac)
        denominator = self._make_random_positive_integer(self._max_number_to_denominator, self._min_number_to_denominator)
        if denominator == 1:
            numerator = 1
        else:
            numerator = denominator - self._make_random_positive_integer(denominator-1, 1)
        
        frac = number_on_the_left_side_of_frac + sy.Rational(numerator, denominator)
        if frac.denominator == 1:
            latex_problem_to_add = f"{frac.numerator}"
        else:
            latex_problem_to_add = f"{number_on_the_left_side_of_frac} \\frac{{{numerator}}}{{{denominator}}}"
        string_for_eval_to_add = f"sy.Rational({frac.numerator}, {frac.denominator})"
        
        return latex_problem_to_add, string_for_eval_to_add
    