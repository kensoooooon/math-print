from random import choice, randint, random, sample, shuffle

import sympy as sy


class LogarithmCalculationProblem:
    
    def __init__(self, **settings):
        self._problem_type_list = settings["problem_type_list"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        selected_problem_type = choice(self._problem_type_list)
        
        if selected_problem_type == "change_of_base_formula":
            latex_answer, latex_problem = self._make_change_of_base_problem()
        elif selected_problem_type == "add_and_subtraction_without_change_of_base_formula":
            latex_answer, latex_problem = self._make_add_and_subtraction_without_change_of_base_formula()
        elif selected_problem_type == "add_and_subtraction_with_change_of_base_formula":
            latex_answer, latex_problem = self._make_add_and_subtraction_with_change_of_base_formula()
        
        return latex_answer, latex_problem
    
    def _make_change_of_base_problem(self):
        common_base = choice([2, 3, 5, 7])
        logarithm_base = common_base ** randint(2, 10 - common_base)
        logarithm_antilog = common_base ** randint(2, 10 - common_base)
        latex_problem = f"\log_{{{logarithm_base}}} {logarithm_antilog}"
        
        denominator = int(sy.log(logarithm_base, common_base))
        numerator = int(sy.log(logarithm_antilog, common_base))
        answer = sy.Rational(numerator, denominator)
        latex_answer = f" = {sy.latex(answer)}"
        
        return latex_answer, latex_problem
    
    def _make_add_and_subtraction_without_change_of_base_formula(self):

        def random_pop_from_two_list(list1, list2):
            while True:
                if not(list1):
                    selected_list = list2
                    selected_type = "minus"
                elif not(list2):
                    selected_list = list1
                    selected_type = "plus"
                else:
                    if random() > 0.5:
                        selected_list = list1
                        selected_type = "plus"
                    else:
                        selected_list = list2
                        selected_type = "minus"
                popped_value = selected_list.pop()
                yield (popped_value, selected_type)
                
                if not(list1) and not(list2):
                    break

        base_and_antilog_list = [2, 3, 5, 7, 11]
        common_base = choice(base_and_antilog_list)

        numerator_list = []
        denominator_list = []

        for _ in range(4):
            if random() > 0.6:
                antilog_base = common_base
                if random() > 0.5:
                    numerator_list.append(antilog_base)
                else:
                    denominator_list.append(antilog_base)
            else:
                antilog_base = choice(base_and_antilog_list)
                numerator_list.append(antilog_base)
                denominator_list.append(antilog_base)
                
        multiplied_logarithm_antilog_list = []
        first_num = numerator_list.pop()
        multiplied_logarithm_antilog_list.append(first_num)

        for num in numerator_list:
            if random() > 0.5:
                multiplied_logarithm_antilog_list.append(num)
            else:
                multiplied_logarithm_antilog_list[-1] = num * multiplied_logarithm_antilog_list[-1]


        divided_logarithm_antilog_list = []
        first_num = denominator_list.pop()
        divided_logarithm_antilog_list.append(first_num)

        for num in denominator_list:
            if random() > 0.3:
                divided_logarithm_antilog_list.append(num)
            else:
                divided_logarithm_antilog_list[-1] = num * divided_logarithm_antilog_list[-1]

        shuffle(multiplied_logarithm_antilog_list)
        shuffle(divided_logarithm_antilog_list)

        antilog_numerator = 1
        for antilog in multiplied_logarithm_antilog_list:
            antilog_numerator = antilog_numerator * antilog

        antilog_denominator = 1
        for antilog in divided_logarithm_antilog_list:
            antilog_denominator = antilog_denominator * antilog

        frac = sy.Rational(antilog_numerator, antilog_denominator)

        log = sy.log(frac, common_base)

        problem = ""
        first_antilog = multiplied_logarithm_antilog_list.pop()
        problem += f"\log_{{{common_base}}} {first_antilog}"

        for antilog, selected_type in random_pop_from_two_list(multiplied_logarithm_antilog_list, divided_logarithm_antilog_list):
            if selected_type == "plus":
                problem += f"+ \log_{{{common_base}}} {antilog}"
            elif selected_type == "minus":
                problem += f"- \log_{{{common_base}}} {antilog}"
        
        latex_answer = f"= {sy.latex(log)}"
        latex_problem = problem
        
        return latex_answer, latex_problem
    
    def _make_add_and_subtraction_with_change_of_base_formula(self):
        base_and_antilog_candidate = [2, 3, 5, 7]
        x, y = sample(base_and_antilog_candidate, 2)
        
        num_checker = random()
        if num_checker < 0.33:
            # log(log + log) type
            a, b, c, d, e, f = [randint(1, 3) for _ in range(6)]
            
            out_term = sy.Rational(a, b)
            in_term1 = sy.Rational(c, d)
            in_term2 = sy.Rational(e, f)
            out_term_latex = f"\log_{{{x ** b}}} {y ** a}"
            in_term1_latex = f"\log_{{{y ** d}}} {x ** c}"
            in_term2_latex = f"\log_{{{y ** f}}} {x ** e}"
            
            def plus_minus_checker():
                check_num = randint(0, 1)

                if check_num == 0:
                    return "plus"
                else:
                    return "minus"
            
            plus_minus_set = plus_minus_checker()
            
            if plus_minus_set == "plus":
                answer = out_term * (in_term1 + in_term2)
                latex_answer = f"= {sy.latex(answer)}"
                if random() > 0.5:
                    latex_problem = f"{out_term_latex} ({in_term1_latex} + {in_term2_latex})"
                else:
                    latex_problem = f"({in_term1_latex} + {in_term2_latex}) {out_term_latex} "

            elif plus_minus_set == "minus":
                answer = out_term * (in_term1 - in_term2)
                latex_answer = f"= {sy.latex(answer)}"
                if random() > 0.5:
                    latex_problem = f"{out_term_latex} ({in_term1_latex} - {in_term2_latex})"
                else:
                    latex_problem = f"({in_term1_latex} - {in_term2_latex}) {out_term_latex} "

            return latex_answer, latex_problem
        
        elif (num_checker >= 0.33) and (num_checker <= 0.66):
            # (log \pm log)(log \pm log) type
            a, b, c, d, e, f, g, h = [randint(1, 3) for _ in range(8)]
            left_term1 = sy.Rational(a, b)
            left_term2 = sy.Rational(c, d)
            right_term1 = sy.Rational(e, f)
            right_term2 = sy.Rational(g, h)
            left_term1_latex = f"\log_{{{x ** b}}} {y ** a}"
            left_term2_latex = f"\log_{{{x ** d}}} {y ** c}"
            right_term1_latex = f"\log_{{{y ** f}}} {x ** e}"
            right_term2_latex = f"\log_{{{y ** h}}} {x ** g}"

            
            def plus_minus_checker():
                check_num = randint(0, 3)
                
                if check_num == 0:
                    return "plus plus"
                elif check_num == 1:
                    return "plus minus"
                elif check_num == 2:
                    return "minus plus"
                else:
                    return "minus minus"
            
            plus_minus_set = plus_minus_checker()
            
            if plus_minus_set == "plus plus":
                answer = (left_term1 + left_term2) * (right_term1 + right_term2)
                latex_answer = f" = {sy.latex(answer)}"
                latex_problem = f"({left_term1_latex} + {left_term2_latex})({right_term1_latex} + {right_term2_latex})"
            elif plus_minus_set == "plus minus":
                answer = (left_term1 + left_term2) * (right_term1 - right_term2)
                latex_answer = f" = {sy.latex(answer)}"
                latex_problem = f"({left_term1_latex} + {left_term2_latex})({right_term1_latex} - {right_term2_latex})"
            elif plus_minus_set == "minus plus":
                answer = (left_term1 - left_term2) * (right_term1 + right_term2)
                latex_answer = f" = {sy.latex(answer)}"
                latex_problem = f"({left_term1_latex} - {left_term2_latex})({right_term1_latex} + {right_term2_latex})"
            elif plus_minus_set == "minus minus":
                answer = (left_term1 - left_term2) * (right_term1 - right_term2)
                latex_answer = f" = {sy.latex(answer)}"
                latex_problem = f"({left_term1_latex} - {left_term2_latex})({right_term1_latex} - {right_term2_latex})"
                
            return latex_answer, latex_problem

        elif num_checker > 0.66:
            # log - log + log - log
            
            def log_latex_maker(base, antilog, coefficient=1):
                """
                need add \sqrt disturbance system?
                """
                # k log_x y -> k log_x y, log_x y^k , l log_x^l y^k 
                
                num_checker = random()
                if num_checker < 0.33:
                    # k log_x y
                    if coefficient == 1:
                        log_latex = f"\log_{{{base}}} {antilog}"
                    else:
                        log_latex = f"{coefficient} \log_{{{base}}} {antilog}"
                # log_x y^k
                elif (0.33 <= num_checker) and (num_checker <= 0.66): 
                    log_latex = f"\log_{{{x}}} {antilog ** coefficient}"
                # l log_x^l y^k
                else:
                    disturbance_num = randint(2, 3)
                    log_latex = f"{disturbance_num} \log_{{{base ** disturbance_num}}} {antilog ** coefficient}"
                
                return log_latex
            
            # redefine to suppress too high value
            base_and_antilog_candidate = [2, 3, 5]
            x, y = sample(base_and_antilog_candidate, 2)
            a, b, c, k = [randint(1, 3) for _ in range(4)]
            
            plus_log1_latex = " + " + log_latex_maker(x, y, k)
            minus_log1_latex = " - " + log_latex_maker(x, y, k)

            if random() > 0.5:
                plus_log2_latex = " + " + log_latex_maker(x, (x ** y) * a * b)
                minus_log2_latex = " - " + log_latex_maker(x, a * b)
                latex_answer = f"= {sy.latex(y)}"
            else:
                plus_log2_latex = " + " + log_latex_maker(x, a * b)
                minus_log2_latex = " - " + log_latex_maker(x, (x ** y) * a * b)
                latex_answer = f"= {sy.latex(-y)}"
            
            num_list = [plus_log1_latex, minus_log1_latex, plus_log2_latex, minus_log2_latex]
            shuffle(num_list)
            
            latex_problem = ""
            first_num = num_list.pop()
            if " + " in first_num:
                first_num = first_num.replace("+", "")
                print(f"first_num: {first_num}")
            latex_problem += first_num
            for num in num_list:
                latex_problem += num
            
            return latex_answer, latex_problem
