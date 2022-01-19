from random import choice, randint, random

import sympy as sy


class NumberWithoutBracketCalculateProblem:
    def __init__(self, **settings):
        self._term_number = settings["term_number"]
        self._operator_to_use_list = settings["operator_to_use_list"]
        self._number_to_use_list = settings["number_to_use_list"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        # 小数表示用の判定リスト
        used_number_type_list = []
        latex_problem = ""
        string_for_eval = ""
        
        first_number_type = choice(self._number_to_use_list)
        
        if first_number_type == "one_digit_integer":
            latex_problem_to_add, string_for_eval_to_add = self._make_latex_and_eval_one_digit_integer()
        elif first_number_type == "two_digit_integer":
            latex_problem_to_add, string_for_eval_to_add = self._make_latex_and_eval_two_digit_integer()
        elif first_number_type == "decimal":
            latex_problem_to_add, string_for_eval_to_add = self._make_latex_and_eval_decimal()
        elif first_number_type == "frac":
            latex_problem_to_add, string_for_eval_to_add = self._make_latex_and_eval_frac()
        else:
            raise ValueError(f"first_number_type: {first_number_type}. It may be wrong.")
        
        used_number_type_list.append(first_number_type)
        
        latex_problem +=  latex_problem_to_add
        string_for_eval += string_for_eval_to_add
        
        for _ in range(self._term_number - 1):
            selected_operator_type = choice(self._operator_to_use_list)
            if selected_operator_type == "plus":
                operator_for_eval = "+"
                operator_for_latex = "+"
            elif selected_operator_type == "minus":
                operator_for_eval = "-"
                operator_for_latex = "-"
            else:
                raise ValueError(f"selected_operator_type: {selected_operator_type}. It may be wrong.")

            selected_number_type = choice(self._number_to_use_list)
            if selected_number_type == "one_digit_integer":
                latex_problem_to_add, string_for_eval_to_add = self._make_latex_and_eval_one_digit_integer()
            elif selected_number_type == "two_digit_integer":
                latex_problem_to_add, string_for_eval_to_add = self._make_latex_and_eval_two_digit_integer()
            elif selected_number_type == "decimal":
                latex_problem_to_add, string_for_eval_to_add = self._make_latex_and_eval_decimal()
            elif selected_number_type == "frac":
                latex_problem_to_add, string_for_eval_to_add = self._make_latex_and_eval_frac()
            else:
                raise ValueError(f"selected_number_type: {selected_number_type}. It may be wrong.")
            
            used_number_type_list.append(selected_number_type)
            
            latex_problem += f"{operator_for_latex} {latex_problem_to_add}"
            string_for_eval += f"{operator_for_eval} {string_for_eval_to_add}"
        
        answer = eval(string_for_eval)
        if ("frac" not in set(used_number_type_list)) and ("decimal" in set(used_number_type_list)):
            answer = float(answer)
        latex_answer = f"= {sy.latex(answer)}"
        
        return latex_answer, latex_problem

    def _make_latex_and_eval_one_digit_integer(self):
        number = randint(1, 9)
        
        integer = sy.Integer(number)
        
        latex_problem_to_add = sy.latex(integer)
        string_for_eval_to_add = f"sy.Integer({number})"
        
        return latex_problem_to_add, string_for_eval_to_add

    def _make_latex_and_eval_two_digit_integer(self):
        number = randint(10, 99)
        
        integer = sy.Integer(number)
        
        latex_problem_to_add = sy.latex(integer)
        string_for_eval_to_add = f"sy.Integer({number})"
        
        return latex_problem_to_add, string_for_eval_to_add

    def _make_latex_and_eval_decimal(self):
        while True:
            denominator = 10
            numerator = randint(1, 100)
            frac = sy.Rational(numerator, denominator)
            
            if frac.denominator != 1:
                break
        
        latex_problem_to_add = sy.latex(float(frac))
        string_for_eval_to_add = f"sy.Rational({frac.numerator}, {frac.denominator})"
        
        return latex_problem_to_add, string_for_eval_to_add
    
    def _make_latex_and_eval_frac(self):
        while True:
            denominator = randint(2, 20)
            numerator = randint(2, 20)
            frac = sy.Rational(numerator, denominator)
            
            if frac.denominator != 1:
                break
        
        latex_problem_to_add = f"\\frac{{ {numerator} }}{{ {denominator} }}"
        string_for_eval_to_add = f"sy.Rational({frac.numerator}, {frac.denominator})"
        
        return latex_problem_to_add, string_for_eval_to_add