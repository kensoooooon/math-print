from operator import le
from random import choice, randint, random

import sympy as sy


class RecurrenceRelationProblem:
    """漸化式から一般項を求める問題と解答を出力
    
    Attributes:
        _problem_types (list): 問題となる漸化式の候補を格納
        latex_answer (str): latex形式で記述された解答
        latex_problem (str): latex形式で記述された問題
    """
    def __init__(self, **settings):
        """初期処理
        
        Args:
            settings (dict): 問題の設定を格納
        """
        sy.init_printing(order='grevlex')
        self._problem_types = settings["problem_type_list"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        """問題の対象とする漸化式を決定し、解答と問題を出力する

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Raises:
            ValueError: 
        """
        selected_problem_type = choice(self._problem_types)
        if selected_problem_type == "arithmetic_progression":
            latex_answer, latex_problem = self._make_arithmetic_progression_problem()
        elif selected_problem_type == "geometric_progression":
            latex_answer, latex_problem = self._make_geometric_progression_problem()
        elif selected_problem_type == "progression_of_differences":
            latex_answer, latex_problem = self._make_progression_of_differences_problem()
        elif selected_problem_type == "harmonic_progression":
            latex_answer, latex_problem = self._make_harmonic_progression_problem()
        elif selected_problem_type == "linear_characteristic_equation":
            latex_answer, latex_problem = self._make_linear_characteristic_equation_problem()
        elif selected_problem_type == "coefficient_comparison_to_geometric_progression":
            latex_answer, latex_problem = self._make_coefficient_comparison_to_geometric_progression_problem()
        else:
            raise ValueError(f"selected_problem_type is {selected_problem_type}.")
        return latex_answer, latex_problem
    
    def _make_arithmetic_progression_problem(self):
        """等差型の漸化式の解答と問題を出力する
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        common_difference, common_difference_latex = self._make_random_integer()
        first_term, first_term_latex = self._make_random_integer()
        n = sy.Symbol("n", real=True)
        general_term = common_difference * n + (first_term - common_difference)
        general_term_latex = sy.latex(sy.simplify(general_term))
        # a_{n+1}-a_{n}=d
        if random() > 0.5:
            latex_problem = f"\\( a_{{1}} = {first_term_latex}, \\quad a_{{n+1}} - a_{{n}} = {common_difference_latex} \\) "
        # a_{n+1} = a_{n} + d
        else:
            if common_difference > 0:
                latex_problem = f"\\( a_{{1}} = {first_term_latex}, \\quad a_{{n+1}} = a_{{n}} + {common_difference_latex} \\)"
            else:
                latex_problem = f"\\( a_{{1}} = {first_term_latex}, \\quad a_{{n+1}} = a_{{n}} {common_difference_latex} \\)"
        latex_answer = ""
        latex_answer += f"\\( a_{{n+1}} - a_{{n}} = {common_difference_latex} \\)より、数列 \\( a_{{n}} \\)は、\n"
        latex_answer += f"初項\\( {first_term_latex} \\)、公差\\( {common_difference_latex} \\)の等差数列である。よって、\n"
        if common_difference > 0:
            latex_answer += f"\\( a_{{n}} = {first_term_latex} + (n - 1) {common_difference_latex} \\)"
        else:
            latex_answer += f"\\( a_{{n}} = {first_term_latex} + (n - 1) ({common_difference_latex}) \\)"
        latex_answer += f"\\( = {general_term_latex} \\)"
        return latex_answer, latex_problem

    def _make_geometric_progression_problem(self):
        """等比型の漸化式の解答と問題を出力する
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        common_ratio, common_ratio_latex = self._make_random_integer(nearer_distance_from_zero=2, farther_distance_from_zero=7)
        first_term, first_term_latex = self._make_random_integer(nearer_distance_from_zero=2, farther_distance_from_zero=7)
        n = sy.Symbol("n", real=True)
        general_term = first_term * (common_ratio ** (n - 1))
        general_term_latex = sy.latex(sy.simplify(general_term))
        # a_{n+1} = r a_{n}
        if random() > 0.5:
            latex_problem = f"\\( a_{{1}} = {first_term_latex}, \\quad a_{{n+1}} = {common_ratio_latex} a_{{n}}\\)"
        # a_{n+1} / a_{n} = r
        else:
            latex_problem = f"\\( a_{{1}} = {first_term_latex}, \\quad \\frac{{a_{{n+1}}}}{{a_{{n}}}} = {common_ratio_latex} \\)"
        latex_answer = ""
        latex_answer += f"\\( a_{{n+1}} = {common_ratio_latex} a_{{n}} \\)より、数列 \\( a_{{n}} \\)は、\n"
        latex_answer += f"初項\\( {first_term_latex} \\)、公差\\( {common_ratio_latex} \\)の等比数列である。よって、\n"
        if common_ratio > 0:
            latex_answer += f"\\( a_{{n}} = {first_term_latex} \\cdot {common_ratio_latex}^{{n-1}} \\)"
        elif common_ratio < 0:
            latex_answer += f"\\( a_{{n}} = {first_term_latex} \\cdot ({common_ratio_latex})^{{n-1}} \\)"
        latex_answer += f"\\( = {general_term_latex} \\)"
        return latex_answer, latex_problem

    def _make_progression_of_differences_problem(self):
        """階差型(a_n+1 - a_n = f(n))の漸化式の問題と解答を出力する

        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_answer (str): latex形式で記述された問題
        """
        # arithmetic progression
        if random() > 0.5:
            first_term, first_term_latex = self._make_random_integer()
            n = sy.Symbol("n", real=True)
            coefficient_of_n, coefficient_of_n_latex = self._make_random_integer(farther_distance_from_zero=7)
            constant_number, constant_number_latex = self._make_random_integer()
            progression_of_differences = coefficient_of_n * n + constant_number
            progression_of_differences_latex = sy.latex(progression_of_differences)
            # a_{n+1} - a_{n} = f(n)
            if random() > 0.5:
                latex_problem = f"\\( a_{{1}} = {first_term_latex}, \\quad  a_{{n+1}} - a_{{n}} = {progression_of_differences_latex} \\)"
            # a_{n+1} - a_{n} - f(n) = 0
            else:
                if coefficient_of_n > 0:
                    latex_problem = f"\\( a_{{1}} = {first_term_latex}, \\quad a_{{n+1}} - a_{{n}} {sy.latex(-1 * progression_of_differences)} = 0\\)"
                else:
                    latex_problem = f"\\( a_{{1}} = {first_term_latex}, \\quad a_{{n+1}} - a_{{n}}  + {sy.latex(-1 * progression_of_differences)} = 0\\)"
            latex_answer = f"\\( a_{{n+1}} - a_{{n}} = {progression_of_differences_latex} \\)より、\\( {{ {progression_of_differences_latex} }}\\)は、数列\\( {{a_{n}}} \\)の階差数列である。 \n"
            k = sy.Symbol("k", real=True)
            progression_of_differences_for_sum = coefficient_of_n * k + constant_number
            progression_of_differences_for_sum_latex = sy.latex(progression_of_differences_for_sum)
            latex_answer += f"\\( n \\geqq 2 \\)のとき、\\( a_{{n}} = a_{{1}} + \\sum\\limits_{{k=1}}^{{n-1}} ({progression_of_differences_for_sum_latex}) \\)\n"
            # add function part.
            sum_of_value = sy.summation(progression_of_differences, (n, 1, n-1))
            general_term = first_term + sum_of_value
            general_term_latex = sy.latex(general_term)
            latex_answer += f"\\( = {general_term_latex} \\) \n"
            latex_answer += f"また\\( n = 1 \\)のときを計算すると、\\( a_{{1}} = {sy.latex(general_term.subs(n, 1)) }\\)となるため、この式は\\( n = 1 \\)の時も成り立つ。\n"
            latex_answer += f"よって、\\( a_{{n}} = {general_term_latex} \\)"
        # geometric progression
        else:
            first_term, first_term_latex = self._make_random_integer()
            n = sy.Symbol("n", real=True)
            common_ratio, common_ratio_latex = self._make_random_integer()
            progression_of_differences = first_term * (common_ratio ** (n - 1))
            progression_of_differences_latex = sy.latex(progression_of_differences)
            # a_{n+1} - a_{n} = f(n)
            if random() > 0.5:
                latex_problem = f"\\( a_{{1}} = {first_term_latex}, \\quad  a_{{n+1}} - a_{{n}} = {progression_of_differences_latex} \\)"
            # a_{n+1} - a_{n} - f(n) = 0
            else:
                if first_term > 0:
                    latex_problem = f"\\( a_{{1}} = {first_term_latex}, \\quad a_{{n+1}} - a_{{n}} {sy.latex(-1 * progression_of_differences)} = 0\\)"
                else:
                    latex_problem = f"\\( a_{{1}} = {first_term_latex}, \\quad a_{{n+1}} - a_{{n}}  + {sy.latex(-1 * progression_of_differences)} = 0\\)"
            latex_answer = f"\\( a_{{n+1}} - a_{{n}} = {progression_of_differences_latex} \\)より、\\( {{ {progression_of_differences_latex} }}\\)は、数列\\( {{a_{n}}} \\)の階差数列である。 \n"
            k = sy.Symbol("k", real=True)
            progression_of_differences_for_sum = first_term * (common_ratio ** (k - 1))
            progression_of_differences_for_sum_latex = sy.latex(progression_of_differences_for_sum)
            latex_answer += f"\\( n \\geqq 2 \\)のとき、\\( a_{{n}} = a_{{1}} + \\sum\\limits_{{k=1}}^{{n-1}} ({progression_of_differences_for_sum_latex}) \\)\n"
            sum_of_value = sy.summation(progression_of_differences, (n, 1, n-1))
            general_term = first_term + sum_of_value
            general_term_latex = sy.latex(general_term)
            latex_answer += f"\\( = {general_term_latex} \\) \n"
            latex_answer += f"また\\( n = 1 \\)のときを計算すると、\\( a_{{1}} = {sy.latex(general_term.subs(n, 1)) }\\)となるため、この式は\\( n = 1 \\)の時も成り立つ。\n"
            latex_answer += f"よって、\\( a_{{n}} = {general_term_latex} \\)"
        return latex_answer, latex_problem
    
    def _make_harmonic_progression_problem(self):
        """調和数列型(a_n+1 a_n - p a_n+1 + p a_n = 0)の漸化式の問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        first_term, first_term_latex = self._make_random_integer()
        a_n_plus_1 = sy.Symbol("a_{{n+1}}", real=True)
        a_n = sy.Symbol("a_{{n}}", real=True)
        p, p_latex = self._make_random_integer()
        left = a_n_plus_1 * a_n - p * a_n_plus_1 + p * a_n
        left_latex = sy.latex(left)
        right = 0
        right_latex = sy.latex(right)
        latex_problem = f"\\( a_{{1}} = {first_term_latex}, \\quad {left_latex} = {right_latex} \\)"
        if p > 0:
            latex_answer = f"\\( a_{{n+1}} = 0 \\)と仮定すると、\\( 0 - 0 + {p_latex} a_{{n}} = 0\\)より、\\( a_{{n}} = 0 \\)となる。\n"
        else:
            latex_answer = f"\\( a_{{n+1}} = 0 \\)と仮定すると、\\( 0 + 0 {p_latex} a_{{n}} = 0\\)より、\\( a_{{n}} = 0\\)となる。 \n"
        latex_answer += f"すなわち、\\( a_{{n+1}} = a_{{n}} = a_{{n-1}} = \\cdots = a_{{2}} = a_{{1}} = 0\\)となるが、"
        latex_answer += f"これは\\( a_{{1}} = {first_term_latex} \\)と矛盾する。\n"
        latex_answer += f"よって、全ての自然数\\( n \\)において、\\( a_{{n}} \\neq 0 \\)であることが示せた。\n"
        latex_answer += f"ここで、与えられた漸化式の両辺を\\( a_{{n+1}} a_{{n}} \\)で割ると、"
        divided_left = sy.simplify(left / (a_n_plus_1 * a_n))
        divided_left_latex = sy.latex(divided_left)
        latex_answer += f"\\( {divided_left_latex} = {right_latex} \\)となる。\n"
        rearranged_left_latex = f"\\frac{{1}}{{{a_n_plus_1}}} - \\frac{{1}}{{{a_n}}}"
        rearranged_right = -1 * sy.Rational(1, p)
        rearranged_right_latex = sy.latex(rearranged_right)
        latex_answer += f"これを整理すると、\\( {rearranged_left_latex} = {rearranged_right_latex} \\)となる。\n"
        first_term_of_arithmetic_progression = sy.Rational(1, first_term)
        first_term_of_arithmetic_progression_latex = sy.latex(first_term_of_arithmetic_progression)
        common_difference_of_arithmetic_progression = rearranged_right
        common_difference_of_arithmetic_progression_latex = sy.latex(common_difference_of_arithmetic_progression)
        latex_answer += f"これにより、数列 \\( {sy.latex(1 / a_n)} \\)は、初項\\( \\frac{{1}}{{a_1}} = {first_term_of_arithmetic_progression_latex} \\)、公差\\( {common_difference_of_arithmetic_progression_latex} \\)の等差数列となるため、\n"
        n = sy.Symbol("n", real=True)
        general_term_of_arithmetic_progression =  first_term_of_arithmetic_progression + (n - 1) * common_difference_of_arithmetic_progression
        general_term_of_arithmetic_progression_latex = sy.latex(general_term_of_arithmetic_progression)
        if common_difference_of_arithmetic_progression > 0:
            latex_answer += f"\\(  {sy.latex(1 / a_n)} = {first_term_latex} + (n - 1) \\cdot {common_difference_of_arithmetic_progression_latex} = {general_term_of_arithmetic_progression_latex} \\)となる。\n"
        else:
            latex_answer += f"\\(  {sy.latex(1 / a_n)} = {first_term_latex} + (n - 1) \\cdot ({common_difference_of_arithmetic_progression_latex}) = {general_term_of_arithmetic_progression_latex} \\)となる。\n"
        general_term = sy.simplify((first_term * p) / (p - first_term * (n - 1)))
        general_term_latex  = sy.latex(general_term)
        latex_answer += f"これを整理すると、\\( a_{{n}} = {general_term_latex} \\)"
        return latex_answer, latex_problem
    
    def _make_linear_characteristic_equation_problem(self):
        """一次の特性方程式を用いるタイプ(a_n+1 = p a_n + q)の漸化式の問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        a_n_plus_1 = sy.Symbol("a_{{n+1}}", real=True)
        a_n = sy.Symbol("a_{{n}}", real=True)
        p, p_latex = self._make_random_integer(nearer_distance_from_zero=2, farther_distance_from_zero=5)
        characteristic_answer, _ = self._make_random_integer(farther_distance_from_zero=4)
        q = characteristic_answer * (1 - p)
        if random() > 0.5:
            first_term = characteristic_answer + randint(1, 10)
        else:
            first_term = characteristic_answer - randint(1, 10)
        first_term_latex = sy.latex(first_term)
        latex_problem = f"\\(a_{{1}} = {first_term_latex}, \\quad \\)"
        problem_display_checker = random()
        # a_{{n+1}} = p a_{{n}} + q
        if problem_display_checker < 0.33:
            left = a_n_plus_1
            left_latex = sy.latex(a_n_plus_1)
            right = p * a_n + q
            right_latex = sy.latex(right)
        # a_{{n+1}} - p a_{{n}} = q
        elif 0.33 <= problem_display_checker < 0.66:
            left = a_n_plus_1 - p * a_n
            left_latex = sy.latex(left)
            right = q
            right_latex = sy.latex(right)
        # a_{{n+1}} - p a_{{n}} - q = 0
        else:
            left = a_n_plus_1 - p * a_n - q
            left_latex = sy.latex(left)
            right = 0
            right_latex = sy.latex(right)
        latex_problem += f"\\( {left_latex} = {right_latex} \\)"
        # a_n - characteristic_answer as b_n
        rearranged_recurrence_relation = sy.Eq(a_n_plus_1, p * a_n + q)
        rearranged_recurrence_relation_latex = sy.latex(rearranged_recurrence_relation)
        latex_answer = f"\\( {rearranged_recurrence_relation_latex} \\)を変形すると、"
        b_n_equation = sy.Eq(a_n - characteristic_answer, sy.factor(p * (a_n - characteristic_answer)))
        b_n_equation_latex = sy.latex(b_n_equation)
        latex_answer += f"\\( {b_n_equation_latex} \\)となる。\n"
        a_1 = sy.Symbol("a_{{1}}", real=True)
        first_term_of_b_n =first_term - characteristic_answer
        first_term_of_b_n_latex= sy.latex(first_term_of_b_n)
        latex_answer += f"すなわち、数列\\( {{{sy.latex(b_n_equation.lhs)}}}\\)は、初項が\\( {sy.latex(a_1 - characteristic_answer)} = {first_term_of_b_n_latex} \\)、"
        latex_answer += f"公比が\\( {p_latex} \\)の等比数列である。\n"
        n = sy.Symbol("n", real=True)
        general_term_of_b_n = first_term_of_b_n * (p ** (n - 1))
        general_term_of_b_n_latex = sy.latex(general_term_of_b_n)
        latex_answer += f"よって、\\( {sy.latex(b_n_equation.lhs)} = {general_term_of_b_n_latex} \\)となり、"
        general_term = general_term_of_b_n + characteristic_answer
        general_term_latex = sy.latex(general_term)
        latex_answer += f"\\( {sy.latex(a_n)} = {general_term_latex} \\)となる。"
        return latex_answer, latex_problem
    
    def _make_coefficient_comparison_to_geometric_progression_problem(self):
        """係数比較を行った後、等比数列に帰着するタイプ(a_{n+1} = p a_{n} + f(n))の漸化式の問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Developing:
            a_{n+1} = p a_{n} + f(n)
        """
        first_term, first_term_latex = self._make_random_integer(farther_distance_from_zero=5)
        a_n_plus_1 = sy.Symbol("a_{{n+1}}", real=True)
        a_n_plus_1_latex = sy.latex(a_n_plus_1)
        a_n = sy.Symbol("a_{{n}}", real=True)
        a_n_latex = sy.latex(a_n)
        p, p_latex = self._make_random_integer(nearer_distance_from_zero=2, farther_distance_from_zero=4)
        print(f"p: {p}")
        n = sy.Symbol("n", real=True)
        selected_expression_of_degree_n = choice(["linear", "quadratic"])
        # f(n) = sn + t (-> a_{n+1} + α(n+1) + β = p(a_{n} + αn + β))
        if selected_expression_of_degree_n == "linear":
            alpha, alpha_latex = self._make_random_integer(farther_distance_from_zero=5)
            beta, beta_latex = self._make_random_integer(farther_distance_from_zero=5)
            s = alpha * (p - 1)
            s_latex = sy.latex(s)
            t = -alpha + (p - 1) * beta
            t_latex = sy.latex(t)
            expression_of_degree_n = s * n + t
        # f(n) = sn^2 + tn + u (-> a_{n+1} + α(n+1)^2 + β(n+1) + γ = p(a_{n} + αn^2 + βn + γ))
        elif selected_expression_of_degree_n == "quadratic":
            alpha, alpha_latex = self._make_random_integer(farther_distance_from_zero=5)
            beta, beta_latex = self._make_random_integer(farther_distance_from_zero=5)
            gamma, gamma_latex = self._make_random_integer(farther_distance_from_zero=5)
            s = alpha * (p - 1)
            s_latex = sy.latex(s)
            t = beta * p - 2 * alpha - beta
            t_latex = sy.latex(t)
            u = p * gamma - alpha - beta - gamma
            u_latex = sy.latex(u)
            expression_of_degree_n = s * (n ** 2) + t * n + u
        expression_of_degree_n_latex = sy.latex(expression_of_degree_n)
        print(f"expression_of_degree_n: {expression_of_degree_n}")
        display_type_checker = random()
        left = a_n_plus_1
        left_latex = sy.latex(left)
        right = p * a_n + expression_of_degree_n
        right_latex = f"{sy.latex(p * a_n)}"
        right_poly_coeffs = sy.poly(right, a_n, n).coeffs()
        most_highest_n_coeff = right_poly_coeffs[1]
        if most_highest_n_coeff > 0:
            right_latex += f"+ {expression_of_degree_n_latex}"
        else:
            right_latex += expression_of_degree_n_latex
        rearranged_progression_latex = f"{left_latex} = {right_latex}"
        # a_{n+1} = p a_{n} + f(n) (same as above)
        if display_type_checker < 0.33:
            pass
        # a_{n+1} - p a_{n} = f(n)
        elif 0.33 <= display_type_checker < 0.66:
            left = a_n_plus_1 - p * a_n
            left_latex = sy.latex(left)
            right_latex = expression_of_degree_n_latex
        # a_{n+1} - p a_{n} - f(n) = 0
        else:
            left_latex = f"{a_n_plus_1_latex}"
            if p > 0:
                left_latex += f"- {p_latex} {a_n_latex}"
            else:
                left_latex += f"+ {sy.latex(p * -1)} {a_n_latex}"
            negative_expression_of_degree_n = -1 * expression_of_degree_n
            most_highest_n_coeff = sy.poly(negative_expression_of_degree_n).coeffs()[0]
            if most_highest_n_coeff > 0:
                left_latex += f"+ {sy.latex(negative_expression_of_degree_n)}"
            else:
                left_latex += f"{sy.latex(negative_expression_of_degree_n)}"
            right_latex = sy.latex(0)
        progression_latex = f"{left_latex} = {right_latex}"
        latex_problem = f"\\( a_{{1}} = {first_term_latex}, \\quad {progression_latex} \\)"
        # a_{n+1} + α(n+1) + β = p(a_{n} + αn + β)
        if selected_expression_of_degree_n == "linear":
            latex_answer = f"与えられた漸化式、\\( {rearranged_progression_latex} \\)の\\( {a_n_latex} \\)の係数である\\( \\underline{{{p_latex}}} \\)に注目し、"
            latex_answer += f"\\( {a_n_plus_1_latex} + \\alpha (n + 1) + \\beta = \\underline{{{p_latex}}} ({a_n_latex} + \\alpha n + \\beta ) \\)"
            latex_answer += f"となるように定数\\( \\alpha \\)と\\( \\beta \\)を定めていく。\n"
            rearranged_left = a_n_plus_1
            rearranged_left_latex = sy.latex(rearranged_left)
            rearranged_right_latex = f"{sy.latex(p * a_n)}"
            coefficient_of_alpha_n = p - 1
            coefficient_of_alpha_n_latex = sy.latex(coefficient_of_alpha_n)
            if coefficient_of_alpha_n == 1:
                rearranged_right_latex += f"+ \\alpha {sy.latex(n)}"
            elif coefficient_of_alpha_n == -1:
                rearranged_right_latex += f"- \\alpha {sy.latex(n)}"
            elif coefficient_of_alpha_n > 0:
                rearranged_right_latex += f"+ {coefficient_of_alpha_n_latex} \\alpha {sy.latex(n)}"
            else:
                rearranged_right_latex += f"{coefficient_of_alpha_n_latex} \\alpha {sy.latex(n)}"
            constant_part_latex = f"- \\alpha"
            if (p - 1) > 0:
                constant_part_latex += f"+ {sy.latex(p - 1)} \\beta"
            else:
                constant_part_latex += f"{sy.latex(p - 1)} \\beta"
            rearranged_right_latex += f"+ ({constant_part_latex})"
            latex_answer += f"この式を整理すると、\\( {rearranged_left_latex} = {rearranged_right_latex} \\)となる。\n"
            latex_answer += f"これを元の漸化式\\( {rearranged_progression_latex} \\)と比較すると、"
            latex_answer += f"\\( {coefficient_of_alpha_n} \\alpha = {s_latex}, \\quad {constant_part_latex} = {t_latex} \\)より、"
            latex_answer += f"\\( \\alpha = {alpha_latex}, \\quad \\beta = {beta_latex} \\)となる。\n"
            common_ratio_progression_left_latex = f"{a_n_plus_1_latex}"
            common_ratio_progression_right_latex = f"{p_latex} ( {a_n_latex}"
            if alpha > 0:
                common_ratio_progression_left_latex += f"+ {alpha_latex} (n + 1)"
                common_ratio_progression_right_latex += f"+ {alpha_latex} n"
            else:
                common_ratio_progression_left_latex += f"{alpha_latex} (n + 1)"
                common_ratio_progression_right_latex += f"{alpha_latex} n"
            if beta > 0:
                common_ratio_progression_left_latex += f"+ {beta_latex}"
                common_ratio_progression_right_latex += f"+ {beta_latex})"
            else:
                common_ratio_progression_left_latex += f"{beta_latex}"
                common_ratio_progression_right_latex += f"{beta_latex})"
            latex_answer += f"よって、\\( {common_ratio_progression_left_latex} = {common_ratio_progression_right_latex} \\)となるため、\n"
            general_term_left = a_n + alpha * n + beta
            general_term_left_latex = sy.latex(general_term_left)
            latex_answer += f"数列\\({{ {general_term_left_latex} }} \\)は、初項"
            if alpha > 0:
                latex_answer += f"\\( a_{{1}} + {alpha_latex} \\cdot 1"
            else:
                latex_answer += f"\\( a_{{1}} {alpha_latex} \\cdot 1"
            if beta > 0:
                latex_answer += f" + {beta_latex}"
            else:
                latex_answer += f" {beta_latex}"
            common_ratio_first_term = first_term + alpha * 1 + beta
            common_ratio_first_term_latex = sy.latex(common_ratio_first_term)
            latex_answer += f"= {common_ratio_first_term_latex} \\)、公比\\( {p_latex} \\)の等比数列である。\n"
            general_term_right = common_ratio_first_term * (p ** (n - 1))
            general_term_right_latex = sy.latex(general_term_right)
            latex_answer += f"ゆえに、\\( {general_term_left_latex} = {general_term_right_latex} \\)であり、これを整理すると、"
            final_general_term_left = a_n
            final_general_term_left_latex = sy.latex(final_general_term_left)
            final_general_term_right = general_term_right - (alpha * n + beta)
            final_general_term_right_latex = sy.latex(final_general_term_right)
            latex_answer += f"\\( {final_general_term_left_latex} = {final_general_term_right_latex} \\)となる。"
        elif selected_expression_of_degree_n == "quadratic":
            latex_answer = f"与えられた漸化式、\\( {rearranged_progression_latex} \\)の\\( {a_n_latex} \\)の係数である\\( \\underline{{{p_latex}}} \\)に注目し、"
            latex_answer += f"\\( {a_n_plus_1_latex} + \\alpha (n + 1)^2 + \\beta (n + 1) + \\gamma = \\underline{{{p_latex}}} ({a_n_latex} + \\alpha n^2 + \\beta n + \\gamma) \\)"
            latex_answer += f"となるように定数\\( \\alpha \\)と\\( \\beta \\)と\\( \\gamma \\)を定めていく。\n"
            rearranged_left = a_n_plus_1
            rearranged_left_latex = sy.latex(rearranged_left)
            rearranged_right_latex = f"{sy.latex(p * a_n)}"
            coefficient_of_alpha_n_square = p - 1
            coefficient_of_alpha_n_square_latex = sy.latex(coefficient_of_alpha_n_square)
            n_square_part = f"{coefficient_of_alpha_n_square_latex} \\alpha"
            if coefficient_of_alpha_n_square > 0:
                rearranged_right_latex += f"+ {n_square_part}  {sy.latex(n ** 2)}"
            else:
                rearranged_right_latex += f"{n_square_part}  {sy.latex(n ** 2)}"
            beta_coefficient_in_n = p - 1
            beta_coefficient_in_n_latex = sy.latex(beta_coefficient_in_n)
            if beta_coefficient_in_n == 1:
                n_part = "-2 \\alpha + \\beta"
            elif beta_coefficient_in_n == -1:
                n_part = "-2 \\alpha - \\beta"
            elif beta_coefficient_in_n > 0:
                n_part = f"-2 \\alpha + {beta_coefficient_in_n_latex} \\beta"
            else:
                n_part = f"-2 \\alpha {beta_coefficient_in_n_latex} \\beta"
            rearranged_right_latex += f"+ ({n_part}) n"
            gamma_coefficient_in_constant_part = p - 1
            gamma_coefficient_in_constant_part_latex = sy.latex(gamma_coefficient_in_constant_part)
            if gamma_coefficient_in_constant_part == 1:
                constant_part = "- \\alpha - \\beta + \\gamma"
                rearranged_right_latex += f"+ ({constant_part})"
            elif gamma_coefficient_in_constant_part == -1:
                constant_part = "- \\alpha - \\beta - \\gamma"
                rearranged_right_latex += f"+ ({constant_part})"
            elif gamma_coefficient_in_constant_part > 0:
                constant_part = f"- \\alpha - \\beta + {gamma_coefficient_in_constant_part_latex} \\gamma"
                rearranged_right_latex += f"+ ({constant_part})"
            else:
                constant_part = f"- \\alpha - \\beta {gamma_coefficient_in_constant_part_latex} \\gamma"
                rearranged_right_latex += f"+ ({constant_part})"
            latex_answer += f"この式を整理すると、\\( {rearranged_left_latex} = {rearranged_right_latex} \\)となる。\n"
            latex_answer += f"これを元の漸化式\\( {rearranged_progression_latex} \\)と比較すると、"
            latex_answer += f"\\( {coefficient_of_alpha_n} \\alpha = {s_latex}, \\quad"
            if beta_coefficient_in_n > 0:
                
                
                
        return latex_answer, latex_problem
        
    def _make_random_integer(self, nearer_distance_from_zero=1, farther_distance_from_zero=10, positive_or_negative=None):
        """原点からの距離がnearer_distance_from_zero以上farther_distance_from_zero以下の範囲の整数を出力

        Args:
            nearer_distance_from_zero (int, optional): 原点により近いポイントまでの距離。デフォルトは10
            farther_distance_from_zero (int, optional): 原点からより遠いポイントまでの距離。デフォルトは10
            positive_or_negative (Union[str, NoneType], optional): 正負の指定。デフォルトはNone.

        Raises:
            ValueError: nearer_distance_from_zeroとfarther_distance_from_zeroの大小関係が入れ替わっていたとき。
                あるいは0より小さかったとき。あるいは整数ではなかったときに挙上
            TypeError: positive_or_negativeがpositive, negative, Noneのいずれでもなかったときに挙上

        Returns:
            integer (sy.Integer): 計算に用いる整数
            integer_latex (str): latex形式で記述された整数
        """
        if nearer_distance_from_zero >= farther_distance_from_zero:
            raise ValueError(
                f"'nearer_distance_from_zero' is {nearer_distance_from_zero}."\
                f"'farther_distance_from_zero' is {farther_distance_from_zero}."\
                "farther_distance_from_zero must be more than nearer_distance_from_zero."\
                )
        if (nearer_distance_from_zero < 0) or not(isinstance(nearer_distance_from_zero, int)):
            raise ValueError(f"'nearer_distance_from_zero' is {nearer_distance_from_zero}. It must be integer and zero or more.")
        if (farther_distance_from_zero < 0) or not(isinstance(farther_distance_from_zero, int)):
            raise ValueError(f"'farther_distance_from_zero' is {farther_distance_from_zero}. It must be integer and zero or more.")
        
        if positive_or_negative == "positive":
            integer = sy.Integer(randint(nearer_distance_from_zero, farther_distance_from_zero))
        elif positive_or_negative == "negative":
            integer = sy.Integer(randint(-farther_distance_from_zero, -nearer_distance_from_zero))
        elif positive_or_negative is None:
            if random() > 0.5:
                integer = sy.Integer(randint(nearer_distance_from_zero, farther_distance_from_zero))
            else:
                integer = sy.Integer(randint(-farther_distance_from_zero, -nearer_distance_from_zero))
        else:
            raise TypeError(f"'positive_or_negative' is {positive_or_negative}. It must be 'positive', 'negative or None.")
        
        integer_latex = sy.latex(integer)
        return integer, integer_latex
