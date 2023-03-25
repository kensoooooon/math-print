from random import choice, randint, random


import sympy as sy


class SameDenominatorCalculate:
    """同じ分母の足し算・引き算の問題を出力
    
    Attributes:
        _calculate_type (list): 計算に使用される演算子が格納
        _term_numbers (list): 問題の項数が格納
        latex_answer (str): latex形式で記述された解答
        latex_problem (str): latex形式で記述された問題
    """
    def __init__(self, **settings):
        """初期設定
        
        Args:
            settings (dict): 問題の各種設定
        """
        sy.init_printing(order='grevlex')
        self._calculate_type = settings["calculate_type"]
        self._term_numbers = settings["term_number"]
        self.latex_answer, self.latex_problem = self._make_problem()
    
    def _make_problem(self):
        """指定された計算の条件を満たす問題と解答を出力するコントローラ
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題 
        
        Developing:
            真分数のみ
            計算結果は約分しない正の値
            途中表示も約分は不可
        """
        if self._calculate_type == ["addition"]:
            latex_answer, latex_problem = self._make_addition_only_problem()
        elif self._calculate_type == ["subtraction"]:
            latex_answer = "dummy answer"
            latex_problem = "dummy problem"
        elif self._calculate_type == ["addition", "subtraction"]:
            latex_answer = "dummy answer"
            latex_problem = "dummy problem"
        return latex_answer, latex_problem
    
    def _make_addition_only_problem(self):
        """足し算だけの計算問題を作成
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        latex_problem = ""
        string_
        denominator = randint(2, 18)
        term_number = int(choice(self._term_numbers))
        for _ in range(term_number):
            
        
        # divided?
        if term_number == 2:
            pass
        elif term_number == 3:
            pass
        elif term_number == 4:
            pass
        else:
            raise ValueError(f"'term_number' is {term_number}. This must be 2, 3 or 4.")
        

    def _make_latex_and_eval_proper_fraction(self):
        denominator = randint(2, 18)
        numerator = denominator - randint(1, denominator-1)
        latex_problem_to_add = f"\\frac{{ {numerator} }}{{ {denominator} }}"
        string_for_eval_to_add = f"sy.Rational({numerator}, {denominator})"
        return latex_problem_to_add, string_for_eval_to_add