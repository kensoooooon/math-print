from random import choice, randint, random, shuffle


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
            latex_answer, latex_problem = self._make_subtraction_only_problem()
        elif self._calculate_type == ["addition", "subtraction"]:
            problem_checker = random()
            if 0 <= problem_checker < 0.25:
                latex_answer, latex_problem = self._make_addition_only_problem()
            elif 0.25 <= problem_checker < 0.5:
                latex_answer, latex_problem = self._make_subtraction_only_problem()
            else:
                latex_answer, latex_problem = self._make_mixed_problem()
            # for making.
            # latex_answer, latex_problem = self._make_mixed_problem()
        return latex_answer, latex_problem
    
    def _make_addition_only_problem(self):
        """足し算だけの計算問題を作成
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        common_denominator = randint(5, 18)
        term_number = int(choice(self._term_numbers))
        if term_number == 2:
            numerator1 = randint(1, common_denominator - 2)
            numerator2 = randint(1, common_denominator - numerator1 - 1)
            latex_answer = f"= \\frac{{{numerator1 + numerator2}}}{{{common_denominator}}}"
            if random() > 0.5:
                numerator1, numerator2 = numerator2, numerator1
            latex_problem = f"\\frac{{{numerator1}}}{{{common_denominator}}} + \\frac{{{numerator2}}}{{{common_denominator}}}"
            latex_answer = f"= \\frac{{{numerator1 + numerator2}}}{{{common_denominator}}}"
        elif term_number == 3:
            max_numerator = randint(4, common_denominator)
            numerator1 = randint(1, max_numerator - 3)
            numerator2 = randint(1, max_numerator - numerator1 - 2)
            numerator3 = randint(1, max_numerator - numerator1 - numerator2 - 1)
            numerators = [numerator1, numerator2, numerator3]
            shuffle(numerators)
            numerator1, numerator2, numerator3 = numerators
            latex_problem = f"\\frac{{{numerator1}}}{{{common_denominator}}}"
            latex_problem += f"+ \\frac{{{numerator2}}}{{{common_denominator}}}"
            latex_problem += f"+ \\frac{{{numerator3}}}{{{common_denominator}}}"
            latex_answer = f"= \\frac{{{numerator1 + numerator2 + numerator3}}}{{{common_denominator}}}"
        else:
            raise ValueError(f"'term_number' is {term_number}. This must be 2 or 3.")
        return latex_answer, latex_problem
    
    def _make_subtraction_only_problem(self):
        """引き算だけの計算問題を作成
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
        """
        common_denominator = randint(6, 20)
        term_number = int(choice(self._term_numbers))
        if term_number == 2:
            numerator1 = randint(2, common_denominator - 1)
            numerator2 = randint(1, numerator1 - 1)
            latex_problem = f"\\frac{{{numerator1}}}{{{common_denominator}}} - \\frac{{{numerator2}}}{{{common_denominator}}}"
            latex_answer = f"= \\frac{{{numerator1 - numerator2}}}{{{common_denominator}}}"
        elif term_number == 3:
            numerator1 = randint(4, common_denominator - 1)
            sum_of_numerator2_and_3 = randint(2, numerator1 - 1)
            numerator2 = randint(1, sum_of_numerator2_and_3 - 1)
            numerator3 = sum_of_numerator2_and_3 - numerator2
            if random() > 0.5:
                numerator2, numerator3 = numerator3, numerator2
            latex_problem = f"\\frac{{{numerator1}}}{{{common_denominator}}}"
            latex_problem += f"- \\frac{{{numerator2}}}{{{common_denominator}}}"
            latex_problem += f"- \\frac{{{numerator3}}}{{{common_denominator}}}"
            latex_answer = f"= \\frac{{{numerator1 - numerator2 - numerator3}}}{{{common_denominator}}}"
        else:
            raise ValueError(f"'term_number' is {term_number}. This must be 2 or 3.")
        return latex_answer, latex_problem
    
    def _make_mixed_problem(self):
        """足し算と引き算が混合された計算問題を作成
        
        Returns:
            latex_answer (str): latex形式で記述された解答
            latex_problem (str): latex形式で記述された問題
           
        Developing:
            ・真分数かつ答えは正
            ・アクセスの方と共通の項をとるなら、とるので、3項限定
            →a+b-c or a-b+c
            →→本質的に同じ？←途中でも負にならないように(1-2...はNG) 
        """
        common_denominator = randint(6, 20)
        # a + b -c
        if random() > 0.5:
            """
            common_denominator: 6
            plus_numerator1: 5
            plus_numerator2 = randint(1, common_denominator - plus_numerator1 - 1)
            """
            plus_numerator1 = randint(2, common_denominator - 1)
            # plus_numerator2 = randint(1, common_denominator - plus_numerator1 - 1)
            plus_numerator2 = randint(1, common_denominator - plus_numerator1)
            minus_numerator = randint(1, plus_numerator1 + plus_numerator2 - 1)
            latex_problem = f"\\frac{{{plus_numerator1}}}{{{common_denominator}}}"
            latex_problem += f"+ \\frac{{{plus_numerator2}}}{{{common_denominator}}}"
            latex_problem += f"- \\frac{{{minus_numerator}}}{{{common_denominator}}}"
            latex_answer = f"= \\frac{{{plus_numerator1 + plus_numerator2 - minus_numerator}}}{{{common_denominator}}}"
        # a - b + c
        else:
            plus_numerator1 = randint(2, common_denominator - 1)
            minus_numerator = randint(1, plus_numerator1 - 1)
            plus_numerator2 = randint(1, common_denominator - plus_numerator1 + minus_numerator - 1)
            latex_problem = f"\\frac{{{plus_numerator1}}}{{{common_denominator}}}"
            latex_problem += f"- \\frac{{{minus_numerator}}}{{{common_denominator}}}"
            latex_problem += f"+ \\frac{{{plus_numerator2}}}{{{common_denominator}}}"
            latex_answer = f"= \\frac{{{plus_numerator1 - minus_numerator + plus_numerator2}}}{{{common_denominator}}}"
        return latex_answer, latex_problem
