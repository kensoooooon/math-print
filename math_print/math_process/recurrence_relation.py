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
        print(f"selected_problem_type: {selected_problem_type}")
        if selected_problem_type == "arithmetic_progression":
            latex_answer, latex_problem = self._make_arithmetic_progression_problem()
        elif selected_problem_type == "geometric_progression":
            latex_answer, latex_problem = self._make_geometric_progression_problem()
        elif selected_problem_type == "progression_of_differences":
            latex_answer, latex_problem = self._make_progression_of_differences_problem()
        elif selected_problem_type == "harmonic_progression":
            latex_answer, latex_problem = self._make_harmonic_progression_problem()
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
        """階差型の漸化式の問題と解答を出力する

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
        """調和数列型の問題と解答を出力
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        
        Developing:
            a_n+1 a_n - p a_n+1 + p a_n = 0
        """
        first_term, first_term_latex = self._make_random_integer()
        print(f"first_term: {first_term}")
        a_n_plus_1 = sy.Symbol("a_{{n+1}}", real=True)
        a_n = sy.Symbol("a_{{n}}", real=True)
        p, p_latex = self._make_random_integer()
        print(f"p: {p}")
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
        latex_answer += f"よって、全ての自然数\\( n \\)において、\\( a_{{n}} \\neq 0 \\)であることが示せた。"
        latex_answer += f"ここで、与えられた漸化式の両辺を\\( a_{{n+1}} a_{{n}} \\)で割ると、\n"
        divided_left = sy.simplify(left / (a_n_plus_1 * a_n))
        divided_left_latex = sy.latex(divided_left)
        latex_answer += f"\\( {divided_left_latex} = {right_latex} \\)となる。これを整理すると、\n"
        # rearranged_left = (p / a_n_plus_1) - (p / a_n)
        # rearranged_left_latex = sy.latex(sy.simplify(rearranged_left))
        rearranged_left_latex = f"\\frac{{1}}{{{a_n_plus_1}}} - \\frac{{1}}{{{a_n}}}"
        rearranged_right = -1 * sy.Rational(1, p)
        rearranged_right_latex = sy.latex(rearranged_right)
        latex_answer += f"\\( {rearranged_left_latex} = {rearranged_right_latex} \\)となる。これにより、数列 \\( {sy.latex(1 / a_n)} \\)は、"
        first_term_of_arithmetic_progression = sy.Rational(1, first_term)
        first_term_of_arithmetic_progression_latex = sy.latex(first_term_of_arithmetic_progression)
        common_difference_of_arithmetic_progression = rearranged_right
        common_difference_of_arithmetic_progression_latex = sy.latex(common_difference_of_arithmetic_progression)
        latex_answer += f"初項\\( \\frac{{1}}{{a_1}} = {first_term_of_arithmetic_progression_latex} \\)、公差\\( {common_difference_of_arithmetic_progression_latex} \\)の等差数列となるため、\n"
        n = sy.Symbol("n", real=True)
        general_term_of_arithmetic_progression =  first_term_of_arithmetic_progression + (n - 1) * common_difference_of_arithmetic_progression
        general_term_of_arithmetic_progression_latex = sy.latex(general_term_of_arithmetic_progression)
        latex_answer += f"\\(  {sy.latex(1 / a_n)} = {general_term_of_arithmetic_progression_latex} \\)となる。これを整理すると、"
        general_term = sy.simplify((first_term * p) / (p - first_term * (n - 1)))
        print(f"general_term: {general_term}")
        general_term_latex  = sy.latex(general_term)
        latex_answer += f"\\( a_{{n}} = {general_term_latex} \\)"
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
