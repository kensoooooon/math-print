from random import choice, randint

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
        """
        selected_problem_type = choice(self._problem_types)
        if selected_problem_type == "arithmetic_progression":
            latex_answer, latex_problem = self._make_arithmetic_progression_problem()
        elif selected_problem_type == "geometric_progression":
            latex_answer, latex_problem = self._make_geometric_progression_problem()
        elif selected_problem_type == "progression_of_differences":
            latex_answer, latex_problem = self._make_progression_of_differences_problem()
        
        return latex_answer, latex_problem
    
    def _make_arithmetic_progression_problem(self):
        """等差型の漸化式の解答と問題を出力する
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        n = sy.Symbol("n")
        common_difference, common_difference_latex = self._make_random_integer_without_zero()
        first_term, first_term_latex = self._make_random_integer_without_zero()
        coefficient_of_n_latex = sy.latex(common_difference)
        constant_term = first_term - common_difference
        constant_term_latex = sy.latex(constant_term)
        if constant_term > 0:
            general_term_latex = f"{common_difference_latex} n + {constant_term_latex}"
        elif constant_term < 0:
            general_term_latex = f"{common_difference_latex} n {constant_term_latex}"
        else:
            general_term_latex = f"{common_difference_latex} n" 
        # a_{n+1}-a_{n}=d
        if random() > 0.5:
            latex_problem = f"\\( a_{{1}} = {first_term_latex}, a_{{n+1}} - a_{{n}} = {common_difference_latex} \\) "
            latex_answer = ""
            latex_answer += f"\\( a_{{n+1}} - a_{{n}} = {common_difference_latex} \\)より、数列 \\( a_{{n}} \\)は \n"
            latex_answer += f"初項\\( {first_term_latex} \\)、公差\\( {common_difference_latex} \\)の等差数列である。よって、 \n"
            if common_difference > 0:
                latex_answer += f"\\( a_{{n}} = {first_term_latex} + (n - 1) {common_difference_latex} \\)"
            else:
                latex_answer += f"\\( a_{{n}} = {first_term_latex} + (n - 1) ({common_difference_latex}) \\)"
            latex_answer += f"\\( {general_term_latex} \\)"
        # a_{n+1} = a_{n} + d
        else:
            if common_difference > 0:
                latex_problem = f"\\( a_{{1}} = {first_term_latex}, a_{{n+1}} = a_{{n}} + {common_difference_latex} \\)"
                latex_answer = f""
            else:
                latex_problem = f"\\( a_{{1}} = {first_term_latex}, a_{{n+1}} = a_{{n}} {common_difference_latex} \\)"
        
        
    
    def _make_random_integer_without_zero(self, min_num=-10, max_num=10):
        """指定された最小値から最大値の範囲の整数とそのlatexを出力

        Args:
            min_num (int, optional): 最小値。デフォルトは-10
            max_num (int, optional): 最大値。デフォルトは-10

        Returns:
            integer (sy.Integer): 整数
            integer_latex (str): latex形式で記述された整数
        """
        if random() > 0.5:
            integer = sy.Integer(randint(1, 10))
        else:
            integer = sy.Integer(randint(-10, -1))
        integer_latex = sy.latex(integer)
        return integer, integer_latex
            
